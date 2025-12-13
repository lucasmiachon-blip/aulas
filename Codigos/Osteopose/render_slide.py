import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuração do Slide (16:9)
fig, ax = plt.figure(figsize=(16, 9), facecolor='#F9F9F9'), plt.gca()
ax.set_facecolor('#F9F9F9') # Fundo "Off-white" muito suave para não cansar o olho
ax.set_xlim(0, 160)
ax.set_ylim(0, 90)
ax.axis('off')

# Paleta de Cores (Invertendo o Dark Mode)
NAVY_BLUE = '#0a192f' # Azul escuro profundo (para texto e números)
GOLD_ACCENT = '#D4AF37' # Aquele toque dourado sutil
TEXT_COLOR = '#333333' # Cinza chumbo para leitura

# 1. Título
plt.text(80, 78, "Objetivos Educacionais", ha='center', va='center', 
         fontsize=38, fontname='Arial', weight='bold', color=NAVY_BLUE)

# Linha decorativa fina abaixo do título
line = patches.FancyArrowPatch((60, 72), (100, 72), color=GOLD_ACCENT, linewidth=2)
ax.add_patch(line)

# Dados dos Pontos (Texto original da sua imagem)
points = [
    "Modelos de Risco & Limitações",
    "A Nova Era dos Limiares?",
    "Fratura iminente",
    "Treat to target",
    "Anabolic First"
]

# Função para desenhar cada item "limpo" (Sem caixa)
def draw_item(x, y, number, text):
    # O Círculo do Número (Âncora Visual)
    circle = patches.Circle((x, y), radius=3.5, color=NAVY_BLUE)
    ax.add_patch(circle)
    
    # O Número dentro do círculo
    plt.text(x, y-1, str(number), ha='center', va='center', 
             fontsize=22, weight='bold', color='white')
    
    # O Texto ao lado (Livre, sem bordas)
    # Quebra de linha manual para textos longos se necessário
    plt.text(x + 6, y, text, ha='left', va='center', 
             fontsize=18, weight='regular', color=TEXT_COLOR)

# Layout: Linha 1 (3 itens) e Linha 2 (2 itens centralizados)
# Coordenadas calculadas para simetria perfeita
y_row1 = 55
y_row2 = 30

# Linha 1 (3 itens simétricos - Item 2 no centro)
draw_item(35, y_row1, 1, points[0])   # 45 unidades à esquerda do centro
draw_item(80, y_row1, 2, points[1])  # No centro (80)
draw_item(125, y_row1, 3, points[2])  # 45 unidades à direita do centro

# Linha 2 (2 itens simétricos)
draw_item(45, y_row2, 4, points[3])   # 35 unidades à esquerda do centro
draw_item(115, y_row2, 5, points[4])  # 35 unidades à direita do centro

plt.tight_layout()
plt.savefig('slide_objetivos.png', dpi=150, bbox_inches='tight', facecolor='#F9F9F9')
print("Slide renderizado e salvo como 'slide_objetivos.png'")
plt.show()

