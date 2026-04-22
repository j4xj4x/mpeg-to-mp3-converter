import subprocess
import os

def convertir_carpeta_mpeg_a_mp3(carpeta_entrada, carpeta_salida, bitrate="192k"):
    # Crear carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)

    # Extensiones soportadas
    extensiones = (".mpeg", ".mpg")

    for archivo in os.listdir(carpeta_entrada):
        if archivo.lower().endswith(extensiones):
            ruta_entrada = os.path.join(carpeta_entrada, archivo)

            nombre_base = os.path.splitext(archivo)[0]
            ruta_salida = os.path.join(carpeta_salida, nombre_base + ".mp3")

            comando = [
                "ffmpeg",
                "-i", ruta_entrada,
                "-vn",          # sin video
                "-ab", bitrate,
                "-y",
                ruta_salida
            ]

            try:
                subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"✔ Convertido: {archivo}")
            except subprocess.CalledProcessError:
                print(f"✖ Error al convertir: {archivo}")

if __name__ == "__main__":
    carpeta_mpeg = r"C:\ruta\de\entrada\videos_mpeg"
    carpeta_mp3 = r"C:\ruta\de\salida\audios_mp3"

    convertir_carpeta_mpeg_a_mp3(carpeta_mpeg, carpeta_mp3)
