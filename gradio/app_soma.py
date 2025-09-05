import gradio as gr


def somar(n1, n2):
    return n1 + n2


print(somar(5, 4))

iface = gr.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora de soma",
    description="Insira dois números para obter a soma",
    theme="default",
)

iface.launch()
