import sys
import subprocess

def convert_video_to_audio(video_path, audio_path):
    command = f"ffmpeg -i {video_path} {audio_path}"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python convert_video_to_audio.py <ruta_video> <ruta_audio>")
        sys.exit(1)

    video_path = sys.argv[1]
    audio_path = sys.argv[2]
    convert_video_to_audio(video_path, audio_path)
    
