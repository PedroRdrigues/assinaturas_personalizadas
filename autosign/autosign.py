# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:59:33 2025

@author: PedroRdrigues
"""

import getpass
import requests
from tkinter import messagebox
import configparser
from os import listdir


""" USAR O LISTDIR PARA VERIFICAR QUANTOS ARQUIVOS EXISTEM DENTRO DO DIRETÓRIO 'USERS' E VERIFICAR OS DADOS DE CADA UM """


# Criar um objeto ConfigParser
config = configparser.ConfigParser()

# Ler o arquivo INI
config.read("config.ini")

# Usuário de e-mail
email = config["USER"]["email"]

# Opção do programa gerenciador de e-mails
option = config["USER"]["option"]

image = config["SERVER"]["image"]




"""INTERFACE PARA CONFIGURAÇÃO DO USUÁRIO E SELEÇÃO DE OPÇÕES DE PROGRAMA GERENCIADOR DE E-MAIL"""




# URL da imagem
url = f'localhosto:8000/{image}' # usar configração de host de um arquivo .ini

# Caminho do arquivo onde você quer salvar a imagem
caminho_outlook = f'C:\\Users\\{getpass.getuser(\
)}\\AppData\\Roaming\\Microsoft\\Assinaturas\\testes_arquivos\\image001.jpg'
    
caminho_thunderbird = f'C:\\Windows\\autosign\\ass-{email}.png'


if option == 'outlook':
    caminho_arquivo = caminho_outlook
elif option == 'thunderbird':
    caminho_arquivo = caminho_thunderbird

try:
    # Baixando a imagem
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Salvando a imagem no arquivo
        with open(caminho_arquivo, 'wb') as f:
            f.write(response.content)

except Exception as e:
    messagebox.showerror(
              title='AutoSign',
              message=f"Requisição de download falhou: {e}"
              )
