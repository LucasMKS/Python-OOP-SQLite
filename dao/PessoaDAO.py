from model.pessoa import pessoa

class PessoaDAO:
  conexao = None
  cursor = None

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur

  def getAll(self, orderBy = False):
    sql = "SELECT id, nome FROM pessoa "
    if orderBy == True:
      sql = sql + " ORDER BY nome"

    try:
      self.cursor.execute(sql)
      resultado = self.cursor.fetchall()

      pessoas = []
      for linha in resultado:
        Pessoa = pessoa(linha[0], linha[1])
        pessoas.append(Pessoa)

      return pessoas
    except Exception as e:
      return e

  #Função/método para inserir no banco.
  def save(self, Pessoa):
    sql = "INSERT INTO Pessoa (nome) VALUES (%s)"

    try:
      self.cursor.execute(sql, Pessoa.nome)
      self.conexao.commit()
      Pessoa.id = self.cursor.lastrowid 
      return Pessoa
    except Exception as e:
      return e

    
