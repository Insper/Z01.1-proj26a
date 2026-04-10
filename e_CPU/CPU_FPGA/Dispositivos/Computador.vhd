-------------------------------------------------------------------
-- Elementos de Sistemas
-------------------------------------------------------------------
-- Luciano Pereira
-------------------------------------------------------------------
-- Descricao :
-- Entidade central do desenvolvimento do computador
-------------------------------------------------------------------
-- Historico:
--  29/11/2016 : Criacao do projeto
-------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity Computador is
   generic(
        IS_SIMULATION : std_logic := '1'
   );
   port(
        -- Sistema
        CLOCK_50     : in    std_logic;
        RESET_N      : in    std_logic;
        LEDR         : out   std_logic_vector(9 downto 0);
        SW           : in    std_logic_vector(9 downto 0);
		  GPIO  			: inout std_logic_vector(35 downto 0)
		  --GPIO(26 to 35)    : out    std_logic_vector(9 downto 0)
       );
end entity;


architecture logic of Computador is

	component CPU is
		 port(
			  clock       :	in  std_logic;
			  inM         : in  std_logic_vector(15 downto 0);
			  instruction : in  std_logic_vector(17 downto 0);
			  reset       : in  std_logic;
			  outM        : out std_logic_vector(15 downto 0);
			  writeM      : out std_logic;
			  addressM    : out std_logic_vector(14 downto 0);
			  pcout       : out std_logic_vector(14 downto 0)
	  );
	end component;

	component ROM is
		port(
			address	  : in std_logic_vector (14 downto 0);
			clock	    : in std_logic  := '1';
			q		      : out std_logic_vector (17 downto 0)
		);
	end component;

	component MemoryIO is
		port(
		  CLK				: IN  STD_LOGIC;
		  ADDRESS		: IN  STD_LOGIC_VECTOR (14 DOWNTO 0);
		  
		  --RAM
        INPUT			: IN  STD_LOGIC_VECTOR (15 DOWNTO 0);
        LOAD			: IN  STD_LOGIC ;
        OUTPUT			: OUT STD_LOGIC_VECTOR (15 DOWNTO 0);
		  
		  --INPUTS/OUTPUTS
        SW  	: in std_logic_vector(9 downto 0);
		  GPIN	: inout std_logic_vector(9 downto 0);
        LED 	: OUT std_logic_vector(9 downto 0);		  
		  GPOUT 	: INOUT std_logic_vector(9 downto 0)
			 );
	end component;

  signal INPUT        : std_logic_vector(15 downto 0) := "1111111111111111";
  signal ADDRESS      : std_logic_vector(14 downto 0) := (others => '0') ; -- meio 00100101101010
  signal LOAD         : std_logic := '0';
  signal GPOUT10		 : std_logic_vector(9 downto 0);
  signal GPIN10		 : std_logic_vector(9 downto 0);

  signal RST_CPU              : std_logic := '1';

  signal OUTPUT_RAM   : std_logic_vector(15 downto 0);
  signal INSTRUCTION  : std_logic_vector(17 downto 0);
  signal PC           : std_logic_vector(14 downto 0);

begin

GPIN10 <= GPIO(9 downto 0);
GPOUT10 <= GPIO(35 downto 26);


MAIN_CPU : CPU port map (
    clock       => CLOCK_50,
    inM         => OUTPUT_RAM,
    instruction => instruction,
    reset       => RST_CPU,
    outM        => INPUT,
    writeM      => LOAD,
    addressM    => ADDRESS,
    pcout       => PC
	);

ROM32k : ROM port map (
    address	=> PC(14 downto 0),
    clock	  => CLOCK_50,
    q		    => INSTRUCTION
    );

MEMORY_MAPED : MemoryIO port map (
    CLK         => CLOCK_50,
    ADDRESS		 => ADDRESS,
    INPUT       => INPUT,
    LOAD        => LOAD,
    OUTPUT		 => OUTPUT_RAM,
    SW          => SW,
	 GPIN        => GPIN10,
    LED         => LEDR,
	 GPOUT       => GPOUT10
   );

end logic;
