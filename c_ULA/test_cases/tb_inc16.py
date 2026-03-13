import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_inc16(dut):

    inA = [0b0000000000000000, 0b1111111111111111, 0b0000000000000101, 0b1111111111111011]
    outq =[0b0000000000000001, 0b0000000000000000, 0b0000000000000110, 0b1111111111111100]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


