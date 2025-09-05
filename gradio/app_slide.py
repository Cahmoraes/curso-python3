import gradio as gr
import numpy as np
from PIL import Image
import gradio as gr
import numpy as np
from PIL import Image
import io
import base64


def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
    """Cria um HTML de slide a partir dos parâmetros fornecidos.

    Recebe um array numpy como `imagem` (quando fornecido), converte para PNG em
    memória, codifica em base64 e insere como data URI no HTML. Não tenta decodificar
    bytes como UTF-8 (isso causava UnicodeDecodeError).
    """
    estilo = (
        f"background-color: {cor_fundo};",
        f"color: {cor_texto};",
        "padding: 20px;",
        "text-align: center;",
    )

    # Converte a imagem para base64 se estiver presente
    imagem_html = ""
    if imagem is not None:
        buffered = io.BytesIO()
        Image.fromarray(imagem).save(buffered, format="PNG")
        # encode image bytes to base64 string (não decodificar bytes como UTF-8)
        img_str = base64.b64encode(buffered.getvalue()).decode("ascii")
        imagem_html = (
            f"<img src='data:image/png;base64,{img_str}' "
            "style='max-width: 100%; height: auto;'>"
        )

    estilo_str = " ".join(estilo)
    slide_html = f"""
    <div style='{estilo_str}'>
      <h1>{titulo}</h1>
      <p>{texto}</p>
      {imagem_html}
    </div>
    """
    return slide_html


iface = gr.Interface(
    fn=criar_slide,
    inputs=[
        gr.Textbox(label="Título do Slide", placeholder="Digite o título..."),
        gr.Textbox(label="Texto do Slide", placeholder="Digite o texto..."),
        gr.Image(type="numpy", label="Imagem do Slide"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
    ],
    outputs=gr.HTML(label="Slide customizado"),
    title="Criador de Slides",
    description="Crie um slide personalizado",
)


if __name__ == "__main__":
    iface.launch()
