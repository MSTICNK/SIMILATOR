import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.registers import Registers
regs = Registers()
def test_registers():
    regs = Registers()

    # Test verileri yaz
    regs.write(1, 412)   # x1 = 412
    regs.write(2, 100)   # x2 = 100
    regs.write(0, 999)   # x0 değişmemeli!
    regs.write(4, 394)   # x4 = 394

    # Test sonuçlarını kontrol et
    assert regs.read(1) == 412  # x1 412 olmalı
    assert regs.read(2) == 100  # x2 100 olmalı
    assert regs.read(0) == 0    # x0 0 olmalı (değişmemeli)
    assert regs.read(4) == 394  # x4 394 olmalı

# Test verileri yaz
regs.write(1, 412)   # x1 = 412
regs.write(2, 100)  # x2 = 100
regs.write(0, 999)  # x0 değişmemeli!
regs.write(4 ,394)  # x4 = 394
print("Test Sonuçları:")
print("x1:", regs.read(1))  # 42 olmalı
print("x2:", regs.read(2))  # 100 olmalı
print("x0:", regs.read(0))  # 0 olmalı

regs.dump()
