import svpy
from svpy import *
svpy.writefile = open("../lab6_2_provided/design_source/main_test.sv", 'w')
import svmath
import utils
svwrite("`timescale 1ns / 1ps\n")
dump_queue()
svwrite("//////////////////////////////////////////////////////////////////////////////////\n")
dump_queue()
svwrite("// Company: \n")
dump_queue()
svwrite("// Engineer: \n")
dump_queue()
svwrite("// \n")
dump_queue()
svwrite("// Create Date: 11/21/2024 03:45:50 PM\n")
dump_queue()
svwrite("// Design Name: \n")
dump_queue()
svwrite("// Module Name: main_test\n")
dump_queue()
svwrite("// Project Name: \n")
dump_queue()
svwrite("// Target Devices: \n")
dump_queue()
svwrite("// Tool Versions: \n")
dump_queue()
svwrite("// Description: \n")
dump_queue()
svwrite("// \n")
dump_queue()
svwrite("// Dependencies: \n")
dump_queue()
svwrite("// \n")
dump_queue()
svwrite("// Revision:\n")
dump_queue()
svwrite("// Revision 0.01 - File Created\n")
dump_queue()
svwrite("// Additional Comments:\n")
dump_queue()
svwrite("// \n")
dump_queue()
svwrite("//////////////////////////////////////////////////////////////////////////////////\n")
dump_queue()
svwrite("\n")
dump_queue()
from svmath import *
svwrite("\n")
dump_queue()
svwrite("module main_test();\n")
dump_queue()
svwrite("timeunit 10ns;\n")
dump_queue()
svwrite("timeprecision 1ns;\n")
dump_queue()
svwrite("    logic Clk;\n")
dump_queue()
svwrite("    logic reset_rtl_0;\n")
dump_queue()
svwrite("    \n")
dump_queue()
svwrite("    //USB signals\n")
dump_queue()
svwrite("    logic [0:0] gpio_usb_int_tri_i;\n")
dump_queue()
svwrite("    logic gpio_usb_rst_tri_o;\n")
dump_queue()
svwrite("    logic usb_spi_miso;\n")
dump_queue()
svwrite("    logic usb_spi_mosi;\n")
dump_queue()
svwrite("    logic usb_spi_sclk;\n")
dump_queue()
svwrite("    logic usb_spi_ss;\n")
dump_queue()
svwrite("    \n")
dump_queue()
svwrite("    //UART\n")
dump_queue()
svwrite("    logic uart_rtl_0_rxd;\n")
dump_queue()
svwrite("    logic uart_rtl_0_txd;\n")
dump_queue()
svwrite("    \n")
dump_queue()
svwrite("    //HDMI\n")
dump_queue()
svwrite("    logic hdmi_tmds_clk_n;\n")
dump_queue()
svwrite("    logic hdmi_tmds_clk_p;\n")
dump_queue()
svwrite("    logic [2:0]hdmi_tmds_data_n;\n")
dump_queue()
svwrite("    logic [2:0]hdmi_tmds_data_p;\n")
dump_queue()
svwrite("        \n")
dump_queue()
svwrite("    //HEX displays\n")
dump_queue()
svwrite("    logic [7:0] hex_segA;\n")
dump_queue()
svwrite("    logic [3:0] hex_gridA;\n")
dump_queue()
svwrite("    logic [7:0] hex_segB;\n")
dump_queue()
svwrite("    logic [3:0] hex_gridB;\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("    mb_usb_hdmi_top test(.*);\n")
dump_queue()
svwrite("    \n")
dump_queue()
svwrite("    always begin:CLOCK_GEN\n")
dump_queue()
svwrite("        #1 Clk = ~Clk;\n")
dump_queue()
svwrite("    end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("    initial begin: TEST_VECTORS\n")
dump_queue()
svwrite("        Clk = 0;\n")
dump_queue()
svwrite("        reset_rtl_0 = 1;\n")
dump_queue()
svwrite("        #16\n")
dump_queue()
svwrite("        reset_rtl_0 = 0;\n")
dump_queue()
svwrite("    end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("endmodule\n")
dump_queue()
svpy.writefile.close()