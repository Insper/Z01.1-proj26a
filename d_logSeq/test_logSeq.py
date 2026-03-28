from cocotb_test.simulator import run
import pytest
import os

def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)

def test_flipflopjk():
    run(vhdl_sources=[source("conceito_a/flipflopjk.vhd")], 
        toplevel="flipflopjk", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module="tb_flipflopjk" , 
        toplevel_lang="vhdl")

def test_flipflopt():
    run(vhdl_sources=[source("conceito_a/flipflopt.vhd")], 
        toplevel="flipflopt", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_flipflopt', 
        toplevel_lang="vhdl")

def test_counterdown():
    run(vhdl_sources=[source('conceito_a/counterdown.vhd'),source("conceito_a/flipflopt.vhd")], 
        toplevel="counterdown", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_counterdown', 
        toplevel_lang="vhdl")

def test_flipflopd():
    run(vhdl_sources=[source("flipflopd.vhd")], 
        toplevel="flipflopd", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_flipflopd', 
        toplevel_lang="vhdl")

def test_binarydigit():
    run(vhdl_sources=[source("binarydigit.vhd"),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], 
        toplevel="binarydigit", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_binarydigit', 
        toplevel_lang="vhdl")

def test_register8():
    run(vhdl_sources=[source('register8.vhd'),source("binarydigit.vhd"),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], 
        toplevel="register8", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_register8', 
        toplevel_lang="vhdl")

def test_register16():
    run(vhdl_sources=[source('register16.vhd'),source('register8.vhd'),source("binarydigit.vhd"),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], 
        toplevel="register16", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_register16', 
        toplevel_lang="vhdl")

def test_register32():
    run(vhdl_sources=[source('register32.vhd'),source('register16.vhd'),source('register8.vhd'),source("binarydigit.vhd"), source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], 
        toplevel="register32", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_register32', 
        toplevel_lang="vhdl")

def test_register64():
    run(vhdl_sources=[source('register64.vhd'),source('register32.vhd'),source('register16.vhd'),source('register8.vhd'), source("binarydigit.vhd"),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], 
        toplevel="register64", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_register64', 
        toplevel_lang="vhdl")


def test_pc():
    run(vhdl_sources=[source("pc.vhd"),source('register16.vhd'),source('register8.vhd'),source('binarydigit.vhd'),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd'),source('../../b_logComb/src/mux16.vhd'),source('../../c_ULA/src/inc16.vhd'), source('../../c_ULA/src/add16.vhd'), source('../../c_ULA/src/fulladder.vhd')], 
        toplevel="pc", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_pc', 
        toplevel_lang="vhdl")


def test_ram8():
    run(vhdl_sources=[source('ram8.vhd'), source('register16.vhd'), source('register8.vhd'), source('binarydigit.vhd'), source('flipflopd.vhd'), source('../../b_logComb/src/mux2way.vhd'), source('../../b_logComb/src/mux8way16.vhd'), source('../../b_logComb/src/dmux8way.vhd')], 
        toplevel="ram8", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_ram8', 
        toplevel_lang="vhdl")


def test_ram64():
    run(vhdl_sources=[source('ram64.vhd'), source('ram8.vhd'), source('register16.vhd'), source('register8.vhd'), source('binarydigit.vhd'), source('flipflopd.vhd'), source('../../b_logComb/src/mux2way.vhd'), source('../../b_logComb/src/mux8way16.vhd'), source('../../b_logComb/src/dmux8way.vhd')], 
        toplevel="ram64", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_ram64', 
        toplevel_lang="vhdl")


def test_ram512():
    run(vhdl_sources=[source('ram512.vhd'), source('ram64.vhd'), source('ram8.vhd'), source('register16.vhd'), source('register8.vhd'), source('binarydigit.vhd'), source('flipflopd.vhd'), source('../../b_logComb/src/mux2way.vhd'), source('../../b_logComb/src/mux8way16.vhd'), source('../../b_logComb/src/dmux8way.vhd')], 
        toplevel="ram512", 
        python_search=[os.path.join(os.path.dirname(__file__), 'test_cases')],
        module='tb_ram512', 
        toplevel_lang="vhdl")


if __name__ == "__main__":
    test_flipflopd()

