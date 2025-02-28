# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:56:26 2025

@author: PedroRdrigues
"""

from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont

""" CRIAR UMA CLASSE "ASSINATURA" E A PARTIR DELA CRIAR METODOS DE CRIAÇÃO DAS ASSINATURAS ESPECIFICAS """

@dataclass()
class Assinatura:
    nomeColaborador:str
    cargo:str
    empresa:str
    contatos:str
    email:str
    
    def __post_init__(self):
        if 'Motocenter' in self.empresa.title():
            print(f'Created siginature from {self.empresa}')
            self.motocenter(self.nomeColaborador, self.cargo, self.empresa, self.contatos, self.email)
            
        elif 'Veículos' in self.empresa.title() or 'Fiat' in self.empresa.title():
            print(f'Created siginature from {self.empresa}')
            self.veiculos(self.nomeColaborador, self.cargo, self.empresa, self.contatos, self.email)
            
        elif 'Participações' in self.empresa.title():
            print(f'Created siginature from {self.empresa}')
            self.holding(self.nomeColaborador, self.cargo, self.empresa, self.contatos, self.email)
    
    
        
    @staticmethod    
    def motocenter(nomeColaborador:str, cargo:str, empresa:str, contatos:str, email:str):
        # Carregar a imagem base
        imagem_base = Image.open(
            'assets/img-base/ass-honda.png')
        
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
            'assets/fonts/Montserrat-Medium.ttf', 13))
        
        # NUMERO
        draw.text((43, 108),str(contatos), fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 12))
        
        #E-MAIL
        draw.text((43, 123), f'{email}@grupomonaco.com.br', fill='#fff',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Medium.ttf', 12))
        
        
        # Salvar a nova imagem
        imagem_base.save(f'assinaturas/ass-{email}.png')
        
        
    @staticmethod
    def holding(nomeColaborador:str, cargo:str, empresa:str, contatos:list, email:str):
        # Carregar a imagem base
        imagem_base = Image.open(
            'assets/img-base/ass-holding.png')
        
        # Criar um objeto para desenhar
        draw = ImageDraw.Draw(imagem_base)
        
        # NOME
        draw.text((25, 18), nomeColaborador , fill='#000', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Bold.ttf', 28))
        # draw.text(xy, text, args, kwargs)
        
        # CARGO
        draw.text((25, 51), cargo, fill='#000',
                  font=ImageFont.truetype('assets/fonts/Montserrat-SemiBold.ttf', 13))
        
        #EMPRESA
        draw.text((43, 82), empresa, fill='#000', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Regular.ttf', 13.5))
        
        # CONTATOS
        draw.text((43, 100),str(contatos), fill='#000', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Regular.ttf', 13.5))
        
        #E-MAIL
        draw.text((43, 117), f'{email}@grupomonaco.com.br', fill='#000',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Regular.ttf', 13.5))
        
        
        # Salvar a nova imagem
        imagem_base.save(f'assinaturas/ass-{email}.png')
        
        
    @staticmethod    
    def veiculos(nomeColaborador:str, cargo:str, empresa:str, contatos:list, email:str):
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
        draw.text((43, 92), "Mônaco Veículos", fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 12))
        
        # NUMERO
        draw.text((43, 108),str(contatos), fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 12))
        
        #E-MAIL
        draw.text((43, 123), f'{email}@grupomonaco.com.br', fill='#fff',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Medium.ttf', 12))
        
        
        # Salvar a nova imagem
        imagem_base.save(f'assinaturas/ass-{email}.png')
    
