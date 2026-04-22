# T1-INF1407-2026

Componentes do Grupo: Bruno Miksucas Pimenta (2110717) e Pedro Bittencourt (2111415)

Nome do Projeto: MySongProfileApp

O MySongProfileApp é um website onde o usuário pode criar e editar uma lista com as top 5 músicas favoritas dele.
O website foi hosteado na plataforma On Render.

Para acessar o site, basta acessar o link: https://t1-inf1407-2026-j4pm.onrender.com

O MySongProfileApp possui três telas principais:
 - Home
 - Perfil
 - Configurações

 - A tela Home apenas apresenta uma mensagem de boas-vindas e um hyperlink que redireciona o usuário para a tela de perfil (caso ele esteja logado, senão será redirecionado para a tela de login)
 - A tela Perfil é a tela principal que contem os CRUDs do site.
     - Na tela perfil, enquanto a lista do usuário não possuir 5 músicas, haverá um hyperlink que permite que ele adicione músicas novas na lista, além de poder editar informações de outras músicas também. O usuário não pode preencher apenas parcialmente as informações de uma música, ele deve adicionar o título, artista e gênero.
     - Além disso, o usuário pode editar informações de uma música de forma individual, e também deletá-las.
 - A tela Configurações serve para o usuário alterar suas informações pessoais, inclusive senha.


Como navegar pelo site:
  - Em todas as telas (exceto as de login/cadastro/redefinição de senha) há uma barra de navegação no canto esquerdo, contendo botões que levam à cada uma das telas acima mencionadas, além de um botão para fazer Login/Logout.


O que não está funcionando:
  - Não conseguimos fazer com que o sistema envie um link pelo email para o usuário redefinir a senha, então após preencher o email da conta que será enviado o email, quando o usuário (deslogado) clicar no botão de Login, ele vai ser levado à tela de redefinição de senha.

Notas:
  - O MySongProfileApp originalmente era para utilizar uma API do Spotify para buscar músicas/álbuns e depois mostrar algumas estatísticas sobre o perfil do usuário baseado nas músicas/albuns escolhidos, mas devido a uma mudança de planos, o escopo do aplicativo foi bem reduzido, porém mantendo funcionalidades que atendem aos requerimentos mínimos do trabalho.
