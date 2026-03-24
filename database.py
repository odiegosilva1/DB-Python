from peewee import *  # type: ignore

db = SqliteDatabase('database.db')


# Criando a tabela de usuários
class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db

# Criando a tabela de anuncios
class Anuncio(Model):
    usuario = ForeignKeyField(Usuario , backref='anuncios') 

    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()

    class Meta:
        database = db      

