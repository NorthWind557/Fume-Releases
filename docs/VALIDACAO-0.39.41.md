# Validar o Fume 0.39.41

Atualize o **J8 primeiro**, seguindo os comandos abaixo, e depois os dois PCs. A atualização preserva contas, IDs, certificados e Manter conectado. Não reinstale Termux/Tailscale e não execute `init`.

## 1. Comandos para colar no Termux do J8

Execute uma linha por vez. Baixe o pacote antes de parar o serviço.

```sh
curl --fail --location --retry 3 -o "$HOME/Fume_Contas_Servidor_0.39.41.zip" "https://github.com/NorthWind557/Fume-Releases/releases/download/v0.39.41/Fume_Contas_Servidor_0.39.41.zip"
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" parar
python -m zipfile -e "$HOME/Fume_Contas_Servidor_0.39.41.zip" "$HOME/fume-servidor-atualizacao-03941"
python "$HOME/fume-servidor-atualizacao-03941/atualizar_servidor.py"
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" iniciar
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" estado
```

Espere **Atualização copiada** no quarto comando. Depois de iniciar, consulte `estado` novamente se ainda estiver preparando. O esperado é **Teste HTTPS agora: ok** e **API respondeu por HTTPS neste J8**. Se a atualização falhar, preserve a mensagem, não apague dados nem gere outro certificado. O comando `iniciar` reativa o serviço que estiver instalado.

## 2. Perfil e GIFs

1. Confira Waifu’s Love Room e outros jogos Itch no perfil: todas as imagens preenchem 4:3, com corte proporcional como na Biblioteca. A borda inferior pode ficar fora do recorte; não deve haver encolhimento para mostrar tudo.
2. Em Editar perfil, envie um GIF em avatar, moldura inteira, fundo e miniperfil. Salve, feche/reabra e confira no outro PC. GIFs mantêm os bytes originais; a área de exibição faz o recorte proporcional. O limite é 8 MB, 1920×1080, 120 quadros e 50 milhões de pixels acumulados por arquivo. A conta tem cota de mídia de 64 MB.
3. No editor de molduras, adicione uma imagem/GIF, ajuste posição, tamanho, pivô e rotação. Duplique, reordene e oculte uma camada. Teste Desfazer/Refazer.
4. Experimente repetições e percursos quadrado/círculo/estrela, sentido inverso, fase, duração, giro, pulsação e giro 3D aparente. O giro 3D é a simulação de uma imagem plana. Reabra a composição depois de salvar e confira no outro PC. Até 12 camadas e 128 cópias no total.
5. Passe o mouse no nome do cabeçalho e no nome grande do perfil. Os miniperfis e Abrir perfil devem ter o mesmo tamanho. Abra o perfil a partir da Loja, Biblioteca e Configurações.

## 3. Compra separada da instalação

1. Com créditos de teste, compre dois ou mais jogos ainda não cadastrados. Devem aparecer na Biblioteca como não instalados. **A compra não inicia downloads, verificações ou envios ao MEGA.** A Lista de Desejos permanece.
2. Reinicie o Fume. Os jogos adquiridos continuam vinculados à conta. Dados já lidos na Loja podem preencher o cadastro sem novas consultas; os coletores normais continuam disponíveis em Metadados.
3. Clique Instalar na Biblioteca. A solicitação aparece em **Biblioteca → Downloads**, com edição/servidor e o fluxo de verificação humana do ouo.io. A confirmação humana continua sendo feita por você.
4. Troque de aba e retorne a Downloads; a solicitação continua. Feche/reabra: retome pelo botão Continuar. Verificações temporárias de sites precisam ser abertas de novo; os arquivos já completos e a solicitação persistem.
5. Cliques repetidos em Instalar não criam solicitações paralelas para o mesmo jogo. Se já estiver pronto, use Jogar.
6. O link da origem Ryuugames na Biblioteca abre a Loja interna. O link Steam/DMM/DLsite/Itch original continua separado. Jogos antigos sem associação exata pedem a URL correta; não há adivinhação por nome de pasta.
7. Uma aquisição autoriza novos downloads até ser devolvida. Arquivos já existentes são preservados; um novo download após devolução exige nova compra.

