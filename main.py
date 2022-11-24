from model.pessoa import pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
lucas = pessoa(1, "Lucas Marques")
print(lucas)

#Quero mostrar só o nome
print(lucas.nome)

print("DAQUI PRA FRENTE É ACESSO AO BONCO...")

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados

pessoas = pessoaDAO.getAll(orderBy=True)
for Pessoa in pessoas:
  print(Pessoa)

#Criar um objeto com qualquer ator/atriz...
novo = pessoa(0, "Denzel Washington")
novo = pessoaDAO.save(novo)

#Consulta o banco de novo...
print("NOVA CONSULTA")
pessoas = pessoaDAO.getAll(orderBy=True)
for Pessoa in pessoas:
  print(Pessoa)
