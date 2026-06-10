# Exercício 1

# import tkinter as tk
# from tkinter import messagebox, ttk

# def bemvindo():
    
#     nome_usuario = usuario_nome.get()
#     turno_usaario = usuario_turno.get()

#     if nome_usuario == "" and turno_usaario == "":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e idade! :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá operador {nome_usuario}, registrado no Turno {turno_usaario}.Boa jornada ")

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela_bemvindo)
#     segunda_janela.title("Segunda Janela")
#     segunda_janela.geometry("500x500")




# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações do Usuário")
# janela_bemvindo.geometry("500x500")


# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome: )")
# lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)

# lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite seu turno :)")
# lbl_mensagem_idade.grid(row=3, column=0, pady=10, padx=10)


# usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_nome.grid(row=2,column=1,pady=10,padx=10)

# usuario_turno = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_turno.grid(row=3,column=1,pady=10,padx=10)



# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo)
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)


# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
# btn_fechar_janela.grid(row=4, column=0, pady=10, padx=10)


# janela_bemvindo.mainloop()

#exercício 2 

# import tkinter as tk
# from tkinter import messagebox, ttk

# def calcularr_media(quantidade_peças1):
#     try:
#         media = (quantidade_peças1 ) * 8
#         return media
#     except TypeError:
#         return "Erro"
    
# def bemvindo():
    
#     quantidade_peças1 = produção_1.get()
#     turno_usaario = produção_1.get()

#     if quantidade_peças1 == "" and turno_usaario == "":
#         messagebox.showwarning("Aviso", "a produção daqui a 8horas será de :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"a produção daqui a 8horas será de {quantidade_peças1}")

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela_bemvindo)
#     segunda_janela.title("Segunda Janela")
#     segunda_janela.geometry("500x500")


# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações do Usuário")
# janela_bemvindo.geometry("500x500")


# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="quantidade de peças em 1 hora: )")
# lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)

# produção_1= tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# produção_1.grid(row=2,column=1,pady=10,padx=10)

# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo)
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)


# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
# btn_fechar_janela.grid(row=4, column=0, pady=10, padx=10)

# janela_bemvindo.mainloop()


# Exercício 4

# import tkinter as tk
# from tkinter import messagebox, ttk

# def bemvindo():
   
#     nota1_usuario = nota1_usuario.get()
#     nota2_usuario = nota2_usuario.get()
#     nota3_usuario = nota3_usuario.get()
#     if nota1_usuario == "" and nota2_usuario == "":
#         messagebox.showwarning("Aviso", "por favor avalie a peça:")
#     else:
#         messagebox.showinfo(print(input("Bem-Vindo", f" A média da inpeção desta peça é de  {nota1_usuario + nota2_usuario + nota3_usuario/3  },")))

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela_bemvindo)
#     segunda_janela.title("Segunda Janela")
#     segunda_janela.geometry("500x500")

#     num1 = float(input(" digite o primeiro valor: "))
#     num2 = float(input("digite o segundo valor:"))
#     num3 = float(input("digite o terceiro valor:"))

# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("avaliação de peças")
# janela_bemvindo.geometry("500x500")


# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite a primeira nota :")
# lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)

# lbl_mensagem_nota3 = tk.Label(janela_bemvindo, text="Digite a segunda nota:")
# lbl_mensagem_nota3.grid(row=3, column=0, pady=10, padx=10)

# lbl_mensagem_nota3 = tk.Label(janela_bemvindo, text="Digite a terceira nota :") 
# lbl_mensagem_nota3.grid(row=4, column=0, pady=10, padx=10)


# usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_nome.grid(row=2,column=1,pady=10,padx=10)

# usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_idade.grid(row=3,column=1,pady=10,padx=10)

# usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# usuario_idade.grid(row=4,column=1,pady=10,padx=10)




# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo)
# btn_enviar_mensagem.grid(row=5, column=1, pady=10, padx=10)


# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
# btn_fechar_janela.grid(row=5, column=0, pady=10, padx=10)


# janela_bemvindo.mainloop()

# Exercício 5


# import tkinter as tk
# from tkinter import messagebox, ttk

# def temperatura():
#     if temperatura == ""and 40 =="":
#         messagebox.showwarning ("Baixa carga ")
      
    
    
#     quantidade_peças1 = produção_1.get()
#     turno_usaario = produção_1.get()

#     if quantidade_peças1 == "" and turno_usaario == "":
#         messagebox.showwarning("Aviso", "a produção daqui a 8horas será de :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"a produção daqui a 8horas será de {quantidade_peças1}")

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela_bemvindo)
#     segunda_janela.title("Segunda Janela")
#     segunda_janela.geometry("500x500")


# janela_bemvindo = tk.Tk()
# janela_bemvindo.title(" aviso ")
# janela_bemvindo.geometry("500x500")


# lbl_mensagem_usuario = tk.Label(janela_bemvindo, text=" informe a temperatura do motor:")
# lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)

# produção_1= tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# produção_1.grid(row=2,column=1,pady=10,padx=10)

# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=("bemvindo"))
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)


# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
# btn_fechar_janela.grid(row=4, column=0, pady=10, padx=10)

# janela_bemvindo.mainloop()

