import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_flipflopjk(dut):

    inJ     = [0, 0, 1, 1, 1]
    inK     = [0, 1, 0, 1, 1]
    outq    = [0, 0, 1, 0, 1]
    outnotq = [1, 1, 0, 1, 0]
    
    clock = Clock(dut.clock, len(inJ), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(inJ)):
        dut.J.value = inJ[i]
        dut.K.value = inK[i]

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i] and dut.notq.value == outnotq[i])
        if not condition:
            if not dut.q.value == outq[i]:
                dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            if not dut.notq.value == outnotq[i]:
                dut._log.error("Expected value: " + "{0:b}".format(outnotq[i]) + " Obtained value: " + str(dut.notq.value) )
            assert condition, "Error in test {0}!".format(i) 

