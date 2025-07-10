import time
import pyfiglet
import tkinter as tk
from threading import Thread

def run():
    def draw_letter_slowly(letter, text_widget):
        ascii_art = pyfiglet.figlet_format(letter, font="banner")
        lines = ascii_art.split('\n')

        for line in lines:
            modified_line = ''
            for char in line:
                if char == ' ':
                    modified_line += ' '
                else:
                    modified_line += '*'
            text_widget.insert(tk.END, modified_line + '\n')
            text_widget.see(tk.END)
            text_widget.update_idletasks()
            time.sleep(0.3)

    def on_draw_click():
        user_input = entry.get().strip()
        if user_input.lower() in ('quit', 'q'):
            root.quit()
        else:
            text_widget.delete(1.0, tk.END)
            thread = Thread(target=draw_letter_slowly, args=(user_input, text_widget))
            thread.start()

    root = tk.Tk()
    root.title("Dot Matrix Printer")

    label = tk.Label(root, text="Enter a letter:")
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Helvetica", 24))
    entry.pack(pady=10)
    entry.bind('<Return>', lambda event: on_draw_click())


    text_widget = tk.Text(root, font=("Courier", 12), height=20, width=60)
    text_widget.pack(pady=10)

    draw_button = tk.Button(root, text="Draw", command=on_draw_click, font=("Helvetica", 18))
    draw_button.pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    run()