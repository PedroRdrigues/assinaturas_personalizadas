# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:27:47 2025

@author: PedroRdrigues
"""

from assinatura import Assinatura
from utils import formatar_telefone


nomeColaborador = 'Pedro Henrique Rodrigues'.strip().title().split(' ')
nomeColaborador = f"{nomeColaborador[0]} {nomeColaborador[-1]}"

cargo = 'Auxiliar de TI'

empresa = 'Mônaco Participações'

fone = '9130758492'

cell = '91992512077'

contatos = " / ".join(formatar_telefone([fone, cell]))

email = 'pedrorodrigues'.lower()


Assinatura(nomeColaborador, cargo, empresa, contatos, email)
print(f'Assinatura de {nomeColaborador} criada')
