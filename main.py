from ai.video_generator import generate_video
from youtube.uploader import upload_video

if __name__ == '__main__':
    video_path, title, description = generate_video()
    upload_video(video_path, title, description)