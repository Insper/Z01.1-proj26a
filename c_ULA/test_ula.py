from cocotb_test.simulator import run
import pytest
import os

def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)

def test_zerador16():
    run(vhdl_sources=[source("zerador16.vhd")], 
        toplevel="zerador16", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_zerador16" , 
        toplevel_lang="vhdl")

def test_inversor16():
    run(vhdl_sources=[source("inversor16.vhd")], 
        toplevel="inversor16", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_inversor16" , 
        toplevel_lang="vhdl")

def test_comparador16():
    run(vhdl_sources=[source("comparador16.vhd")], 
        toplevel="comparador16", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_comparador16" , 
        toplevel_lang="vhdl")

def test_fulladder():
    run(vhdl_sources=[source("fulladder.vhd")], 
        toplevel="fulladder", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_fulladder" , 
        toplevel_lang="vhdl")

def test_halfadder():
    run(vhdl_sources=[source("halfadder.vhd")], 
        toplevel="halfadder", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_halfadder" , 
        toplevel_lang="vhdl")

def test_add16():
    run(vhdl_sources=[source("add16.vhd"), source("fulladder.vhd")], 
        toplevel="add16", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_add16" , 
        toplevel_lang="vhdl")

def test_inc16():
    run(vhdl_sources=[source("inc16.vhd"), source('add16.vhd'), source('fulladder.vhd')], 
        toplevel="inc16", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_inc16" , 
        toplevel_lang="vhdl")

def test_alu():
    run(vhdl_sources=[source("alu.vhd"),source("zerador16.vhd"), source("inversor16.vhd"), source("add16.vhd"), source("fulladder.vhd"), source("../../b_logComb/src/and16.vhd"), source("comparador16.vhd"), source("../../b_logComb/src/mux16.vhd")], 
        toplevel="alu", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_alu" , 
        toplevel_lang="vhdl")


  
if __name__ == "__main__":
    test_zerador16()
    test_inversor16()
    test_comparador16()
    test_fulladder()
    test_halfadder()
    test_add16()
    test_inc16()
    test_alu()
