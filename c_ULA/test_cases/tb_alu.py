import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_alu(dut):

    inX =     [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000]
    inY =     [0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF]
    outsaida =[0x0000, 0x0001, 0xFFFF, 0x0000, 0xFFFF, 0xFFFF, 0x0000, 0x0000, 0x0001, 0x0001, 0x0000, 0xFFFF, 0xFFFE, 0xFFFF, 0x0001, 0xFFFF, 0x0000, 0xFFFF]
    inzx = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
    innx = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    inzy = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    inny = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    inf  = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    inno = [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    outng= [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    outzr= [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    
    

    for i in range(len(inX)):
        dut.x.value = inX[i]
        dut.y.value = inY[i]
        dut.zx.value = inzx[i]
        dut.nx.value = innx[i]
        dut.zy.value = inzy[i]
        dut.ny.value = inny[i]
        dut.f.value =  inf[i]
        dut.no.value = inno[i]

        await Timer(1, units="ns")
        condition = (dut.saida.value == outsaida[i] and dut.zr.value == outzr[i] and dut.ng.value == outng[i])
        if not condition:
            if not (dut.saida.value == outsaida[i]):
                dut._log.error("Expected value: " + "{0:016b}".format(outsaida[i]) + " Obtained value: " + str(dut.saida.value) )
            if not (dut.zr.value == outzr[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outzr[i]) + " Obtained value: " + str(dut.zr.value) )
            if not (dut.ng.value == outng[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outng[i]) + " Obtained value: " + str(dut.ng.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")

