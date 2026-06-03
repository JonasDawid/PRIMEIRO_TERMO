# import tkinter as tk
# from tkinter import messagebox, ttk

# def bemvindo():
#     # .get() serve para buscar o texto da caixa
#     nome_usuario = usuario_nome.get()
#     idade_usaario = usuario_idade.get()

#     if nome_usuario == "" and idade_usaario == "":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e idade! :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! e sua idade é {idade_usaario}")

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela_bemvindo)
#     segunda_janela.title("Segunda Janela")
#     segunda_janela.geometry("500x500")



# # Janela
# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações do Usuário")
# janela_bemvindo.geometry("500x500")

# # Componentes
# # Labels
# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
# lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)

# lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade :)")
# lbl_mensagem_idade.grid(row=3, column=0, pady=10, padx=10)

# # Entrys
# usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_nome.grid(row=2,column=1,pady=10,padx=10)

# usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_idade.grid(row=3,column=1,pady=10,padx=10)

# # Componentes de ComboBox
# combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrocos", "Egito", "Escócia"], width=30)
# combo_nivel.grid(row=1, column=1, pady=10, padx=10)

# # Botão
# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo)
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)

# btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela", command=janela_bemvindo)
# btn_segunda_janela.grid(row=4, column=2, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
# btn_fechar_janela.grid(row=4, column=0, pady=10, padx=10)

# # Rodar interface
# janela_bemvindo.mainloop()

# import tkinter as tk
# from tkinter import messagebox, ttk

# def empréstimo ():
#     # .get() serve para buscar o texto da caixa
#     nome_usuario = usuario_nome.get()
#     idade_usaario = usuario_idade.get()

#     if nome_usuario == "" and idade_usaario == "":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e idade! :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! e sua idade é {idade_usaario}")

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela_bemvindo)
#     segunda_janela.title("Segunda Janela")
#     segunda_janela.geometry("500x500")



# # Janela
# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("bem- vindo a biblioteca ")
# janela_bemvindo.geometry("500x550")

# # Componentes
# # Labels
# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
# lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)


# # Entrys
# usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_nome.grid(row=2,column=1,pady=10,padx=10)



# # Componentes de ComboBox
# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="selecione a categoria do livro :)")
# lbl_mensagem_usuario.grid(row=1, column=0, pady=10, padx=10)
# combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["comum", "raro", "técnico", "infantil"], width=30)
# combo_nivel.grid(row=1, column=1, pady=10, padx=10)

# # Botão
# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command= janela_bemvindo)
# btn_enviar_mensagem.grid(row= 12, column=2, pady=10, padx=10)

# btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela", command=janela_bemvindo)
# btn_segunda_janela.grid(row=12, column=1, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
# btn_fechar_janela.grid(row=12 , column=0, pady=10, padx=10)

# # Rodar interface
# janela_bemvindo.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def emprestimo():
    nome_usuario = usuario_nome.get()
    idade_usuario = usuario_idade.get()
    categoria = combo_nivel.get()

    if nome_usuario == "" or idade_usuario == "":
        messagebox.showwarning(
            "Aviso",
            "Por favor, digite seu nome e idade!"
        )
    else:
        messagebox.showinfo(
            "Bem-vindo",
            f"Olá {nome_usuario}!\n"
            f"Idade: {idade_usuario}\n"
            f"Categoria escolhida: {categoria}"
        )


def segunda_janela():
    nova_janela = tk.Toplevel(janela_bemvindo)
    nova_janela.title("Área de Empréstimos")
    nova_janela.geometry("400x300")

    lbl = tk.Label(
        nova_janela,
        text="Bem-vindo à área de empréstimos!",
        font=("Arial", 12)
    )
    lbl.pack(pady=20)


# # Janela principal
# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Biblioteca")
# janela_bemvindo.geometry("500x300")


# titulo = tk.Label(
#     janela_bemvindo,
#     text="SISTEMA DE BIBLIOTECA",
#     font=("Arial", 18, "bold")
# )

# titulo.grid(row=0, column=0, columnspan=2, pady=20)
# # Nome
# lbl_nome = tk.Label(
#     janela_bemvindo,
#     text="Digite seu nome:"
# )
# lbl_nome.grid(row=2, column=2, padx=10, pady=10)

# usuario_nome = tk.Entry(
#     janela_bemvindo,
#     width=30
# )
# usuario_nome.grid(row=0, column=1, padx=10, pady=10)

# # Categoria
# lbl_categoria = tk.Label(
#     janela_bemvindo,
#     text="Selecione a categoria:"
# )
# lbl_categoria.grid(row=2, column=0, padx=10, pady=10)

# combo_nivel = ttk.Combobox(
#     janela_bemvindo,
#     values=["Comum", "Raro", "Técnico", "Infantil"],
#     width=27
# )
# combo_nivel.grid(row=2, column=1, padx=10, pady=10)
# combo_nivel.current(0)

# # Botões
# btn_enviar = tk.Button(
#     janela_bemvindo,
#     text="Enviar",
#     command=emprestimo
# )
# btn_enviar.grid(row=3, column=0, pady=20)

# btn_abrir = tk.Button(
#     janela_bemvindo,
#     text="Abrir Segunda Janela",
#     command=segunda_janela
# )
# btn_abrir.grid(row=3, column=1)

# btn_fechar = tk.Button(
#     janela_bemvindo,
#     text="Fechar",
#     command=janela_bemvindo.destroy
# )
# btn_fechar.grid(row=3, column=2)

# # Executar
# janela_bemvindo.mainloop()

# Janela principal
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Biblioteca")
janela_bemvindo.geometry("500x300")

# Título
titulo = tk.Label(
    janela_bemvindo,
    text="📚 SISTEMA DE BIBLIOTECA",
    font=("Arial", 18, "bold")
)
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Nome
lbl_nome = tk.Label(
    janela_bemvindo,
    text="Digite seu nome:"
)
lbl_nome.grid(row=1, column=0, padx=10, pady=10, sticky="w")

usuario_nome = tk.Entry(
    janela_bemvindo,
    width=30
)
usuario_nome.grid(row=1, column=1, padx=10, pady=10)

# Categoria
lbl_categoria = tk.Label(
    janela_bemvindo,
    text="Selecione a categoria:"
)
lbl_categoria.grid(row=2, column=0, padx=10, pady=10, sticky="w")

combo_nivel = ttk.Combobox(
    janela_bemvindo,
    values=["Comum", "Raro", "Técnico", "Infantil"],
    width=27
)
combo_nivel.grid(row=2, column=1, padx=10, pady=10)
combo_nivel.current(0)

# Botões
btn_enviar = tk.Button(
    janela_bemvindo,
    text="Enviar",
    command=emprestimo
)
btn_enviar.grid(row=3, column=0, padx=10, pady=20)

btn_abrir = tk.Button(
    janela_bemvindo,
    text="Abrir Segunda Janela",
    command=segunda_janela
)
btn_abrir.grid(row=3, column=1, padx=10, pady=20)

btn_fechar = tk.Button(
    janela_bemvindo,
    text="Fechar",
    command=janela_bemvindo.destroy
)
btn_fechar.grid(row=4, column=0, columnspan=2, pady=10)

# Executar
janela_bemvindo.mainloop()