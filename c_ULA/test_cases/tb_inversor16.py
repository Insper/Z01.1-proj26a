import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_inversor16(dut):

    ina = [0x0000, 0x0000]
    inz = [0, 1]
    outy =[0x0000, 0xFFFF]
    
    for i in range(len(ina)):
        dut.a.value = ina[i]
        dut.z.value = inz[i]

        await Timer(1, units="ns")
        condition = (dut.y.value == outy[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outy[i]) + " Obtained value: " + str(dut.y.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


