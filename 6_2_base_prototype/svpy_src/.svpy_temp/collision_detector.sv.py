import svpy
from svpy import *
svpy.writefile = open("../lab6_2_provided/design_source/collision_detector.sv", 'w')
import svmath
import utils
from svmath import *
from structs import JOBB
svwrite("\n")
dump_queue()
obb1 = JOBB("obb1")
obb2 = JOBB("obb2")
svwrite("\n")
dump_queue()
svwrite("module collision_detector(\n")
dump_queue()
svwrite("    ")
svpy.inline_state = True
svwrite(obb1.declare("input"))
svpy.inline_state = False
svwrite(",\n")
dump_queue()
svwrite("    ")
svpy.inline_state = True
svwrite(obb2.declare("input"))
svpy.inline_state = False
svwrite(",\n")
dump_queue()
svwrite("    output logic is_collision\n")
dump_queue()
svwrite(");\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Steps:\n")
dump_queue()
svwrite("//  1. Generate bases of A and B (maybe move this to external module later to minimize cos/sin use)\n")
dump_queue()
svwrite("//  2. Project points of B onto axes of A\n")
dump_queue()
svwrite("//      - Need to get points of rects A and B from pos, dimensions, and angle\n")
dump_queue()
svwrite("///     - Get points RELATIVE to rectangle A\n")
dump_queue()
svwrite("//      - Will refer to this coordinate system as UV coords\n")
dump_queue()
svwrite("//  3. Get minimum and maximum u and v of B\n")
dump_queue()
svwrite("//  4. Use simple comparisons to check for separating axis\n")
dump_queue()
svwrite("//  5. Repeat steps for A onto B\n")
dump_queue()
svwrite("//  6. Use big OR gate to combine all the checks\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Get points of A and B\n")
dump_queue()
svwrite("//  - Need to rotate first, then subtract\n")
dump_queue()
points1 = [obb1.Point0, obb1.Point1, obb1.Point2, obb1.Point3]
points2 = [obb2.Point0, obb2.Point1, obb2.Point2, obb2.Point3]
svwrite("\n")
dump_queue()
svwrite("//// TEST 1: A onto B\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Project points of A onto axes of B\n")
dump_queue()
points1_u = []
points1_v = []
for point in points1:
    relative = point - obb2.pos
    point_u = Fixed(7, 25)
    point_v = Fixed(7, 25)

    point_u.declare()
    point_v.declare()

    point_u.assign(relative.Dot(obb2.u))
    point_v.assign(relative.Dot(obb2.v))

    points1_u.append(point_u)
    points1_v.append(point_v)
