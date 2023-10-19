import keyboard

# Variável global para armazenar o valor
contador = 0

def incrementar_contador(event):
    global contador
    if event.name == "a":  # Substitua "a" pela tecla desejada
        contador += 1
        print(f"Contador: {contador}")

# Adiciona um manipulador de eventos para a tecla desejada
keyboard.on_press_key("a", incrementar_contador)

# Mantém o programa em execução
keyboard.wait("esc")  # Espere até a tecla "esc" ser pressionada

# Limpa o manipulador de eventos
keyboard.unhook_all()