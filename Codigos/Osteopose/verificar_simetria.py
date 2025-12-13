# Análise de Simetria do Layout

# Dimensões do slide
WIDTH = 160
HEIGHT = 90
CENTER_X = WIDTH / 2  # 80

print("=" * 60)
print("ANÁLISE DE SIMETRIA DO LAYOUT")
print("=" * 60)

# Título
titulo_x = 80
print(f"\n1. TÍTULO:")
print(f"   Posição X: {titulo_x}")
print(f"   Centro do slide: {CENTER_X}")
print(f"   ✓ Simétrico: {titulo_x == CENTER_X}")

# Linha decorativa
line_start = 60
line_end = 100
line_center = (line_start + line_end) / 2
dist_start = CENTER_X - line_start
dist_end = line_end - CENTER_X
print(f"\n2. LINHA DECORATIVA:")
print(f"   Início: {line_start}, Fim: {line_end}")
print(f"   Centro da linha: {line_center}")
print(f"   Distância do início ao centro: {dist_start}")
print(f"   Distância do fim ao centro: {dist_end}")
print(f"   ✓ Simétrico: {dist_start == dist_end} ({dist_start == dist_end})")

# Linha 1 (3 itens)
y_row1 = 55
items_row1 = [
    ("Item 1", 25),
    ("Item 2", 70),
    ("Item 3", 115)
]

print(f"\n3. LINHA 1 (y={y_row1}):")
for name, x in items_row1:
    dist = abs(x - CENTER_X)
    side = "esquerda" if x < CENTER_X else "direita" if x > CENTER_X else "centro"
    print(f"   {name}: x={x}, distância do centro: {dist}, lado: {side}")

# Verificar simetria da linha 1
item1_x, item2_x, item3_x = 25, 70, 115
dist1 = CENTER_X - item1_x  # 55
dist3 = item3_x - CENTER_X  # 35
item2_centered = item2_x == CENTER_X  # False (deveria ser 80)

print(f"\n   Análise de simetria:")
print(f"   - Item 1 está a {dist1} unidades do centro")
print(f"   - Item 3 está a {dist3} unidades do centro")
print(f"   - Item 2 está no centro? {item2_centered} (posição: {item2_x}, deveria ser {CENTER_X})")
print(f"   ✗ NÃO SIMÉTRICO: Item 1 e Item 3 têm distâncias diferentes ({dist1} vs {dist3})")

# Linha 2 (2 itens)
y_row2 = 30
items_row2 = [
    ("Item 4", 45),
    ("Item 5", 95)
]

print(f"\n4. LINHA 2 (y={y_row2}):")
for name, x in items_row2:
    dist = abs(x - CENTER_X)
    side = "esquerda" if x < CENTER_X else "direita" if x > CENTER_X else "centro"
    print(f"   {name}: x={x}, distância do centro: {dist}, lado: {side}")

# Verificar simetria da linha 2
item4_x, item5_x = 45, 95
dist4 = CENTER_X - item4_x  # 35
dist5 = item5_x - CENTER_X  # 15

print(f"\n   Análise de simetria:")
print(f"   - Item 4 está a {dist4} unidades do centro")
print(f"   - Item 5 está a {dist5} unidades do centro")
print(f"   ✗ NÃO SIMÉTRICO: Item 4 e Item 5 têm distâncias diferentes ({dist4} vs {dist5})")

# Sugestões para tornar simétrico
print(f"\n" + "=" * 60)
print("SUGESTÕES PARA TORNAR SIMÉTRICO:")
print("=" * 60)

# Linha 1: 3 itens simétricos
# Se queremos espaçamento igual, podemos usar:
spacing_row1 = 45  # espaçamento entre itens
item1_sym = CENTER_X - spacing_row1  # 35
item2_sym = CENTER_X  # 80
item3_sym = CENTER_X + spacing_row1  # 125

print(f"\nLinha 1 (3 itens) - Sugestão:")
print(f"   Item 1: x={item1_sym} (atual: 25)")
print(f"   Item 2: x={item2_sym} (atual: 70) ← deve estar no centro")
print(f"   Item 3: x={item3_sym} (atual: 115)")

# Linha 2: 2 itens simétricos
spacing_row2 = 35  # espaçamento do centro
item4_sym = CENTER_X - spacing_row2  # 45
item5_sym = CENTER_X + spacing_row2  # 115

print(f"\nLinha 2 (2 itens) - Sugestão:")
print(f"   Item 4: x={item4_sym} (atual: 45) ✓")
print(f"   Item 5: x={item5_sym} (atual: 95) ← deve estar a {spacing_row2} do centro")

print(f"\n" + "=" * 60)


