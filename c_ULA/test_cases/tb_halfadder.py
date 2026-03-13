import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_halfadder(dut):

    inA =     [0, 0, 1, 1]
    inB =     [0, 1, 0, 1]
    outsoma = [0, 1, 1, 0]
    outvaium= [0, 0, 0, 1]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.soma.value == outsoma[i] and dut.vaium.value == outvaium[i])
        if not condition:
            if not (dut.soma.value == outsoma[i]):
                dut._log.error("Expected value soma: " + "{0:b}".format(outsoma[i]) + " Obtained value soma: " + str(dut.soma.value) )
            if not (dut.vaium.value == outvaium[i]):
                dut._log.error("Expected value vaium: " + "{0:b}".format(outvaium[i]) + " Obtained value vaium: " + str(dut.vaium.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


