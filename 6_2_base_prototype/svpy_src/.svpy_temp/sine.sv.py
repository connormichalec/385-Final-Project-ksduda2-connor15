import svpy
from svpy import *
svpy.writefile = open("../lab6_2_provided/design_source/sine.sv", 'w')
import svmath
import utils
from math import sin, ceil, pi
svwrite("\n")
dump_queue()
svwrite("module sin\n")
dump_queue()
svwrite("(\n")
dump_queue()
svwrite("    input [9:0] theta,     //10 bits of precision, first 3 are integer part (unsigned)\n")
dump_queue()
svwrite("    output [15:0] out\n")
dump_queue()
svwrite(");\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("parameter ADDR_WIDTH = 10;\n")
dump_queue()
svwrite("parameter DATA_WIDTH =  16;\n")
dump_queue()
svwrite("logic [9:0] addr_reg;\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("parameter [0:2**ADDR_WIDTH-1][DATA_WIDTH-1:0] ROM = {\n")
dump_queue()
# max = ceil(2 * pi * 2**7)
max = 2**10
for i in range(max):
    line = svmath.to_bits(sin(i / 2**7), 2, 14)
    if i != max - 1:
        line += ","
    svwrite(line, "\n")
svwrite("};\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("assign out[DATA_WIDTH-1:0] = ROM[theta][DATA_WIDTH-1:0];\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("endmodule")
dump_queue()
svpy.writefile.close()