import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video_and_extract_audio(url: str, output_dir: str) -> dict:
    """
    A tool that downloads a YouTube video and extracts its audio.
    
    Args:
        url (str): The YouTube video URL.
        output_dir (str): The directory to save files in.

    Returns:
        dict: A dictionary containing paths to the video and audio files.
              Returns {'error': message} on failure.
    """
    try:
        print(f"Tool: Downloading video from {url}")
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        video_filename = "original_video.mp4"
        video_path = os.path.join(output_dir, video_filename)
        stream.download(output_path=output_dir, filename=video_filename)
        print(f"Tool: Video saved to {video_path}")

        print("Tool: Extracting audio...")
        video_clip = VideoFileClip(video_path)
        audio_filename = "original_audio.mp3"
        audio_path = os.path.join(output_dir, audio_filename)
        video_clip.audio.write_audiofile(audio_path, logger=None)
        video_clip.close()
        print(f"Tool: Audio saved to {audio_path}")

        return {"video_path": video_path, "audio_path": audio_path}

    except Exception as e:
        print(f"ERROR in media_tools: {e}")
        return {"error": str(e)}