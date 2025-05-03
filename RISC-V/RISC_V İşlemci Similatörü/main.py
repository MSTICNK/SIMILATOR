import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from core.cpu import CPU
import os

class RISC_V_Simulator:
    def __init__(self, root):
        self.cpu = CPU()
        self.root = root
        self.root.title("RISC-V İşlemci Simülatörü")
        self.root.geometry("800x800")

        # Arka plan resmi (orijinal resim yedekte)
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "arkaplan.jpg")
        self.original_bg_image = Image.open(image_path)
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Boyut değişiminde arka planı güncelle
        self.root.bind("<Configure>", self.resize_background)

        # Girişler ve butonlar
        self.reg_label = tk.Label(root, text="Register Değeri Atama (örneğin: x5 = d-10):",
                                  font=("Impact", 20), bg="#2a2a2a", fg="#DAA520")
        self.reg_label.place(x=100, y=80)

        self.reg_input = tk.Entry(root, width=40, font=("Roboto", 24, "bold"), bg='#555555', fg='white')
        self.reg_input.place(x=100, y=130)

        self.set_btn = tk.Button(root, text="Register'a Değer Ata", command=self.set_register,
                                 font=("Impact", 18), bg="#4caf50", fg="white", relief="raised", bd=4)
        self.set_btn.place(x=100, y=200)

        self.op_label = tk.Label(root, text="İşlem Yap (örneğin: ADD x5 x6 x7):",
                                 font=("Impact", 20), bg="#2a2a2a", fg="#DAA520")
        self.op_label.place(x=100, y=400)

        self.op_input = tk.Text(root, height=6, width=45, font=("Roboto", 24, "bold"),
                                bg='#555555', fg='white')  # Buraya fg='white' eklendi
        self.op_input.place(x=100, y=450)

        self.execute_btn = tk.Button(root, text="İşlemi Gerçekleştir", command=self.execute_operations,
                                     font=("Impact", 18), bg="#f44336", fg="white", relief="raised", bd=4)
        self.execute_btn.place(x=100, y=700)

        self.result_label = tk.Label(root, text="Sonuçlar:", font=("Impact", 20), bg="#2a2a2a", fg="#DAA520")
        self.result_label.place(x=1100, y=80)

        self.result_text = tk.Text(root, height=32, width=20, font=("Helvetica", 18, "bold"),
                                   bg="#555555", fg="white", bd=2)  # Buraya da fg='white' eklendi
        self.result_text.place(x=1100, y=130)

    def resize_background(self, event):
        if event.widget == self.root:
            new_width = event.width
            new_height = event.height
            resized_image = self.original_bg_image.resize((new_width, new_height))
            self.bg_photo = ImageTk.PhotoImage(resized_image)
            self.bg_label.configure(image=self.bg_photo)
            self.bg_label.image = self.bg_photo

    def set_register(self):
        instruction = self.reg_input.get()
        try:
            reg, value = instruction.split("=")
            reg = reg.strip()
            value = value.strip()
            self.cpu.set_register(reg, value)
            self.reg_input.delete(0, tk.END)
            self.update_registers()
        except Exception as e:
            messagebox.showerror("Hata", f"Değer atama hatası: {str(e)}")

    def set_registers_bulk(self, reg_val_dict):
        errors = []
        for reg, value in reg_val_dict.items():
            try:
                self.set_register(reg, value)
            except ValueError as e:
                errors.append(f"{reg} için hata: {str(e)}")
        return errors

    def execute_operations(self):
        instructions = self.op_input.get("1.0", tk.END).strip().split("\n")
        errors = []
        for idx, instruction in enumerate(instructions):
            try:
                self.cpu.execute(instruction.strip())
            except Exception as e:
                errors.append(f"Satır {idx + 1}: {str(e)}")
        if errors:
            messagebox.showerror("Hatalı İşlemler", "\n".join(errors))
        self.op_input.delete(1.0, tk.END)
        self.update_registers()

    def update_registers(self):
        registers = self.cpu.get_registers()
        self.result_text.delete(1.0, tk.END)
        for reg, value in registers.items():
            self.result_text.insert(tk.END, f"{reg}: {value}\n")


# Ana pencereyi oluştur
root = tk.Tk()
simulator = RISC_V_Simulator(root)

# Uygulamayı başlat
root.mainloop()
