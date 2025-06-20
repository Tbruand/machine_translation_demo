import gradio as gr
from translation.translator import Translator

def translate_text(text, model_name, temperature):
    if not text.strip():
        return "Veuillez entrer un texte."
    translator = Translator()
    try:
        # On utilise la méthode translate (phrase par phrase)
        translation = translator.translate(text, model_name=model_name, temperature=temperature)
        return translation
    except Exception as e:
        return f"Erreur : {e}"

def launch_app():
    translator = Translator()
    model_names = list(translator.models.keys())

    with gr.Blocks() as demo:
        gr.Markdown("# Démo Traduction Automatique")
        
        with gr.Row():
            text_input = gr.Textbox(label="Texte à traduire (en anglais)", lines=3)
            temperature_slider = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, value=0.5, label="Température")
        
        model_dropdown = gr.Dropdown(choices=model_names, value=model_names[0], label="Choisir un modèle")
        
        translate_button = gr.Button("Traduire")
        output_box = gr.Textbox(label="Traduction", lines=3)
        
        translate_button.click(
            fn=translate_text,
            inputs=[text_input, model_dropdown, temperature_slider],
            outputs=output_box
        )
    
    demo.launch()

if __name__ == "__main__":
    launch_app()