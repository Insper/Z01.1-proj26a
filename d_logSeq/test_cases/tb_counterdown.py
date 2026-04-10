import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_counterdown(dut):

    outq = [0b111, 0b110, 0b101, 0b100, 0b011, 0b010, 0b001, 0b000]
    
    clock = Clock(dut.clock, len(outq), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(outq)):

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)


