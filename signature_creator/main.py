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

numero = " / ".join(formatar_telefone(['9130758492', '91992512077']))


email = 'pedrorodrigues'.lower()

Assinatura(nomeColaborador, cargo, empresa, numero, email)
print(f'Assinatura de {nomeColaborador} criada')
