from core.cpu import CPU
from core.memory import Memory
cpu = CPU()
cpu.set_register("x1", "d-10")
cpu.set_register("x2", "d-20")
cpu.execute("ADD x1 x2 x3")
print(cpu.get_registers()["x3"])  # (30, 'd')

def test_add():
    cpu = CPU()
    mem = Memory()
    mem.write(0, "ADD x1 x2 x3")
    cpu.registers["x1"] = 10
    cpu.registers["x2"] = 5
    cpu.execute(mem.read(0))
    assert cpu.registers["x3"] == 15
    print("✅ test_add geçti")

def test_div_zero():
    cpu = CPU()
    mem = Memory()
    mem.write(0, "DIV x1 x2 x3")
    cpu.registers["x1"] = 10
    cpu.registers["x2"] = 0
    try:
        cpu.execute(mem.read(0))
    except ZeroDivisionError:
        print("✅ test_div_zero geçti (sıfıra bölme hatası yakalandı)")
    else:
        print("❌ test_div_zero başarısız")

def test_logic():
    cpu = CPU()
    mem = Memory()
    mem.write(0, "AND x1 x2 x3")
    cpu.registers["x1"] = 0b1010
    cpu.registers["x2"] = 0b1100
    cpu.execute(mem.read(0))
    assert cpu.registers["x3"] == (0b1010 & 0b1100)
    print("✅ test_logic geçti")

def test_invalid_instruction():
    cpu = CPU()
    try:
        cpu.execute("INVALID x1 x2 x3")
    except ValueError as e:
        print("✅ test_invalid_instruction geçti (hata yakalandı)")
    else:
        print("❌ test_invalid_instruction başarısız")

if __name__ == "__main__":
    test_add()
    test_div_zero()
    test_logic()
    test_invalid_instruction()
