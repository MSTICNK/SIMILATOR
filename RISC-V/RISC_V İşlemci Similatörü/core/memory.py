class Memory:
    def __init__(self):
        # Basit bir RAM: adres (int) -> komut (str) şeklinde saklanır
        self.memory = {}

    def write(self, address, instruction):
        """
        Belleğe komut yaz. Örn: memory.write(0, "ADD x1 x2 x3")
        """
        if not isinstance(address, int):
            raise ValueError("Adres tam sayı olmalı.")
        self.memory[address] = instruction

    def read(self, address):
        """
        Verilen adresteki komutu oku.
        """
        if not isinstance(address, int):
            raise ValueError("Adres tam sayı olmalı.")
        return self.memory.get(address, "NOP")  # Adreste veri yoksa 'NOP' (işlem yok)

    def get_all_memory(self):
        """
        Bütün belleği döndür (arayüzde göstermek için)
        """
        return dict(sorted(self.memory.items()))
