from PIL import Image
import os

pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp']
input_folder = 'images'  # Diretório das imagens pretas originais
output_folder = 'images/white'  # Diretório das novas imagens brancas

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def change_color(image_path, output_path):
    image = Image.open(image_path).convert('RGBA')
    data = image.getdata()

    new_data = []
    for item in data:
        if item[0] < 50 and item[1] < 50 and item[2] < 50:  # Mudança de preto (ou escuro) para branco
            new_data.append((255, 255, 255, item[3]))  # Mantém a transparência
        else:
            new_data.append(item)

    image.putdata(new_data)
    image.save(output_path)

for piece in pieces:
    input_path = f'{input_folder}/{piece}.png'
    output_path = f'{output_folder}/{piece.replace("b", "w")}.png'
    change_color(input_path, output_path)

print("As cores das peças foram trocadas com sucesso!")
