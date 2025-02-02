import streamlit as st
from pathlib import Path
import google.generativeai as genai
import tempfile  # Import tempfile module to handle temporary files

from api_key import api_key  # Ensure this file contains your API key

genai.configure(api_key=api_key)

# Configure AI model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "As a highly skilled medical practitioner specializing in image analysis, you are tasked with analyzing medical images.\n\n"
        "Your Responsibilities include:\n"
        "1. **Detailed Analysis**: Thoroughly analyze each image, focusing on identifying any abnormalities.\n"
        "2. **Findings Report**: Document all observed anomalies or signs of disease. Clearly articulate your observations.\n"
        "3. **Recommendations and Next Steps**: Based on your analysis, suggest potential next steps, such as additional tests or consultations.\n"
        "4. **Treatment Suggestions**: If appropriate, recommend possible treatment options or interventions.\n\n"
        "**Important Notes:**\n"
        "1. **Scope of Response**: Only respond if the image pertains to human health issues.\n"
        "2. **Clarity of Image**: If the image quality impedes clear analysis, note that certain details may be unclear.\n"
        "3. **Disclaimer**: Accompany your analysis with the disclaimer: 'Consult with a Doctor before making any medical decisions.'\n\n"
        "Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis."
    )
)



def upload_to_gemini(image_data, mime_type="image/png"):
    """Saves image data as a temporary file and uploads it to Gemini."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(image_data)  # Write image bytes to the temp file
        temp_file_path = temp_file.name  # Get the file path
    
    file = genai.upload_file(temp_file_path, mime_type=mime_type)  # Upload to Gemini
    return file

st.set_page_config(page_title="MedVision", page_icon="🧠")
st.image("IMG_20250201_225611.png", width=150)

st.title("MedVision: AI for Medical Imaging")
st.subheader("Transforming medical imaging with AI-powered insights.")

uploaded_file = st.file_uploader("Upload the medical image and let the AI do the rest!", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    submit = st.button("Generate the Analysis")
    
    if submit:
        image_data = uploaded_file.read()
        file = upload_to_gemini(image_data, mime_type="image/png")
        
        chat_session = model.start_chat(history=[
            {"role": "user", "parts": [file, "Analyze this medical image and provide insights."]},
        ])
        
        response = chat_session.send_message("Provide a detailed analysis of the uploaded image.")
        analysis_text = response.text
        
        st.subheader("AI Analysis Result:")
        st.write(response.text)

st.markdown("""
    <br><br>
    <hr>
    <p style="text-align: center;">Developed with love🩷 by Rihan <a href="https://www.linkedin.com/in/sk-rihan-akhtar/" target="_blank">Linkedin</a> | 
    <a href="https://github.com/devrihan" target="_blank">GitHub</a></p>
    <style>
        hr {
            border: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)