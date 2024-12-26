import tkinter as tk
from tkinter import simpledialog

class OverlayMemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memo Overlay")
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.8)
        self.root.geometry('400x300')
        self.root.configure(bg='lightgray')
        self.memo_text = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12), bg='lightgray', fg='black', bd=0)
        self.memo_text.pack(expand=True, fill=tk.BOTH)
        self.save_button = tk.Button(self.root, text="Save Memo", command=self.save_memo, font=("Arial", 12), bg='lightblue')
        self.save_button.pack(side=tk.BOTTOM, fill=tk.X)

    def save_memo(self):
        memo_content = self.memo_text.get("1.0", tk.END).strip()
        if memo_content:
            with open("memo.txt", "w") as file:
                file.write(memo_content)
            print("saved!")
        else:
            print("empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OverlayMemoApp(root)
    root.mainloop()
