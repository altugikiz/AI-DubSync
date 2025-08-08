# AI-DubSync 🎬🔊

**AI-DubSync** is an AI-powered application that automatically dubs YouTube videos into different languages. It performs video downloading, audio extraction, transcription, translation, and AI voice synthesis in a single workflow.

## 🌟 Features

- 📹 **YouTube Video Download**: High-quality video downloading using yt-dlp
- 🎵 **Automatic Audio Extraction**: Audio file extraction from videos using MoviePy
- 📝 **Smart Transcription**: Speech-to-text conversion using Google Cloud Speech-to-Text API
- 🌍 **Multi-language Translation**: Text translation to different languages using Google Translate API
- 🗣️ **AI Voice Synthesis**: Natural voice generation using Google Text-to-Speech
- 🎬 **Automatic Video Merging**: Combining new voiceover with original video
- 🔄 **Flow-based Processing**: Organized workflow using LangGraph

## 🏗️ Project Structure

```
AI-DubSync/
├── src/
│   ├── graph.py              # Main workflow graph
│   ├── tools/
│   │   ├── media_tools.py    # Video/audio processing tools
│   │   ├── transcription_tools.py  # Transcription tools
│   │   ├── translation_tools.py    # Translation tools
│   │   └── tts_tools.py      # Text-to-speech tools
│   └── nodes/
│       ├── video_processor.py      # Video processing node
│       ├── transcription_node.py   # Transcription node
│       ├── translation_node.py     # Translation node
│       └── tts_node.py            # TTS node
├── main.py                   # Main application file
├── .env                     # Environment variables (API keys)
└── requirements.txt         # Python dependencies
```

## 🛠️ Technology Stack

- **Python 3.8+** - Main programming language
- **yt-dlp** - YouTube video downloading
- **MoviePy** - Video/audio processing
- **Google Cloud APIs** - Speech-to-Text, Translate, Text-to-Speech
- **LangGraph** - Workflow orchestration
- **FFmpeg** - Media processing backend

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-DubSync.git
cd AI-DubSync
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. FFmpeg Installation
Add FFmpeg to your system PATH:
- Windows: [Download FFmpeg](https://ffmpeg.org/download.html) and add to PATH
- With Chocolatey: `choco install ffmpeg`

### 5. Google Cloud Setup

#### Get API Keys:
1. Create a [Google Cloud Console](https://console.cloud.google.com/) account
2. Create a new project
3. Enable the following APIs:
   - Speech-to-Text API
   - Translation API  
   - Text-to-Speech API
4. Create a Service Account and download the JSON key file

#### Set Environment Variables:
Create a `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
```

## 💻 Usage

### Basic Usage
```bash
python main.py
```

### Customization in Code
```python
# Change settings in main.py file
test_url = "https://www.youtube.com/watch?v=VIDEO_ID"
target_lang = "Turkish"  # or "English", "Spanish", "French" etc.
```

## 🔧 Workflow

1. **Video Download** 📥
   - Video is downloaded from YouTube URL
   - Audio file is automatically extracted

2. **Transcription** 🎤
   - Audio is converted to text using Google Speech-to-Text API
   - Timestamps are preserved

3. **Translation** 🌐
   - Translation to target language using Google Translate API
   - Context-aware accurate translation

4. **Voice Synthesis** 🗣️
   - Natural voice generation using Google Text-to-Speech
   - Various voice options available

5. **Video Merging** 🎬
   - New voiceover is combined with original video
   - High-quality output format

## 📋 Requirements

```txt
moviepy>=1.0.3
yt-dlp>=2023.7.6
google-cloud-speech>=2.0.0
google-cloud-translate>=3.0.0
google-cloud-texttospeech>=2.0.0
langgraph>=0.1.0
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Important Notes

- Google Cloud APIs have usage quotas and pricing
- Be mindful of YouTube video copyright regulations
- Ensure sufficient disk space for large video files
- Internet connection is required for all operations

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🆘 Troubleshooting

### Common Errors:

**HTTP Error 400: Bad Request**
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Check video URL validity

**MoviePy Import Error**
- Verify FFmpeg is properly installed
- Reinstall with `pip install moviepy`

**Google API Errors**
- Check API key validity
- Verify service account JSON file path
- Check API quotas in Google Cloud Console

## 🔮 Future Features

- [ ] Web interface (Streamlit/Flask)
- [ ] Batch video processing
- [ ] Custom voice models
- [ ] Subtitle support
- [ ] Different video platform support
- [ ] Docker containerization

---

⭐ **Don't forget to star if you liked it!** ⭐