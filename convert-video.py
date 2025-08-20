import os
import subprocess

def converter_video(pasta, formato_entrada, formato_saida):
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(f".{formato_entrada.lower()}"):
            caminho_entrada = os.path.join(pasta, arquivo)
            nome_sem_extensao = os.path.splitext(arquivo)[0]
            caminho_saida = os.path.join(pasta, f"{nome_sem_extensao}.{formato_saida}")

            print(f"Convertendo: {arquivo} -> {nome_sem_extensao}.{formato_saida}")

            try:
                subprocess.run([
                    "ffmpeg", "-i", caminho_entrada,
                    "-c:v", "copy",
                    "-c:a", "copy",
                    caminho_saida
                ], check=True)
                print(f"✅ Sucesso: {caminho_saida}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao converter {arquivo}: {e}")

pasta_videos = input("Caminho da pasta do vídeo: ")
formato_entrada = input("Formato de entrada: ")
formato_saida = input("Formato de saída: ")

if os.path.isdir(pasta_videos):
    converter_video(pasta_videos, formato_entrada, formato_saida)
else:
    print(f"Caminho inválido: {pasta_videos}")