# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:56:26 2025

@author: PedroRdrigues
"""

from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont

""" CRIAR UMA CLASSE "ASSINATURA" E A PARTIR DELA CRIAR METODOS DE CRIAÇÃO DAS ASSINATURAS ESPECIFICAS """

# Classe de criação de assinaturas
@dataclass()
class Assinatura:
    nomeColaborador: str
    cargo: str
    empresa: str
    contatos: str
    email: str

    def __post_init__(self):  # Verifica qual a empresa do usuário e chama o respectivo método
        if 'Motocenter' in self.empresa.title():
            print(f'Created siginature from {self.empresa}')
            self.motocenter()

        elif 'Veículos' in self.empresa.title() or 'Fiat' in self.empresa.title():
            print(f'Created siginature from {self.empresa}')
            self.veiculos()

        elif 'Participações' in self.empresa.title():
            print(f'Created siginature from {self.empresa}')
            self.holding()

    def motocenter(self):
        # Carregar a imagem base
        self.imagem_base = Image.open(
            'assets/img-base/ass-honda.png')

        # Criar um objeto para desenhar
        draw = ImageDraw.Draw(self.imagem_base)

        # NOME
        draw.text((25, 16), self.nomeColaborador, fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Bold.ttf', 28))
        # draw.text(xy, text, args, kwargs)

        # CARGO
        draw.text((25, 51), self.cargo, fill='#fff',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Bold.ttf', 13))

        # EMPRESA
        draw.text((43, 92), self.empresa, fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 13))

        # NUMERO
        draw.text((43, 108), str(self.contatos), fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 12))

        # E-MAIL
        draw.text((43, 123), f'{self.email}@grupomonaco.com.br', fill='#fff',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Medium.ttf', 12))

        self.saveImage()

    def holding(self):
        # Carregar a imagem base
        self.imagem_base = Image.open(
            'assets/img-base/ass-holding.png')

        # Criar um objeto para desenhar
        draw = ImageDraw.Draw(self.imagem_base)

        # NOME
        draw.text((25, 18), self.nomeColaborador, fill='#000', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Bold.ttf', 28))
        # draw.text(xy, text, args, kwargs)

        # CARGO
        draw.text((25, 51), self.cargo, fill='#000',
                  font=ImageFont.truetype('assets/fonts/Montserrat-SemiBold.ttf', 13))

        # EMPRESA
        draw.text((43, 82), self.empresa, fill='#000', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Regular.ttf', 13.5))

        # CONTATOS
        draw.text((43, 100), str(self.contatos), fill='#000', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Regular.ttf', 13.5))

        # E-MAIL
        draw.text((43, 117), f'{self.email}@grupomonaco.com.br', fill='#000',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Regular.ttf', 13.5))

        self.saveImage()

    def veiculos(self):
        # Carregar a imagem base
        self.imagem_base = Image.open(
            'assets/img-base/ass-fiat.png')

        # Criar um objeto para desenhar
        draw = ImageDraw.Draw(self.imagem_base)

        # NOME
        draw.text((25, 16), self.nomeColaborador, fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Bold.ttf', 28))
        # draw.text(xy, text, args, kwargs)

        # CARGO
        draw.text((25, 51), self.cargo, fill='#fff',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Bold.ttf', 13))

        # EMPRESA
        draw.text((43, 92), "Mônaco Veículos", fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 12))

        # NUMERO
        draw.text((43, 108), str(self.contatos), fill='#fff', font=ImageFont.truetype(
            'assets/fonts/Montserrat-Medium.ttf', 12))

        # E-MAIL
        draw.text((43, 123), f'{self.email}@grupomonaco.com.br', fill='#fff',
                  font=ImageFont.truetype('assets/fonts/Montserrat-Medium.ttf', 12))

        self.saveImage()

    # Salvar a nova imagem
    @staticmethod
    def saveImage(imagem_base, email):
        imagem_base.save(f'assinaturas/ass-{email}.png')
        
        """ CRIAR UMA FORMA DE SALVAR A IMAGEM EM UM SERVIDOR """
        import requests
        
        url = "http://localhost:8000"  # Substitua pelo URL do seu servidor
        
        # Abra a imagem no modo binário
        with open("assinaturas/ass-pedrorodrigues.png", "rb") as img:
            files = {"file": img}  # O dicionário deve conter a chave esperada pelo servidor
            response = requests.post(url, files=files)
        
        # Verificar a resposta do servidor
        if response.status_code == 200:
            print("Imagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar imagem: {response.status_code} - {response.text}")

