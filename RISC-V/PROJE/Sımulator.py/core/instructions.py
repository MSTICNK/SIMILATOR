from core.registers import Registers

class InstructionSet:
    def __init__(self, registers):
        self.registers = registers  # Registers nesnesini buraya ekliyoruz
        self.instructions = {
            "LOAD": self.load,
            "ADD": self.add,
            "SUB": self.sub,
            "MUL": self.mul,
            "DIV": self.div
        }

    def load(self, rd, value):
        """ Verilen değeri register'a yükler """
        self.registers.write(rd, value)
        print(f"Loaded value {value} into register {rd}")

    def add(self, rd, rs1, rs2):
        """ rd = rs1 + rs2 işlemi """
        try:
            result = self.registers.read(rs1) + self.registers.read(rs2)
            self.registers.write(rd, result)
            print(f"Added {self.registers.read(rs1)} and {self.registers.read(rs2)}, result in {rd}: {result}")
        except KeyError as e:
            print(f"Invalid register: {e}")

    def sub(self, rd, rs1, rs2):
        """ rd = rs1 - rs2 işlemi """
        try:
            result = self.registers.read(rs1) - self.registers.read(rs2)
            self.registers.write(rd, result)
            print(f"Subtracted {self.registers.read(rs1)} and {self.registers.read(rs2)}, result in {rd}: {result}")
        except KeyError as e:
            print(f"Invalid register: {e}")

    def mul(self, rd, rs1, rs2):
        """ rd = rs1 * rs2 işlemi """
        try:
            result = self.registers.read(rs1) * self.registers.read(rs2)
            self.registers.write(rd, result)
            print(f"Multiplied {self.registers.read(rs1)} and {self.registers.read(rs2)}, result in {rd}: {result}")
        except KeyError as e:
            print(f"Invalid register: {e}")

    def div(self, rd, rs1, rs2):
        """ rd = rs1 / rs2 işlemi (0'a bölme kontrolü) """
        try:
            divisor = self.registers.read(rs2)  # rs2'yi al
            if divisor == 0:
                raise ZeroDivisionError("Cannot divide by zero!")  # Sıfıra bölme hatası
            result = self.registers.read(rs1) // divisor  # Bölüm işlemi
            self.registers.write(rd, result)  # Sonuç kaydına yaz
            print(f"Divided {self.registers.read(rs1)} by {divisor}, result in {rd}: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Invalid register: {e}")

        if self.registers.read(rs2) == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
        result = self.registers.read(rs1) // self.registers.read(rs2)
        self.registers.write(rd, result)

    def execute(self, command):
        """ Komutları çalıştırma """
        parts = command.split()

        if len(parts) < 2:
            print("Invalid instruction format! Ensure command follows the format: OPERATION rd, rs1, rs2")
            return

        operation = parts[0].upper()
        args = parts[1:]

        try:
            if operation in self.instructions:
                # Komutu çalıştırırken parametreleri uygun tipte işliyoruz
                parsed_args = [int(arg) if arg.isdigit() else arg for arg in args]
                self.instructions[operation](*parsed_args)
            else:
                print(f"Unknown instruction: {operation}. Available operations: LOAD, ADD, SUB, MUL, DIV")
        except Exception as e:
            print(f"Error executing instruction {command}: {e}")
