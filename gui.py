import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser
from changelog_report import generate_report, LOG_DIR

def open_log_folder():
    webbrowser.open(LOG_DIR.resolve().as_uri())

def launch_gui():
    def run_report():
        generate_report()
        with open(LOG_DIR / 'commit_details.txt', 'r', encoding='utf-8') as f:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f.read())
        messagebox.showinfo("Relatório", "Relatórios gerados com sucesso!")

    root = tk.Tk()
    root.title("Changelog Report")
    root.geometry("600x400")

    tk.Label(root, text="Changelog Report GUI", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(root, text="Gerar Relatório", command=run_report, width=20).pack(pady=5)
    tk.Button(root, text="Abrir Pasta de Logs", command=open_log_folder, width=20).pack(pady=5)

    global result_text
    result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
    result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    root.mainloop()