import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv

# Load environment variables from .env file
# This line loads the GOOGLE_API_KEY we set earlier
load_dotenv()

# --- Node 1: Download Video and Extract Audio ---
def download_and_extract_audio(state: dict) -> dict:
    """
    Downloads a video from a YouTube URL and extracts its audio.
    
    Args:
        state (dict): The current state of the graph. 
                      Must contain 'youtube_url'.

    Returns:
        dict: The updated state with paths to the downloaded video and extracted audio.
    """
    print("--- Starting Node: Download and Extract Audio ---")
    
    # Get the URL from the current state
    youtube_url = state.get("youtube_url")
    if not youtube_url:
        raise ValueError("YouTube URL is not provided in the state.")
        
    # Define an output directory to store our files
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    try:
        # --- Video Download ---
        print(f"Downloading video from: {youtube_url}")
        yt = YouTube(youtube_url)
        
        # Get the best progressive stream (video + audio)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Define video file path and download
        video_filename = "original_video.mp4"
        video_path = os.path.join(output_dir, video_filename)
        stream.download(output_path=output_dir, filename=video_filename)
        print(f"Video downloaded successfully to: {video_path}")
        
        # --- Audio Extraction ---
        print("Extracting audio from the video...")
        video_clip = VideoFileClip(video_path)
        
        # Define audio file path and extract
        audio_filename = "original_audio.mp3"
        audio_path = os.path.join(output_dir, audio_filename)
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close() # Close the clip to free up resources
        print(f"Audio extracted successfully to: {audio_path}")

        # --- Update the state ---
        # We add the paths of the new files to our state dictionary
        # so the next node in the graph can use them.
        state['original_video_path'] = video_path
        state['original_audio_path'] = audio_path
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # In case of an error, we can add it to the state to handle it later
        state['error'] = str(e)

    return state

# --- Main execution block to test this node ---
if __name__ == '__main__':
    # This is a simple way to test our function in isolation.
    # We create a sample state and run the function.
    
    # A sample YouTube URL to test with (a short creative commons video)
    test_url = "https://www.youtube.com/watch?v=M-P4QBt-FWw"
    
    initial_state = {
        "youtube_url": test_url,
        "target_language": "Turkish" # We'll use this in a later node
    }
    
    # Run the function with our initial state
    final_state = download_and_extract_audio(initial_state)
    
    print("\n--- Function execution finished ---")
    print("Final State:")
    # Pretty print the final state
    import json
    print(json.dumps(final_state, indent=2))