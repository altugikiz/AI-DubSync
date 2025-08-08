import os
from src.state import AppState
from src.tools.gemini_client import text_to_speech

def synthesis_node(state: AppState) -> AppState:
    """
    The node responsible for converting the translated text to speech.
    """
    print("--- NODE: Synthesizing Speech (TTS) ---")

    if state.get("error"):
        print(f"Skipping TTS due to a previous error: {state['error']}")
        return state

    translated_text = state.get("translated_text")
    if not translated_text:
        state["error"] = "Translated text not found in state."
        return state

    output_dir = "output"
    dubbed_audio_path = os.path.join(output_dir, "dubbed_audio.mp3")

    # We need to provide a more specific language code for the TTS API (e.g., 'tr-TR')
    # We can create a simple mapping for this.
    language_map = {"Turkish": "tr-TR", "English": "en-US", "Spanish": "es-ES"}
    target_language = state.get("target_language", "Turkish") # Default to Turkish
    language_code = language_map.get(target_language, "tr-TR") 

    result = text_to_speech(translated_text, language_code, dubbed_audio_path)

    if "error" in result:
        state["error"] = result["error"]
    else:
        state["dubbed_audio_path"] = result["dubbed_audio_path"]
        print("Speech synthesis successful.")
        
    return state