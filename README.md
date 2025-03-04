# Transcripcion Video a Texto

Este proyecto convierte un archivo de video a audio y luego transcribe el audio usando el modelo **Whisper** de OpenAI.

## Requisitos

Este proyecto requiere las siguientes bibliotecas de Python:

- **torch**: Para trabajar con modelos de aprendizaje profundo, como Whisper.
- **whisper**: Modelo de transcripción de audio a texto de OpenAI.
- **numpy**: Para manipulación de arrays y cálculos matemáticos.
- **soundfile**: Para leer y escribir archivos de audio.
- **json**: Para manejar datos JSON.
- **subprocess**: Para ejecutar comandos del sistema, como FFmpeg.

### Instalación de Paquetes de Python

Los paquetes de Python necesarios se pueden instalar usando pip:

- torch
- whisper
- numpy
- soundfile

## Instalación

**1. Clona este repositorio:**

```bash
   git clone https://github.com/your-username/video-to-text-transcription.git
```

```bash
   cd video-to-text-transcription
```

**2. Instala las dependencias:**

```bash
   pip install -r requirements.txt
```

## Uso

**1. Ejecuta el script principal**

Este script pedirá al usuario la ruta del archivo de video, realizará la conversión y la transcripción.

```bash
python main.py
```

### Contribuciones

¡Las contribuciones son bienvenidas! Si tienes mejoras o correcciones, no dudes en hacer un pull request.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.
