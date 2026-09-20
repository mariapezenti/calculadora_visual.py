import customtkinter as ctk

app = ctk.CTk()
app.title("Calculadora")
app.geometry("300x400")

tela = ctk.CTkFrame(
    app, 
    width=280, 
    height=50, 
    front=("Arial",24),
    justify="right"
)
tela.pack(pady=20)

frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack()

def clique_botao(texto):
    tela.insert("end", texto)

botoes = ['7','8','9','/']

for i, txt in enumerate(botoes):
btn = ctk.CTkButton(
      frame_botoes, 
      text=txt, 
      width=30,
      height=30, 
      font=("Arial",20),
      command=lambda t=txt: clique_botao(t)
)
btn.grid(row=0, column=i, padx=5, pady=5)

app.mainloop()