// ----- verilog IO linker generated -----

// --- parameter ---
localparam pf_DEPTH = 4096 ;
localparam pf_S_DATA_WIDTH = 8 ;
localparam pf_S_KEEP_ENABLE = (S_DATA_WIDTH>8) ;
localparam pf_S_KEEP_WIDTH = (S_DATA_WIDTH/8) ;
localparam pf_M_DATA_WIDTH = 8 ;
localparam pf_M_KEEP_ENABLE = (M_DATA_WIDTH>8) ;
localparam pf_M_KEEP_WIDTH = (M_DATA_WIDTH/8) ;
localparam pf_ID_ENABLE = 0 ;
localparam pf_ID_WIDTH = 8 ;
localparam pf_DEST_ENABLE = 0 ;
localparam pf_DEST_WIDTH = 8 ;
localparam pf_USER_ENABLE = 1 ;
localparam pf_USER_WIDTH = 1 ;
localparam pf_FRAME_FIFO = 0 ;
localparam pf_USER_BAD_FRAME_VALUE = 1'b1 ;
localparam pf_USER_BAD_FRAME_MASK = 1'b1 ;
localparam pf_DROP_BAD_FRAME = 0 ;
localparam pf_DROP_WHEN_FULL = 0 ;
localparam pf_S_KEEP_WIDTH_INT = S_KEEP_ENABLE?S_KEEP_WIDTH:1 ;
localparam pf_M_KEEP_WIDTH_INT = M_KEEP_ENABLE?M_KEEP_WIDTH:1 ;
localparam pf_S_DATA_WORD_SIZE = S_DATA_WIDTH/S_KEEP_WIDTH_INT ;
localparam pf_M_DATA_WORD_SIZE = M_DATA_WIDTH/M_KEEP_WIDTH_INT ;
localparam pf_EXPAND_BUS = M_KEEP_WIDTH_INT>S_KEEP_WIDTH_INT ;
localparam pf_DATA_WIDTH = EXPAND_BUS?M_DATA_WIDTH:S_DATA_WIDTH ;
localparam pf_KEEP_WIDTH = EXPAND_BUS?M_KEEP_WIDTH_INT:S_KEEP_WIDTH_INT ;

// --- input/output ---
wire pf_s_clk ;
wire pf_s_rst ;
wire [ pf_S_DATA_WIDTH-1:0 ] pf_s_axis_tdata ;
wire [ pf_S_KEEP_WIDTH-1:0 ] pf_s_axis_tkeep ;
wire pf_s_axis_tvalid ;
wire pf_s_axis_tready ;
wire pf_s_axis_tlast ;
wire [ pf_ID_WIDTH-1:0 ] pf_s_axis_tid ;
wire [ pf_DEST_WIDTH-1:0 ] pf_s_axis_tdest ;
wire [ pf_USER_WIDTH-1:0 ] pf_s_axis_tuser ;
wire pf_m_clk ;
wire pf_m_rst ;
wire [ pf_M_DATA_WIDTH-1:0 ] pf_m_axis_tdata ;
wire [ pf_M_KEEP_WIDTH-1:0 ] pf_m_axis_tkeep ;
wire pf_m_axis_tvalid ;
wire pf_m_axis_tready ;
wire pf_m_axis_tlast ;
wire [ pf_ID_WIDTH-1:0 ] pf_m_axis_tid ;
wire [ pf_DEST_WIDTH-1:0 ] pf_m_axis_tdest ;
wire [ pf_USER_WIDTH-1:0 ] pf_m_axis_tuser ;
wire pf_s_status_overflow ;
wire pf_s_status_bad_frame ;
wire pf_s_status_good_frame ;
wire pf_m_status_overflow ;
wire pf_m_status_bad_frame ;
wire pf_m_status_good_frame ;
wire [ pf_DATA_WIDTH-1:0 ] pf_pre_fifo_axis_tdata ;
wire [ pf_KEEP_WIDTH-1:0 ] pf_pre_fifo_axis_tkeep ;

