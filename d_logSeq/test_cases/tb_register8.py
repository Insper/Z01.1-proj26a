import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_register8(dut):

    ininput =   [0b00100001, 0b11011110, 0b11011110, 0b11111111]
    inload  =   [1, 0, 1, 0]
    outoutput = [0b00100001, 0b00100001, 0b11011110, 0b11011110]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:08b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


