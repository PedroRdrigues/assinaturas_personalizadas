# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:56:26 2025

@author: PedroRdrigues
"""

from PIL import Image, ImageDraw, ImageFont

""" CRIAR UMA CLASSE "ASSINATURA" E A PARTIR DELA CRIAR METODOS DE CRIAÇÃO DAS ASSINATURAS ESPECIFICAS """
#class Assinatura:
    #def holding():
    #def motocenter():
    #def veiculos():
        
        
def assinatura(nomeColaborador:str, cargo:str, empresa:str, telefones:list, email:str):
    # Carregar a imagem base
    imagem_base = Image.open(
        'assets/img-base/ass-fiat.png')
    
    # Criar um objeto para desenhar
    draw = ImageDraw.Draw(imagem_base)
    
    # NOME
    draw.text((25, 16), nomeColaborador , fill='#fff', font=ImageFont.truetype(
        'assets/fonts/Montserrat-Bold.ttf', 28))
    # draw.text(xy, text, args, kwargs)
    
    # CARGO
    draw.text((25, 51), cargo, fill='#fff',
              font=ImageFont.truetype('assets/fonts/Montserrat-Bold.ttf', 13))
    
    #EMPRESA
    draw.text((43, 92), empresa, fill='#fff', font=ImageFont.truetype(
        'assets/fonts/Montserrat-Medium.ttf', 12))
    
    # NUMERO
    draw.text((43, 108),str(telefones), fill='#fff', font=ImageFont.truetype(
        'assets/fonts/Montserrat-Medium.ttf', 12))
    
    #E-MAIL
    draw.text((43, 123), f'{email}@grupomonaco.com.br', fill='#fff',
              font=ImageFont.truetype('assets/fonts/Montserrat-Medium.ttf', 12))
    
    
    # Salvar a nova imagem
    imagem_base.save(f'assinaturas/ass-{email}.png')

