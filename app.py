import code
from tkinter import INSERT
import pyodbc

dados_conexao=(
    "Driver={SQL Server};"
    "Server=myserver;"
    "Database=mydb"
    "Username=myusername"
    "password=mypassword"
)

conexao=pyodbc.connect(dados_conexao)

cursor=conexao.cursor()

cod='g'

while cod!='f':
    nome=input('Digite seu nome:')
    produto=input('Digite o produto comprado')
    
    data_compra=input('Digite a data da compra: ')
    nacionalidade=input('Nacionalidade do cliente: ')
    
    preco=float(input('Preço do Produto: '))
    sexo=input('Digite M para sexo masculino e F para feminino: ')
    
    cpf=input("Digite o CPF do cliente: ")
    
    comando= """INSERT INTO loja
    VALUES
    ('{nome}', '{produto}', '{data_compra}', '{nacionalidade}', '{preco}', '{sexo}', {cpf} )"""
    cursor.execute(comando)
    cursor.commit()

    cod=input('Digite f para parar e qualquer tecla para continuar: ')
          






