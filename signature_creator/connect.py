# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:29:21 2025

@author: PedroRdrigues
"""

from dataclasses import dataclass, field
import cx_Oracle
from tkinter import messagebox


""" FAZ A CONEXÃO COM O BANCO DE DADOS """


# Classe para manipular o db
class DB:
    def connect_db(self):  # Estabelece uma conexão com o db e cria um corsor
        try:
            self.connection = cx_Oracle.connect(
                # usar configuração de um arquivo .ini
                'DEV', 'Monaco@2025', 'localhost:1521/XEPDB1')

            self.cursor = self.connection.cursor()

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror(
                title='AutoSign',
                message=f"Erro ao conectar ao banco de dados: {e}"
            )

            self.cursor.close()
            self.connection.close()

    def close_db(self):  # Fechar a conexão e o cursor
        self.cursor.close()
        self.connection.close()

    def countTable(self):  # Faz a contagem de quantas linhas existem na tabela
        self.connect_db()
        self.cursor.execute("SELECT COUNT(*) FROM user_assinatura")
        c = [i for i in self.cursor][0][0]

        if isinstance(c, int):
            return c

        self.close_db()

    # criar um método que faça um SELECT de cada email_user da tabela


# Classe para coleta de dados de determinado usuário
@dataclass
class UserAssinatura(DB):
    id_user: str = field(init=False)
    nome: str = field(init=False)
    cargo: str = field(init=False)
    empresa: str = field(init=False)
    telefone: str = field(init=False)
    celeular: str = field(init=False)
    email_user: str

    def __post_init__(self):
        # self.user_data = list
        self.select_userData()

    def select_userData(self):  # Faz a consulta dos dados do usuário
        self.connect_db()

        self.cursor.execute("""
                            SELECT * FROM user_assinatura 
                            WHERE email_user = :email_user
                            """,
                            {'email_user': self.email_user})

        self.user_data = [u for u in self.cursor]
        self.setDatas()
        self.close_db()

    def setDatas(self):  # Define os valores de cada variavel com os dados do usuário
        self.id_user = self.user_data[0][0]
        self.nome = self.user_data[0][1]
        self.cargo = self.user_data[0][2]
        self.empresa = self.user_data[0][3]
        self.telefone = self.user_data[0][4]
        self.celular = self.user_data[0][5]
