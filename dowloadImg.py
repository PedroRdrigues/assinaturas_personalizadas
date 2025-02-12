# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:59:33 2025

@author: PedroRdrigues
"""
import getpass
import requests

# URL da imagem
url = 'http://127.0.0.1:8000/pedrorodrigues.png'

# Nome do arquivo onde você quer salvar a imagem
nome_arquivo = f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Assinaturas\\testes_arquivos\\image001.jpg'

# Baixando a imagem
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Salvando a imagem no arquivo
    with open(nome_arquivo, 'wb') as f:
        f.write(response.content)
    print(f'Imagem salva como {nome_arquivo}')
else:
    print('Erro ao baixar a imagem. Status code:', response.status_code)
