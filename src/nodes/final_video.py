import os
from src.state import AppState
from src.tools.media_tools import combine_video_and_audio

def final_video_node(state: AppState) -> AppState:
    """
    The final node, responsible for combining the original video with the new dubbed audio.
    """
    print("--- NODE: Creating Final Dubbed Video ---")

    if state.get("error"):
        print(f"Skipping final video creation due to a previous error: {state['error']}")
        return state

    video_path = state.get("original_video_path")
    audio_path = state.get("dubbed_audio_path")

    if not video_path or not audio_path:
        state["error"] = "Original video or dubbed audio path not found in state."
        return state

    output_dir = "output"
    final_video_path = os.path.join(output_dir, "AI_DubSync_FINAL.mp4")
    
    result = combine_video_and_audio(video_path, audio_path, final_video_path)

    if "error" in result:
        state["error"] = result["error"]
    else:
        state["final_video_path"] = result["final_video_path"]
        print("Final video created successfully!")
        
    return state