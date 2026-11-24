"""Publish only a reviewed binary delivery and its signed public configuration."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import urllib.request
from urllib.parse import urlsplit
from zipfile import ZipFile

REPO='NorthWind557/Fume-Releases'


def require(value,message):
    if not value:raise ValueError(message)


def gh(*args,data=None):
    result=subprocess.run(['gh',*args],input=None if data is None else json.dumps(data).encode(),capture_output=True)
    if result.returncode:
        detail=result.stderr.decode('utf-8','replace')[-1800:]
        token=os.environ.get('GH_TOKEN','')
        if token:detail=detail.replace(token,'[redacted]')
        raise ValueError('GitHub: '+str(args[:3])+' — '+detail)
    return result.stdout


def digest(path):
    with path.open('rb') as source:return hashlib.file_digest(source,'sha256').hexdigest()


def verify(envelope):
    payload=base64.b64decode(envelope['payload'],validate=True);signature=base64.b64decode(envelope['signature'],validate=True)
    require(len(payload)<=32768 and len(signature)==384,'Manifesto inválido.')
    with tempfile.TemporaryDirectory() as directory:
        file=Path(directory)/'signature';file.write_bytes(signature)
        result=subprocess.run(['openssl','dgst','-sha256','-verify','distribution-public.pem','-signature',str(file)],input=payload,capture_output=True)
        require(result.returncode==0,'A assinatura do manifesto não confere.')
    return json.loads(payload)


def main():
    require(os.environ['GITHUB_REPOSITORY']==REPO,'Repositório inesperado.')
    config=json.loads(Path('publication.json').read_text());version=config['version']
    require(re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+',version),'Versão inválida.')
    tag='v'+version;bundle=f'Fume_{version}_Instalador_Windows_x64.zip'
    names={bundle,bundle+'.sha256',f'Fume_Contas_Servidor_{version}.zip',f'VALIDACAO-{version}.md'}
    require(os.environ['GITHUB_REF']=='refs/heads/staging/'+version,'Branch de entrega inesperado.')
    main=json.loads(gh('api',f'repos/{REPO}/git/ref/heads/main'))
    require(main['object']['sha']==config['release_target'],'A referência pública mudou; confira a entrega antes de continuar.')
    archive=Path('delivery.zip');parts=config['parts'];total=0
    require(1<=len(parts)<=32,'Quantidade de partes inválida.')
    with archive.open('xb') as output:
        for index,item in enumerate(parts):
            require(item['path']==f'delivery/{index:03}.part','Caminho de parte inesperado.')
            path=Path(item['path']);require(path.is_file() and 0<path.stat().st_size<=8*1024*1024 and path.stat().st_size==item['bytes'],'Tamanho de parte incorreto.')
            require(digest(path)==item['sha256'],'Hash de parte incorreto.')
            data=path.read_bytes();total+=len(data);require(total<=220*1024*1024,'Entrega excede o limite.');output.write(data)
    require(digest(archive)==config['artifact_sha256'],'Hash da entrega não confere.')
    directory=Path('release');directory.mkdir()
    with ZipFile(archive) as package:
        require(set(package.namelist())==names and len(package.namelist())==len(names),'Conteúdo inesperado na entrega.')
        for name in names:
            require(package.getinfo(name).file_size<=512*1024*1024,'Arquivo excede o limite.')
            (directory/name).write_bytes(package.read(name))
    require(digest(directory/bundle)==config['bundle_sha256'],'Hash do instalador não confere.')
    require((directory/(bundle+'.sha256')).read_text().strip()==config['bundle_sha256']+'  '+bundle,'Lista de hash não confere.')
    manifest=config['bootstrap'];payload=verify(manifest)
    release=payload['release']
    require(release['version']==version and release['sha256']==config['bundle_sha256'] and release['size']==(directory/bundle).stat().st_size and release['url']==f'https://github.com/{REPO}/releases/download/{tag}/{bundle}','A referência assinada não corresponde à entrega.')
    # Fail closed if the J8 published a newer operational configuration since
    # the owner prepared this signed release manifest. Never reset its fields.
    previous=json.loads(gh('api',f'repos/{REPO}/contents/docs/bootstrap.json'))
    require(previous['sha']==config['bootstrap_base_sha'],'O J8 ou outra publicação atualizou o manifesto. Prepare outra assinatura sobre a versão atual.')
    notes=Path('release-notes.md');notes.write_text(f'''Fume {version}

Perfil reorganizado em duas colunas permanentes, loja de pontos com personalizações originais, miniperfil, carteiras GC/GP, carrinho, aquisições, devoluções e eventos promocionais no J8.

Baixe o ZIP, extraia-o e execute o Setup Windows x64. A atualização pelo Fume continua disponível sem configurar token GitHub.

O pacote pequeno do servidor e o roteiro de validação estão nos arquivos anexados. Atualize o servidor do J8 uma vez para habilitar as novas funções de perfil e compras. Contas, IDs e sessões existentes são preservados.
''')
    existing=subprocess.run(['gh','release','view',tag,'--repo',REPO,'--json','isDraft'],capture_output=True)
    if existing.returncode==0:require(json.loads(existing.stdout)['isDraft'],'Esta versão já está publicada; os arquivos não serão substituídos.')
    else:gh('release','create',tag,'--repo',REPO,'--target',config['release_target'],'--draft','--title','Fume '+version,'--notes-file',str(notes))
    gh('release','upload',tag,*[str(directory/name) for name in sorted(names)],'--repo',REPO,'--clobber')
    uploaded=next(item for item in json.loads(gh('api',f'repos/{REPO}/releases')) if item['tag_name']==tag)
    assets={a['name']:a for a in uploaded['assets']}
    require(set(assets)==names,'Os arquivos publicados não correspondem à entrega.')
    for name in names:
        require(assets[name]['size']==(directory/name).stat().st_size and assets[name]['digest']=='sha256:'+digest(directory/name),'O GitHub não confirmou o hash de '+name)
    gh('release','edit',tag,'--repo',REPO,'--draft=false','--latest')
    # This transport has no Authorization header and does not use gh's token.
    anonymous=hashlib.sha256();received=0
    with urllib.request.urlopen(urllib.request.Request(release['url'],headers={'User-Agent':'Fume-public-download-check'}),timeout=45) as source:
        while part:=source.read(1024*1024):
            received+=len(part);require(received<=release['size'],'Download público excede o tamanho.');anonymous.update(part)
    require(received==release['size'] and anonymous.hexdigest()==release['sha256'],'O download público sem token não corresponde à entrega.')
    print('Download público sem Authorization confirmado por tamanho e SHA-256.')
    content=base64.b64encode((json.dumps(manifest,indent=2)+'\n').encode()).decode()
    identity={'name':'NorthWind557','email':'360101070+NorthWind557@users.noreply.github.com'}
    gh('api','--method','PUT',f'repos/{REPO}/contents/docs/bootstrap.json','--input','-',data={'message':'Publicar distribuição autenticada do Fume '+version,'content':content,'sha':previous['sha'],'branch':'main','author':identity,'committer':identity})
    gh('api','--method','DELETE',f'repos/{REPO}/git/refs/heads/staging/{version}')
    print('Release pública e manifesto assinado publicados com os hashes conferidos. O branch temporário de entrega foi removido.')


if __name__=='__main__':
    try:main()
    except Exception as exc:
        print(str(exc) if isinstance(exc,ValueError) else 'Publicação não concluída. Os detalhes privados de transporte não foram registrados.');raise SystemExit(1)
