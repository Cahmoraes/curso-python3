import tkinter as tk

window = tk.Tk()
window.geometry("300x150")
window.title("Gerencia Frases")

frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Estado do label e do input
label_text = tk.StringVar(value="Olá mundo")
entry_text = tk.StringVar()

# Label vinculado ao StringVar
label = tk.Label(frame, textvariable=label_text)
label.pack(fill="x", expand=True)

# Campo de entrada
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill="x", expand=True)

frase_inp = tk.Entry(frame, textvariable=entry_text)
frase_inp.pack(fill="x", expand=True)
frase_inp.focus()  # foco inicial


def enviar():
    # Atualiza o label com o texto do input
    label_text.set(entry_text.get())


def copiar_do_label():
    # (opcional) copia o texto do label para o input
    entry_text.set(label_text.get())


button = tk.Button(frame, text="Enviar", command=enviar)
button.pack(pady=4)

# (opcional) botão para copiar do label para o input
btn_copiar = tk.Button(frame, text="Copiar do label", command=copiar_do_label)
btn_copiar.pack()

window.mainloop()
