from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='João', idade=30)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome='João').first()
    # print(pessoa.idade)


def alterar_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Ashia').first()
    pessoa.nome = 'Marcela'
    pessoa.save()


def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #alterar_pessoas()
    excluir_pessoas()
    consulta_pessoas()
