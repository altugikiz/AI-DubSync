import os
from src.state import AppState
from src.tools.media_tools import download_video_and_extract_audio

def process_video_node(state: AppState) -> AppState:
    """
    The node responsible for downloading the video and extracting audio.
    It uses the media_tools for the actual work.
    
    Args:
        state (AppState): The current state of the application.

    Returns:
        AppState: The updated state.
    """
    print("--- NODE: Processing Video ---")
    
    youtube_url = state.get("youtube_url")
    if not youtube_url:
        print("Error: YouTube URL is missing.")
        state["error"] = "YouTube URL not found in state."
        return state
        
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Call the tool to do the heavy lifting
    result = download_video_and_extract_audio(youtube_url, output_dir)
    
    # Update the state with the results from the tool
    if "error" in result:
        print(f"Error during video processing: {result['error']}")
        state["error"] = result["error"]
    else:
        state["original_video_path"] = result["video_path"]
        state["original_audio_path"] = result["audio_path"]
        print("Video processed successfully.")
        
    return state