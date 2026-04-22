# 🎧 MPEG to MP3 Converter

Script en Python para convertir archivos **.mpeg / .mpg a .mp3** usando FFmpeg desde rutas externas.

---

## 🚀 Características

* Conversión automática de múltiples archivos
* Soporte para carpetas externas
* Creación automática de carpeta de salida
* Configuración de bitrate
* Ligero y fácil de usar

---

## 📦 Requisitos

* Python 3.12 (o 3.10+ recomendado)
* FFmpeg instalado y agregado al PATH

---

## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/j4xj4x/MPEG-to-MP3-Converter.git
cd mpeg-to-mp3-converter
```

---

## 🪟 Instalación de FFmpeg en Windows

1. Descarga FFmpeg desde la página oficial:
   https://ffmpeg.org/download.html

2. Selecciona una build para Windows (por ejemplo desde gyan.dev)

3. Descarga la versión en formato `.zip`

4. Extrae el contenido y coloca los archivos ejecutables en una carpeta, por ejemplo:

```plaintext
C:\ffmpeg\
```

Asegúrate de que la estructura quede así:

```plaintext
C:\ffmpeg\ffmpeg.exe
C:\ffmpeg\ffprobe.exe
```

5. Agrega la carpeta al PATH:

```plaintext
C:\ffmpeg
```

👉 Esto se hace desde:

* Variables de entorno del sistema
* Editar la variable **Path**
* Agregar la ruta anterior

6. Verifica la instalación:

```bash
ffmpeg -version
```

---

## ▶️ Uso

1. Abre el archivo `script.py`

2. Define las rutas de entrada y salida:

```python
carpeta_mpeg = r"C:\ruta\de\entrada\audios_mpeg"
carpeta_mp3 = r"C:\ruta\de\salida\audios_mp3"
```

3. Ejecuta el script:

```bash
python script.py
```