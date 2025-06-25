import google.generativeai as genai
import os

# Set your Gemini API key
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def summarize_invoice(raw_text):
    prompt = f"""
    You are an invoice analyzer. Extract and summarize the following fields:
    - Vendor Name
    - Invoice Date
    - Invoice Number
    - Total Amount
    - Line Items (if present)

    Raw Invoice Text:
    {raw_text}
    """
    response = model.generate_content(prompt)
    return response.text
