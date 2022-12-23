from models import Pessoas, Usuarios


def inserir_pessoas():
    pessoa = Pessoas(nome='João', idade=30)
    print(pessoa)
    pessoa.save()


def consultar_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='João').first()
    print(pessoa.idade)


def alterar_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Marcela').first()
    pessoa.nome = 'Ashia'
    pessoa.save()


def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome='').first()
    pessoa.delete()


def inserir_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consultar_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)


def excluir_usuario(nome):
    usuario = Usuarios.query.filter_by().first()
    usuario.delete()


if __name__ == '__main__':
    inserir_usuario('pedrin', '198090')
    consultar_usuario()
