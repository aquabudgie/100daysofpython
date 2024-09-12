import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Tkinter Test")
    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack(padx=20, pady=20)
    window.mainloop()


if __name__ == "__main__":
    main()
