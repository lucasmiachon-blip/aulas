# Conversor TS para MP4

Script Python com interface gráfica para converter vídeos TS (Transport Stream) para MP4.

## Requisitos

1. **Python 3.6+** (já vem com tkinter no Windows)
2. **FFmpeg** - Ferramenta de conversão de vídeo

### Instalar FFmpeg no Windows

1. Baixe o FFmpeg em: https://ffmpeg.org/download.html
2. Ou use Chocolatey: `choco install ffmpeg`
3. Adicione o FFmpeg ao PATH do sistema:
   - Abra "Variáveis de Ambiente" no Windows
   - Adicione o caminho do FFmpeg (ex: `C:\ffmpeg\bin`) ao PATH

## Como usar

1. Execute o script:
   ```bash
   python converter_ts_mp4.py
   ```

2. Na interface gráfica:
   - Clique em **"📁 Selecionar Vídeos TS"**
   - Selecione um ou mais arquivos `.ts`
   - (Opcional) Escolha uma pasta de saída diferente
   - Clique em **"▶️ Converter para MP4"**

3. Aguarde a conversão! A barra de progresso mostrará o andamento.

## Recursos

- ✅ Interface gráfica intuitiva
- ✅ Seleção múltipla de arquivos
- ✅ Barra de progresso
- ✅ Escolha de pasta de saída
- ✅ Relatório de conversão com sucessos e erros
- ✅ Verificação automática do FFmpeg

## Notas

- Os arquivos MP4 serão salvos na mesma pasta dos arquivos TS (ou na pasta escolhida)
- A qualidade de vídeo está configurada para CRF 23 (boa qualidade)
- O preset está em "medium" (balance entre velocidade e qualidade)

