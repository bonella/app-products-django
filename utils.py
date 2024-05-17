import google.generativeai as genai
import PIL.Image
# import os

# imagem = PIL.Image.open('media/526.webp') 
imagem = PIL.Image.open('media/celular.png') 

# genai.configure(api_key=os.environ['API_KEY'])
genai.configure(api_key='AIzaSyBoaVpoMveINc4BAszHp9O35nGGLJSwPwY')

# model = genai.GenerativeModel('gemini-pro') # Texto
model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content('Quanto custa uma tv 55 polegadas da Samsung?') # Texto
response = model.generate_content(['Com base na imagem, gere uma descrição de venda desse produto', imagem])

print(response.text)