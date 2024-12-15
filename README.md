# video-to-text-transcription
Convert video to audio and transcribe the audio using OpenAI's Whisper model
Escribeme todo esto en un unico .md

 Video-to-Text Transcription

Este proyecto convierte un archivo de video a audio y luego transcribe el audio usando el modelo **Whisper** de OpenAI.

## Requisitos

- Python 3.7 o superior
- FFmpeg
- PyTorch
- Whisper (de OpenAI)
- SoundFile

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/video-to-text-transcription.git
   cd video-to-text-transcription
Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
Uso
1. Convertir un video a audio
Este paso convierte un archivo de video (por ejemplo, en formato MP4) a un archivo de audio MP3, utilizando FFmpeg.

Asegúrate de que tu archivo de video esté disponible en la ruta especificada en el script src/convert_video_to_audio.py.

Para realizar la conversión, ejecuta el siguiente comando:

bash
Copiar código
python src/convert_video_to_audio.py
Este comando generará un archivo de audio MP3 con la misma duración y contenido que el video original.

2. Transcribir el audio a texto
Una vez convertido el video a audio, el siguiente paso es transcribir el audio a texto utilizando el modelo Whisper de OpenAI.

Asegúrate de que tu archivo de audio MP3 esté disponible en la ruta especificada en el script src/transcribe_audio.py.

Para transcribir el audio, ejecuta el siguiente comando:

bash
Copiar código
python src/transcribe_audio.py
Esto generará un archivo JSON con la transcripción y los segmentos de audio, donde se indicarán los tiempos de inicio y fin de cada segmento junto con el texto transcrito.

Ejemplo
Si deseas probar el proyecto con un archivo de ejemplo, puedes agregar tu propio archivo de video en la carpeta assets/ y cambiar las rutas en los scripts.

Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna mejora o corrección, siéntete libre de hacer un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

markdown
Copiar código

Este archivo `README.md` incluye:

1. **Descripción general** del proyecto.
2. **Requisitos** para ejecutar el código.
3. **Instrucciones de instalación**.
4. **Instrucciones de uso** para convertir videos a audio y luego transcribirlos.
5. **Ejemplo** de cómo usar el código.
6. **Contribuciones** abiertas para otros desarrolladores.
7. **Licencia** para indicar que el código está bajo la Licencia MIT (esto es opcional, pero es buena práctica incluir una licencia para proyectos open source).

Este formato es muy común para proyectos de código abierto y facilita que otros usuarios comprendan rápidamente cómo usar tu repositorio y cómo pueden contribuir.
