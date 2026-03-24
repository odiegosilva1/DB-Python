from database import db, Usuario, Anuncio

db.connect()
db.create_tables([Usuario, Anuncio])

# Criando um usuário
#usuario1 = Usuario.create(nome='João Silva', email='joao.silva@example.com', senha='senha123')
#usuario1 = Usuario.create(nome='Maria Silva', email='maria.silva@example.com', senha='senha123')
#usuario1 = Usuario.create(nome='jujubinha', email='jujubinha@example.com', senha='senha123')

lista_usuarios = Usuario.select()
print("Lista de usuários:")

for u in lista_usuarios:
    print("-", u.nome, "-", u.email)