import sys
import whisper

def transcribe_audio(audio_path, output_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python transcribe_audio.py <ruta_audio> <ruta_transcripcion>")
        sys.exit(1)

    audio_path = sys.argv[1]
    output_path = sys.argv[2]
    transcribe_audio(audio_path, output_path)

# Transcribe the audio and save to JSON
transcribe_and_save_json(audio_array, sample_rate)
