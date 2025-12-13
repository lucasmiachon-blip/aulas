import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

# Tentar carregar a imagem
try:
    img = Image.open('slide_objetivos.png')
    img_array = np.array(img)
    
    # Dimensões da imagem
    height, width = img_array.shape[:2]
    center_x = width / 2
    
    print("=" * 60)
    print("ANÁLISE DE SIMETRIA DA IMAGEM RENDERIZADA")
    print("=" * 60)
    print(f"\nDimensões da imagem: {width} x {height}")
    print(f"Centro horizontal: {center_x}")
    
    # Análise básica: verificar se há simetria de cores/pixels
    # Dividir a imagem ao meio e comparar
    left_half = img_array[:, :width//2]
    right_half = img_array[:, width//2:]
    
    # Espelhar a metade direita para comparar
    right_half_flipped = np.fliplr(right_half)
    
    # Comparar as duas metades (usando diferença absoluta)
    diff = np.abs(left_half.astype(float) - right_half_flipped.astype(float))
    similarity = 1 - (np.mean(diff) / 255.0)
    
    print(f"\nSimilaridade de simetria (0-1): {similarity:.3f}")
    print(f"   (1.0 = perfeitamente simétrico, 0.0 = completamente assimétrico)")
    
    if similarity > 0.95:
        print("   ✓ A imagem é MUITO SIMÉTRICA")
    elif similarity > 0.85:
        print("   ~ A imagem é Razoavelmente simétrica")
    else:
        print("   ✗ A imagem NÃO é simétrica")
    
    print("\n" + "=" * 60)
    print("NOTA: Esta análise compara pixels, mas elementos visuais")
    print("(como texto) podem não ser perfeitamente simétricos mesmo")
    print("com layout simétrico devido a diferenças no conteúdo.")
    print("=" * 60)
    
except FileNotFoundError:
    print("Imagem 'slide_objetivos.png' não encontrada.")
    print("Execute primeiro 'python render_slide.py' para gerar a imagem.")
except Exception as e:
    print(f"Erro ao analisar a imagem: {e}")


