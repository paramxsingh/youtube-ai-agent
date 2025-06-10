import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY

def generate_video():
    prompt = "Generate a short video script on trending AI news."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    script = response.choices[0].text.strip()
    # Placeholder logic for video creation
    video_path = "output_videos/sample.mp4"
    return video_path, "Trending AI News", script