class Pessoa:
  def __init__(self, nome = None, idade=30):
    self.idade = idade
    self.name = nome

  def cumprimentar(self):
    return f'Olá {id(self)}'

if __name__ == '__main__':
  p = Pessoa('Simone')
  print(p.cumprimentar())
  print(p.name)
  p.name = 'Everton Reis'
  print(p.name)
  print(p.idade)
