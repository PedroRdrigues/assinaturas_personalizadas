# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:39:42 2025

@author: PedroRdrigues
"""

def formatar_telefone(numeros):
    numero_formatado = list()
    for numero in numeros:
        if len(numero) == 11:
            numero_formatado.append(f"({numero[:2]}) {numero[2:7]}-{numero[7:]}")
        elif len(numero) == 10:
            numero_formatado.append(f"({numero[:2]}) {numero[2:6]}-{numero[6:]}")
    
    return numero_formatado