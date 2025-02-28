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


"""INTERFACE PARA CONFIGURAÇÃO DO USUÁRIO E SELEÇÃO DE OPÇÕES DE PROGRAMA GERENCIADOR DE E-MAIL"""


for user in listdir("users/"):
    # Criar um objeto ConfigParser
    config = configparser.ConfigParser()
    
    # Ler o arquivo INI
    config.read(f"users/{user}")
    
    # Usuário de e-mail
    email = config["USER"]["email"]
    
    # Opção do programa gerenciador de e-mails
    option = config["USER"]["option"]
    
    # Nome da imagem armazenada no servidor    
    image = config["SERVER"]["image"]
    
    
    # URL da imagem
    url = f'http://10.3.132.89:8085//{image}'
    
    # Caminho do arquivo onde você quer salvar a imagem    
    if option == 'Outlook': # Salva dentro dos arquivos internos do outlook 2010
        caminho_arquivo = f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Assinaturas\\123teste_arquivos\\image001.jpg'
    
    elif option == 'ThunderBird': # Deve ser selecionado onde irá ser salvo a assinatura
        caminho_arquivo = f'{config["USER"]["path"]}\\{image}'

    
    
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
