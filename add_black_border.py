from PIL import Image, ImageDraw
import os

def add_black_border(image_path, output_path, border_width=5):
    # Abre a imagem
    image = Image.open(image_path).convert('RGBA')
    draw = ImageDraw.Draw(image)
    
    # Obtém as dimensões da imagem
    width, height = image.size
    
    # Desenha o contorno preto
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline='black', width=border_width)
    
    # Salva a imagem com o contorno
    image.save(output_path)

input_folder = 'images/white'
output_folder = 'images/white_with_border'

# Cria o diretório de saída, se não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Adiciona o contorno preto a todas as imagens no diretório
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        add_black_border(input_path, output_path)

print("Contorno preto adicionado às imagens com sucesso!")
