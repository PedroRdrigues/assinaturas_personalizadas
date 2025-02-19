# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:29:21 2025

@author: PedroRdrigues
"""

import cx_Oracle


""" FAZER A CONEXÃO COM O BANCO DE DADOS """


# Parâmetros de conexão (ajuste conforme necessário)
username = 'DEV'
password = 'Monaco@2025'
dsn = 'localhost:1521/XEPDB1'  # O DSN padrão do Oracle XE (ajuste conforme seu banco)

try:
    # Estabelecendo a conexão
    connection = cx_Oracle.connect(username, password, dsn)
    print("Conexão bem-sucedida!")

    # Criando um cursor para executar consultas SQL
    cursor = connection.cursor()

    # Exemplo de consulta SQL
    cursor.execute("SELECT * FROM user_assinatura")
    for row in cursor:
        print(row)

except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    # Fechar a conexão e o cursor
    cursor.close()
    connection.close()
