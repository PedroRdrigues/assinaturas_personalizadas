# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 23:18:44 2025

@author: PedroRdrigues
"""

import http.server
import socketserver
import os

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Obtém o tamanho do conteúdo
        field_data = self.rfile.read(content_length)  # Lê os dados enviados

        # Define o diretório de upload
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        # Salva o arquivo
        file_path = os.path.join(upload_dir, "imagem_recebida.png")
        with open(file_path, "wb") as f:
            f.write(field_data)

        # Responde ao cliente
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Upload recebido com sucesso!")

# Inicia o servidor na porta 8000
PORT = 8000
with socketserver.TCPServer(("127.0.0.1", PORT), UploadHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()
