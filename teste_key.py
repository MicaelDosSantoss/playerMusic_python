import keyboard

t = 0

def press_space(event):
    print(event.name)

keyboard.on_press(press_space)

keyboard.wait("esc")  

keyboard.unhook_all()