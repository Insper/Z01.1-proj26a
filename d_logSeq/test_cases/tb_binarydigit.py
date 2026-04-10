import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock


@cocotb.test()
async def tb_binarydigit(dut):

    ininput =   [0, 1, 1, 0]
    inload  =   [1, 0, 1, 0]
    outoutput = [0, 0, 1, 1]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


