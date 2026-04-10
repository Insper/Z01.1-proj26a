import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_flipflopd(dut):

    ind      = [0, 1, 0, 0, 1, 1]
    inpreset = [0, 0, 1, 0, 0, 0]
    inclear  = [1, 0, 0, 0, 0, 1]
    outq     = [0, 1, 1, 0, 1, 0]
    
    clock = Clock(dut.clock, len(ind), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ind)):
        dut.d.value = ind[i]
        dut.preset.value = inpreset[i]
        dut.clear.value = inclear[i]

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)

