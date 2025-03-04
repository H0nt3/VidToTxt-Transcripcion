import os
import subprocess

def convert_video_to_audio(video_path, audio_path):
    command = f"ffmpeg -i {video_path} {audio_path}"
    subprocess.run(command, shell=True, check=True)

def transcribe_audio(audio_path, transcript_path):
    command = f"python src/transcribe_audio.py --audio {audio_path} --output {transcript_path}"
    subprocess.run(command, shell=True, check=True)

def main():
    video_path = input("Por favor, ingresa la ruta del archivo de video: ")
    audio_path = "output_audio.mp3"
    transcript_path = "transcription.json"

    if not os.path.exists(video_path):
        print(f"El archivo {video_path} no existe.")
        return

    print("Convirtiendo video a audio...")
    convert_video_to_audio(video_path, audio_path)
    print("Transcripción de audio a texto...")
    transcribe_audio(audio_path, transcript_path)
    print(f"Transcripción completada. El archivo de transcripción se ha guardado como {transcript_path}")

if __name__ == "__main__":
    main()
