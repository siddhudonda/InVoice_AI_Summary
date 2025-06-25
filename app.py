import gradio as gr
from ocr_utils import extract_text_from_image
from llm_summary import summarize_invoice

def process_invoice(file):
    text = extract_text_from_image(file)
    summary = summarize_invoice(text)
    return summary

iface = gr.Interface(
    fn=process_invoice,
    inputs=gr.Image(type="filepath", label="Upload Invoice (Image or PDF Screenshot)"),
    outputs=gr.Textbox(label="Invoice Summary"),
    title="Invoice Summary Generator",
    description="Upload an invoice image to extract key financial details using OCR + Gemini."
)

if __name__ == "__main__":
    iface.launch()
