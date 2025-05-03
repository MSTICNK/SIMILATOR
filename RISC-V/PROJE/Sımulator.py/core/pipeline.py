class Pipeline:
    def __init__(self, memory, registers, instruction_set):
        self.memory = memory
        self.registers = registers
        self.instruction_set = instruction_set
        self.instruction_register = None
        self.pc = 0  # Program counter (PC)

    def fetch(self, pc):
        """ Bellekten komut al """
        self.instruction_register = self.memory.read(pc)
        print(f"Fetched instruction: {self.instruction_register}")

    def decode(self):
        """ Komutu çözümle """
        parts = self.instruction_register.split()
        operation = parts[0].upper()

        # Parametre sayısı kontrolü
        if operation == "LOAD":
            if len(parts) != 3:
                print("Hata: LOAD komutunda eksik parametre.")
                return None
            rd = parts[1]  # Burada x0 gibi register adlarını kullanıyoruz
            imm = int(parts[2])  # İmmadiat değerini integer'a dönüştürüyoruz
            return (operation, rd, imm)
        elif operation == "ADD":
            if len(parts) != 4:  # ADD için 3 operand bekliyoruz
                print("Hata: ADD komutunda eksik parametre.")
                return None
            rd = parts[1]
            rs1 = parts[2]
            rs2 = parts[3]  # Üçüncü operand eklendi
            return (operation, rd, rs1, rs2)
        elif operation == "SUB":
            if len(parts) != 4:  # SUB için 3 operand bekliyoruz
                print("Hata: SUB komutunda eksik parametre.")
                return None
            rd = parts[1]
            rs1 = parts[2]
            rs2 = parts[3]  # Üçüncü operand eklendi
            return (operation, rd, rs1, rs2)
        else:
            print("Hata: Bilinmeyen komut.")
            return None

    def execute(self, decoded_instruction):
        """Komutu çalıştır"""
        if decoded_instruction:
            operation = decoded_instruction[0]
            if operation == "LOAD":
                self.instruction_set.load(decoded_instruction[1], decoded_instruction[2])
            elif operation == "ADD":
                # ADD komutunda 3 parametre bekleniyor, yani (rs1, rs2, rd)
                self.instruction_set.add(decoded_instruction[1], decoded_instruction[2], decoded_instruction[3])
            elif operation == "SUB":
                self.instruction_set.sub(decoded_instruction[1], decoded_instruction[2], decoded_instruction[3])
            elif operation == "MUL":
                self.instruction_set.mul(decoded_instruction[1], decoded_instruction[2], decoded_instruction[3])
            elif operation == "DIV":
                self.instruction_set.div(decoded_instruction[1], decoded_instruction[2], decoded_instruction[3])
            # Diğer komutlar burada eklenebilir

    def run_cycle(self, pc):
        """ Pipeline döngüsünü çalıştır """
        self.fetch(pc)        # Fetch komutunu al
        decoded_instruction = self.decode()  # Komut çözümle
        self.execute(decoded_instruction)        # Komutu çalıştır
