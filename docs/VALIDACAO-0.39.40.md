# Validação do Fume 0.39.40

Esta versão amplia perfis e introduz a economia de teste em GC/GP. Atualize o servidor do J8 uma vez antes de testar compras e novas personalizações. Não execute `init`; contas, IDs, certificados, sessões, partida automática e distribuição continuam preservados. Consulte ATUALIZAR-SERVIDOR-J8.md.

## 1. Atualização e conta

- Atualize pelo Fume, sem token GitHub. Confirme 0.39.40 em Ajuda.
- Confirme que Manter conectado conserva a conta e o ID nos dois PCs.
- No J8, atualize pelo guia. Confirme `Teste HTTPS agora: ok`; no PC, Diagnosticar conexão e Reconectar conta salva.
- Criar uma conta continua usando apenas usuário/senha. No assistente, estar conectado no site do Tailscale não substitui entrar no aplicativo Tailscale do Windows.

## 2. Perfil e editor

- Abra o perfil pelo nome/foto superior. Fundo cobre a área da página; painel central tem gradiente distinto; descrição integra o cabeçalho.
- Reduza a largura até o limite já existente do Fume: coluna principal e lateral continuam lado a lado. Não devem se empilhar.
- Os seis favoritos usam áreas 4:3 iguais. Verifique capas DMM/FANZA e composição customizada da Biblioteca, inclusive logo e recorte.
- Em Editar perfil, visite Geral, Avatar e moldura, Fundo do perfil, Miniperfil, Tema, Emblema em destaque, Gerenciar vitrines e Privacidade. Emblemas não são conquistas fictícias: ficam aguardando a implementação futura.
- Altere nome/descrição, cores pelo seletor, transparência e direção do gradiente. Escolha visibilidade e habilite/reordene favoritos e atividade.
- Teste salvar, cancelar, retomar e descartar rascunho. Em dois PCs, edição concorrente deve preservar o rascunho e avisar conflito.
- Faça uploads gratuitos de avatar, fundo, moldura PNG transparente e miniperfil (PNG/JPG/WebP ou GIF até 8 MB, 120 quadros, 1920×1080 e 50 milhões de pixels acumulados). Verifique o segundo PC após salvar.

## 3. Loja de pontos e miniperfil

- Entre por Loja de pontos no topo ou no perfil. Há dois exemplos originais para cada categoria: avatar, moldura, fundo, miniperfil e tema.
- Em Créditos de teste, adicione uma quantidade específica de GC e GP. O saldo deve somar somente à conta conectada. Esta opção é temporária e pode ser desativada no servidor.
- Obtenha um item com GP, confira desconto único e posse em Meus itens. Equipar prepara a prévia; Salvar alterações publica o perfil. Reequipar não cobra novamente.
- Uploads e gradiente próprio são gratuitos.
- Mantenha o cursor sobre nome/foto, mova-o para o miniperfil e abra o perfil pelo card. O fundo próprio deve aparecer; os dois exemplos da loja usam animação nativa. Escape, minimizar e bandeja fecham o card.
- Com outra conta, perfil privado, imagens e atividade não devem ficar disponíveis. Perfil compartilhado deve mostrar somente dados publicados. Não há sistema de amigos nesta etapa.

## 4. GC, carrinho e compras

