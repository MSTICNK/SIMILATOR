class Registers:
    def __init__(self):
        self.registers = [0] * 32

    def get_register_index(self, reg_name):
        """ Register adını alır ('x2', 'x5' gibi) ve integer index'e çevirir """
        if isinstance(reg_name, str) and reg_name.startswith("x") and reg_name[1:].isdigit():
            index = int(reg_name[1:])
            if 0 <= index < 32:
                return index
        raise ValueError(f"Geçersiz register adı: {reg_name}")

    def read(self, reg_name):
        """ Register'dan değer okuma (string veya int olarak girebilirsin) """
        reg_num = self.get_register_index(reg_name) if isinstance(reg_name, str) else reg_name
        return self.registers[reg_num]

    def write(self, reg_name, value):
        """ Register'a değer yazma (x0 hariç) """
        reg_num = self.get_register_index(reg_name) if isinstance(reg_name, str) else reg_name
        if reg_num != 0:
            self.registers[reg_num] = value

    def dump(self):
        print("\n--- REGISTER DUMP ---")
        for i, value in enumerate(self.registers):
            print(f"x{i}: {value}")
        print("---------------------\n")

    def set_register(self, reg_name, value):
        """ Register'a değer atama """
        reg_num = self.get_register_index(reg_name) if isinstance(reg_name, str) else reg_name
        if 0 <= reg_num < len(self.registers):
            self.registers[reg_num] = value
        else:
            print(f"Hata: Geçersiz register dizini {reg_num}")

    def get_register(self, reg_name):
        """ Register'dan değer okuma """
        reg_num = self.get_register_index(reg_name) if isinstance(reg_name, str) else reg_name
        if 0 <= reg_num < len(self.registers):
            return self.registers[reg_num]
        else:
            print(f"Hata: Geçersiz register dizini {reg_num}")
            return None
