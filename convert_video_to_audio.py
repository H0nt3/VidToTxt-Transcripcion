import subprocess

# Input video file path
video_file = "/path/to/your/video.mp4"

# Output audio file path
audio_file = "/path/to/your/audio.mp3"

# FFmpeg command for conversion
command = [
    "ffmpeg",
    "-i", video_file,       # Input file
    "-vn",                  # Disable video processing
    "-ar", "16000",         # Audio sample rate (Hz)
    "-ac", "1",             # Audio channel (mono)
    "-b:a", "48k",          # Audio bitrate
    "-y",                   # Overwrite the output file if it exists
    audio_file              # Output file
]

# Run the FFmpeg command
try:
    subprocess.run(command, check=True)
    print(f"File successfully converted: {audio_file}")
except subprocess.CalledProcessError as e:
    print(f"Error converting the file: {e}")