## 4. Primeiro envio MEGA e reinstalação

Use primeiro um jogo pequeno. O MEGAcmd precisa estar conectado à conta correta no Windows.

1. Sem envio automático, **Manter arquivos locais mesmo após o primeiro envio ao MEGA.** fica marcado e não pode ser desmarcado.
2. Com envio habilitado e MEGA configurado, deixe marcado: o primeiro download Ryuugames é preparado, enviado e confirmado; a cópia local fica pronta para jogar.
3. Em outra solicitação, desmarque antes de clicar Instalar. Downloads deve avisar que o primeiro processo termina **arquivado no MEGA e não instalado no PC**, usando espaço temporário local para preparar/enviar. Só a cópia gerenciada autorizada é removida após confirmação; alterações locais suspendem o descarte.
4. Depois de arquivado, clique Instalar de novo: deve baixar a cópia registrada no MEGA, verificar e manter localmente. Esta restauração não envia novamente nem aplica a remoção do primeiro envio.
5. A escolha fica registrada por solicitação. Alterar a configuração global não concede permissão de remover arquivos de uma tarefa anterior que preservaria a cópia local.
6. Se a cópia MEGA não puder ser confirmada, veja a mensagem e escolha Ryuugames explicitamente. O Fume não troca silenciosamente a origem.

## 5. Possíveis atualizações e arquivos

1. No menu do jogo na Biblioteca, use Verificar mudanças na página. O Fume compara título/versão, idiomas e grupos de servidores; não compara contadores de visualizações ou anúncios.
2. Quando houver diferenças, aparece **Há mudanças na página do jogo. Pode haver atualização disponível**, com os motivos. Isto é um indício, não uma confirmação de que os arquivos mudaram.
3. **Baixar edição / atualização do Ryuugames** permite escolher a origem nova mesmo que exista pacote antigo no MEGA. Não há nova cobrança pela mesma aquisição válida.
4. Para um jogo já instalado, o material baixado fica para revisão. Em Downloads, use **Revisar atualização em cópia separada**, ou Preparação → Atualizar jogo associado. Confira os novos arquivos e conflitos antes de substituir a cópia de trabalho e publicar pelo fluxo de Edições. A instalação original e o pacote anterior ficam preservados durante a revisão.
5. Na Biblioteca, Conferir alterações locais mostra quantidades de arquivos novos, alterados e removidos quando há manifesto anterior. Instalações antigas sem manifesto mantêm a comparação global e começam o registro detalhado nas novas operações.
6. O catálogo guarda caminho relativo, tamanho e SHA-256 por arquivo/revisão. Observar a página ou os arquivos não altera a referência instalada. O manifesto acompanha o backup do catálogo.

**Cobertura:** somente pasta principal do jogo e subpastas. AppData, Documentos e quaisquer saves externos ficam fora. O backup de jogos continua ZIP completo; o envio realmente incremental fica para etapa posterior.

## 6. Resíduo invisível na Área de Trabalho

Esta correção precisa de confirmação no seu Windows real; o teste automatizado com proxy sintético não reproduz toda a combinação de driver, monitores e WebView.

1. Em modo janela, mova o Fume para uma posição fácil de reconhecer.
2. Maximize e deixe outro aplicativo/Área de Trabalho à frente. Teste cliques e seleção de ícones na área da última janela normal.
3. Recolha o Fume ao tray e repita. Depois mova a janela normal para outra posição e teste novamente.
4. Se bloquear, abra **Ajuda → Copiar diagnóstico de cliques (5 segundos)**. Dentro de cinco segundos, minimize/recolha e reproduza a situação. O diagnóstico vai para a área de transferência; cole na conversa. Não captura senhas, tokens nem títulos de outras janelas.

## 7. Testes e pendências

A entrega exige os testes Python de contas, perfis, economia, operação e distribuição; cliente HTTPS real; compra/instalação/fila/manifestos; e interface WPF no Windows. Os cenários acima validam os serviços externos no seu ambiente.

Continuam para validação posterior: promoções e cenários de falha técnica de compra/recuperação/devolução. Conquistas, amigos, mensagens, presentes e modificadores de preço por tags não entram nesta rodada.