// --- instance module ---
axis_async_fifo_adapter # (
	.DEPTH ( pf_DEPTH ) ,
	.S_DATA_WIDTH ( pf_S_DATA_WIDTH ) ,
	.S_KEEP_ENABLE ( pf_S_KEEP_ENABLE ) ,
	.S_KEEP_WIDTH ( pf_S_KEEP_WIDTH ) ,
	.M_DATA_WIDTH ( pf_M_DATA_WIDTH ) ,
	.M_KEEP_ENABLE ( pf_M_KEEP_ENABLE ) ,
	.M_KEEP_WIDTH ( pf_M_KEEP_WIDTH ) ,
	.ID_ENABLE ( pf_ID_ENABLE ) ,
	.ID_WIDTH ( pf_ID_WIDTH ) ,
	.DEST_ENABLE ( pf_DEST_ENABLE ) ,
	.DEST_WIDTH ( pf_DEST_WIDTH ) ,
	.USER_ENABLE ( pf_USER_ENABLE ) ,
	.USER_WIDTH ( pf_USER_WIDTH ) ,
	.FRAME_FIFO ( pf_FRAME_FIFO ) ,
	.USER_BAD_FRAME_VALUE ( pf_USER_BAD_FRAME_VALUE ) ,
	.USER_BAD_FRAME_MASK ( pf_USER_BAD_FRAME_MASK ) ,
	.DROP_BAD_FRAME ( pf_DROP_BAD_FRAME ) ,
	.DROP_WHEN_FULL ( pf_DROP_WHEN_FULL ) ,
	.S_KEEP_WIDTH_INT ( pf_S_KEEP_WIDTH_INT ) ,
	.M_KEEP_WIDTH_INT ( pf_M_KEEP_WIDTH_INT ) ,
	.S_DATA_WORD_SIZE ( pf_S_DATA_WORD_SIZE ) ,
	.M_DATA_WORD_SIZE ( pf_M_DATA_WORD_SIZE ) ,
	.EXPAND_BUS ( pf_EXPAND_BUS ) ,
	.DATA_WIDTH ( pf_DATA_WIDTH ) ,
	.KEEP_WIDTH ( pf_KEEP_WIDTH ) 
)
aa_inst
(
	.s_clk ( pf_s_clk ) ,
	.s_rst ( pf_s_rst ) ,
	.s_axis_tdata ( pf_s_axis_tdata ) ,
	.s_axis_tkeep ( pf_s_axis_tkeep ) ,
	.s_axis_tvalid ( pf_s_axis_tvalid ) ,
	.s_axis_tready ( pf_s_axis_tready ) ,
	.s_axis_tlast ( pf_s_axis_tlast ) ,
	.s_axis_tid ( pf_s_axis_tid ) ,
	.s_axis_tdest ( pf_s_axis_tdest ) ,
	.s_axis_tuser ( pf_s_axis_tuser ) ,
	.m_clk ( pf_m_clk ) ,
	.m_rst ( pf_m_rst ) ,
	.m_axis_tdata ( pf_m_axis_tdata ) ,
	.m_axis_tkeep ( pf_m_axis_tkeep ) ,
	.m_axis_tvalid ( pf_m_axis_tvalid ) ,
	.m_axis_tready ( pf_m_axis_tready ) ,
	.m_axis_tlast ( pf_m_axis_tlast ) ,
	.m_axis_tid ( pf_m_axis_tid ) ,
	.m_axis_tdest ( pf_m_axis_tdest ) ,
	.m_axis_tuser ( pf_m_axis_tuser ) ,
	.s_status_overflow ( pf_s_status_overflow ) ,
	.s_status_bad_frame ( pf_s_status_bad_frame ) ,
	.s_status_good_frame ( pf_s_status_good_frame ) ,
	.m_status_overflow ( pf_m_status_overflow ) ,
	.m_status_bad_frame ( pf_m_status_bad_frame ) ,
	.m_status_good_frame ( pf_m_status_good_frame ) ,
	.pre_fifo_axis_tdata ( pf_pre_fifo_axis_tdata ) ,
	.pre_fifo_axis_tkeep ( pf_pre_fifo_axis_tkeep ) 
) ; 

// --- assign input/inout ---
assign pf_s_clk =  ;
assign pf_s_rst =  ;
assign pf_s_axis_tdata =  ;
assign pf_s_axis_tkeep =  ;
assign pf_s_axis_tvalid =  ;
assign pf_s_axis_tlast =  ;
assign pf_s_axis_tid =  ;
assign pf_s_axis_tdest =  ;
assign pf_s_axis_tuser =  ;
assign pf_m_clk =  ;
assign pf_m_rst =  ;
assign pf_m_axis_tready =  ;
assign pf_pre_fifo_axis_tdata =  ;
assign pf_pre_fifo_axis_tkeep =  ;
