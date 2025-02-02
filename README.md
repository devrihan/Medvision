# MedVision: AI for Medical Imaging

MedVision is an AI-powered platform designed to assist healthcare professionals in analyzing medical images. The application leverages Google's Gemini AI model to provide insights, identify abnormalities, and offer recommendations based on uploaded medical images. It also features a real-time chatbot that answers user questions about the image analysis.

## Tech Stack

- **Frontend**: Streamlit (for the UI and web interface)
- **Backend**: Google Gemini AI model for image analysis and natural language processing
- **Cloud Storage**: Temporary file storage for image handling

## Setup and Installation

### Prerequisites

Before running the application, ensure you have the following installed:

1. **Python** 3.7+
2. **Streamlit**: Install Streamlit to run the app.
3. **Google Generative AI**: You will need to sign up for an API key from Google Cloud and configure it.

### Steps to Set Up

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/devrihan/MedVision.git
    cd MedVision
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `secrets.toml` file in the `.streamlit` folder (or use Streamlit secrets management in your environment) with the following content:

    ```toml
    [api_key]
    your_google_api_key = "YOUR_API_KEY_HERE"
    ```

4. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

5. The app will now be live in your browser at `http://localhost:8501`.

## Usage

1. **Upload an Image**: Click on the "Upload the medical image and let the AI do the rest!" button to upload a medical image (JPEG, PNG, or JPG).
2. **View Analysis**: After the image is uploaded, click "Generate the Analysis" to receive AI-generated insights and recommendations.

## Development

If you'd like to contribute to this project or run it locally for development, feel free to fork the repository and submit pull requests. Contributions are welcome!

### Folder Structure

```bash
.
├── app.py                # Main Streamlit application script
├── requirements.txt      # Python dependencies for the project
├── secrets.toml          # API key configuration for Google Generative AI
└── README.md             # Project documentation
