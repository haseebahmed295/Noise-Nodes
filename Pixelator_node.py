import bpy
from .utils import ShaderNode
class ShaderNodePixelator(ShaderNode):
    bl_name='Pixelator'
    bl_label='Pixelator'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Division'].default_value = 10
        self.inputs['Scale'].default_value = (1,1,1)

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
        vector_socket = nt.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
        vector_socket.subtype = 'NONE'
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = 0.0
        vector_socket.max_value = 0.0
        vector_socket.attribute_domain = 'POINT'
        
        #Socket Input Map
        input_map_socket = nt.interface.new_socket(name = "Input Map", in_out='INPUT', socket_type = 'NodeSocketVector')
        input_map_socket.subtype = 'NONE'
        input_map_socket.default_value = (0.0, 0.0, 0.0)
        input_map_socket.min_value = 0.0
        input_map_socket.max_value = 1.0
        input_map_socket.attribute_domain = 'POINT'
        input_map_socket.hide_value = True
        
        #Socket Division
        division_socket = nt.interface.new_socket(name = "Division", in_out='INPUT', socket_type = 'NodeSocketFloat')
        division_socket.subtype = 'NONE'
        division_socket.default_value = 10.0
        division_socket.min_value = 0.0
        division_socket.max_value = 3.4028234663852886e+38
        division_socket.attribute_domain = 'POINT'
        
        #Socket Scale
        scale_socket = nt.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
        scale_socket.subtype = 'XYZ'
        scale_socket.default_value = (1.0, 1.0, 1.0)
        scale_socket.min_value = -3.4028234663852886e+38
        scale_socket.max_value = 3.4028234663852886e+38
        scale_socket.attribute_domain = 'POINT'
        
        #Socket Offset
        offset_socket = nt.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
        offset_socket.subtype = 'XYZ'
        offset_socket.default_value = (0.0, 0.0, 0.0)
        offset_socket.min_value = -3.4028234663852886e+38
        offset_socket.max_value = 3.4028234663852886e+38
        offset_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Frame.004
        frame_004 = nt.nodes.new("NodeFrame")
        frame_004.label = "3D Sawtooth"
        frame_004.name = "Frame.004"
        frame_004.label_size = 20
        frame_004.shrink = True
        
        #node Frame
        frame = nt.nodes.new("NodeFrame")
        frame.label = "Check for Input"
        frame.name = "Frame"
        frame.label_size = 20
        frame.shrink = True
        
        #node Math.094
        math_094 = nt.nodes.new("ShaderNodeMath")
        math_094.name = "Math.094"
        math_094.operation = 'SUBTRACT'
        math_094.use_clamp = False
        #Value_002
        math_094.inputs[2].default_value = 0.5
        
        #node Math.095
        math_095 = nt.nodes.new("ShaderNodeMath")
        math_095.name = "Math.095"
        math_095.operation = 'MULTIPLY'
        math_095.use_clamp = False
        #Value_002
        math_095.inputs[2].default_value = 0.5
        
        #node Reroute.060
        reroute_060 = nt.nodes.new("NodeReroute")
        reroute_060.name = "Reroute.060"
        #node Math.096
        math_096 = nt.nodes.new("ShaderNodeMath")
        math_096.name = "Math.096"
        math_096.operation = 'MULTIPLY'
        math_096.use_clamp = False
        #Value_002
        math_096.inputs[2].default_value = 0.5
        
        #node Math.097
        math_097 = nt.nodes.new("ShaderNodeMath")
        math_097.name = "Math.097"
        math_097.operation = 'SUBTRACT'
        math_097.use_clamp = False
        #Value_002
        math_097.inputs[2].default_value = 0.5
        
        #node Math.098
        math_098 = nt.nodes.new("ShaderNodeMath")
        math_098.name = "Math.098"
        math_098.operation = 'MULTIPLY'
        math_098.use_clamp = False
        #Value_002
        math_098.inputs[2].default_value = 0.5
        
        #node Reroute.061
        reroute_061 = nt.nodes.new("NodeReroute")
        reroute_061.name = "Reroute.061"
        #node Reroute.062
        reroute_062 = nt.nodes.new("NodeReroute")
        reroute_062.name = "Reroute.062"
        #node Math.099
        math_099 = nt.nodes.new("ShaderNodeMath")
        math_099.name = "Math.099"
        math_099.operation = 'SUBTRACT'
        math_099.use_clamp = False
        #Value_002
        math_099.inputs[2].default_value = 0.5
        
        #node Reroute.063
        reroute_063 = nt.nodes.new("NodeReroute")
        reroute_063.name = "Reroute.063"
        #node Reroute.064
        reroute_064 = nt.nodes.new("NodeReroute")
        reroute_064.name = "Reroute.064"
        #node Reroute.065
        reroute_065 = nt.nodes.new("NodeReroute")
        reroute_065.name = "Reroute.065"
        #node Separate XYZ.002
        separate_xyz_002 = nt.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz_002.name = "Separate XYZ.002"
        
        #node Combine XYZ.001
        combine_xyz_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz_001.name = "Combine XYZ.001"
        
        #node Reroute.073
        reroute_073 = nt.nodes.new("NodeReroute")
        reroute_073.name = "Reroute.073"
        #node Reroute.074
        reroute_074 = nt.nodes.new("NodeReroute")
        reroute_074.name = "Reroute.074"
        #node Reroute.075
        reroute_075 = nt.nodes.new("NodeReroute")
        reroute_075.name = "Reroute.075"
        #node Reroute.076
        reroute_076 = nt.nodes.new("NodeReroute")
        reroute_076.name = "Reroute.076"
        #node Reroute.077
        reroute_077 = nt.nodes.new("NodeReroute")
        reroute_077.name = "Reroute.077"
        #node Reroute.078
        reroute_078 = nt.nodes.new("NodeReroute")
        reroute_078.name = "Reroute.078"
        #node Reroute.079
        reroute_079 = nt.nodes.new("NodeReroute")
        reroute_079.name = "Reroute.079"
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Reroute.046
        reroute_046 = nt.nodes.new("NodeReroute")
        reroute_046.name = "Reroute.046"
        #node Math.128
        math_128 = nt.nodes.new("ShaderNodeMath")
        math_128.name = "Math.128"
        math_128.operation = 'MULTIPLY'
        math_128.use_clamp = False
        #Value_001
        math_128.inputs[1].default_value = 0.5
        #Value_002
        math_128.inputs[2].default_value = 0.5
        
        #node Math.129
        math_129 = nt.nodes.new("ShaderNodeMath")
        math_129.name = "Math.129"
        math_129.operation = 'MULTIPLY'
        math_129.use_clamp = False
        #Value_001
        math_129.inputs[1].default_value = 0.5
        #Value_002
        math_129.inputs[2].default_value = 0.5
        
        #node Math.068
        math_068 = nt.nodes.new("ShaderNodeMath")
        math_068.name = "Math.068"
        math_068.operation = 'MULTIPLY'
        math_068.use_clamp = False
        #Value_001
        math_068.inputs[1].default_value = 0.5
        #Value_002
        math_068.inputs[2].default_value = 0.5
        
        #node Reroute.047
        reroute_047 = nt.nodes.new("NodeReroute")
        reroute_047.name = "Reroute.047"
        #node Math.130
        math_130 = nt.nodes.new("ShaderNodeMath")
        math_130.name = "Math.130"
        math_130.operation = 'MULTIPLY'
        math_130.use_clamp = False
        #Value_001
        math_130.inputs[1].default_value = 0.5
        #Value_002
        math_130.inputs[2].default_value = 0.5
        
        #node Math.131
        math_131 = nt.nodes.new("ShaderNodeMath")
        math_131.name = "Math.131"
        math_131.operation = 'MULTIPLY'
        math_131.use_clamp = False
        #Value_001
        math_131.inputs[1].default_value = 0.5
        #Value_002
        math_131.inputs[2].default_value = 0.5
        
        #node Math.069
        math_069 = nt.nodes.new("ShaderNodeMath")
        math_069.name = "Math.069"
        math_069.operation = 'MULTIPLY'
        math_069.use_clamp = False
        #Value_001
        math_069.inputs[1].default_value = 0.5
        #Value_002
        math_069.inputs[2].default_value = 0.5
        
        #node Reroute.080
        reroute_080 = nt.nodes.new("NodeReroute")
        reroute_080.name = "Reroute.080"
        #node Math.125
        math_125 = nt.nodes.new("ShaderNodeMath")
        math_125.name = "Math.125"
        math_125.operation = 'MULTIPLY'
        math_125.use_clamp = False
        #Value_002
        math_125.inputs[2].default_value = 0.5
        
        #node Math.126
        math_126 = nt.nodes.new("ShaderNodeMath")
        math_126.name = "Math.126"
        math_126.operation = 'MULTIPLY'
        math_126.use_clamp = False
        #Value_002
        math_126.inputs[2].default_value = 0.5
        
        #node Math.127
        math_127 = nt.nodes.new("ShaderNodeMath")
        math_127.name = "Math.127"
        math_127.operation = 'MULTIPLY'
        math_127.use_clamp = False
        #Value_002
        math_127.inputs[2].default_value = 0.5
        
        #node Reroute
        reroute = nt.nodes.new("NodeReroute")
        reroute.name = "Reroute"
        #node Reroute.001
        reroute_001 = nt.nodes.new("NodeReroute")
        reroute_001.name = "Reroute.001"
        #node Reroute.002
        reroute_002 = nt.nodes.new("NodeReroute")
        reroute_002.name = "Reroute.002"
        #node Math.101
        math_101 = nt.nodes.new("ShaderNodeMath")
        math_101.name = "Math.101"
        math_101.operation = 'SUBTRACT'
        math_101.use_clamp = False
        #Value
        math_101.inputs[0].default_value = 1.0
        #Value_002
        math_101.inputs[2].default_value = 0.5
        
        #node Math.102
        math_102 = nt.nodes.new("ShaderNodeMath")
        math_102.name = "Math.102"
        math_102.operation = 'SUBTRACT'
        math_102.use_clamp = False
        #Value
        math_102.inputs[0].default_value = 1.0
        #Value_002
        math_102.inputs[2].default_value = 0.5
        
        #node Math.103
        math_103 = nt.nodes.new("ShaderNodeMath")
        math_103.name = "Math.103"
        math_103.operation = 'SUBTRACT'
        math_103.use_clamp = False
        #Value
        math_103.inputs[0].default_value = 1.0
        #Value_002
        math_103.inputs[2].default_value = 0.5
        
        #node Reroute.066
        reroute_066 = nt.nodes.new("NodeReroute")
        reroute_066.name = "Reroute.066"
        #node Reroute.067
        reroute_067 = nt.nodes.new("NodeReroute")
        reroute_067.name = "Reroute.067"
        #node Mix.006
        mix_006 = nt.nodes.new("ShaderNodeMix")
        mix_006.name = "Mix.006"
        mix_006.blend_type = 'MIX'
        mix_006.clamp_factor = True
        mix_006.clamp_result = False
        mix_006.data_type = 'RGBA'
        mix_006.factor_mode = 'UNIFORM'
        #Factor_Vector
        mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_006.inputs[2].default_value = 0.0
        #B_Float
        mix_006.inputs[3].default_value = 0.0
        #A_Vector
        mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix_006.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_006.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Math.104
        math_104 = nt.nodes.new("ShaderNodeMath")
        math_104.name = "Math.104"
        math_104.operation = 'DIVIDE'
        math_104.use_clamp = False
        #Value_002
        math_104.inputs[2].default_value = 0.5
        
        #node Math.105
        math_105 = nt.nodes.new("ShaderNodeMath")
        math_105.name = "Math.105"
        math_105.operation = 'ABSOLUTE'
        math_105.use_clamp = False
        #Value_001
        math_105.inputs[1].default_value = 0.5
        #Value_002
        math_105.inputs[2].default_value = 0.5
        
        #node Math.106
        math_106 = nt.nodes.new("ShaderNodeMath")
        math_106.name = "Math.106"
        math_106.operation = 'SUBTRACT'
        math_106.use_clamp = False
        #Value
        math_106.inputs[0].default_value = 1.0
        #Value_002
        math_106.inputs[2].default_value = 0.5
        
        #node Math.107
        math_107 = nt.nodes.new("ShaderNodeMath")
        math_107.name = "Math.107"
        math_107.operation = 'MODULO'
        math_107.use_clamp = False
        #Value_002
        math_107.inputs[2].default_value = 0.5
        
        #node Math.108
        math_108 = nt.nodes.new("ShaderNodeMath")
        math_108.name = "Math.108"
        math_108.operation = 'DIVIDE'
        math_108.use_clamp = False
        #Value_002
        math_108.inputs[2].default_value = 0.5
        
        #node Reroute.068
        reroute_068 = nt.nodes.new("NodeReroute")
        reroute_068.name = "Reroute.068"
        #node Mix.007
        mix_007 = nt.nodes.new("ShaderNodeMix")
        mix_007.name = "Mix.007"
        mix_007.blend_type = 'MIX'
        mix_007.clamp_factor = True
        mix_007.clamp_result = False
        mix_007.data_type = 'RGBA'
        mix_007.factor_mode = 'UNIFORM'
        #Factor_Vector
        mix_007.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_007.inputs[2].default_value = 0.0
        #B_Float
        mix_007.inputs[3].default_value = 0.0
        #A_Vector
        mix_007.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_007.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix_007.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_007.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Math.109
        math_109 = nt.nodes.new("ShaderNodeMath")
        math_109.name = "Math.109"
        math_109.operation = 'DIVIDE'
        math_109.use_clamp = False
        #Value_002
        math_109.inputs[2].default_value = 0.5
        
        #node Math.110
        math_110 = nt.nodes.new("ShaderNodeMath")
        math_110.name = "Math.110"
        math_110.operation = 'MULTIPLY'
        math_110.use_clamp = False
        #Value_002
        math_110.inputs[2].default_value = 0.5
        
        #node Math.111
        math_111 = nt.nodes.new("ShaderNodeMath")
        math_111.name = "Math.111"
        math_111.operation = 'ABSOLUTE'
        math_111.use_clamp = False
        #Value_001
        math_111.inputs[1].default_value = 0.5
        #Value_002
        math_111.inputs[2].default_value = 0.5
        
        #node Math.112
        math_112 = nt.nodes.new("ShaderNodeMath")
        math_112.name = "Math.112"
        math_112.operation = 'SUBTRACT'
        math_112.use_clamp = False
        #Value
        math_112.inputs[0].default_value = 1.0
        #Value_002
        math_112.inputs[2].default_value = 0.5
        
        #node Math.113
        math_113 = nt.nodes.new("ShaderNodeMath")
        math_113.name = "Math.113"
        math_113.operation = 'MODULO'
        math_113.use_clamp = False
        #Value_002
        math_113.inputs[2].default_value = 0.5
        
        #node Math.114
        math_114 = nt.nodes.new("ShaderNodeMath")
        math_114.name = "Math.114"
        math_114.operation = 'DIVIDE'
        math_114.use_clamp = False
        #Value_002
        math_114.inputs[2].default_value = 0.5
        
        #node Reroute.069
        reroute_069 = nt.nodes.new("NodeReroute")
        reroute_069.name = "Reroute.069"
        #node Mix.008
        mix_008 = nt.nodes.new("ShaderNodeMix")
        mix_008.name = "Mix.008"
        mix_008.blend_type = 'MIX'
        mix_008.clamp_factor = True
        mix_008.clamp_result = False
        mix_008.data_type = 'RGBA'
        mix_008.factor_mode = 'UNIFORM'
        #Factor_Vector
        mix_008.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_008.inputs[2].default_value = 0.0
        #B_Float
        mix_008.inputs[3].default_value = 0.0
        #A_Vector
        mix_008.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_008.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix_008.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_008.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Math.117
        math_117 = nt.nodes.new("ShaderNodeMath")
        math_117.name = "Math.117"
        math_117.operation = 'SUBTRACT'
        math_117.use_clamp = False
        #Value
        math_117.inputs[0].default_value = 1.0
        #Value_002
        math_117.inputs[2].default_value = 0.5
        
        #node Math.118
        math_118 = nt.nodes.new("ShaderNodeMath")
        math_118.name = "Math.118"
        math_118.operation = 'MODULO'
        math_118.use_clamp = False
        #Value_002
        math_118.inputs[2].default_value = 0.5
        
        #node Math.119
        math_119 = nt.nodes.new("ShaderNodeMath")
        math_119.name = "Math.119"
        math_119.operation = 'DIVIDE'
        math_119.use_clamp = False
        #Value_002
        math_119.inputs[2].default_value = 0.5
        
        #node Reroute.072
        reroute_072 = nt.nodes.new("NodeReroute")
        reroute_072.name = "Reroute.072"
        #node Math.124
        math_124 = nt.nodes.new("ShaderNodeMath")
        math_124.name = "Math.124"
        math_124.operation = 'MULTIPLY'
        math_124.use_clamp = False
        #Value_002
        math_124.inputs[2].default_value = 0.5
        
        #node Math.132
        math_132 = nt.nodes.new("ShaderNodeMath")
        math_132.name = "Math.132"
        math_132.operation = 'MULTIPLY'
        math_132.use_clamp = False
        #Value_002
        math_132.inputs[2].default_value = 0.5
        
        #node Math.120
        math_120 = nt.nodes.new("ShaderNodeMath")
        math_120.name = "Math.120"
        math_120.operation = 'DIVIDE'
        math_120.use_clamp = False
        #Value_002
        math_120.inputs[2].default_value = 0.5
        
        #node Math.121
        math_121 = nt.nodes.new("ShaderNodeMath")
        math_121.name = "Math.121"
        math_121.operation = 'ABSOLUTE'
        math_121.use_clamp = False
        #Value_001
        math_121.inputs[1].default_value = 0.5
        #Value_002
        math_121.inputs[2].default_value = 0.5
        
        #node Math.123
        math_123 = nt.nodes.new("ShaderNodeMath")
        math_123.name = "Math.123"
        math_123.operation = 'MULTIPLY'
        math_123.use_clamp = False
        #Value_002
        math_123.inputs[2].default_value = 0.5
        
        #node Math.134
        math_134 = nt.nodes.new("ShaderNodeMath")
        math_134.name = "Math.134"
        math_134.operation = 'MULTIPLY'
        math_134.use_clamp = False
        #Value_002
        math_134.inputs[2].default_value = 0.5
        
        #node Reroute.070
        reroute_070 = nt.nodes.new("NodeReroute")
        reroute_070.name = "Reroute.070"
        #node Math.122
        math_122 = nt.nodes.new("ShaderNodeMath")
        math_122.name = "Math.122"
        math_122.operation = 'SUBTRACT'
        math_122.use_clamp = False
        #Value_002
        math_122.inputs[2].default_value = 0.5
        
        #node Math.115
        math_115 = nt.nodes.new("ShaderNodeMath")
        math_115.name = "Math.115"
        math_115.operation = 'SUBTRACT'
        math_115.use_clamp = False
        #Value_002
        math_115.inputs[2].default_value = 0.5
        
        #node Math.100
        math_100 = nt.nodes.new("ShaderNodeMath")
        math_100.name = "Math.100"
        math_100.operation = 'SUBTRACT'
        math_100.use_clamp = False
        #Value_002
        math_100.inputs[2].default_value = 0.5
        
        #node Math.133
        math_133 = nt.nodes.new("ShaderNodeMath")
        math_133.name = "Math.133"
        math_133.operation = 'MULTIPLY'
        math_133.use_clamp = False
        #Value_002
        math_133.inputs[2].default_value = 0.5
        
        #node Reroute.071
        reroute_071 = nt.nodes.new("NodeReroute")
        reroute_071.name = "Reroute.071"
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.operation = 'GREATER_THAN'
        math.use_clamp = False
        #Value_001
        math.inputs[1].default_value = 0.0
        #Value_002
        math.inputs[2].default_value = 0.5
        
        #node Texture Coordinate
        texture_coordinate = nt.nodes.new("ShaderNodeTexCoord")
        texture_coordinate.name = "Texture Coordinate"
        texture_coordinate.from_instancer = False
        
        #node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.operation = 'ABSOLUTE'
        math_001.use_clamp = False
        #Value_001
        math_001.inputs[1].default_value = 0.5
        #Value_002
        math_001.inputs[2].default_value = 0.5
        
        #node Mix
        mix = nt.nodes.new("ShaderNodeMix")
        mix.name = "Mix"
        mix.blend_type = 'MIX'
        mix.clamp_factor = True
        mix.clamp_result = False
        mix.data_type = 'RGBA'
        mix.factor_mode = 'UNIFORM'
        #Factor_Vector
        mix.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix.inputs[2].default_value = 0.0
        #B_Float
        mix.inputs[3].default_value = 0.0
        #A_Vector
        mix.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Reroute.003
        reroute_003 = nt.nodes.new("NodeReroute")
        reroute_003.name = "Reroute.003"
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.operation = 'DIVIDE'
        math_002.use_clamp = False
        #Value
        math_002.inputs[0].default_value = 1.0
        #Value_002
        math_002.inputs[2].default_value = 0.5
        
        #node Separate XYZ
        separate_xyz = nt.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz.name = "Separate XYZ"
        
        #node Separate XYZ.001
        separate_xyz_001 = nt.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz_001.name = "Separate XYZ.001"
        
        #initialize nt links
        #reroute_060.Output -> math_094.Value
        nt.links.new(reroute_060.outputs[0], math_094.inputs[0])
        #math_095.Value -> math_094.Value
        nt.links.new(math_095.outputs[0], math_094.inputs[1])
        #math_096.Value -> math_097.Value
        nt.links.new(math_096.outputs[0], math_097.inputs[1])
        #reroute_061.Output -> math_097.Value
        nt.links.new(reroute_061.outputs[0], math_097.inputs[0])
        #reroute_064.Output -> reroute_060.Input
        nt.links.new(reroute_064.outputs[0], reroute_060.inputs[0])
        #reroute_065.Output -> reroute_061.Input
        nt.links.new(reroute_065.outputs[0], reroute_061.inputs[0])
        #math_098.Value -> math_099.Value
        nt.links.new(math_098.outputs[0], math_099.inputs[1])
        #reroute_062.Output -> math_099.Value
        nt.links.new(reroute_062.outputs[0], math_099.inputs[0])
        #reroute_063.Output -> reroute_062.Input
        nt.links.new(reroute_063.outputs[0], reroute_062.inputs[0])
        #reroute_075.Output -> math_113.Value
        nt.links.new(reroute_075.outputs[0], math_113.inputs[1])
        #reroute_070.Output -> math_120.Value
        nt.links.new(reroute_070.outputs[0], math_120.inputs[0])
        #reroute_070.Output -> math_121.Value
        nt.links.new(reroute_070.outputs[0], math_121.inputs[0])
        #math_121.Value -> math_120.Value
        nt.links.new(math_121.outputs[0], math_120.inputs[1])
        #reroute_070.Output -> math_123.Value
        nt.links.new(reroute_070.outputs[0], math_123.inputs[0])
        #math_120.Value -> math_123.Value
        nt.links.new(math_120.outputs[0], math_123.inputs[1])
        #math_123.Value -> math_118.Value
        nt.links.new(math_123.outputs[0], math_118.inputs[0])
        #reroute_076.Output -> math_119.Value
        nt.links.new(reroute_076.outputs[0], math_119.inputs[1])
        #math_120.Value -> mix_008.Factor
        nt.links.new(math_120.outputs[0], mix_008.inputs[0])
        #math_119.Value -> mix_008.A
        nt.links.new(math_119.outputs[0], mix_008.inputs[6])
        #math_117.Value -> mix_008.B
        nt.links.new(math_117.outputs[0], mix_008.inputs[7])
        #math_119.Value -> math_117.Value
        nt.links.new(math_119.outputs[0], math_117.inputs[1])
        #math_118.Value -> math_119.Value
        nt.links.new(math_118.outputs[0], math_119.inputs[0])
        #math_109.Value -> mix_007.A
        nt.links.new(math_109.outputs[0], mix_007.inputs[6])
        #math_112.Value -> mix_007.B
        nt.links.new(math_112.outputs[0], mix_007.inputs[7])
        #math_109.Value -> math_112.Value
        nt.links.new(math_109.outputs[0], math_112.inputs[1])
        #reroute_075.Output -> math_109.Value
        nt.links.new(reroute_075.outputs[0], math_109.inputs[1])
        #math_113.Value -> math_109.Value
        nt.links.new(math_113.outputs[0], math_109.inputs[0])
        #math_111.Value -> math_114.Value
        nt.links.new(math_111.outputs[0], math_114.inputs[1])
        #math_114.Value -> math_110.Value
        nt.links.new(math_114.outputs[0], math_110.inputs[1])
        #reroute_069.Output -> math_111.Value
        nt.links.new(reroute_069.outputs[0], math_111.inputs[0])
        #reroute_069.Output -> math_114.Value
        nt.links.new(reroute_069.outputs[0], math_114.inputs[0])
        #reroute_069.Output -> math_110.Value
        nt.links.new(reroute_069.outputs[0], math_110.inputs[0])
        #math_110.Value -> math_113.Value
        nt.links.new(math_110.outputs[0], math_113.inputs[0])
        #math_114.Value -> mix_007.Factor
        nt.links.new(math_114.outputs[0], mix_007.inputs[0])
        #reroute_066.Output -> math_115.Value
        nt.links.new(reroute_066.outputs[0], math_115.inputs[0])
        #reroute_072.Output -> math_122.Value
        nt.links.new(reroute_072.outputs[0], math_122.inputs[0])
        #mix_008.Result -> math_103.Value
        nt.links.new(mix_008.outputs[2], math_103.inputs[1])
        #mix_007.Result -> math_102.Value
        nt.links.new(mix_007.outputs[2], math_102.inputs[1])
        #math_115.Value -> reroute_069.Input
        nt.links.new(math_115.outputs[0], reroute_069.inputs[0])
        #reroute_071.Output -> math_132.Value
        nt.links.new(reroute_071.outputs[0], math_132.inputs[0])
        #math_122.Value -> reroute_070.Input
        nt.links.new(math_122.outputs[0], reroute_070.inputs[0])
        #reroute_071.Output -> math_134.Value
        nt.links.new(reroute_071.outputs[0], math_134.inputs[0])
        #math_104.Value -> mix_006.A
        nt.links.new(math_104.outputs[0], mix_006.inputs[6])
        #math_106.Value -> mix_006.B
        nt.links.new(math_106.outputs[0], mix_006.inputs[7])
        #math_104.Value -> math_106.Value
        nt.links.new(math_104.outputs[0], math_106.inputs[1])
        #math_107.Value -> math_104.Value
        nt.links.new(math_107.outputs[0], math_104.inputs[0])
        #math_105.Value -> math_108.Value
        nt.links.new(math_105.outputs[0], math_108.inputs[1])
        #math_108.Value -> math_124.Value
        nt.links.new(math_108.outputs[0], math_124.inputs[1])
        #reroute_068.Output -> math_105.Value
        nt.links.new(reroute_068.outputs[0], math_105.inputs[0])
        #reroute_068.Output -> math_108.Value
        nt.links.new(reroute_068.outputs[0], math_108.inputs[0])
        #reroute_068.Output -> math_124.Value
        nt.links.new(reroute_068.outputs[0], math_124.inputs[0])
        #math_124.Value -> math_107.Value
        nt.links.new(math_124.outputs[0], math_107.inputs[0])
        #math_108.Value -> mix_006.Factor
        nt.links.new(math_108.outputs[0], mix_006.inputs[0])
        #mix_006.Result -> math_101.Value
        nt.links.new(mix_006.outputs[2], math_101.inputs[1])
        #math_100.Value -> reroute_068.Input
        nt.links.new(math_100.outputs[0], reroute_068.inputs[0])
        #reroute_074.Output -> math_104.Value
        nt.links.new(reroute_074.outputs[0], math_104.inputs[1])
        #reroute_074.Output -> math_107.Value
        nt.links.new(reroute_074.outputs[0], math_107.inputs[1])
        #reroute_071.Output -> math_133.Value
        nt.links.new(reroute_071.outputs[0], math_133.inputs[0])
        #separate_xyz_002.X -> reroute_072.Input
        nt.links.new(separate_xyz_002.outputs[0], reroute_072.inputs[0])
        #separate_xyz_002.Y -> reroute_066.Input
        nt.links.new(separate_xyz_002.outputs[1], reroute_066.inputs[0])
        #reroute_067.Output -> math_100.Value
        nt.links.new(reroute_067.outputs[0], math_100.inputs[0])
        #separate_xyz_002.Z -> reroute_067.Input
        nt.links.new(separate_xyz_002.outputs[2], reroute_067.inputs[0])
        #separate_xyz_002.Z -> reroute_063.Input
        nt.links.new(separate_xyz_002.outputs[2], reroute_063.inputs[0])
        #separate_xyz_002.Y -> reroute_065.Input
        nt.links.new(separate_xyz_002.outputs[1], reroute_065.inputs[0])
        #separate_xyz_002.X -> reroute_064.Input
        nt.links.new(separate_xyz_002.outputs[0], reroute_064.inputs[0])
        #math_103.Value -> math_095.Value
        nt.links.new(math_103.outputs[0], math_095.inputs[0])
        #math_102.Value -> math_096.Value
        nt.links.new(math_102.outputs[0], math_096.inputs[0])
        #math_101.Value -> math_098.Value
        nt.links.new(math_101.outputs[0], math_098.inputs[0])
        #math_094.Value -> combine_xyz_001.X
        nt.links.new(math_094.outputs[0], combine_xyz_001.inputs[0])
        #math_097.Value -> combine_xyz_001.Y
        nt.links.new(math_097.outputs[0], combine_xyz_001.inputs[1])
        #math_099.Value -> combine_xyz_001.Z
        nt.links.new(math_099.outputs[0], combine_xyz_001.inputs[2])
        #reroute_080.Output -> math_127.Value
        nt.links.new(reroute_080.outputs[0], math_127.inputs[0])
        #reroute_076.Output -> math_118.Value
        nt.links.new(reroute_076.outputs[0], math_118.inputs[1])
        #reroute_080.Output -> math_125.Value
        nt.links.new(reroute_080.outputs[0], math_125.inputs[0])
        #reroute_080.Output -> math_126.Value
        nt.links.new(reroute_080.outputs[0], math_126.inputs[0])
        #reroute_073.Output -> reroute_071.Input
        nt.links.new(reroute_073.outputs[0], reroute_071.inputs[0])
        #reroute_073.Output -> reroute_080.Input
        nt.links.new(reroute_073.outputs[0], reroute_080.inputs[0])
        #reroute_074.Output -> math_098.Value
        nt.links.new(reroute_074.outputs[0], math_098.inputs[1])
        #reroute_075.Output -> math_096.Value
        nt.links.new(reroute_075.outputs[0], math_096.inputs[1])
        #reroute_076.Output -> math_095.Value
        nt.links.new(reroute_076.outputs[0], math_095.inputs[1])
        #math_126.Value -> reroute_074.Input
        nt.links.new(math_126.outputs[0], reroute_074.inputs[0])
        #math_127.Value -> reroute_076.Input
        nt.links.new(math_127.outputs[0], reroute_076.inputs[0])
        #math_125.Value -> reroute_075.Input
        nt.links.new(math_125.outputs[0], reroute_075.inputs[0])
        #reroute_079.Output -> math_127.Value
        nt.links.new(reroute_079.outputs[0], math_127.inputs[1])
        #reroute_078.Output -> math_125.Value
        nt.links.new(reroute_078.outputs[0], math_125.inputs[1])
        #reroute_077.Output -> math_126.Value
        nt.links.new(reroute_077.outputs[0], math_126.inputs[1])
        #combine_xyz_001.Vector -> group_output.Vector
        nt.links.new(combine_xyz_001.outputs[0], group_output.inputs[0])
        #mix.Result -> separate_xyz_002.Vector
        nt.links.new(mix.outputs[2], separate_xyz_002.inputs[0])
        #reroute_003.Output -> math_001.Value
        nt.links.new(reroute_003.outputs[0], math_001.inputs[0])
        #math_001.Value -> math.Value
        nt.links.new(math_001.outputs[0], math.inputs[0])
        #math.Value -> mix.Factor
        nt.links.new(math.outputs[0], mix.inputs[0])
        #reroute_003.Output -> mix.B
        nt.links.new(reroute_003.outputs[0], mix.inputs[7])
        #texture_coordinate.Generated -> mix.A
        nt.links.new(texture_coordinate.outputs[0], mix.inputs[6])
        #reroute_046.Output -> math_129.Value
        nt.links.new(reroute_046.outputs[0], math_129.inputs[0])
        #reroute_046.Output -> math_068.Value
        nt.links.new(reroute_046.outputs[0], math_068.inputs[0])
        #reroute_046.Output -> math_128.Value
        nt.links.new(reroute_046.outputs[0], math_128.inputs[0])
        #reroute_047.Output -> math_131.Value
        nt.links.new(reroute_047.outputs[0], math_131.inputs[0])
        #reroute_047.Output -> math_069.Value
        nt.links.new(reroute_047.outputs[0], math_069.inputs[0])
        #reroute_047.Output -> math_130.Value
        nt.links.new(reroute_047.outputs[0], math_130.inputs[0])
        #math_134.Value -> math_122.Value
        nt.links.new(math_134.outputs[0], math_122.inputs[1])
        #math_132.Value -> math_115.Value
        nt.links.new(math_132.outputs[0], math_115.inputs[1])
        #math_133.Value -> math_100.Value
        nt.links.new(math_133.outputs[0], math_100.inputs[1])
        #reroute_002.Output -> math_134.Value
        nt.links.new(reroute_002.outputs[0], math_134.inputs[1])
        #reroute_001.Output -> math_132.Value
        nt.links.new(reroute_001.outputs[0], math_132.inputs[1])
        #reroute.Output -> math_133.Value
        nt.links.new(reroute.outputs[0], math_133.inputs[1])
        #math_002.Value -> reroute_073.Input
        nt.links.new(math_002.outputs[0], reroute_073.inputs[0])
        #group_input.Division -> math_002.Value
        nt.links.new(group_input.outputs[1], math_002.inputs[1])
        #group_input.Input Map -> reroute_003.Input
        nt.links.new(group_input.outputs[0], reroute_003.inputs[0])
        #group_input.Scale -> separate_xyz.Vector
        nt.links.new(group_input.outputs[2], separate_xyz.inputs[0])
        #separate_xyz.X -> reroute_079.Input
        nt.links.new(separate_xyz.outputs[0], reroute_079.inputs[0])
        #separate_xyz.Y -> reroute_078.Input
        nt.links.new(separate_xyz.outputs[1], reroute_078.inputs[0])
        #separate_xyz.Z -> reroute_077.Input
        nt.links.new(separate_xyz.outputs[2], reroute_077.inputs[0])
        #separate_xyz_001.X -> reroute_002.Input
        nt.links.new(separate_xyz_001.outputs[0], reroute_002.inputs[0])
        #separate_xyz_001.Y -> reroute_001.Input
        nt.links.new(separate_xyz_001.outputs[1], reroute_001.inputs[0])
        #separate_xyz_001.Z -> reroute.Input
        nt.links.new(separate_xyz_001.outputs[2], reroute.inputs[0])
        #group_input.Offset -> separate_xyz_001.Vector
        nt.links.new(group_input.outputs[3], separate_xyz_001.inputs[0])
       


