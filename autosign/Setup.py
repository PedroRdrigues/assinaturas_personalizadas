# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:09:54 2025

@author: PedroRdrigues
"""

""" CRIAR UMA INTERFACE QUE POSSA SER UTILIZADA PARA A CONFIGURAÇÃO DA ASSINATURA DO COLABORADOR """


import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.windows()
        self.widgets()

    def windows(self):
        self.title("AutoSign")
        self.geometry("400x150")
        self.resizable(False, False)
        self.grid_columnconfigure((0, 1), weight=1)

    def widgets(self):
        # Entry para informar qual o usuário do colaborador
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="E-mail User")
        self.entry.grid(row=0, column=0, padx=20, pady=(
            0, 20), sticky="ew", columnspan=2)

        # Checkbox para configuração do Outlook.
        self.checkbox_outlook = customtkinter.CTkCheckBox(self, text="Outlook")
        self.checkbox_outlook.grid(
            row=1, column=0, padx=20, pady=(0, 20), sticky="e")

        # Checkbox para configuração do ThunderBird.
        self.checkbox_thunderbird = customtkinter.CTkCheckBox(
            self, text="ThunderBird")
        self.checkbox_thunderbird.grid(
            row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        # Botão para gerar o arquivo .xml com o nome do usuário.
        self.button = customtkinter.CTkButton(
            self, text="Gerar AutoSign", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=20, pady=20,
                         sticky="ew", columnspan=2)

    def button_callback(self):
        print("Assinatura criada!")
        print(self.entry.get())


App().mainloop()
