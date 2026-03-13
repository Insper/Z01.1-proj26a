import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def tb_add16(dut):

    inA = [0b0000000000000000, 0b0000000000000000, 0b1111111111111111, 0b1010101010101010, 0b0011110011000011, 0b0001001000110100, 0b0000000000000001]
    inB = [0b0000000000000001, 0b1111111111111111, 0b1111111111111111, 0b0101010101010101, 0b0000111111110000, 0b1001100001110110, 0b1111111111111111]
    outq =[0b0000000000000001, 0b1111111111111111, 0b1111111111111110, 0b1111111111111111, 0b0100110010110011, 0b1010101010101010, 0b0000000000000000]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


