from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import psycopg2

# Criação da janela principal
login = Tk()
login.geometry("800x500")
login.title("Sistema de Empréstimo")

# Adicionando um Frame vertical à esquerda com cor cinza escuro e largura aumentada
frame_esquerdo = Frame(login, bg="#333333", width=200)  # Largura aumentada para 200 pixels
frame_esquerdo.place(x=0, y=0, height=500)  # Posição e altura do frame

# Caminho para a imagem
img_path = 'C:/Users/Carlos/Downloads/PYTHON.PNG'

# Carregar a imagem e criar o objeto ImageTk.PhotoImage
imagem = Image.open(img_path)
imagem = imagem.resize((150, 150))  # Ajuste o tamanho da imagem conforme necessário
imagem_tk = ImageTk.PhotoImage(imagem)

# Adicionar a imagem ao Frame e centralizá-la
label_imagem = Label(frame_esquerdo, image=imagem_tk, bg="#333333")  # Background para combinar com o frame
label_imagem.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centralizar a imagem no frame

# Texto de Login
texto_login = Label(login, text="Sistema de Empréstimo", font=("Arial Black", 17), fg="#3b3b3b")
texto_login.place(x=280, y=50)

# Texto "Aluno" e "Turma"
texto_aluno = Label(login, text="Aluno:", font=("Arial", 12))
texto_aluno.place(x=270, y=150)

texto_turma = Label(login, text="Turma:", font=("Arial", 12))
texto_turma.place(x=265, y=220)

# Campo de Aluno
campo_aluno = Entry(login, font=(10), width=20)
campo_aluno.place(x=320, y=150)

def obter(eventObject):
    v = combo.get()


# Campo de Turma
combo = Combobox(login)
combo["values"]= ("3K", "3J", "3C", "3D","Selecione sua Turma")
combo.current(4) 
combo.place(x=320, y=220)
combo.bind('<<ComboboxSelected>>',obter)

# Botão
botao_entrar = Button(login, text="Entrar no Sistema", bg="#3b3b3b", fg="White", font=("Arial Black", 11))
botao_entrar.place(x=310, y=330)

# Iniciar o loop principal
login.mainloop()
