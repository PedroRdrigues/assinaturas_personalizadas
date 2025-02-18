# Assinaturas Personalizadas

## Autosign

Deve ser alocado no C:/Windows/ para que não tenha fácil acesso do usuário.


Ao executar o Setup, deve ser iniciado uma interface para que possa ser feita o ajuste para configuração (usuário e gerenciador de e-mail).


Ao ser executado, cria um arquivo .xml onde estará contendo informações de usuário e gerenciador de e-mail.


O arquivo .xml estará dentro do diretório users com o nome do usuário do colaborador, por exemplo usuario.xml.


O arquivo autosign.exe irá procurar pelo diretório users e realizará a atualização das assinaturas de todos os usuáirios.


Caso um usuário não seja encontrado, o autosign irá excluir o arquivo .xml do respectivo usuário.



## Signature Creator

Faz a conexão com o banco de dados e realiza a criação das assinaturas de todos os colaboradores


Envia as assinaturas atualizadas para um Web Server para que possam ser armazenadas e disponibilizadas para o *_autosigin_*