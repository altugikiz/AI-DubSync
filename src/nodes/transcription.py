# src/nodes/transcription.py

from src.state import AppState
from src.tools.gemini_client import transcribe_audio_file

def transcription_node(state: AppState) -> AppState:
    """
    The node responsible for transcribing the audio file.
    It uses the gemini_client tool for the actual work.
    
    Args:
        state (AppState): The current state of the application.

    Returns:
        AppState: The updated state.
    """
    print("--- NODE: Transcribing Audio ---")
    
    # Check for errors from the previous node
    if state.get("error"):
        print(f"Skipping transcription due to previous error: {state['error']}")
        return state

    audio_path = state.get("original_audio_path")
    if not audio_path:
        print("Error: Audio path is missing.")
        state["error"] = "Audio path not found in state."
        return state
        
    # Call the tool to do the heavy lifting
    result = transcribe_audio_file(audio_path)
    
    # Update the state with the results from the tool
    if "error" in result:
        print(f"Error during transcription: {result['error']}")
        state["error"] = result["error"]
    else:
        state["transcription"] = result["transcription"]
        print("Transcription successful.")
        
    return state