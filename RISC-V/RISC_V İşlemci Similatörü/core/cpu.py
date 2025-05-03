class Memory:
    def __init__(self):
        self.memory = {}

    def write(self, address, value):
        self.memory[address] = value

    def read(self, address):
        return self.memory.get(address, None)


class CPU:
    def __init__(self):
        self.registers = {f"x{i}": ("0", 'd') for i in range(32)}  # default olarak decimal string
        self.memory = Memory()

    def get_registers(self):
        return self.registers

    def set_register(self, reg, value):
        """Register'a d- veya b- ile değer ata (string olarak saklar)"""
        if reg == "x0":
            raise ValueError("x0 sabittir , değiştirelemez.")

        if value.startswith('d-'):
            val = value[2:]  # direkt string olarak sakla
            self.registers[reg] = (val, 'd')
        elif value.startswith('b-'):
            val = value[2:]
            if not all(c in '01' for c in val):
                raise ValueError("Hatalı binary format!")
            self.registers[reg] = (val, 'b')
        else:
            raise ValueError("Hatalı format! 'd-' veya 'b-' ile başlamalı.")



    def check_register_base(self, reg1, reg2):
        """İki register aynı tabanda mı kontrol et"""
        _, base1 = self.registers[reg1]
        _, base2 = self.registers[reg2]
        return base1 == base2

    def convert_to_int(self, value, base):
        return int(value, 10 if base == 'd' else 2)

    def convert_to_str(self, value, base):
        return str(value) if base == 'd' else bin(value)[2:]

    def execute(self, instruction):
        parts = instruction.strip().split()
        if len(parts) != 4:
            raise ValueError("Komut formatı hatalı! Örn: ADD x1 x2 x3")

        op, r_dest, r_src1, r_src2 = parts

        if not self.check_register_base(r_src1, r_src2):
            raise ValueError("Farklı tabandaki sayılarla işlem yapılamaz!")

        val1_str, base = self.registers[r_src1]
        val2_str, _ = self.registers[r_src2]

        val1 = self.convert_to_int(val1_str, base)
        val2 = self.convert_to_int(val2_str, base)

        if op == "ADD":
            result = val1 + val2
        elif op == "SUB":
            result = val1 - val2
        elif op == "MUL":
            result = val1 * val2
        elif op == "DIV":
            if val2 == 0:
                raise ZeroDivisionError("0'a bölme hatası!")
            result = val1 // val2
        elif op == "AND":
            result = val1 & val2
        elif op == "OR":
            result = val1 | val2
        elif op == "XOR":
            result = val1 ^ val2
        else:
            raise ValueError("Geçersiz işlem komutu!")

        if r_dest == "x0":
            return  # x0 değişemez

        result_str = self.convert_to_str(result, base)
        self.registers[r_dest] = (result_str, base)

    def print_registers(self):
        print("\n--- REGISTER DURUMU ---")
        for reg, (val, base) in self.registers.items():
            if base == 'd':
                print(f"{reg}: d-{val}")
            else:
                print(f"{reg}: b-{val}")
