/*module*/
//module
/*
module
Copyright (c) 2019 Alex Forencich

Permission is hereby g
*/

// Language: Verilog 2001

`timescale 1ns / 1ps

/*
 * AXI4-Stream asynchronous FIFO with width converter
 */

module wrap #(
	parameter DROP_BAD_FRAME = 0,
	parameter DROP_WHEN_FULL = 0,
	parameter M_DATA_WIDTH = 16,
	parameter M_KEEP_WIDTH = M_DATA_WIDTH/8,
	parameter SSSS = 1
)
(
	
	output wire [M_DATA_WIDTH-1:0]  ddd,
	output wire [M_KEEP_WIDTH-1:0]  ccc
);
inout [SSSS-1:0] abcd;
endmodule