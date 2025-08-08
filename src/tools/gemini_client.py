import os
import time
import google.generativeai as genai
from google.cloud import texttospeech
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
    

def text_to_speech(text_to_synthesize: str, language_code: str, output_path: str) -> dict:
    """
    Synthesizes speech from text using Google Cloud Text-to-Speech.
    
    Args:
        text_to_synthesize (str): The text to be synthesized.
        language_code (str): The BCP-47 language code (e.g., 'tr-TR' for Turkish).
        output_path (str): The path to save the output MP3 file.

    Returns:
        dict: A dictionary with the path to the audio file.
              Returns {'error': message} on failure.
    """
    try:
        print(f"Tool: Synthesizing speech for language '{language_code}'...")
        
        # Instantiate a client
        client = texttospeech.TextToSpeechClient()
        
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text_to_synthesize)
        
        # Build the voice request, select the language and a high-quality voice
        # WaveNet voices are Google's most natural-sounding voices.
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code, 
            name=f"{language_code}-Wavenet-A" # Example: 'tr-TR-Wavenet-A' (Male voice)
        )
        
        # Select the type of audio file you want
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
        # Perform the text-to-speech request
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        
        # The response's audio_content is binary.
        with open(output_path, "wb") as out:
            out.write(response.audio_content)
            
        print(f"Tool: Speech synthesized and saved to {output_path}")
        return {"dubbed_audio_path": output_path}

    except Exception as e:
        error_message = f"An error occurred during Text-to-Speech synthesis: {e}"
        print(f"ERROR in gemini_client: {error_message}")
        return {"error": error_message}