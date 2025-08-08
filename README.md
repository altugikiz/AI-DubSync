# AI-DubSync 🎬🔊

**AI-DubSync**, YouTube videolarını otomatik olarak farklı dillere seslendiren yapay zeka destekli bir uygulamadır. Video indirme, ses çıkarma, transkripsiyon, çeviri ve yapay zeka seslendirimini tek bir akışta gerçekleştirir.

## 🌟 Özellikler

- 📹 **YouTube Video İndirme**: yt-dlp kullanarak yüksek kaliteli video indirme
- 🎵 **Otomatik Ses Çıkarma**: MoviePy ile videolardan ses dosyası çıkarma
- 📝 **Akıllı Transkripsiyon**: Google Cloud Speech-to-Text API ile ses-metin dönüşümü
- 🌍 **Çoklu Dil Çevirisi**: Google Translate API ile metinleri farklı dillere çevirme
- 🗣️ **Yapay Zeka Seslendirim**: Google Text-to-Speech ile doğal ses üretimi
- 🎬 **Otomatik Video Birleştirme**: Yeni seslendirme ile orijinal videoyu birleştirme
- 🔄 **Akış Tabanlı İşleme**: LangGraph ile organize edilmiş iş akışı

## 🏗️ Proje Yapısı

```
AI-DubSync/
├── src/
│   ├── graph.py              # Ana iş akışı grafiği
│   ├── tools/
│   │   ├── media_tools.py    # Video/ses işleme araçları
│   │   ├── transcription_tools.py  # Transkripsiyon araçları
│   │   ├── translation_tools.py    # Çeviri araçları
│   │   └── tts_tools.py      # Metin-ses dönüşüm araçları
│   └── nodes/
│       ├── video_processor.py      # Video işleme düğümü
│       ├── transcription_node.py   # Transkripsiyon düğümü
│       ├── translation_node.py     # Çeviri düğümü
│       └── tts_node.py            # TTS düğümü
├── main.py                   # Ana uygulama dosyası
├── .env                     # Çevre değişkenleri (API anahtarları)
└── requirements.txt         # Python bağımlılıkları
```

## 🛠️ Teknoloji Yığını

- **Python 3.8+** - Ana programlama dili
- **yt-dlp** - YouTube video indirme
- **MoviePy** - Video/ses işleme
- **Google Cloud APIs** - Speech-to-Text, Translate, Text-to-Speech
- **LangGraph** - İş akışı orchestration
- **FFmpeg** - Media processing backend

## 🚀 Kurulum

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/your-username/AI-DubSync.git
cd AI-DubSync
```

### 2. Sanal Ortam Oluşturun
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. FFmpeg Kurulumu
FFmpeg'i sistem PATH'inize ekleyin:
- Windows: [FFmpeg indirin](https://ffmpeg.org/download.html) ve PATH'e ekleyin
- Chocolatey ile: `choco install ffmpeg`

### 5. Google Cloud Ayarları

#### API Anahtarlarını Alın:
1. [Google Cloud Console](https://console.cloud.google.com/) hesap oluşturun
2. Yeni bir proje oluşturun
3. Aşağıdaki API'leri etkinleştirin:
   - Speech-to-Text API
   - Translation API  
   - Text-to-Speech API
4. Service Account oluşturun ve JSON key dosyasını indirin

#### Çevre Değişkenlerini Ayarlayın:
`.env` dosyası oluşturun:
```env
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
```

## 💻 Kullanım

### Temel Kullanım
```bash
python main.py
```

### Kod İçinde Özelleştirme
```python
# main.py dosyasında ayarları değiştirin
test_url = "https://www.youtube.com/watch?v=VIDEO_ID"
target_lang = "Turkish"  # veya "English", "Spanish", "French" vb.
```

## 🔧 İş Akışı

1. **Video İndirme** 📥
   - YouTube URL'sinden video indirilir
   - Ses dosyası otomatik olarak çıkarılır

2. **Transkripsiyon** 🎤
   - Google Speech-to-Text API ile ses metne dönüştürülür
   - Zaman damgaları korunur

3. **Çeviri** 🌐
   - Google Translate API ile hedef dile çeviri
   - Bağlam korunarak doğru çeviri

4. **Seslendirme** 🗣️
   - Google Text-to-Speech ile doğal ses üretimi
   - Çeşitli ses seçenekleri

5. **Video Birleştirme** 🎬
   - Yeni seslendirme orijinal video ile birleştirilir
   - Kaliteli çıktı formatı

## 📋 Gereksinimler

```txt
moviepy>=1.0.3
yt-dlp>=2023.7.6
google-cloud-speech>=2.0.0
google-cloud-translate>=3.0.0
google-cloud-texttospeech>=2.0.0
langgraph>=0.1.0
```

## 🤝 Katkı Sağlama

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## ⚠️ Önemli Notlar

- Google Cloud API'larının kullanım kotaları ve ücretlendirmesi vardır
- YouTube videolarının telif hakkı kurallarına dikkat edin
- Büyük video dosyaları için yeterli disk alanı bulundurun
- İnternet bağlantısı tüm işlemler için gereklidir

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 🆘 Sorun Giderme

### Yaygın Hatalar:

**HTTP Error 400: Bad Request**
- yt-dlp'yi güncelleyin: `pip install --upgrade yt-dlp`
- Video URL'sinin doğruluğunu kontrol edin

**MoviePy Import Hatası**
- FFmpeg'in doğru kurulduğunu kontrol edin
- `pip install moviepy` ile yeniden yükleyin

**Google API Hataları**
- API anahtarlarınızın doğruluğunu kontrol edin
- Service account JSON dosyasının yolunu kontrol edin
- API kotalarınızı Google Cloud Console'dan kontrol edin

## 🔮 Gelecek Özellikler

- [ ] Web arayüzü (Streamlit/Flask)
- [ ] Batch video işleme
- [ ] Özel ses modelleri
- [ ] Subtitle/altyazı desteği
- [ ] Farklı video platformları desteği
- [ ] Docker containerization

---

⭐ **Beğendiyseniz yıldız vermeyi unutmayın!** ⭐