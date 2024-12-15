Video-to-Text Transcription

Este proyecto convierte un archivo de video a audio y luego transcribe el audio usando el modelo **Whisper** de OpenAI.

## Requisitos

- Python 3.7 o superior
- FFmpeg
- PyTorch
- Whisper (de OpenAI)
- SoundFile
- NumPy
- Subprocess

### Paquetes de Python

Los paquetes de Python necesarios se pueden instalar usando `pip`:

- `torch`
- `whisper`
- `numpy`
- `soundfile`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/video-to-text-transcription.git
   ```

   ```bash
   cd video-to-text-transcription
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   
Uso

1. Convertir un video a audio
   
Este paso convierte un archivo de video (por ejemplo, en formato MP4) a un archivo de audio MP3, utilizando FFmpeg.

Asegúrate de que tu archivo de video esté disponible en la ruta especificada en el script src/convert_video_to_audio.py.

Para realizar la conversión, ejecuta el siguiente comando:

```bash
python src/convert_video_to_audio.py
```

Este comando generará un archivo de audio MP3 con la misma duración y contenido que el video original.

2. Transcribir el audio a texto
   
Una vez convertido el video a audio, el siguiente paso es transcribir el audio a texto utilizando el modelo Whisper de OpenAI.

Asegúrate de que tu archivo de audio MP3 esté disponible en la ruta especificada en el script src/transcribe_audio.py.

Para transcribir el audio, ejecuta el siguiente comando:

```bash
python src/transcribe_audio.py
```

Esto generará un archivo JSON con la transcripción y los segmentos de audio, donde se indicarán los tiempos de inicio y fin de cada segmento junto con el texto transcrito.


Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna mejora o corrección, siéntete libre de hacer un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
