"""
Script para baixar e configurar FFmpeg automaticamente
"""
import os
import sys
import subprocess
import urllib.request
import zipfile
import shutil
from pathlib import Path

FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
FFMPEG_DIR = Path(__file__).parent / "ffmpeg"
FFMPEG_BIN = FFMPEG_DIR / "ffmpeg-*-essentials_build" / "bin"

def baixar_ffmpeg():
    """Baixa o FFmpeg do site oficial"""
    print("Baixando FFmpeg...")
    zip_path = Path(__file__).parent / "ffmpeg.zip"
    
    try:
        urllib.request.urlretrieve(FFMPEG_URL, zip_path)
        print("✓ Download concluído!")
        return zip_path
    except Exception as e:
        print(f"Erro ao baixar: {e}")
        return None

def extrair_ffmpeg(zip_path):
    """Extrai o FFmpeg"""
    print("Extraindo FFmpeg...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(FFMPEG_DIR)
        print("✓ Extração concluída!")
        return True
    except Exception as e:
        print(f"Erro ao extrair: {e}")
        return False

def encontrar_ffmpeg():
    """Encontra o executável do FFmpeg"""
    # Procura em locais comuns
    locais_comuns = [
        Path("C:/ffmpeg/bin/ffmpeg.exe"),
        Path("C:/Program Files/ffmpeg/bin/ffmpeg.exe"),
        Path(os.environ.get("ProgramFiles", "")) / "ffmpeg/bin/ffmpeg.exe",
    ]
    
    # Procura na pasta do projeto
    if FFMPEG_DIR.exists():
        for bin_dir in FFMPEG_DIR.glob("*/bin"):
            ffmpeg_exe = bin_dir / "ffmpeg.exe"
            if ffmpeg_exe.exists():
                return ffmpeg_exe
    
    # Verifica locais comuns
    for local in locais_comuns:
        if local.exists():
            return local
    
    return None

def verificar_ffmpeg():
    """Verifica se FFmpeg está disponível"""
    try:
        resultado = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            check=True
        )
        return True, "ffmpeg"
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Tenta encontrar localmente
        ffmpeg_path = encontrar_ffmpeg()
        if ffmpeg_path and ffmpeg_path.exists():
            try:
                resultado = subprocess.run(
                    [str(ffmpeg_path), '-version'],
                    capture_output=True,
                    check=True
                )
                return True, str(ffmpeg_path)
            except:
                pass
        return False, None

def main():
    print("=" * 50)
    print("Instalador de FFmpeg")
    print("=" * 50)
    print()
    
    # Verifica se já está instalado
    instalado, caminho = verificar_ffmpeg()
    if instalado:
        print(f"✓ FFmpeg já está instalado em: {caminho}")
        return
    
    print("FFmpeg não encontrado. Iniciando instalação...")
    print()
    
    # Baixa FFmpeg
    zip_path = baixar_ffmpeg()
    if not zip_path:
        print("\n❌ Falha ao baixar FFmpeg.")
        print("Por favor, instale manualmente:")
        print("1. Baixe em: https://ffmpeg.org/download.html")
        print("2. Extraia e adicione ao PATH")
        return
    
    # Extrai
    if not extrair_ffmpeg(zip_path):
        print("\n❌ Falha ao extrair FFmpeg.")
        return
    
    # Remove zip
    try:
        zip_path.unlink()
    except:
        pass
    
    # Encontra o executável
    ffmpeg_exe = encontrar_ffmpeg()
    if ffmpeg_exe:
        print(f"\n✓ FFmpeg instalado em: {ffmpeg_exe}")
        print("\n⚠️  IMPORTANTE:")
        print("O FFmpeg foi instalado localmente no projeto.")
        print("O script converter_ts_mp4.py foi atualizado para usar este FFmpeg.")
    else:
        print("\n❌ FFmpeg não foi encontrado após instalação.")
        print("Por favor, instale manualmente.")

if __name__ == "__main__":
    main()


