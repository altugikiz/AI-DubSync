import os
import yt_dlp
from moviepy.editor import VideoFileClip

def download_video_and_extract_audio(url: str, output_dir: str) -> dict:
    """
    A tool that downloads a YouTube video using yt-dlp and extracts its audio.
    
    Args:
        url (str): The YouTube video URL.
        output_dir (str): The directory to save files in.

    Returns:
        dict: A dictionary containing paths to the video and audio files.
              Returns {'error': message} on failure.
    """
    try:
        video_filename = "original_video.mp4"
        video_path = os.path.join(output_dir, video_filename)
        
        # --- Video Download with yt-dlp ---
        print(f"Tool: Downloading video using yt-dlp from {url}")
        
        # Options for yt-dlp
        # We want the best video format that includes audio, in mp4 format.
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': video_path,
            'quiet': True, # Suppress console output from yt-dlp
            'merge_output_format': 'mp4',
            'overwrites': True, # Overwrite file if it exists
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Tool: Video saved to {video_path}")
        
        if not os.path.exists(video_path):
             raise FileNotFoundError("yt-dlp failed to download the video file.")

        # --- Audio Extraction (MoviePy part remains the same) ---
        print("Tool: Extracting audio...")
        video_clip = VideoFileClip(video_path)
        audio_filename = "original_audio.mp3"
        audio_path = os.path.join(output_dir, audio_filename)
        video_clip.audio.write_audiofile(audio_path, logger=None)
        video_clip.close()
        print(f"Tool: Audio saved to {audio_path}")

        return {"video_path": video_path, "audio_path": audio_path}

    except Exception as e:
        # Catching yt-dlp specific errors or any other exception
        error_message = f"An error occurred in yt-dlp or moviepy: {e}"
        print(f"ERROR in media_tools: {error_message}")
        return {"error": error_message}