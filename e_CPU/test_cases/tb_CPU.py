import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def tb_CPU(dut):

    ininstruction = [0x00000, 0x00000, 0x23810, 0x00001, 0x22390, 0x0000C, 0x20603, 0x00001, 0x23810, 0x00002, 0x20620, 0x00000, 0x00000]
    inM           = [      0,  0x8009,  0x8009,  0x8009,  0x8106,  0x8106,  0x0000,  0x0000,  0x8106,  0x8106,  0x0000,  0x0000,  0x8009]
    inreset       = [      1,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]
    
    outM          = [ 0x0000,  0x0000,  0x8009,  0x0001,  0x8009,  0x000C,  0x00FD,  0x0001,  0x8106,  0x0002,  0x8106,  0x0000,  0x0000]
    outAddress    = [ 0x0000,  0x0000,  0x0000,  0x0001,  0x0001,  0x000C,  0x000C,  0x0001,  0x0001,  0x0002,  0x0002,  0x0000,  0x0000]
    outWrite      = [      0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       1,       0,       0]
    outpcout      = [ 0x0000,  0x0001,  0x0002,  0x0003,  0x0004,  0x0005,  0x000C,  0x000D,  0x000E,  0x000F,  0x0010,  0x0011,  0x0012]
    

    clock = Clock(dut.clock, len(ininstruction), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)

    for i in range(len(ininstruction)):
        dut.instruction.value = ininstruction[i]
        dut.inM.value = inM[i]
        dut.reset.value = inreset[i]

        await FallingEdge(dut.clock)

        if i > 1:
            condition = (dut.outM.value == outM[i] and dut.writeM.value == outWrite[i] and dut.addressM.value == outAddress[i] and
                        dut.pcout.value == outpcout[i])
            if not condition:
                if not (dut.outM.value == outM[i]):
                    dut._log.error("Expected value outM: " + "{0:016b}".format(outM[i]) + " Obtained value outM: " + str(dut.outM.value) )
                if not (dut.writeM.value == outWrite[i]):
                    dut._log.error("Expected value writeM: " + "{0:b}".format(outWrite[i]) + " Obtained value writeM: " + str(dut.writeM.value) )
                if not (dut.addressM.value == outAddress[i]):
                    dut._log.error("Expected value addressM: " + "{0:015b}".format(outAddress[i]) + " Obtained value addressM: " + str(dut.addressM.value) )
                if not (dut.pcout.value == outpcout[i]):
                    dut._log.error("Expected value pcout: " + "{0:015b}".format(outpcout[i]) + " Obtained value pcout: " + str(dut.pcout.value) )
                assert condition, "Error in test {0}!".format(i)
            await Timer(1, units="ns")

