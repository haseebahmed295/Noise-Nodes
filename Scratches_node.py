import bpy
from .utils import ShaderNode
class ShaderNodeScratches(ShaderNode):
    bl_name='Scratches Noise'
    bl_label='Scratches Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Ratio'].default_value = 0.5
        self.inputs['Scale'].default_value = 5
        self.inputs['Spread'].default_value = 1
        self.inputs['Detail'].default_value = 2

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')

        value_socket = nt.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        value_socket.subtype = 'NONE'
        value_socket.default_value = 0.0
        value_socket.min_value = 0.0
        value_socket.max_value = 0.0
        value_socket.attribute_domain = 'POINT'
        
        #Socket Cells
        cells_socket = nt.interface.new_socket(name = "Cells", in_out='OUTPUT', socket_type = 'NodeSocketColor')
        cells_socket.attribute_domain = 'POINT'
        
        #Socket Falloff
        falloff_socket = nt.interface.new_socket(name = "Falloff", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        falloff_socket.subtype = 'NONE'
        falloff_socket.default_value = 0.0
        falloff_socket.min_value = -3.4028234663852886e+38
        falloff_socket.max_value = 3.4028234663852886e+38
        falloff_socket.attribute_domain = 'POINT'
        
        #Socket Vector
        vector_socket = nt.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
        vector_socket.subtype = 'NONE'
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = 0.0
        vector_socket.max_value = 1.0
        vector_socket.attribute_domain = 'POINT'
        vector_socket.hide_value = True
        
        #Socket Scale
        scale_socket = nt.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
        scale_socket.subtype = 'NONE'
        scale_socket.default_value = 5.0
        scale_socket.min_value = -3.4028234663852886e+38
        scale_socket.max_value = 3.4028234663852886e+38
        scale_socket.attribute_domain = 'POINT'
        
        #Socket Ratio
        ratio_socket = nt.interface.new_socket(name = "Ratio", in_out='INPUT', socket_type = 'NodeSocketFloat')
        ratio_socket.subtype = 'NONE'
        ratio_socket.default_value = 0.5
        ratio_socket.min_value = -10000.0
        ratio_socket.max_value = 10000.0
        ratio_socket.attribute_domain = 'POINT'
        
        #Socket Spread
        spread_socket = nt.interface.new_socket(name = "Spread", in_out='INPUT', socket_type = 'NodeSocketFloat')
        spread_socket.subtype = 'NONE'
        spread_socket.default_value = 1.0
        spread_socket.min_value = -2.0
        spread_socket.max_value = 2.0
        spread_socket.attribute_domain = 'POINT'
        
        #Socket Detail
        detail_socket = nt.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
        detail_socket.subtype = 'NONE'
        detail_socket.default_value = 2.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Math.072
        math_072 = nt.nodes.new("ShaderNodeMath")
        math_072.name = "Math.072"
        math_072.hide = True
        math_072.operation = 'ABSOLUTE'
        math_072.use_clamp = False
        #Value_001
        math_072.inputs[1].default_value = 0.5
        #Value_002
        math_072.inputs[2].default_value = 0.5
        
        #node Math.058
        math_058 = nt.nodes.new("ShaderNodeMath")
        math_058.name = "Math.058"
        math_058.hide = True
        math_058.operation = 'SUBTRACT'
        math_058.use_clamp = False
        #Value_001
        math_058.inputs[1].default_value = 0.5
        #Value_002
        math_058.inputs[2].default_value = 0.5
        
        #node Math.073
        math_073 = nt.nodes.new("ShaderNodeMath")
        math_073.name = "Math.073"
        math_073.hide = True
        math_073.operation = 'MULTIPLY'
        math_073.use_clamp = True
        #Value_002
        math_073.inputs[2].default_value = 0.5
        
        #node Math.080
        math_080 = nt.nodes.new("ShaderNodeMath")
        math_080.name = "Math.080"
        math_080.hide = True
        math_080.operation = 'MULTIPLY'
        math_080.use_clamp = True
        #Value_002
        math_080.inputs[2].default_value = 0.5
        
        #node Noise Texture.004
        noise_texture_004 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_004.name = "Noise Texture.004"
        noise_texture_004.noise_dimensions = '3D'
        noise_texture_004.noise_type = 'FBM'
        noise_texture_004.normalize = True
        #W
        noise_texture_004.inputs[1].default_value = 0.0
        #Roughness
        noise_texture_004.inputs[4].default_value = 0.5
        #Lacunarity
        noise_texture_004.inputs[5].default_value = 2.0
        #Offset
        noise_texture_004.inputs[6].default_value = 0.0
        #Gain
        noise_texture_004.inputs[7].default_value = 1.0
        #Distortion
        noise_texture_004.inputs[8].default_value = 0.0
        
        #node Separate RGB.003
        separate_rgb_003 = nt.nodes.new("ShaderNodeSeparateColor")
        separate_rgb_003.name = "Separate RGB.003"
        separate_rgb_003.mode = 'RGB'
        
        #node Math.076
        math_076 = nt.nodes.new("ShaderNodeMath")
        math_076.name = "Math.076"
        math_076.hide = True
        math_076.operation = 'ABSOLUTE'
        math_076.use_clamp = False
        #Value_001
        math_076.inputs[1].default_value = 0.5
        #Value_002
        math_076.inputs[2].default_value = 0.5
        
        #node Math.074
        math_074 = nt.nodes.new("ShaderNodeMath")
        math_074.name = "Math.074"
        math_074.hide = True
        math_074.operation = 'SUBTRACT'
        math_074.use_clamp = False
        #Value_001
        math_074.inputs[1].default_value = 0.5
        #Value_002
        math_074.inputs[2].default_value = 0.5
        
        #node Math.077
        math_077 = nt.nodes.new("ShaderNodeMath")
        math_077.name = "Math.077"
        math_077.hide = True
        math_077.operation = 'SUBTRACT'
        math_077.use_clamp = False
        #Value_001
        math_077.inputs[1].default_value = 0.5
        #Value_002
        math_077.inputs[2].default_value = 0.5
        
        #node Math.079
        math_079 = nt.nodes.new("ShaderNodeMath")
        math_079.name = "Math.079"
        math_079.hide = True
        math_079.operation = 'ABSOLUTE'
        math_079.use_clamp = False
        #Value_001
        math_079.inputs[1].default_value = 0.5
        #Value_002
        math_079.inputs[2].default_value = 0.5
        
        #node Math.075
        math_075 = nt.nodes.new("ShaderNodeMath")
        math_075.name = "Math.075"
        math_075.hide = True
        math_075.operation = 'MULTIPLY'
        math_075.use_clamp = True
        #Value_002
        math_075.inputs[2].default_value = 0.5
        
        #node Math.078
        math_078 = nt.nodes.new("ShaderNodeMath")
        math_078.name = "Math.078"
        math_078.hide = True
        math_078.operation = 'MULTIPLY'
        math_078.use_clamp = True
        #Value_002
        math_078.inputs[2].default_value = 0.5
        
        #node Math.081
        math_081 = nt.nodes.new("ShaderNodeMath")
        math_081.name = "Math.081"
        math_081.hide = True
        math_081.operation = 'MULTIPLY'
        math_081.use_clamp = True
        #Value_002
        math_081.inputs[2].default_value = 0.5
        
        #node Math.071
        math_071 = nt.nodes.new("ShaderNodeMath")
        math_071.name = "Math.071"
        math_071.hide = True
        math_071.operation = 'DIVIDE'
        math_071.use_clamp = True
        #Value_002
        math_071.inputs[2].default_value = 0.5
        
        #node Reroute.013
        reroute_013 = nt.nodes.new("NodeReroute")
        reroute_013.name = "Reroute.013"
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Mix.008
        mix_008 = nt.nodes.new("ShaderNodeMix")
        mix_008.name = "Mix.008"
        mix_008.hide = True
        mix_008.blend_type = 'ADD'
        mix_008.clamp_factor = True
        mix_008.clamp_result = False
        mix_008.data_type = 'RGBA'
        mix_008.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_008.inputs[0].default_value = 1.0
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
        
        #node Mix.014
        mix_014 = nt.nodes.new("ShaderNodeMix")
        mix_014.name = "Mix.014"
        mix_014.hide = True
        mix_014.blend_type = 'MULTIPLY'
        mix_014.clamp_factor = True
        mix_014.clamp_result = False
        mix_014.data_type = 'RGBA'
        mix_014.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_014.inputs[0].default_value = 1.0
        #Factor_Vector
        mix_014.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_014.inputs[2].default_value = 0.0
        #B_Float
        mix_014.inputs[3].default_value = 0.0
        #A_Vector
        mix_014.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_014.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix_014.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_014.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Math.083
        math_083 = nt.nodes.new("ShaderNodeMath")
        math_083.name = "Math.083"
        math_083.hide = True
        math_083.operation = 'DIVIDE'
        math_083.use_clamp = False
        #Value
        math_083.inputs[0].default_value = 10.0
        #Value_002
        math_083.inputs[2].default_value = 0.5
        
        #node Math.085
        math_085 = nt.nodes.new("ShaderNodeMath")
        math_085.name = "Math.085"
        math_085.hide = True
        math_085.operation = 'MULTIPLY'
        math_085.use_clamp = False
        #Value_002
        math_085.inputs[2].default_value = 0.5
        
        #node Voronoi Texture.007
        voronoi_texture_007 = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture_007.name = "Voronoi Texture.007"
        voronoi_texture_007.distance = 'EUCLIDEAN'
        voronoi_texture_007.feature = 'F1'
        voronoi_texture_007.normalize = False
        voronoi_texture_007.voronoi_dimensions = '3D'
        #W
        voronoi_texture_007.inputs[1].default_value = 0.0
        #Detail
        voronoi_texture_007.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture_007.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture_007.inputs[5].default_value = 2.0
        #Smoothness
        voronoi_texture_007.inputs[6].default_value = 1.0
        #Exponent
        voronoi_texture_007.inputs[7].default_value = 0.5
        #Randomness
        voronoi_texture_007.inputs[8].default_value = 1.0
        
        #node Voronoi Texture.003
        voronoi_texture_003 = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture_003.name = "Voronoi Texture.003"
        voronoi_texture_003.distance = 'EUCLIDEAN'
        voronoi_texture_003.feature = 'F1'
        voronoi_texture_003.normalize = False
        voronoi_texture_003.voronoi_dimensions = '3D'
        #W
        voronoi_texture_003.inputs[1].default_value = 0.0
        #Detail
        voronoi_texture_003.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture_003.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture_003.inputs[5].default_value = 2.0
        #Smoothness
        voronoi_texture_003.inputs[6].default_value = 1.0
        #Exponent
        voronoi_texture_003.inputs[7].default_value = 0.5
        #Randomness
        voronoi_texture_003.inputs[8].default_value = 1.0
        
        #node Reroute.016
        reroute_016 = nt.nodes.new("NodeReroute")
        reroute_016.name = "Reroute.016"
        #node Reroute.015
        reroute_015 = nt.nodes.new("NodeReroute")
        reroute_015.name = "Reroute.015"
        #node Math.084
        math_084 = nt.nodes.new("ShaderNodeMath")
        math_084.name = "Math.084"
        math_084.hide = True
        math_084.operation = 'POWER'
        math_084.use_clamp = False
        #Value
        math_084.inputs[0].default_value = 10.0
        #Value_002
        math_084.inputs[2].default_value = 0.5
        
        #node Math.086
        math_086 = nt.nodes.new("ShaderNodeMath")
        math_086.name = "Math.086"
        math_086.hide = True
        math_086.operation = 'ADD'
        math_086.use_clamp = False
        #Value_001
        math_086.inputs[1].default_value = 1.0
        #Value_002
        math_086.inputs[2].default_value = 0.5
        
        #node Reroute.014
        reroute_014 = nt.nodes.new("NodeReroute")
        reroute_014.name = "Reroute.014"
        #node Reroute.017
        reroute_017 = nt.nodes.new("NodeReroute")
        reroute_017.name = "Reroute.017"
        #node Math.069
        math_069 = nt.nodes.new("ShaderNodeMath")
        math_069.name = "Math.069"
        math_069.operation = 'POWER'
        math_069.use_clamp = True
        #Value_001
        math_069.inputs[1].default_value = 0.4999999701976776
        #Value_002
        math_069.inputs[2].default_value = 0.5
        
        #node Reroute
        reroute = nt.nodes.new("NodeReroute")
        reroute.name = "Reroute"
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
        
        #node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.operation = 'GREATER_THAN'
        math_001.use_clamp = False
        #Value_001
        math_001.inputs[1].default_value = 0.0
        #Value_002
        math_001.inputs[2].default_value = 0.5
        
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.operation = 'ABSOLUTE'
        math.use_clamp = False
        #Value_001
        math.inputs[1].default_value = 0.5
        #Value_002
        math.inputs[2].default_value = 0.5
        
        #node Texture Coordinate
        texture_coordinate = nt.nodes.new("ShaderNodeTexCoord")
        texture_coordinate.name = "Texture Coordinate"
        texture_coordinate.from_instancer = False
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Voronoi Texture
        voronoi_texture = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture.name = "Voronoi Texture"
        voronoi_texture.distance = 'EUCLIDEAN'
        voronoi_texture.feature = 'F2'
        voronoi_texture.normalize = False
        voronoi_texture.voronoi_dimensions = '3D'
        #W
        voronoi_texture.inputs[1].default_value = 0.0
        #Detail
        voronoi_texture.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture.inputs[5].default_value = 2.0
        #Smoothness
        voronoi_texture.inputs[6].default_value = 1.0
        #Exponent
        voronoi_texture.inputs[7].default_value = 0.5
        #Randomness
        voronoi_texture.inputs[8].default_value = 1.0
        
        #node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.operation = 'SUBTRACT'
        math_002.use_clamp = False
        #Value_002
        math_002.inputs[2].default_value = 0.5
        
        #node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.operation = 'MULTIPLY'
        math_003.use_clamp = False
        #Value_002
        math_003.inputs[2].default_value = 0.5
        
        #node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.operation = 'MULTIPLY'
        math_004.use_clamp = False
        #Value_002
        math_004.inputs[2].default_value = 0.5
        

        #initialize nt links
        #noise_texture_004.Color -> separate_rgb_003.Color
        nt.links.new(noise_texture_004.outputs[1], separate_rgb_003.inputs[0])
        #reroute_013.Output -> math_071.Value
        nt.links.new(reroute_013.outputs[0], math_071.inputs[1])
        #voronoi_texture_003.Color -> mix_014.A
        nt.links.new(voronoi_texture_003.outputs[1], mix_014.inputs[6])
        #mix_008.Result -> noise_texture_004.Vector
        nt.links.new(mix_008.outputs[2], noise_texture_004.inputs[0])
        #mix_014.Result -> mix_008.B
        nt.links.new(mix_014.outputs[2], mix_008.inputs[7])
        #reroute_014.Output -> mix_008.A
        nt.links.new(reroute_014.outputs[0], mix_008.inputs[6])
        #separate_rgb_003.Red -> math_058.Value
        nt.links.new(separate_rgb_003.outputs[0], math_058.inputs[0])
        #math_058.Value -> math_072.Value
        nt.links.new(math_058.outputs[0], math_072.inputs[0])
        #math_072.Value -> math_073.Value
        nt.links.new(math_072.outputs[0], math_073.inputs[0])
        #math_074.Value -> math_076.Value
        nt.links.new(math_074.outputs[0], math_076.inputs[0])
        #math_076.Value -> math_075.Value
        nt.links.new(math_076.outputs[0], math_075.inputs[0])
        #math_077.Value -> math_079.Value
        nt.links.new(math_077.outputs[0], math_079.inputs[0])
        #math_079.Value -> math_078.Value
        nt.links.new(math_079.outputs[0], math_078.inputs[0])
        #separate_rgb_003.Green -> math_074.Value
        nt.links.new(separate_rgb_003.outputs[1], math_074.inputs[0])
        #separate_rgb_003.Blue -> math_077.Value
        nt.links.new(separate_rgb_003.outputs[2], math_077.inputs[0])
        #math_080.Value -> math_081.Value
        nt.links.new(math_080.outputs[0], math_081.inputs[0])
        #math_075.Value -> math_080.Value
        nt.links.new(math_075.outputs[0], math_080.inputs[1])
        #math_078.Value -> math_081.Value
        nt.links.new(math_078.outputs[0], math_081.inputs[1])
        #reroute_016.Output -> math_073.Value
        nt.links.new(reroute_016.outputs[0], math_073.inputs[1])
        #reroute_016.Output -> math_075.Value
        nt.links.new(reroute_016.outputs[0], math_075.inputs[1])
        #reroute_016.Output -> math_078.Value
        nt.links.new(reroute_016.outputs[0], math_078.inputs[1])
        #math_071.Value -> group_output.Value
        nt.links.new(math_071.outputs[0], group_output.inputs[0])
        #math_069.Value -> reroute_013.Input
        nt.links.new(math_069.outputs[0], reroute_013.inputs[0])
        #reroute_014.Output -> voronoi_texture_007.Vector
        nt.links.new(reroute_014.outputs[0], voronoi_texture_007.inputs[0])
        #math_073.Value -> math_080.Value
        nt.links.new(math_073.outputs[0], math_080.inputs[0])
        #math_081.Value -> math_071.Value
        nt.links.new(math_081.outputs[0], math_071.inputs[0])
        #reroute_015.Output -> voronoi_texture_003.Scale
        nt.links.new(reroute_015.outputs[0], voronoi_texture_003.inputs[2])
        #reroute_015.Output -> voronoi_texture_007.Scale
        nt.links.new(reroute_015.outputs[0], voronoi_texture_007.inputs[2])
        #math_083.Value -> mix_014.B
        nt.links.new(math_083.outputs[0], mix_014.inputs[7])
        #reroute_015.Output -> math_083.Value
        nt.links.new(reroute_015.outputs[0], math_083.inputs[1])
        #group_input.Scale -> reroute_015.Input
        nt.links.new(group_input.outputs[1], reroute_015.inputs[0])
        #math_084.Value -> reroute_016.Input
        nt.links.new(math_084.outputs[0], reroute_016.inputs[0])
        #math_085.Value -> noise_texture_004.Scale
        nt.links.new(math_085.outputs[0], noise_texture_004.inputs[2])
        #group_input.Ratio -> math_085.Value
        nt.links.new(group_input.outputs[2], math_085.inputs[1])
        #reroute_015.Output -> math_085.Value
        nt.links.new(reroute_015.outputs[0], math_085.inputs[0])
        #math_086.Value -> math_084.Value
        nt.links.new(math_086.outputs[0], math_084.inputs[1])
        #reroute_017.Output -> noise_texture_004.Detail
        nt.links.new(reroute_017.outputs[0], noise_texture_004.inputs[3])
        #group_input.Spread -> math_086.Value
        nt.links.new(group_input.outputs[3], math_086.inputs[0])
        #voronoi_texture_003.Color -> group_output.Cells
        nt.links.new(voronoi_texture_003.outputs[1], group_output.inputs[1])
        #reroute_013.Output -> group_output.Falloff
        nt.links.new(reroute_013.outputs[0], group_output.inputs[2])
        #group_input.Detail -> reroute_017.Input
        nt.links.new(group_input.outputs[4], reroute_017.inputs[0])
        #reroute_014.Output -> voronoi_texture_003.Vector
        nt.links.new(reroute_014.outputs[0], voronoi_texture_003.inputs[0])
        #reroute.Output -> mix_006.B
        nt.links.new(reroute.outputs[0], mix_006.inputs[7])
        #math_001.Value -> mix_006.Factor
        nt.links.new(math_001.outputs[0], mix_006.inputs[0])
        #texture_coordinate.Generated -> mix_006.A
        nt.links.new(texture_coordinate.outputs[0], mix_006.inputs[6])
        #math.Value -> math_001.Value
        nt.links.new(math.outputs[0], math_001.inputs[0])
        #reroute.Output -> math.Value
        nt.links.new(reroute.outputs[0], math.inputs[0])
        #group_input.Vector -> reroute.Input
        nt.links.new(group_input.outputs[0], reroute.inputs[0])
        #mix_006.Result -> reroute_014.Input
        nt.links.new(mix_006.outputs[2], reroute_014.inputs[0])
        #reroute_014.Output -> voronoi_texture.Vector
        nt.links.new(reroute_014.outputs[0], voronoi_texture.inputs[0])
        #reroute_015.Output -> voronoi_texture.Scale
        nt.links.new(reroute_015.outputs[0], voronoi_texture.inputs[2])
        #math_002.Value -> math_069.Value
        nt.links.new(math_002.outputs[0], math_069.inputs[0])
        #math_003.Value -> math_002.Value
        nt.links.new(math_003.outputs[0], math_002.inputs[1])
        #voronoi_texture_007.Distance -> math_003.Value
        nt.links.new(voronoi_texture_007.outputs[0], math_003.inputs[0])
        #voronoi_texture_007.Distance -> math_003.Value
        nt.links.new(voronoi_texture_007.outputs[0], math_003.inputs[1])
        #math_004.Value -> math_002.Value
        nt.links.new(math_004.outputs[0], math_002.inputs[0])
        #voronoi_texture.Distance -> math_004.Value
        nt.links.new(voronoi_texture.outputs[0], math_004.inputs[0])
        #voronoi_texture.Distance -> math_004.Value
        nt.links.new(voronoi_texture.outputs[0], math_004.inputs[1])
   