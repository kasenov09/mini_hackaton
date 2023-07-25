import tkinter as tk
from tkinter import ttk

def on_button_click(button_number):
    print(f"Button {button_number} clicked!")

def create_beautiful_buttons(root):
    def on_language_toggle():
        global language
        if language == "русский":
            language = "английский"
        else:
            language = "русский"
        update_button_texts()

    def update_button_texts():
        translations = {
            "русский": {"Create": "Создать", "Read": "Читать", "Update": "Обновить", "Delete": "Удалить"},
            "английский": {"Create": "Create", "Read": "Read", "Update": "Update", "Delete": "Delete"}
        }
        button1.config(text=translations[language]["Create"])
        button2.config(text=translations[language]["Read"])
        button3.config(text=translations[language]["Update"])
        button4.config(text=translations[language]["Delete"])

    style = ttk.Style()
    style.configure("Beautiful.TButton", 
                    foreground="white", 
                    background="#4CAF50", 
                    font=("Helvetica", 16),
                    padding=10)

    button_frame = ttk.Frame(root)
    button_frame.grid(row=0, column=0, padx=10, pady=10)

    button1 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(1))
    button2 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(2))
    button3 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(3))
    button4 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(4))

    button1.grid(row=6, column=0, padx=20)
    button2.grid(row=0, column=0, padx=40)
    button3.grid(row=0, column=8, padx=50)
    button4.grid(row=6, column=8, padx=80)

    update_button_texts()
    
    language_button = ttk.Button(root, text="LG", command=on_language_toggle)
    
    language_button.grid(row=0, column=1, columnspan=1, pady=1)

    root.columnconfigure((0, 1, 2, 3), weight=1)

if __name__ == "__main__":
    language = "русский"

    root = tk.Tk()
    root.title("Красивые кнопки")
    create_beautiful_buttons(root)
    root.mainloop()