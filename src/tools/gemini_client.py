import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

# Load and configure the API at the module level
load_dotenv()
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(e)
    # This will prevent the application from starting without an API key
    exit()

def transcribe_audio_file(audio_path: str) -> dict:
    """
    A tool that transcribes an audio file using the Gemini 1.5 Pro model.
    
    Args:
        audio_path (str): The path to the audio file.

    Returns:
        dict: A dictionary with the transcription text.
              Returns {'error': message} on failure.
    """
    try:
        print(f"Tool: Uploading audio file to Gemini: {audio_path}")
        audio_file = genai.upload_file(path=audio_path)
        
        while audio_file.state.name == "PROCESSING":
            print("Tool: Waiting for Gemini audio processing...", end="\r")
            time.sleep(2)
            audio_file = genai.get_file(audio_file.name)

        if audio_file.state.name == "FAILED":
            raise ValueError("Gemini file processing failed.")
        
        print("Tool: Audio processed. Sending transcription request.     ")
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        prompt = "Provide a full and accurate transcription of this English audio file. Only output the transcribed text."
        response = model.generate_content([prompt, audio_file])
        
        # Clean up the uploaded file from Gemini's storage
        genai.delete_file(audio_file.name)
        print("Tool: Transcription complete and cloud file deleted.")

        return {"transcription": response.text}
    
    except Exception as e:
        print(f"ERROR in gemini_client: {e}")
        return {"error": str(e)}
    

def translate_text(text_to_translate: str, target_language: str) -> dict:
    """
    A tool that translates a given text to a target language using Gemini.
    
    Args:
        text_to_translate (str): The text to be translated.
        target_language (str): The language to translate the text into.

    Returns:
        dict: A dictionary with the translated text.
              Returns {'error': message} on failure.
    """
    try:
        print(f"Tool: Translating text to {target_language}...")
        
        # We use a standard generative model for this text-to-text task
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        
        # A clear and direct prompt for translation
        prompt = (f"Translate the following English text into {target_language}. "
                  f"Provide only the translated text, without any additional comments or explanations.\n\n"
                  f"Text to translate:\n---\n{text_to_translate}")
        
        response = model.generate_content(prompt)
        
        print("Tool: Translation complete.")
        return {"translated_text": response.text}

    except Exception as e:
        error_message = f"An error occurred during translation: {e}"
        print(f"ERROR in gemini_client: {error_message}")
        return {"error": error_message}