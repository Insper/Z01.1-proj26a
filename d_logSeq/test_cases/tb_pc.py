import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_pc(dut):

    inincrement = [1, 1, 0, 0, 0, 1]
    inload      = [0, 0, 0, 0, 1, 0]
    inreset     = [0, 0, 0, 1, 0, 0]
    ininput     = [0x0000, 0x0000, 0x5555, 0x5555, 0x5555, 0x0000]
    outoutput   = [0x0001, 0x0002, 0x0002, 0x0000, 0x5555, 0x5556]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.increment.value = inincrement[i]
        dut.load.value = inload[i]
        dut.reset.value = inreset[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)

