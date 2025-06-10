# 🎥 YouTube AI Agent

An AI-powered system that automatically creates and uploads YouTube Shorts based on trending topics using OpenAI and the YouTube Data API. Includes thumbnail generation, hashtag optimization, and basic video scripting.


## 🚀 Features

- 🧠 AI-generated short video scripts (OpenAI)
- 🎞️ Automatic video generation (extendable with MoviePy or similar)
- 📷 Thumbnail generation (Pillow)
- 📤 YouTube video upload automation
- 📦 Organized structure and '.env' configuration


## 📁 Project Structure

youtube-ai-agent/
├── ai/ # AI-powered script generation
│ └── video_generator.py
├── youtube/ # Upload logic
│ └── uploader.py
├── thumbnail/ # Thumbnail generation
│ └── generator.py
├── utils/ # Utility functions
│ └── helpers.py
├── main.py # Entry point
├── config.py # API keys and environment setup
├── requirements.txt # Dependencies
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/paramxsingh/youtube-ai-agent.git
cd youtube-ai-agent
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create .env File
Create a .env file with:

ini
Copy
Edit
OPENAI_KEY=your_openai_key
GOOGLE_CLIENT_SECRET_FILE=client_secret.json
🧠 How It Works
main.py triggers AI to generate a video script

Placeholder logic simulates video generation

Thumbnail is generated using PIL

Video is uploaded via YouTube API

📊 Future Enhancements
Actual video rendering using moviepy

Hashtag & title optimization with AI

Full analytics dashboard

Trend scraping (e.g., Google Trends, YouTube trending)

📄 License
MIT

🙌 Contributions Welcome
Feel free to fork, improve, and PR!
