import keyboard
import os

DelayTime = 0 

try:
    user_input = input("Ecolha o delay entre os caracteres\n(0 para nenhum delay)\nDelay : ")
    DelayTime = float(user_input) if user_input else 0
except ValueError:
    print("Input invalido. Delay foi definido para 0.")

print("Pressione '1' para começar a escrever o texto de 'textoredacao.txt'.\n")
keyboard.wait("1")

keyboard.send("backspace", True, True)

file_path = 'essaytext.txt'

# Check if the file exists before attempting to open it
if os.path.exists(file_path):
    try:
        # Opens "essaytext.txt" with UTF-8 encoding to handle all types of characters
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Writes the text from the file with the specified delay
            keyboard.write(text, DelayTime)
    except Exception as e:
        print(f"Um erro ocorreu durante a ecrita: {e}")
else:
    print(f"Erro: '{file_path}' não encontrado. Cheque se o arquivo existe no mesmo diretório do script.")
