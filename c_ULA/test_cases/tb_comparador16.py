import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_comparador16(dut):

    ina =   [0x0000, 0x8000, 0x5555]
    outzr = [1, 0, 0]
    outng = [0, 1, 0]
    
    for i in range(len(ina)):
        dut.a.value = ina[i]

        await Timer(1, units="ns")
        condition = (dut.zr.value == outzr[i] and dut.ng.value == outng[i])
        if not condition:
            if not (dut.zr.value == outzr[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outzr[i]) + " Obtained value: " + str(dut.zr.value) )
            if not (dut.ng.value == outng[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outng[i]) + " Obtained value: " + str(dut.ng.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")

