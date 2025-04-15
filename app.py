# import streamlit as st
# from pathlib import Path
# import google.generativeai as genai
# import tempfile 

# api_key = st.secrets["api_key"]

# genai.configure(api_key=api_key)

# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config,
#     system_instruction=(
#         "As a highly skilled medical practitioner specializing in image analysis, you are tasked with analyzing medical images.\n\n"
#         "Your Responsibilities include:\n"
#         "1. **Detailed Analysis**: Thoroughly analyze each image, focusing on identifying any abnormalities.\n"
#         "2. **Findings Report**: Document all observed anomalies or signs of disease. Clearly articulate your observations.\n"
#         "3. **Recommendations and Next Steps**: Based on your analysis, suggest potential next steps, such as additional tests or consultations.\n"
#         "4. **Treatment Suggestions**: If appropriate, recommend possible treatment options or interventions.\n\n"
#         "**Important Notes:**\n"
#         "1. **Scope of Response**: Only respond if the image pertains to human health issues.\n"
#         "2. **Clarity of Image**: If the image quality impedes clear analysis, note that certain details may be unclear.\n"
#         "3. **Disclaimer**: Accompany your analysis with the disclaimer: 'Consult with a Doctor before making any medical decisions.'\n\n"
#         "Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis."
#     )
# )



# def upload_to_gemini(image_data, mime_type="image/png"):
#     """Saves image data as a temporary file and uploads it to Gemini."""
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
#         temp_file.write(image_data)  
#         temp_file_path = temp_file.name  
    
#     file = genai.upload_file(temp_file_path, mime_type=mime_type)  
#     return file

# st.set_page_config(page_title="Medical Image Analysis", page_icon="🧠")
# st.subheader("Transforming medical imaging with AI-powered insights.")

# uploaded_file = st.file_uploader("Upload the medical image and let the AI do the rest!", type=["jpg", "jpeg", "png"])


# import base64

# st.markdown(
#     """
#     <style>
#         .uploaded-img {
#             width: 100%;
#             max-width: 700px;
#             height: auto;
#             display: block;
#             margin: auto;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# if uploaded_file:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=700)
#     image_data = base64.b64encode(uploaded_file.getvalue()).decode("utf-8")

#     submit = st.button("Generate the Analysis")

#     if submit:
#         image_data = uploaded_file.read()
        
#         loading_placeholder = st.empty()

#         with loading_placeholder.container():
#             st.markdown(
#                 """
#                 <style>
#                 .loading-screen {
#                     position: fixed;
#                     top: 0;
#                     left: 0;
#                     width: 100%;
#                     height: 100%;
#                     background-color: #0E1117;
#                     display: flex;
#                     justify-content: center;
#                     align-items: center;
#                     z-index: 9999;
#                     font-size: 24px;
#                     font-weight: bold;
#                 }
     
#                 .blinking-dot {
#                     width: 8px;
#                     height: 8px;
#                     background-color: green;
#                     border-radius: 50%;
#                     margin-right: 10px;
#                     animation: blink 1s infinite;
#                 }
#                 @keyframes blink {
#                     0% { opacity: 1; }
#                     50% { opacity: 0; }
#                     100% { opacity: 1; }
#                 }
#                 </style>
#                 <div class="loading-screen">
#                     <div class="blinking-dot"></div>
#                     <span>Analyzing the Image... Please wait</span>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#         file = upload_to_gemini(image_data, mime_type="image/png")
#         chat_session = model.start_chat(history=[
#             {"role": "user", "parts": [file, "Analyze this medical image and provide insights."]},
#         ])
#         response = chat_session.send_message("Provide a detailed analysis of the uploaded image.")
#         analysis_text = response.text

#         loading_placeholder.empty()
        
#         st.subheader("AI Analysis Result:")
#         st.write(analysis_text)

        


