from src.state import AppState
from src.tools.gemini_client import translate_text

def translation_node(state: AppState) -> AppState:
    """
    The node responsible for translating the transcribed text.
    It uses the gemini_client tool for the actual work.
    
    Args:
        state (AppState): The current application state.

    Returns:
        AppState: The updated state with the translated text.
    """
    print("--- NODE: Translating Text ---")
    
    if state.get("error"):
        print(f"Skipping translation due to a previous error: {state['error']}")
        return state

    transcription = state.get("transcription")
    target_language = state.get("target_language")

    if not transcription or not target_language:
        print("Error: Transcription or target language is missing.")
        state["error"] = "Transcription or target language not found in state."
        return state

    # Call the translation tool
    result = translate_text(transcription, target_language)

    if "error" in result:
        print(f"Error during translation: {result['error']}")
        state["error"] = result["error"]
    else:
        # Update the state with the new translated text
        state["translated_text"] = result["translated_text"]
        print("Translation successful.")
        
    return state