import gradio as gr
import math


def fatorial(num):
    return (
        math.factorial(num)
        if num >= 0
        else "Fatorial não definido para números negativos"
    )


iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Calculadora de Fatorial",
    description="Insira um número para obter o fatorial",
)

iface.launch()
