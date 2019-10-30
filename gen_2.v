// ----- verilog IO linker generated -----

// --- parameter ---
localparam pf_DROP_BAD_FRAME = 0 ;
localparam pf_DROP_WHEN_FULL = 0 ;

// --- input/output ---
wire [ M_DATA_WIDTH-1:0 ] pf_ddd ;
wire [ M_KEEP_WIDTH-1:0 ] pf_ccc ;
wire [ SSSS-1:0 ] pf_abcd ;

// --- instance module ---
axis_async_fifo_adapter_2 # (
	.DROP_BAD_FRAME ( pf_DROP_BAD_FRAME ) ,
	.DROP_WHEN_FULL ( pf_DROP_WHEN_FULL ) 
)
aa_inst
(
	.ddd ( pf_ddd ) ,
	.ccc ( pf_ccc ) ,
	.abcd ( pf_abcd ) 
) ; 

// --- assign input/inout ---
assign pf_abcd =  ;
