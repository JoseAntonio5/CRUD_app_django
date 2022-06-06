# CRUD Django App

### O projeto
Este é um projeto desenvolvido usando o framework django. O projeto consiste em um aplicativo simples de blog que usa as operações CRUD (Create, Read, Update, Delete).

### Descrição
A aplicação conta com um sistema de autenticação de usuário usando os modelos padrões de usuário do django. É possível cadastrar um novo usuário e usar os usuários cadastrados para fazer login no sistema. Ao fazer login o usuário é redirecionado para a rota de uma página que lista todos os posts criados na aplicação.

O back-end da aplicação foi desenvolvido usando somente o django. O front-end foi desenvolvido usando a template engine padrão do django e bootstrap.  O banco de dados usado foi o SQLite.

### Funcionalidades
 Um usuário pode visualizar os posts sem estar autenticado, porém é necessário fazer login para que seja possível criar um novo post. Na página que exibe todos os posts é mostrado somente o título do post e um botão para ver mais informações sobre o post. Ao clicar nesse botão a aplicação irá redirecionar o usuário para uma página que mostra mais detalhes sobre aquele post, como a descrição e o autor. 

Na página de informações sobre o post, caso o usuário que a acessou seja o autor do post, aparecem botões para editar o conteúdo (título e descrição) ou excluí-lo. Os botões são mostrados somente para o autor, e caso outro usuário tente acessar a rota de editar ou excluir um post que não foi feito por ele, o mesmo será redirecionado para uma página de erro.

Também é possível visitar o seu próprio perfil, ou o perfil de outro usuário. No perfil é mostrado o nome e todos os posts criados por ele.