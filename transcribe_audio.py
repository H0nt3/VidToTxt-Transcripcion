import torch
import whisper
import numpy as np
import soundfile as sf
import json

# Load the Whisper model (using GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium", device=device)

# Function to transcribe and save diarization in JSON format
def transcribe_and_save_json(audio_array, sample_rate=16000, output_file="/path/to/your/output.json"):
    if isinstance(audio_array, np.ndarray):
        # Convert the audio array to float32
        audio_array = audio_array.astype(np.float32)  
        
        # Transcribe the audio with Whisper
        result = model.transcribe(audio_array, fp16=True)  

        # Create a dictionary to store the results
        transcription_data = {
            "transcription": result['text'],
            "segments": []
        }

        # Process the segments if they exist
        if 'segments' in result:
            for segment in result['segments']:
                transcription_data["segments"].append({
                    "start": segment['start'],
                    "end": segment['end'],
                    "text": segment['text']
                })
        
        # Save the results in a JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(transcription_data, f, ensure_ascii=False, indent=4)

        print(f"Transcription and segments saved to {output_file}")
    else:
        print("The audio is not valid or is in an unsupported format.")

# Load the audio file
audio_file = "/path/to/your/audio.mp3"
audio_array, sample_rate = sf.read(audio_file)

# Transcribe the audio and save to JSON
transcribe_and_save_json(audio_array, sample_rate)