svwrite("\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Find max u and v values for rect A\n")
dump_queue()
svwrite("logic signed [31 : 0] max_uA;\n")
dump_queue()
svwrite("logic signed [31 : 0] max_uA_01;    // Max of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] max_uA_23;    // Max of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("logic signed [31 : 0] max_vA;\n")
dump_queue()
svwrite("logic signed [31 : 0] max_vA_01;    // Max of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] max_vA_23;    // Max of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
begin_comb()
svwrite("\n")
dump_queue()
svwrite("// Max u\n")
dump_queue()
svwrite("max_uA_01 = ")
svpy.inline_state = True
svwrite(points1_u[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_u[1])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points1_u[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_uA_01 = ")
svpy.inline_state = True
svwrite(points1_u[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_uA_23 = ")
svpy.inline_state = True
svwrite(points1_u[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_u[3])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points1_u[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_uA_01 = ")
svpy.inline_state = True
svwrite(points1_u[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_uA = max_uA_01;\n")
dump_queue()
svwrite("if (max_uA_23 > max_uA_01) begin\n")
dump_queue()
svwrite("    max_uA = max_uA_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Max v\n")
dump_queue()
svwrite("max_vA_01 = ")
svpy.inline_state = True
svwrite(points1_v[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_v[1])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points1_v[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_vA_01 = ")
svpy.inline_state = True
svwrite(points1_v[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_vA_23 = ")
svpy.inline_state = True
svwrite(points1_v[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_v[3])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points1_v[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_vA_01 = ")
svpy.inline_state = True
svwrite(points1_v[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_vA = max_vA_01;\n")
dump_queue()
svwrite("if (max_vA_23 > max_vA_01) begin\n")
dump_queue()
svwrite("    max_vA = max_vA_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("// Find min u and v values for rect A\n")
dump_queue()
svwrite("logic signed [31 : 0] min_uA;\n")
dump_queue()
svwrite("logic signed [31 : 0] min_uA_01;    // Min of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] min_uA_23;    // Min of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("logic signed [31 : 0] min_vA;\n")
dump_queue()
svwrite("logic signed [31 : 0] min_vA_01;    // Min of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] min_vA_23;    // Min of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
begin_comb()
svwrite("\n")
dump_queue()
svwrite("// Min u\n")
dump_queue()
svwrite("min_uA_01 = ")
svpy.inline_state = True
svwrite(points1_u[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_u[1])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points1_u[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_uA_01 = ")
svpy.inline_state = True
svwrite(points1_u[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_uA_23 = ")
svpy.inline_state = True
svwrite(points1_u[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_u[3])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points1_u[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_uA_01 = ")
svpy.inline_state = True
svwrite(points1_u[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_uA = min_uA_01;\n")
dump_queue()
svwrite("if (min_uA_23 < min_uA_01) begin\n")
dump_queue()
svwrite("    min_uA = min_uA_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Min v\n")
dump_queue()
svwrite("min_vA_01 = ")
svpy.inline_state = True
svwrite(points1_v[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_v[1])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points1_v[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_vA_01 = ")
svpy.inline_state = True
svwrite(points1_v[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_vA_23 = ")
svpy.inline_state = True
svwrite(points1_v[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points1_v[3])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points1_v[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_vA_01 = ")
svpy.inline_state = True
svwrite(points1_v[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_vA = min_vA_01;\n")
dump_queue()
svwrite("if (min_vA_23 < min_vA_01) begin\n")
dump_queue()
svwrite("    min_vA = min_vA_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Check for separating axis\n")
dump_queue()
svwrite("logic separate_min_uA;\n")
dump_queue()
svwrite("logic separate_max_uA;\n")
dump_queue()
svwrite("logic separate_min_vA;\n")
dump_queue()
svwrite("logic separate_max_vA;\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Need to cast width and height of B into same Fixed structure as u and v\n")
dump_queue()
widthB_fixed = Fixed(points1_u[0].integer_bits, points1_u[0].precision, "widthB_fixed")
heightB_fixed = Fixed(points1_u[0].integer_bits, points1_u[0].precision, "heightB_fixed")

widthB_fixed.declare()
widthB_fixed.assign(obb2.halfWidth)
heightB_fixed.declare()
heightB_fixed.assign(obb2.halfHeight)
svwrite("\n")
dump_queue()
begin_comb()
svwrite("separate_min_uA = 1'b0;\n")
dump_queue()
svwrite("if (min_uA >= widthB_fixed) begin\n")
dump_queue()
svwrite("    separate_min_uA = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("separate_max_uA = 1'b0;\n")
dump_queue()
svwrite("if (max_uA <= -widthB_fixed) begin\n")
dump_queue()
svwrite("    separate_max_uA = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("separate_min_vA = 1'b0;\n")
dump_queue()
svwrite("if (min_vA >= heightB_fixed) begin\n")
dump_queue()
svwrite("    separate_min_vA = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("separate_max_vA = 1'b0;\n")
dump_queue()
svwrite("if (max_vA <= -heightB_fixed) begin\n")
dump_queue()
svwrite("    separate_max_vA = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("//// TEST 2: B onto A\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Project points of B onto axes of A\n")
dump_queue()
points2_u = []
points2_v = []
for point in points2:
    relative = point - obb1.pos    
    point_u = Fixed(7, 25)
    point_v = Fixed(7, 25)

    point_u.declare()
    point_v.declare()

    point_u.assign(relative.Dot(obb1.u))
    point_v.assign(relative.Dot(obb1.v))

    points2_u.append(point_u)
    points2_v.append(point_v)
svwrite("\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Find max u and v values for rect B\n")
dump_queue()
svwrite("logic signed [31 : 0] max_uB;\n")
dump_queue()
svwrite("logic signed [31 : 0] max_uB_01;    // Max of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] max_uB_23;    // Max of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("logic signed [31 : 0] max_vB;\n")
dump_queue()
svwrite("logic signed [31 : 0] max_vB_01;    // Max of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] max_vB_23;    // Max of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
begin_comb()
svwrite("\n")
dump_queue()
svwrite("// Max u\n")
dump_queue()
svwrite("max_uB_01 = ")
svpy.inline_state = True
svwrite(points2_u[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_u[1])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points2_u[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_uB_01 = ")
svpy.inline_state = True
svwrite(points2_u[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_uB_23 = ")
svpy.inline_state = True
svwrite(points2_u[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_u[3])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points2_u[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_uB_01 = ")
svpy.inline_state = True
svwrite(points2_u[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_uB = max_uB_01;\n")
dump_queue()
svwrite("if (max_uB_23 > max_uB_01) begin\n")
dump_queue()
svwrite("    max_uB = max_uB_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Max v\n")
dump_queue()
svwrite("max_vB_01 = ")
svpy.inline_state = True
svwrite(points2_v[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_v[1])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points2_v[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_vB_01 = ")
svpy.inline_state = True
svwrite(points2_v[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_vB_23 = ")
svpy.inline_state = True
svwrite(points2_v[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_v[3])
svpy.inline_state = False
svwrite(" > ")
svpy.inline_state = True
svwrite(points2_v[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    max_vB_01 = ")
svpy.inline_state = True
svwrite(points2_v[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("max_vB = max_vB_01;\n")
dump_queue()
svwrite("if (max_vB_23 > max_vB_01) begin\n")
dump_queue()
svwrite("    max_vB = max_vB_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("// Find min u and v values for rect B\n")
dump_queue()
svwrite("logic signed [31 : 0] min_uB;\n")
dump_queue()
svwrite("logic signed [31 : 0] min_uB_01;    // Min of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] min_uB_23;    // Min of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("logic signed [31 : 0] min_vB;\n")
dump_queue()
svwrite("logic signed [31 : 0] min_vB_01;    // Min of points 0 and 1\n")
dump_queue()
svwrite("logic signed [31 : 0] min_vB_23;    // Min of points 2 and 3\n")
dump_queue()
svwrite("\n")
dump_queue()
begin_comb()
svwrite("\n")
dump_queue()
svwrite("// Min u\n")
dump_queue()
svwrite("min_uB_01 = ")
svpy.inline_state = True
svwrite(points2_u[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_u[1])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points2_u[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_uB_01 = ")
svpy.inline_state = True
svwrite(points2_u[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_uB_23 = ")
svpy.inline_state = True
svwrite(points2_u[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_u[3])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points2_u[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_uB_01 = ")
svpy.inline_state = True
svwrite(points2_u[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_uB = min_uB_01;\n")
dump_queue()
svwrite("if (min_uB_23 < min_uB_01) begin\n")
dump_queue()
svwrite("    min_uB = min_uB_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Min v\n")
dump_queue()
svwrite("min_vB_01 = ")
svpy.inline_state = True
svwrite(points2_v[0])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_v[1])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points2_v[0])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_vB_01 = ")
svpy.inline_state = True
svwrite(points2_v[1])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_vB_23 = ")
svpy.inline_state = True
svwrite(points2_v[2])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("if (")
svpy.inline_state = True
svwrite(points2_v[3])
svpy.inline_state = False
svwrite(" < ")
svpy.inline_state = True
svwrite(points2_v[2])
svpy.inline_state = False
svwrite(") begin\n")
dump_queue()
svwrite("    min_vB_01 = ")
svpy.inline_state = True
svwrite(points2_v[3])
svpy.inline_state = False
svwrite(";\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("min_vB = min_vB_01;\n")
dump_queue()
svwrite("if (min_vB_23 < min_vB_01) begin\n")
dump_queue()
svwrite("    min_vB = min_vB_23;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Check for separating axis\n")
dump_queue()
svwrite("logic separate_min_uB;\n")
dump_queue()
svwrite("logic separate_max_uB;\n")
dump_queue()
svwrite("logic separate_min_vB;\n")
dump_queue()
svwrite("logic separate_max_vB;\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("// Need to cast width and height of A into same Fixed structure as u and v\n")
dump_queue()
widthA_fixed = Fixed(points2_u[0].integer_bits, points2_u[0].precision, "widthA_fixed")
heightA_fixed = Fixed(points2_u[0].integer_bits, points2_u[0].precision, "heightA_fixed")

widthA_fixed.declare()
widthA_fixed.assign(obb1.halfWidth)
heightA_fixed.declare()
heightA_fixed.assign(obb1.halfHeight)
svwrite("\n")
dump_queue()
begin_comb()
svwrite("separate_min_uB = 1'b0;\n")
dump_queue()
svwrite("if (min_uB >= widthA_fixed) begin\n")
dump_queue()
svwrite("    separate_min_uB = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("separate_max_uB = 1'b0;\n")
dump_queue()
svwrite("if (max_uB <= -widthA_fixed) begin\n")
dump_queue()
svwrite("    separate_max_uB = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("separate_min_vB = 1'b0;\n")
dump_queue()
svwrite("if (min_vB >= heightA_fixed) begin\n")
dump_queue()
svwrite("    separate_min_vB = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
svwrite("separate_max_vB = 1'b0;\n")
dump_queue()
svwrite("if (max_vB <= -heightA_fixed) begin\n")
dump_queue()
svwrite("    separate_max_vB = 1'b1;\n")
dump_queue()
svwrite("end\n")
dump_queue()
svwrite("\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("////// TYING IT ALL TOGETHER\n")
dump_queue()
svwrite("\n")
dump_queue()
begin_comb()
svwrite("is_collision = ~(separate_min_uA | separate_max_uA | separate_min_vA | separate_max_vA | separate_min_uB | separate_max_uB | separate_min_vB | separate_max_vB);\n")
dump_queue()
end_comb()
svwrite("\n")
dump_queue()
svwrite("endmodule")
dump_queue()
svpy.writefile.close()