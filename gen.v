// ----- verilog IO linker generated -----

// --- parameter ---
localparam sss__DEPTH = 4096 ;
localparam sss__S_DATA_WIDTH = 8 ;
localparam sss__S_KEEP_ENABLE = (S_DATA_WIDTH>8) ;
localparam sss__S_KEEP_WIDTH = (S_DATA_WIDTH/8) ;
localparam sss__M_DATA_WIDTH = 8 ;
localparam sss__M_KEEP_ENABLE = (M_DATA_WIDTH>8) ;
localparam sss__M_KEEP_WIDTH = (M_DATA_WIDTH/8) ;
localparam sss__ID_ENABLE = 0 ;
localparam sss__ID_WIDTH = 8 ;
localparam sss__DEST_ENABLE = 0 ;
localparam sss__DEST_WIDTH = 8 ;
localparam sss__USER_ENABLE = 1 ;
localparam sss__USER_WIDTH = 1 ;
localparam sss__FRAME_FIFO = 0 ;
localparam sss__USER_BAD_FRAME_VALUE = 1'b1 ;
localparam sss__USER_BAD_FRAME_MASK = 1'b1 ;
localparam sss__DROP_BAD_FRAME = 0 ;
localparam sss__DROP_WHEN_FULL = 0 ;
localparam sss__S_KEEP_WIDTH_INT = S_KEEP_ENABLE?S_KEEP_WIDTH:1 ;
localparam sss__M_KEEP_WIDTH_INT = M_KEEP_ENABLE?M_KEEP_WIDTH:1 ;
localparam sss__S_DATA_WORD_SIZE = S_DATA_WIDTH/S_KEEP_WIDTH_INT ;
localparam sss__M_DATA_WORD_SIZE = M_DATA_WIDTH/M_KEEP_WIDTH_INT ;
localparam sss__EXPAND_BUS = M_KEEP_WIDTH_INT>S_KEEP_WIDTH_INT ;
localparam sss__DATA_WIDTH = EXPAND_BUS?M_DATA_WIDTH:S_DATA_WIDTH ;
localparam sss__KEEP_WIDTH = EXPAND_BUS?M_KEEP_WIDTH_INT:S_KEEP_WIDTH_INT ;

// --- input/output ---
wire sss__s_clk ;
wire sss__s_rst ;
wire [ sss__S_DATA_WIDTH-1:0 ] sss__s_axis_tdata ;
wire [ sss__S_KEEP_WIDTH-1:0 ] sss__s_axis_tkeep ;
wire sss__s_axis_tvalid ;
wire sss__s_axis_tready ;
wire sss__s_axis_tlast ;
wire [ sss__ID_WIDTH-1:0 ] sss__s_axis_tid ;
wire [ sss__DEST_WIDTH-1:0 ] sss__s_axis_tdest ;
wire [ sss__USER_WIDTH-1:0 ] sss__s_axis_tuser ;
wire sss__m_clk ;
wire sss__m_rst ;
wire [ sss__M_DATA_WIDTH-1:0 ] sss__m_axis_tdata ;
wire [ sss__M_KEEP_WIDTH-1:0 ] sss__m_axis_tkeep ;
wire sss__m_axis_tvalid ;
wire sss__m_axis_tready ;
wire sss__m_axis_tlast ;
wire [ sss__ID_WIDTH-1:0 ] sss__m_axis_tid ;
wire [ sss__DEST_WIDTH-1:0 ] sss__m_axis_tdest ;
wire [ sss__USER_WIDTH-1:0 ] sss__m_axis_tuser ;
wire sss__s_status_overflow ;
wire sss__s_status_bad_frame ;
wire sss__s_status_good_frame ;
wire sss__m_status_overflow ;
wire sss__m_status_bad_frame ;
wire sss__m_status_good_frame ;
wire [ sss__DATA_WIDTH-1:0 ] sss__pre_fifo_axis_tdata ;
wire [ sss__KEEP_WIDTH-1:0 ] sss__pre_fifo_axis_tkeep ;

