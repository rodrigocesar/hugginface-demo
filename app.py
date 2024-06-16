from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def summarize_text(text):
    return model(text)[0]['summary_text']

with gr.Blocks() as demo:
    text = gr.Textbox(lines=10, label="Input Text")
    summary = gr.Textbox(lines=10, label="Summary")
    gr.Interface(fn=summarize_text, inputs=text, outputs=summary)
    
demo.launch()