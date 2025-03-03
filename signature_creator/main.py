# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:27:47 2025

@author: PedroRdrigues
"""

from assinatura import Assinatura
from connect import UserAssinatura, DB
from utils import formatar_telefone


# nomeColaborador = "Pedro Henrique Rodriguese de Sá".strip().title().split(' ')
# nomeColaborador = f"{nomeColaborador[0]} {nomeColaborador[-1]}"
 
# cargo = "Auxiliar de TI"

# empresa = "Mônaco Participações"

# fone = None

# cell = "91992512077"

# contatos = " / ".join(formatar_telefone([fone, cell]))

# email ="pedrorodrigues".lower()


# Assinatura(nomeColaborador, cargo, empresa, contatos, email)
# print(f'Assinatura de {nomeColaborador} criada')


""" CRIAR UMA COLUNA NO DB PARA USUÁRIOS COM O NOME DA ASSINATURA DESEJAM SER ALTERADOS
    E CASO A COLUNA ESTEJA VAZIA PARA ALGUM USUÁRIO ELE UTILIZARÁ O PADRÃO DO PROGRAMA """


db = DB()

for i in range(db.countTable()):
    user = UserAssinatura('giovanni.mt')
    
    nomeColaborador = user.nome.strip().title().split(' ')
    nomeColaborador = f"{nomeColaborador[0]} {nomeColaborador[-1]}"
    
    cargo = user.cargo
    
    empresa = user.empresa
    
    fone = user.telefone
    
    cell = user.celular
    
    contatos = " / ".join(formatar_telefone([fone, cell]))
    
    email = user.email_user.lower()
    
    
    Assinatura(nomeColaborador, cargo, empresa, contatos, email)
    print(f'Assinatura de {nomeColaborador} criada')
