# Validar o Fume 0.39.39

Esta versão usa o código privado e a distribuição pública da conta NorthWind557. O instalador preserva a Biblioteca, a Lista de Desejos, a configuração HTTPS e a credencial de Manter conectado. A primeira passagem da 0.39.38 para a nova distribuição requer baixar e executar o novo Setup uma vez.

## 1. Atualizar os PCs

Baixe o ZIP na release pública v0.39.39, extraia-o e execute Fume_0.39.39_Setup_Windows_x64.exe. Confirme a versão em Ajuda. Faça isso nos dois PCs. Não remova os dados do Fume nem saia da conta para atualizar.

Em Ajuda, Verificar atualizações deve consultar a distribuição sem pedir token ou conta GitHub. Estar na versão mais recente deve informar que não há uma versão nova. A verificação de assinatura, SHA-256, tamanho, redirecionamento e executável continua obrigatória antes de abrir atualizações.

## 2. Atualizar o J8 uma vez

Use Configurações → Conta → Abrir arquivos para atualizar o J8. Copie Fume_Contas_Servidor_0.39.39.zip para Download do J8. O guia ATUALIZAR-SERVIDOR-J8.md acompanha a pasta; os comandos também estão abaixo, um por vez:

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" parar
```

```sh
python -m zipfile -e "$HOME/storage/downloads/Fume_Contas_Servidor_0.39.39.zip" "$HOME/fume-servidor-atualizacao-03939"
```

```sh
python "$HOME/fume-servidor-atualizacao-03939/atualizar_servidor.py"
```

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" iniciar
```

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" estado
```

Espere Teste HTTPS agora: ok e API respondeu por HTTPS neste J8. Não execute init. No Fume, Diagnosticar conexão e Reconectar conta salva devem funcionar com o mesmo ID. A primeira preparação da API pode levar até três minutos.

## 3. Galeria da Biblioteca

Abra um jogo com pelo menos duas imagens estáticas. Alterne imagens horizontais e verticais, também em modo janela, maximizado e após redimensionar. Confira imagens com proporções iguais e diferentes, clique rapidamente nas setas e teste um GIF. O crossfade deve durar meio segundo, sem fundo vazio, deslocamento lateral ou deformação. A galeria da Loja também deve conservar seu comportamento.

## 4. Capas no perfil

No PC que tem a Biblioteca e as capas personalizadas, abra seu perfil e clique em Sincronizar capas da Biblioteca. Espere Perfil salvo no J8. Confira One Shota Quest III e Deserted Island Castaway Chronicle, além de uma composição Steam com logo e recorte. A vitrine usa a composição final local e preserva sua proporção. Quando só houver endereço remoto disponível, ele continua sendo usado como alternativa, incluindo os hosts DMM/FANZA permitidos.

No segundo PC, na mesma conta, clique em Atualizar perfil. As miniaturas enviadas ao J8 devem aparecer mesmo sem os arquivos originais do primeiro PC. Não é necessário remover e escolher novamente os jogos. Só as capas dos seis jogos selecionados para a vitrine são enviadas.

## 5. Cadastro e privacidade entre duas contas

No segundo PC, saia da conta atual somente quando tiver o usuário e a senha para voltar. Em Configurações → Conta → Criar conta, escolha outro usuário e uma senha de 15 a 128 caracteres. Não deve haver convite nem aprovação. Confira confirmação de senha, nome já cadastrado e entrada na nova conta. Ative Manter conectado se desejar.

Copie o ID da conta original. Na conta nova, use Abrir outro perfil. Com a conta original em Somente eu, não deve ser possível ver o perfil ou suas imagens. Mude a conta original para Outros usuários conectados ao Fume e salve: a conta nova passa a poder ver o perfil e as capas. Retorne a Somente eu e confirme que um novo acesso é recusado.

Uma imagem já recebida pode permanecer na tela do outro PC até ele atualizar o perfil; nenhuma aplicação consegue apagar retroativamente uma cópia já recebida. A API verifica a privacidade a cada nova consulta.

## 6. Preparação de um PC novo

Preparar acesso ao Fume consulta a configuração assinada no Pages, orienta a instalação/entrada no Tailscale, abre a aceitação de acesso ao servidor e testa HTTPS. Só salva o endereço e a impressão do certificado após o teste passar. Depois, Criar conta e Entrar funcionam dentro do Fume, sem GitHub ou arquivos PEM.

Essa etapa depende de uma configuração inicial do publicador no J8 pelo proprietário. Enquanto ela não estiver concluída, o assistente informa que o acesso para PCs novos ainda não foi publicado. Isso não impede o uso dos PCs já configurados. Consulte DISTRIBUICAO-J8.md. O token administrativo do Tailscale precisa ser renovado pelo proprietário quando vencer; ele nunca é entregue aos usuários.

## 7. Backup

Depois de salvar as capas, execute no Termux:

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" backup
```

O backup privado deve incluir as imagens do perfil e as miniaturas da vitrine. Não envie esse backup para repositórios públicos.
