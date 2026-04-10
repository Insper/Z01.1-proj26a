import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_ram512(dut):

    ininput =   [0x0000, 0xAAAA, 0xAAAA, 0xFFFF, 0xFFFF, 0xFFFF, 0xF0F0]
    inload  =   [     1,      0,      1,      0,      0,      1,      0]
    inaddress = [ 0x000,  0x000,  0x003,  0x000,  0x003,  0x13A,  0x13A]
    outoutput = [0x0000, 0x0000, 0xAAAA, 0x0000, 0xAAAA, 0xFFFF, 0xFFFF]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]
        dut.address.value = inaddress[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)

