from core.memory import Memory
from core.registers import Registers
from core.pipeline import Pipeline
from core.instructions import InstructionSet


def test_pipeline():
    # Belleği ve register'ları başlat
    memory = Memory()
    registers = Registers()

    # InstructionSet'i başlatırken registers parametresini geçiyoruz
    instruction_set = InstructionSet(registers)

    # Komutları belleğe yaz
    commands = [
        "LOAD x0 10",  # x0 register'ına 10 yükle
        "ADD x0 x1",  # x0 ve x1'i topla, sonucu x0'a yaz
        "SUB x0 x2"  # x0 ve x2'yi çıkar, sonucu x0'a yaz
    ]

    # Komutları belleğe yaz
    address = 0
    for command in commands:
        memory.write(address, command)
        address += 1  # Sonraki adrese geç

    # Pipeline'ı başlat
    pipeline = Pipeline(memory, registers, instruction_set)

    # İlk komut çalıştırılıyor
    pipeline.run_cycle(0)  # 0. adresi kullanarak komutları çalıştır
    # İkinci komut çalıştırılıyor
    pipeline.run_cycle(1)  # 1. adresi kullanarak komutları çalıştır
    # Üçüncü komut çalıştırılıyor
    pipeline.run_cycle(2)  # 2. adresi kullanarak komutları çalıştır

    # Beklenen değerler
    assert registers.read("x0") == 10  # LOAD x0, 10 komutundan sonra x0 = 10
    assert registers.read("x0") == 10  # ADD x0, x1 komutunda x1 varsayılan olarak 0 olduğu için x0 = 10
    assert registers.read("x0") == 10  # SUB x0, x2 komutunda x2 varsayılan olarak 0 olduğu için x0 = 10

    print(f"Test Passed: {registers.read('x0')}")

