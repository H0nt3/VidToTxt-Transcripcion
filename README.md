# Video-to-Text Transcription

This project converts a video file to audio and then transcribes the audio using OpenAI's **Whisper** model.

## Requirements

This project requires the following Python libraries:

- **torch**: For working with deep learning models, like Whisper.
- **whisper**: OpenAI's audio-to-text transcription model.
- **numpy**: For array manipulation and mathematical calculations.
- **soundfile**: For reading and writing audio files.
- **json**: For handling JSON data.
- **subprocess**: For running system commands, like FFmpeg.

### Python Packages

The required Python packages can be installed using pip:

- torch
- whisper
- numpy
- soundfile

## Installation

**1. Clone this repository:**
   
```bash
   git clone https://github.com/your-username/video-to-text-transcription.git
```
   
```bash
   cd video-to-text-transcription
```

**2. Install the dependencies:**
   
```bash
   pip install -r requirements.txt
```
   
## Usage

**1. Convert a video to audio**
   
This step converts a video file (e.g., in MP4 format) to an MP3 audio file using FFmpeg.

Make sure your video file is available at the path specified in the script src/convert_video_to_audio.py.

To perform the conversion, run the following command:

```bash
python convert_video_to_audio.py
```

This command will generate an MP3 audio file with the same duration and content as the original video.

**2. Transcribe the audio to text**
   
Once the video is converted to audio, the next step is to transcribe the audio to text using OpenAI's Whisper model.

Make sure your MP3 audio file is available at the path specified in the script src/transcribe_audio.py.

To transcribe the audio, run the following command:

```bash
python transcribe_audio.py
```

This will generate a JSON file with the transcription and audio segments, where the start and end times of each segment will be indicated along with the transcribed text.


### Contributions

Contributions are welcome! If you have any improvements or fixes, feel free to make a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
