from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mensagem': 'Pessoa não cadastrada.'
            }
        return response

    def put(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            dados = request.json
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mensagem': 'Pessoa não cadastrada.'
            }
        return response

    def delete(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            pessoa.delete()
            return {'status': 'Sucesso', 'mensagem': f'Cadastro de: {pessoa.nome}, deletado.'}
        except AttributeError:
            return {'status': 'erro', 'mensagem': 'Cadastro não encontrado.'}


class ListarPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade}for i in pessoas]
        return response


class CadastrarPessoa(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class CadastrarAtividade(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


class ListarAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'pessoa': i.pessoa.nome, 'nome': i.nome} for i in atividades]
        return response


class ListarAtividadesId(Resource):
    def get(self, id):
        atividades = Atividades.query.filter_by(id=id)
        response = [{'id': i.id, 'pessoa': i.pessoa.nome, 'nome': i.nome} for i in atividades]
        return response


class DeletarAtividade(Resource):
    def delete(self, id):
        try:
            atividades = Atividades.query.filter_by(id=id).first()
            atividades.delete()
            return {'status': 'Sucesso', f'mensagem': f'Atividade {id} deletada.'}
        except AttributeError:
            return {'status': 'erro', 'mensagem': 'Atividade não encontrada.'}


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListarPessoas, '/listar_pessoas/')
api.add_resource(CadastrarPessoa, '/cadastro_pessoa/')
api.add_resource(CadastrarAtividade, '/cadastro_atividade/')
api.add_resource(ListarAtividades, '/listar_atividades/')
api.add_resource(ListarAtividadesId, '/listar_atividades/<int:id>/')
api.add_resource(DeletarAtividade, '/deletar_atividade/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
