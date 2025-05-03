class Memory:
    def __init__(self):
        self.memory = {}


    def load(self, address, data):
        """ Belleğe veri yükle """
        self.memory[address] = data
        print(f"Adrese Veri Yükleniyor. {address}: {data}")

    def read(self, address):
        """ Bellekten veri oku """
        return self.memory.get(address, "BOŞ")

    def write(self, address, data):
        self.memory[address] = data
        print(f"Adrese Veri Yaz. {address}: {data}")

    def __len__(self):
        # Belleğin boyutunu döndür
        return len(self.memory)

