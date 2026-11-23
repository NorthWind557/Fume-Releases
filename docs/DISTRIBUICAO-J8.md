# Operação da distribuição pelo J8

O instalador e as atualizações ficam nas releases públicas de NorthWind557/Fume-Releases. O código permanece privado em NorthWind557/Fume. O Pages oferece bootstrap.json, um envelope com o JSON em base64 e assinatura RSA/SHA-256. A chave pública acompanha o cliente; a privada não acompanha o código, as releases nem o servidor ZIP comum.

## Configuração inicial do proprietário

Esta configuração é feita uma vez no J8, depois de atualizar a API. Os amigos não executam essas etapas. A chave privada de assinatura é entregue separadamente ao proprietário. Nunca a envie ao repositório público ou aos usuários.

1. Receba o pacote privado do proprietário em um canal privado e copie-o para Download do J8. Extraia-o no diretório privado do Termux, não na pasta pública da instalação Windows.
2. No console Tailscale, crie um API access token de usuário, com a validade desejada de até 90 dias. A criação de compartilhamentos de dispositivo exige esse tipo de credencial; não use chave de autenticação de máquina nem OAuth no lugar dela.
3. No GitHub da conta nova, crie um fine-grained token limitado a Fume-Releases com Contents: read and write. Ele permite atualizar somente esse repositório de distribuição. O token fica no J8 e não entra no cliente. Os usuários do Fume não precisam de conta GitHub.
4. Copie o ID do dispositivo J8 mostrado pela API/console Tailscale. Use o ID do dispositivo, não seu endereço IP nem seu ID de conta Fume.
5. Execute a configuração abaixo. As entradas dos tokens são ocultas e não entram no histórico de comandos. Informe a validade do token Tailscale quando solicitada.

```sh
python "$HOME/fume-contas-piloto/operacao/distribution_j8.py" configurar --key "$HOME/fume-distribuicao-proprietario/distribution-signing.pem"
```

O script lê o endereço e a impressão do certificado da operação existente, sem gerar outro certificado nem alterar contas. Ele confere se a chave privada corresponde à chave pública da versão do Fume. Configuração e chave ficam em ~/.fume-distribution com permissão privada.

6. Publique uma vez e confira o Pages:

```sh
python "$HOME/fume-contas-piloto/operacao/distribution_j8.py" publicar
```

7. Instale o serviço de renovação:

```sh
python "$HOME/fume-contas-piloto/operacao/distribution_j8.py" instalar
```

8. Consulte sem expor os tokens:

```sh
python "$HOME/fume-contas-piloto/operacao/distribution_j8.py" estado
```

O serviço separado usa o runit/Termux:Boot já instalado. Ele verifica de hora em hora e publica um link novo a cada sete dias. Falhas de rede preservam o último manifesto e tentam novamente. Uma publicação concorrente no GitHub é relida para não perder a referência da release. Ele não revoga compartilhamentos já aceitos e não concede acesso aos outros PCs do proprietário.

## Validade e manutenção

Links reutilizáveis admitem até mil aceitações; links não utilizados expiram após 30 dias. Não dependemos da interpretação da validade depois do primeiro uso: a rotação usa links novos a cada sete dias. Se o J8 não conseguir publicar por duas semanas, o cliente deixa de usar a configuração vencida para preparar novos PCs. As sessões e configurações existentes continuam válidas; atualizações podem consultar a referência de release assinada mesmo nesse caso.

A credencial administrativa Tailscale expira em até 90 dias. O proprietário precisa renová-la; estado mostra a data informada. Configure novamente para trocar as credenciais antes do vencimento. O GitHub também pode impor vencimento ao token criado. Não há promessa de manutenção administrativa zero.

Um link de acesso distribuído publicamente pode ser utilizado por qualquer pessoa que o obtenha, conforme a intenção do cadastro aberto. A conta Fume continua exigindo usuário e senha. A autenticação e a privacidade do perfil são verificadas pela API.

## Recuperação

Se a publicação falhar, a API de contas continua em seu serviço separado. Não execute init, não regenere certificado e não restaure o banco por causa de um erro do publicador. Confira estado e a validade das credenciais. Guarde uma cópia privada da chave de assinatura: perdê-la exige migrar a confiança dos clientes por outra atualização.

Os backups automáticos da API protegem contas, certificados e imagens. A configuração do publicador é separada; faça uma cópia privada de ~/.fume-distribution quando estiver configurado. Ela contém segredos e nunca deve virar asset público.
