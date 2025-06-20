import gradio as gr
from translation.translator import Translator
from translation.generation_params import TEMPERATURES

translator = Translator()

def translate_text(sentence, model_name, temperature):
    return translator.translate(sentence, model_name, temperature)

def launch_app():
    model_names = list(translator.models.keys())
    with gr.Blocks() as demo:
        gr.Markdown("# Demo Traduction Automatique avec LLMs")
        sentence = gr.Textbox(label="Texte à traduire")
        model_name = gr.Dropdown(choices=model_names, label="Modèle")
        temperature = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, label="Température", value=0.5)
        output = gr.Textbox(label="Traduction")
        btn = gr.Button("Traduire")
        btn.click(translate_text, inputs=[sentence, model_name, temperature], outputs=output)
    demo.launch()