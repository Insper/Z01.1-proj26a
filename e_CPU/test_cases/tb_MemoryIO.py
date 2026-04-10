import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_MemoryIO(dut):

    inINPUT =   [0xA5A5, 0x0000, 0xAAA3, 0xFFFF, 0x5A5A, 0xFFFF, 0xF0F0, 0xFFFF]
    inLOAD  =   [     1,      0,      1,      0,      1,      0,      0,      1]
    inSW    =   [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x02AA, 0x02AA]
    inADDRESS = [0x0000, 0x0000, 0x2000, 0x2000, 0x3FFF, 0x3FFF, 0x52C1, 0x2000]
    outOUTPUT = [0xA5A5, 0xA5A5, 0xAAA3, 0xAAA3, 0x5A5A, 0x5A5A, 0x02AA, 0xFFFF]
    
    
    clock = Clock(dut.CLK_FAST, len(inINPUT), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.CLK_FAST)
    for i in range(len(inINPUT)):
        dut.INPUT.value = inINPUT[i]
        dut.LOAD.value = inLOAD[i]
        dut.SW.value = inSW[i]
        dut.ADDRESS.value = inADDRESS[i]

        await FallingEdge(dut.CLK_FAST)

        condition = (dut.OUTPUT.value == outOUTPUT[i])
        if not condition:
            dut._log.error("Expected value OUTPUT: " + "{0:016b}".format(outOUTPUT[i]) + " Obtained value OUTPUT: " + str(dut.OUTPUT.value) )
            assert condition, "Error in test {0}!".format(i)

