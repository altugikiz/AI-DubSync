import os
import yt_dlp
from moviepy.editor import VideoFileClip
from moviepy.editor import VideoFileClip, AudioFileClip


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
    


def combine_video_and_audio(video_path: str, audio_path: str, output_path: str) -> dict:
    """
    A tool that combines a video file with a new audio track.
    
    Args:
        video_path (str): Path to the original video file (without its original audio).
        audio_path (str): Path to the new audio file to be added.
        output_path (str): Path to save the final, combined video file.

    Returns:
        dict: A dictionary with the path to the final video file.
              Returns {'error': message} on failure.
    """
    try:
        print("Tool: Combining final video and dubbed audio...")
        
        # Load the original video clip
        video_clip = VideoFileClip(video_path)
        
        # Load the new dubbed audio clip
        dubbed_audio_clip = AudioFileClip(audio_path)
        
        # Set the audio of the video clip to our new audio
        final_clip = video_clip.set_audio(dubbed_audio_clip)
        
        # Write the result to a file
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', logger=None)
        
        # Close the clips to free up resources
        video_clip.close()
        dubbed_audio_clip.close()
        final_clip.close()
        
        print(f"Tool: Final video successfully saved to {output_path}")
        return {"final_video_path": output_path}

    except Exception as e:
        error_message = f"An error occurred during video-audio combination: {e}"
        print(f"ERROR in media_tools: {error_message}")
        return {"error": error_message}