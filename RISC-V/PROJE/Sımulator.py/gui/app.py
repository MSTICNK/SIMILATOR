import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RISC-V Simülatörü")
        layout = QVBoxLayout()

        btn = QPushButton("Çalıştır")
        layout.addWidget(btn)

        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

class RiscVSimulatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RISC-V Simülatörü")
        self.setGeometry(100, 100, 400, 300)

        button = QPushButton('Başlat', self)
        button.clicked.connect(self.on_start_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def on_start_clicked(self):
        print("RISC-V Simülatörü Başlatıldı.")
        from core.processor import Processor

        class GUI:
            def __init__(self):
                self.cpu = Processor()

            def run(self):
                print("RISC-V Simülatörü Başlatıldı! Komutları girin. (Çıkmak için 'exit')")

                while True:
                    command = input("> ")  # Kullanıcıdan komut al
                    if command.strip().lower() == "exit":
                        print("Çıkış yapılıyor...")
                        break

                    result = self.cpu.execute(command)  # Komutu çalıştır
                    print(result)  # Sonucu ekrana bas

        # Uygulamayı başlat
        if __name__ == "__main__":
            GUI().run()

