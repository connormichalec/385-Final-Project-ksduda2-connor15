// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Mon Dec  9 13:33:13 2024
// Host        : Connors_laptop running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub -rename_top display_buffer_bram -prefix
//               display_buffer_bram_ display_buffer_bram_stub.v
// Design      : display_buffer_bram
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7s50csga324-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "blk_mem_gen_v8_4_5,Vivado 2022.2" *)
module display_buffer_bram(clka, rsta, ena, wea, addra, dina, douta, rsta_busy)
/* synthesis syn_black_box black_box_pad_pin="clka,rsta,ena,wea[0:0],addra[11:0],dina[15:0],douta[15:0],rsta_busy" */;
  input clka;
  input rsta;
  input ena;
  input [0:0]wea;
  input [11:0]addra;
  input [15:0]dina;
  output [15:0]douta;
  output rsta_busy;
endmodule