- Abra um jogo com tamanho informado no LINK DOWNLOAD: 85 MB = 85 GC; 1,5 GB = 1500 GC; frações arredondam para cima. Ausência ou tamanho ambíguo usa 400 GC. Não se somam alternativas/patches.
- O J8 consulta a página de origem; se não conseguir confirmar uma ficha ainda desconhecida, avisa e não cobra. A consulta real ao site deve ser validada na conexão do J8.
- Adicione jogos ao carrinho e revise itens/total. Adicionar não reserva desconto. Antes de confirmar, preço vigente é consultado e uma cotação de cinco minutos é apresentada.
- Confirme com saldo suficiente. A carteira deve debitar uma vez, aquisição constar na conta e a ficha indicar posse. Repetir o mesmo pedido não cobra duas vezes.
- A Lista de Desejos deve manter itens e ordem pessoal; adquiridos recebem marcador. Reinstalar jogos já cadastrados localmente não exige compra retroativa.
- Novo download pela ficha exige aquisição. Abrir a página original/usar arquivos próprios continua possível; GC é uma economia interna do Fume, sem pagamento em dinheiro.
- Teste saldo insuficiente: nenhum débito nem aquisição parcial. Não simule falha apagando banco ou mudando relógio do J8.

## 5. Recuperação e devolução

- Em falha técnica de finalização, o cliente consulta o pedido original. Se já foi pago, não compra outra vez. Se o J8 registrar a recuperação elegível, o prazo de 72 horas aparece no histórico.
- Desconto preservado pertence ao pedido registrado, não a um carrinho comum. Repetir a recuperação não renova o prazo. Depois de expirar, um novo pedido usa o preço atual.
- Para devolver: até 72 horas da aquisição e menos de 600 segundos registrados. Exatamente dez minutos não é elegível. Estorno usa o valor efetivamente pago, inclusive desconto.
- Encerre o jogo e sincronize os PCs usados antes de devolver. Sessão ainda aberta ou pendência local bloqueia a devolução. Saves não são apagados.
- Tempo é enviado em intervalos e ao detectar encerramento; o diário local conserva pendências. O servidor agrega dispositivos. Um PC offline não pode transmitir tempo imediatamente: não é uma proteção antifraude/DRM e não afirma conhecer sessões ainda não sincronizadas.
- Jogos que delegam execução a outro launcher podem não permitir rastreamento confiável. A atividade exibida usa sessões novas sincronizadas, sem inventar dados históricos.

## 6. Recompensas e promoções

Valores iniciais de desenvolvimento: cada minuto completo rastreado rende 1 GC + 1 GP; primeira personalização salva rende 100 GP; primeira instalação reconhecida por jogo/conta rende 50 GC + 25 GP. Reinstalação ou repetição de envio não repete o prêmio. Bibliotecas já existentes podem receber o prêmio de instalação na primeira sincronização. São valores de teste, não garantias de resistência a clientes modificados.

Para habilitar a administração na sua conta, no Termux:

```sh
python "$HOME/fume-contas-piloto/fume_accounts.py" administrador
```

Digite o usuário de entrada do Fume quando solicitado. Nenhuma senha/token é publicado. Reinicie/atualize a carteira no PC. Em Loja de pontos → Administrar promoções, configure nome, datas e faixas de visualizações/desconto; revise e publique. Outra conta deve receber os preços durante o período, e perdê-los ao encerrar o evento. Não é necessário recompilar por evento. Contador ausente não equivale a zero. Tags, presentes, amigos/mensagens e conquistas ficam para versões posteriores.

Para desativar os créditos manuais, preservando os saldos:

```sh
python "$HOME/fume-contas-piloto/fume_accounts.py" administrador --desativar-creditos
```

## 7. Janela e regressões

- Alterne Loja/Biblioteca/perfil, troque imagens/GIFs e minimize/restaure várias vezes; repita indo à bandeja durante carregamento.
- Confirme que a Área de Trabalho recebe cliques, inclusive fora da antiga posição do Fume. A correção reforça a ocultação de superfícies WebView após inicialização assíncrona. O teste físico em Avell/Pichau continua necessário para confirmar o caso intermitente relatado.
- Preserve os comportamentos já validados: animações nativas, bordas, barra de rolagem na extrema direita, botões superiores/inferiores e crossfade de 500 ms sem deslocamento.
- Ao terminar, execute backup do servidor; ele inclui carteiras, inventário, pedidos, aquisições, eventos, sessões e imagens, além das contas existentes.
