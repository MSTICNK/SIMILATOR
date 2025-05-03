from core.instructions import InstructionSet
from core.registers import Registers
from core.pipeline import Pipeline

class Processor:
    def __init__(self, memory, registers):
        self.memory = memory
        self.registers = Registers
        self.pipeline = Pipeline(memory, registers)

    def run(self, start_pc):
        """ İşlemciyi çalıştırır, komutları pipeline üzerinden yürütür. """
        pc = start_pc
        while pc < len(self.memory):  # Bellekte komut olduğu sürece çalıştır
            self.pipeline.run_cycle(pc)
            pc += 1  # Bir sonraki komuta geç

    def run_instruction(self, instruction):
        """ Tek bir komutu alır ve işler. """
        parts = instruction.split()

        if len(parts) != 4:
            return "Hata: Komut yanlış formatta!"

        op, rd, rs1, rs2 = parts  # add x1, x2, x3 gibi

        # Eğer register'lar doğru mu kontrol et
        if rd not in self.registers.registers or rs1 not in self.registers.registers or rs2 not in self.registers.registers:
            return "Hata: Geçersiz register!"

        # Komutu çalıştır
        try:
            if op == "add":
                self.pipeline.execute_add(rd, rs1, rs2)
            elif op == "sub":
                self.pipeline.execute_sub(rd, rs1, rs2)
            elif op == "mul":
                self.pipeline.execute_mul(rd, rs1, rs2)
            elif op == "div":
                self.pipeline.execute_div(rd, rs1, rs2)
            else:
                return "Hata: Bilinmeyen komut!"
        except Exception as e:
            return f"Hata: {e}"

        return f"{rd} = {self.registers.read(rd)}"  # Sonucu döndür
