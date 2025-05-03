import unittest
from core.registers import Registers
from core.instructions import InstructionSet
from core.pipeline import Pipeline
from core.memory import Memory


class TestCPU(unittest.TestCase):

    def setUp(self):
        """Test için gerekli başlangıç ayarları"""
        self.registers = Registers()
        self.memory = Memory()  # Memory sınıfını tanımladığınızı varsayıyorum
        self.instruction_set = InstructionSet(self.registers)
        self.pipeline = Pipeline(self.memory, self.registers, self.instruction_set)

    def test_load(self):
        """LOAD komutunu test et"""
        self.instruction_set.load("x1", 10)  # x1 register'ına 10 yükle
        self.assertEqual(self.registers.read("x1"), 10)  # x1 register'ının değeri 10 olmalı

    def test_add(self):
        """ADD komutunu test et"""
        self.registers.write("x1", 5)
        self.registers.write("x2", 3)
        self.instruction_set.add("x3", "x1", "x2")  # x1 + x2 işlemi sonucu x3'e yazılacak
        self.assertEqual(self.registers.read("x3"), 8)  # x3 register'ının değeri 8 olmalı

    def test_sub(self):
        """SUB komutunu test et"""
        self.registers.write("x1", 10)
        self.registers.write("x2", 5)
        self.instruction_set.sub("x3", "x1", "x2")  # x1 - x2 işlemi sonucu x3'e yazılacak
        self.assertEqual(self.registers.read("x3"), 5)  # x3 register'ının değeri 5 olmalı

    def test_mul(self):
        """MUL komutunu test et"""
        self.registers.write("x1", 3)
        self.registers.write("x2", 4)
        self.instruction_set.mul("x3", "x1", "x2")  # x1 * x2 işlemi sonucu x3'e yazılacak
        self.assertEqual(self.registers.read("x3"), 12)  # x3 register'ının değeri 12 olmalı

    def test_div_zero(self):
        """Zero division hatasını test et"""
        self.registers.write("x1", 10)
        self.registers.write("x2", 0)
        with self.assertRaises(ZeroDivisionError):
            self.instruction_set.div("x3", "x1", "x2")  # x2'yi sıfır yaparak hata almayı bekliyoruz

    def test_pipeline(self):
        """Pipeline'da tüm aşamaların çalıştığını test et"""
        self.memory.write(0, "LOAD x1 10")  # x1'e 10 yükle
        self.memory.write(1, "LOAD x2 5")  # x2'ye 5 yükle
        self.memory.write(2, "ADD x1 x2 x3")  # x1 ve x2'yi topla, sonucu x3'e yaz
        self.memory.write(3, "SUB x3 x1 x2")  # x3 ile x1'i çıkar, sonucu x2'ye yaz

        # Pipeline döngüsünü başlat
        self.pipeline.run_cycle(0)  # İlk komut LOAD (x1)
        self.pipeline.run_cycle(1)  # İkinci komut LOAD (x2)
        self.pipeline.run_cycle(2)  # Üçüncü komut ADD
        self.pipeline.run_cycle(3)  # Dördüncü komut SUB

        # Test et, her komut sonrası değerler doğru şekilde işlenmiş mi
        self.assertEqual(self.registers.read("x3"), 15)  # 10 + 5 = 15 olmalı

    def tearDown(self):
        """Test sonrası temizlik işlemleri"""
        self.registers = None
        self.memory = None
        self.instruction_set = None
        self.pipeline = None


if __name__ == "__main__":
    unittest.main()