// --- instance module ---
axis_async_fifo_adapter # (
	.DEPTH ( sss__DEPTH ) ,
	.S_DATA_WIDTH ( sss__S_DATA_WIDTH ) ,
	.S_KEEP_ENABLE ( sss__S_KEEP_ENABLE ) ,
	.S_KEEP_WIDTH ( sss__S_KEEP_WIDTH ) ,
	.M_DATA_WIDTH ( sss__M_DATA_WIDTH ) ,
	.M_KEEP_ENABLE ( sss__M_KEEP_ENABLE ) ,
	.M_KEEP_WIDTH ( sss__M_KEEP_WIDTH ) ,
	.ID_ENABLE ( sss__ID_ENABLE ) ,
	.ID_WIDTH ( sss__ID_WIDTH ) ,
	.DEST_ENABLE ( sss__DEST_ENABLE ) ,
	.DEST_WIDTH ( sss__DEST_WIDTH ) ,
	.USER_ENABLE ( sss__USER_ENABLE ) ,
	.USER_WIDTH ( sss__USER_WIDTH ) ,
	.FRAME_FIFO ( sss__FRAME_FIFO ) ,
	.USER_BAD_FRAME_VALUE ( sss__USER_BAD_FRAME_VALUE ) ,
	.USER_BAD_FRAME_MASK ( sss__USER_BAD_FRAME_MASK ) ,
	.DROP_BAD_FRAME ( sss__DROP_BAD_FRAME ) ,
	.DROP_WHEN_FULL ( sss__DROP_WHEN_FULL ) ,
	.S_KEEP_WIDTH_INT ( sss__S_KEEP_WIDTH_INT ) ,
	.M_KEEP_WIDTH_INT ( sss__M_KEEP_WIDTH_INT ) ,
	.S_DATA_WORD_SIZE ( sss__S_DATA_WORD_SIZE ) ,
	.M_DATA_WORD_SIZE ( sss__M_DATA_WORD_SIZE ) ,
	.EXPAND_BUS ( sss__EXPAND_BUS ) ,
	.DATA_WIDTH ( sss__DATA_WIDTH ) ,
	.KEEP_WIDTH ( sss__KEEP_WIDTH ) 
)
asd_inst
(
	.s_clk ( sss__s_clk ) ,
	.s_rst ( sss__s_rst ) ,
	.s_axis_tdata ( sss__s_axis_tdata ) ,
	.s_axis_tkeep ( sss__s_axis_tkeep ) ,
	.s_axis_tvalid ( sss__s_axis_tvalid ) ,
	.s_axis_tready ( sss__s_axis_tready ) ,
	.s_axis_tlast ( sss__s_axis_tlast ) ,
	.s_axis_tid ( sss__s_axis_tid ) ,
	.s_axis_tdest ( sss__s_axis_tdest ) ,
	.s_axis_tuser ( sss__s_axis_tuser ) ,
	.m_clk ( sss__m_clk ) ,
	.m_rst ( sss__m_rst ) ,
	.m_axis_tdata ( sss__m_axis_tdata ) ,
	.m_axis_tkeep ( sss__m_axis_tkeep ) ,
	.m_axis_tvalid ( sss__m_axis_tvalid ) ,
	.m_axis_tready ( sss__m_axis_tready ) ,
	.m_axis_tlast ( sss__m_axis_tlast ) ,
	.m_axis_tid ( sss__m_axis_tid ) ,
	.m_axis_tdest ( sss__m_axis_tdest ) ,
	.m_axis_tuser ( sss__m_axis_tuser ) ,
	.s_status_overflow ( sss__s_status_overflow ) ,
	.s_status_bad_frame ( sss__s_status_bad_frame ) ,
	.s_status_good_frame ( sss__s_status_good_frame ) ,
	.m_status_overflow ( sss__m_status_overflow ) ,
	.m_status_bad_frame ( sss__m_status_bad_frame ) ,
	.m_status_good_frame ( sss__m_status_good_frame ) ,
	.pre_fifo_axis_tdata ( sss__pre_fifo_axis_tdata ) ,
	.pre_fifo_axis_tkeep ( sss__pre_fifo_axis_tkeep ) 
) ; 

// --- assign input/inout ---
assign sss__s_clk =  ;
assign sss__s_rst =  ;
assign sss__s_axis_tdata =  ;
assign sss__s_axis_tkeep =  ;
assign sss__s_axis_tvalid =  ;
assign sss__s_axis_tlast =  ;
assign sss__s_axis_tid =  ;
assign sss__s_axis_tdest =  ;
assign sss__s_axis_tuser =  ;
assign sss__m_clk =  ;
assign sss__m_rst =  ;
assign sss__m_axis_tready =  ;
assign sss__pre_fifo_axis_tdata =  ;
assign sss__pre_fifo_axis_tkeep =  ;
