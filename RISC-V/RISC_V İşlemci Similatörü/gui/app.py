import tkinter as tk
from tkinter import scrolledtext, messagebox
from core.cpu import CPU


class EmulatorApp:
    def __init__(self, root):
        self.cpu = CPU()
        self.root = root
        self.root.title("emux86 Simülatör")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")

        # Komut girişi
        self.input_label = tk.Label(root, text="Komutları gir (1 satıra 1 komut):", bg="#1e1e1e", fg="white", font=("Consolas", 12))
        self.input_label.pack(pady=(10, 2))

        self.input_text = scrolledtext.ScrolledText(root, height=10, width=90, font=("Consolas", 11), bg="#2e2e2e", fg="white", insertbackground="white")
        self.input_text.pack(padx=10)

        # Çalıştır butonu
        self.run_button = tk.Button(root, text="ÇALIŞTIR", command=self.run_commands, bg="#4caf50", fg="white", font=("Consolas", 12, "bold"))
        self.run_button.pack(pady=10)

        # Çıktı
        self.output_text = scrolledtext.ScrolledText(root, height=15, width=90, font=("Consolas", 11), bg="#2e2e2e", fg="white", state="disabled")
        self.output_text.pack(padx=10, pady=(10, 0))

    def run_commands(self):
        commands = self.input_text.get("1.0", tk.END).strip().split("\n")
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)

        for i, cmd in enumerate(commands, start=1):
            try:
                if cmd.startswith("set "):  # set x1 d-10
                    _, reg, val = cmd.split()
                    self.cpu.set_register(reg, val)
                    self.output_text.insert(tk.END, f"[✓] Satır {i}: {cmd} ✅\n")
                else:
                    self.cpu.execute(cmd)
                    self.output_text.insert(tk.END, f"[✓] Satır {i}: {cmd} ✅\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"[✗] Satır {i}: {cmd} ❌ → Hata: {str(e)}\n", "error")

        self.output_text.insert(tk.END, "\n[📦] Register Durumu:\n")
        for reg, (val, base) in self.cpu.get_registers().items():
            show = f"{reg}: {base}-{val}"
            self.output_text.insert(tk.END, f"{show}\n")

        self.output_text.tag_config("error", foreground="red")
        self.output_text.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmulatorApp(root)
    root.mainloop()
