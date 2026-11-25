# Atualizar o J8 para perfis, carteiras e compras do Fume 0.39.41

Faça esta atualização **uma vez no celular J8**. Os dois PCs usarão o mesmo servidor atualizado. Suas contas, IDs, certificados, sessões salvas e a inicialização automática já validada permanecem. Não reinstale Termux, Tailscale ou Termux:Boot. **Não execute `init`.**

Esta atualização acrescenta GIF em todos os espaços de personalização, composições de moldura editáveis e a referência completa dos jogos adquiridos para a Biblioteca. Os dados anteriores são preservados. Perfis existentes mantêm imagem, descrição e jogos; o novo editor acrescenta estilo e miniperfil.

**Opção mais simples para obter o ZIP:** no Termux, execute este comando e depois prossiga ao item 2:

```sh
curl --fail --location --retry 3 -o "$HOME/storage/downloads/Fume_Contas_Servidor_0.39.41.zip" "https://github.com/NorthWind557/Fume-Releases/releases/download/v0.39.41/Fume_Contas_Servidor_0.39.41.zip"
```

Se a pasta não existir, execute `termux-setup-storage` e permita o acesso. O item 1 descreve a alternativa pelo PC.

## 1. Encontrar o pacote no PC, inclusive após atualização pelo Fume

1. No **PC principal ou segundo PC**, abra o Fume 0.39.41.
2. Clique em **CONFIGURAÇÕES → Conta → Abrir arquivos para atualizar o J8**.
3. O Explorador abrirá a pasta **Servidor_J8**. Nela estão este guia e **Fume_Contas_Servidor_0.39.41.zip**. Você não precisa baixar o ZIP grande do instalador novamente.
4. Conecte o J8 por cabo USB, desbloqueie-o e escolha **Transferência de arquivos** na notificação USB do Android.
5. No PC, abra **Este Computador → Galaxy J8 → Armazenamento interno → Download**.
6. Copie **Fume_Contas_Servidor_0.39.41.zip** para essa pasta Download. Mantenha o nome e não extraia no PC. Não copie o instalador Windows para o celular.

O ZIP contém somente código e instruções; não contém contas, senhas, banco ou certificados privados.

## 2. Parar o serviço automático pelo Termux

Abra o **Termux no J8**. Os comandos desta página são para o Termux, não para o PowerShell do PC. Cada bloco é **um comando separado**: copie, cole, toque em Enviar/Enter e aguarde o `$` reaparecer antes do próximo.

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" parar
```

Espere **Serviço parado. A partida automática também fica desativada até executar iniciar novamente.** Isso impede que a supervisão abra o programa antigo durante a troca de arquivos. Ctrl+C sozinho não é a forma correta de parar o serviço automático.

Se este comando falhar, não aplique a atualização: informe a mensagem. Não abra uma segunda cópia com o comando `servir`.

## 3. Extrair o pacote novo

```sh
python -m zipfile -e "$HOME/storage/downloads/Fume_Contas_Servidor_0.39.41.zip" "$HOME/fume-servidor-atualizacao-03941"
```

O comando pode terminar sem mensagem: é normal. Se o arquivo não for encontrado, confira o nome em Download. Se houver erro de permissão, execute o próximo comando, permita o acesso solicitado pelo Android e repita a extração:

```sh
termux-setup-storage
```

## 4. Aplicar a atualização preservando os dados

```sh
python "$HOME/fume-servidor-atualizacao-03941/atualizar_servidor.py"
```

Espere **Atualização copiada. Contas, IDs, banco e certificado preservados.** O atualizador verifica os arquivos, guarda um backup privado e substitui o código da API e da operação. As configurações de inicialização automática permanecem.

O caminho **Backup privado** deve ficar dentro do Termux. Não copie essa pasta para Downloads ou envie seu conteúdo: ela contém dados da conta e chaves privadas.

Se houver erro, **não execute init** nem apague banco/certificado. Guarde a mensagem e use o comando de iniciar abaixo para tentar reativar a instalação que está no celular. Informe o erro antes de substituir arquivos manualmente.

## 5. Reativar o servidor e a partida automática

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" iniciar
```

Espere **Supervisão iniciada**. A primeira preparação pode levar alguns segundos; aguarde até três minutos antes de consultar o estado. A supervisão fica em segundo plano, portanto o `$` volta normalmente. Não execute `servir` em outra sessão.

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" estado
```

O esperado é **Teste HTTPS agora: ok** e **API respondeu por HTTPS neste J8**. Se estiver preparando, consulte `estado` novamente depois de alguns instantes. Mantenha o Tailscale conectado no celular e nos PCs, como antes.

## 6. Conferir no Fume

1. No PC principal, abra **Configurações → Conta**. Não clique em Sair e não troque endereço/certificado. A sessão salva continua válida.
2. Clique em **Diagnosticar conexão** e, se necessário, **Reconectar conta salva**. Confira o ID já conhecido.
3. Clique no seu nome/foto no canto superior direito. Clique em **Atualizar**, depois em **Sincronizar capas** para enviar as capas já personalizadas.
4. Espere a confirmação **Perfil salvo no J8**. As imagens escolhidas na Biblioteca são enviadas como miniaturas; o restante da Biblioteca não é enviado.
5. No segundo PC com Fume 0.39.41, abra o perfil ou clique em **Atualizar perfil**. A alteração deve aparecer na mesma conta. Atualize ambos os PCs para 0.39.41 antes de editar as novas composições. Clientes anteriores mantêm login e seus dados; não exibem as camadas novas.

Não é necessário digitar a senha novamente se Manter conectado já está funcionando.

## 7. Guardar um backup com o primeiro perfil

Após salvar o primeiro perfil com imagem, execute no Termux:

```sh
python "$HOME/fume-contas-piloto/operacao/operacao_j8.py" backup
```

Espere **Backup privado concluído (contas, certificados e imagens do perfil)**. O servidor continua ligado durante essa cópia. Os backups diários passam a incluir as imagens e continuam limitados às sete cópias mais recentes. O backup do catálogo feito pelo Fume no PC é separado do backup das contas no J8.

## Se precisar desfazer uma atualização

Não restaure o banco por conta própria enquanto o serviço estiver ativo. Informe a mensagem de erro e o caminho do backup mostrado no item 4. Restaurar o banco pode desfazer mudanças e sessões posteriores à cópia. O pacote preserva o certificado; não gere outro para tentar resolver um erro de atualização.

## 8. Sua conta administradora e créditos de teste

A habilitação de administrador é feita somente no J8. Execute o comando abaixo e digite o **usuário de entrada** do Fume quando solicitado:

```sh
python "$HOME/fume-contas-piloto/fume_accounts.py" administrador
```

No Fume, abra Loja de pontos e clique em Atualizar. A aba Administrar promoções aparece somente para a conta habilitada. Os outros usuários não precisam de autorização administrativa para se cadastrar/comprar.

Os créditos manuais estão ativos nesta fase de validação para qualquer conta conectada. Quando desejar desativá-los, execute:

```sh
python "$HOME/fume-contas-piloto/fume_accounts.py" administrador --desativar-creditos
```

A conta administradora continua habilitada. Saldos, compras e inventários são preservados. A configuração fica privada no J8 e não vai ao GitHub Pages.