# st.markdown("""
#     <br><br>
#     <hr>
#     <p style="text-align: center;">Developed with love🩷 by Rihan <a href="https://www.linkedin.com/in/sk-rihan-akhtar/" target="_blank">Linkedin</a> | 
#     <a href="https://github.com/devrihan" target="_blank">GitHub</a></p>
#     <style>
#         hr {
#             border: 1px solid #ddd;
#         }
#     </style>
# """, unsafe_allow_html=True)
import streamlit as st
from pathlib import Path
import google.generativeai as genai
import tempfile 
import base64

api_key = st.secrets["api_key"]
genai.configure(api_key=api_key)

# Model Configuration
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
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(image_data)
        temp_file_path = temp_file.name
    file = genai.upload_file(temp_file_path, mime_type=mime_type)
    return file

# Streamlit Page Config
st.set_page_config(page_title="MedVision - AI Medical Imaging", page_icon="🧠", layout="centered")

# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

mode = st.toggle("🌗 Toggle Dark/Light Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = mode

# Custom CSS
st.markdown(f"""
    <style>
        body {{
            background-color: {'#0E1117' if mode else '#FFFFFF'};
            color: {'#FFFFFF' if mode else '#000000'};
            font-family: 'Segoe UI', sans-serif;
            transition: background-color 0.5s ease, color 0.5s ease;
        }}
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            transition: all 0.3s ease-in-out;
        }}
        .main-title {{
            font-size: 2.2rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 1rem;
            animation: fadeIn 1s ease-in-out;
        }}
        .description {{
            font-size: 1.1rem;
            text-align: center;
            color: {'#bbbbbb' if mode else '#333'};
            animation: slideUp 1s ease-in-out;
        }}
        .upload-box {{
            background-color: {'#1c1f26' if mode else '#f0f0f0'};
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
            text-align: center;
            animation: fadeIn 0.8s ease-in;
        }}
        .stButton > button {{
            background-color: #00c6a2;
            color: white;
            padding: 0.6rem 1.5rem;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            transition: background-color 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #009f89;
        }}
        .footer {{
            text-align: center;
            color: {'#888' if mode else '#555'};
            font-size: 0.9rem;
        }}
        .result-box {{
            background-color: {'#1a1d24' if mode else '#f9f9f9'};
            padding: 1rem 1.5rem;
            border-radius: 10px;
            border: 1px solid {'#333' if mode else '#ccc'};
            animation: fadeIn 1s ease-in-out;
        }}
        @keyframes fadeIn {{
            from {{opacity: 0;}}
            to {{opacity: 1;}}
        }}
        @keyframes slideUp {{
            from {{transform: translateY(20px); opacity: 0;}}
            to {{transform: translateY(0); opacity: 1;}}
        }}
    </style>
""", unsafe_allow_html=True)

# UI Content
st.markdown('<div class="main-title">MedVision 🧠</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Upload your medical image and let AI reveal its insights</div>', unsafe_allow_html=True)

st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a medical image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    st.image(uploaded_file, caption="Preview of Uploaded Image", use_container_width=True)
    submit = st.button("🔍 Generate Analysis")

    if submit:
        image_data = uploaded_file.read()
        with st.spinner("Analyzing image with AI..."):
            file = upload_to_gemini(image_data, mime_type="image/png")
            chat_session = model.start_chat(history=[
                {"role": "user", "parts": [file, "Analyze this medical image and provide insights."]},
            ])
            response = chat_session.send_message("Provide a detailed analysis of the uploaded image.")
            analysis_text = response.text

        st.markdown('<br><div class="result-box">', unsafe_allow_html=True)
        st.subheader("🧬 AI Analysis Result")
        st.write(analysis_text)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <br><hr>
    <p class="footer">Developed with ❤️ by <a href="https://www.linkedin.com/in/sk-rihan-akhtar/" target="_blank">Rihan</a> |
    <a href="https://github.com/devrihan" target="_blank">GitHub</a></p>
""", unsafe_allow_html=True)
