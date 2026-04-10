-------------------------------------------------------------------
-- Elementos de Sistemas
-------------------------------------------------------------------
-- Renan Trevisoli
-------------------------------------------------------------------
-- Descricao :
-- Mapeamento de memoria
-------------------------------------------------------------------
-- LEDs						address=16384
-- SWs						address=16385
-- GPIO(9-0) - input 	address=16386
-- GPIO(26-35) - output address=16387
-------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity MemoryIO is
   PORT(
        CLK				: IN  STD_LOGIC;
		  ADDRESS		: IN  STD_LOGIC_VECTOR (14 DOWNTO 0);
		  
		  --RAM
        INPUT			: IN  STD_LOGIC_VECTOR (15 DOWNTO 0);
        LOAD			: IN  STD_LOGIC ;
        OUTPUT			: OUT STD_LOGIC_VECTOR (15 DOWNTO 0);
		  
		  --INPUTS/OUTPUTS
        SW  	: in std_logic_vector(9 downto 0);
		  GPIN	: INOUT std_logic_vector(9 downto 0);
        LED 	: OUT std_logic_vector(9 downto 0);		  
		  GPOUT 	: INOUT std_logic_vector(9 downto 0)
		);
end entity;


ARCHITECTURE logic OF MemoryIO IS

  component RAM IS
      PORT
      (
          address	: IN STD_LOGIC_VECTOR (13 DOWNTO 0);
          clock		: IN STD_LOGIC  := '1';
          data		: IN STD_LOGIC_VECTOR (15 DOWNTO 0);
          wren		: IN STD_LOGIC ;
          q		   : OUT STD_LOGIC_VECTOR (15 DOWNTO 0)
      );
  end component;

  component Register16 is
    port(
      clock:   in STD_LOGIC;
      input:   in STD_LOGIC_VECTOR(15 downto 0);
      load:    in STD_LOGIC;
      output: out STD_LOGIC_VECTOR(15 downto 0)
      );
  end component;

  SIGNAL LOAD_RAM		: STD_LOGIC := '0';
  SIGNAL LOAD_GPOUT	: STD_LOGIC := '0';
  SIGNAL LOAD_LED		: STD_LOGIC := '0';

  SIGNAL OUTPUT_RAM	: STD_LOGIC_VECTOR(15 downto 0);
  SIGNAL SW16			: STD_LOGIC_VECTOR(15 downto 0);
  SIGNAL LED16			: STD_LOGIC_VECTOR(15 downto 0);
  SIGNAL GPIN16		: STD_LOGIC_VECTOR(15 downto 0);
  SIGNAL GPOUT16		: STD_LOGIC_VECTOR(15 downto 0);

BEGIN

  RAM16: RAM
    PORT MAP(
      address => ADDRESS(13 downto 0),
      clock		=> CLK,
      data		=> INPUT,
      wren		=> LOAD_RAM,
      q		    => OUTPUT_RAM
      );

   reg_LED:  Register16
      port map(
        clock => CLK,
        input => INPUT,
        load  => LOAD_LED,
        output => LED16
        );
		  
   reg_GPout:  Register16
      port map(
        clock => CLK,
        input => INPUT,
        load  => LOAD_GPOUT,
        output => GPOUT16
        );

    ----------------------------------------
    -- Controla os LOAD
    ----------------------------------------
    LOAD_RAM	  <= ???????? 
    LOAD_GPOUT   <= ????????
    LOAD_LED     <= ????????

    ----------------------------------------
    -- SW, LED e GPIO                     --
    ----------------------------------------
    -- Compatibilidade de tamanho
    LED <= LED16(9 downto 0);
	 GPOUT <= GPOUT16(9 downto 0);

    -- Compatibilidade de tamanho
    SW16(15 downto 10) <= (others => '0');
    SW16( 9 DOWNTO  0) <= SW;
	 GPIN16(15 downto 10) <= (others => '0');
    GPIN16( 9 DOWNTO  0) <= GPIN;

    ----------------------------------------
    -- SAIDA do memory I/O                --
    ----------------------------------------
    -- precisar ser: RAM ou SW16
    OUTPUT <= ????????

END logic;
