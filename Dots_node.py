import bpy
from .utils import ShaderNode
class ShaderNodeDots(ShaderNode):
    bl_name='Dot Noise'
    bl_label='Dot Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Variation'].default_value = 0
        self.inputs['Scale'].default_value = 5
        self.inputs['Spread'].default_value = 0.1
        self.inputs['Count'].default_value = 1
        self.inputs['W'].hide = True

    def createNodetree(self, name):
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
               #Socket Value
        
        nt.color_tag = 'NONE'
        nt.description = ""

        #nt interface
        #Socket Value
        value_socket = nt.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        value_socket.default_value = 0.0
        value_socket.min_value = 0.0
        value_socket.max_value = 0.0
        value_socket.subtype = 'NONE'
        value_socket.attribute_domain = 'POINT'
        
        #Socket Color
        color_socket = nt.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
        color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        color_socket.attribute_domain = 'POINT'
        
        #Socket Input
        input_socket = nt.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
        input_socket.default_value = (0.0, 0.0, 0.0)
        input_socket.min_value = 0.0
        input_socket.max_value = 1.0
        input_socket.subtype = 'NONE'
        input_socket.attribute_domain = 'POINT'
        input_socket.hide_value = True
        
        #Socket W
        w_socket = nt.interface.new_socket(name = "W", in_out='INPUT', socket_type = 'NodeSocketFloat')
        w_socket.default_value = 0.0
        w_socket.min_value = -1000.0
        w_socket.max_value = 1000.0
        w_socket.subtype = 'NONE'
        w_socket.attribute_domain = 'POINT'
        
        #Socket Scale
        scale_socket = nt.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
        scale_socket.default_value = 5.0
        scale_socket.min_value = -3.4028234663852886e+38
        scale_socket.max_value = 3.4028234663852886e+38
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        
        #Socket Spread
        spread_socket = nt.interface.new_socket(name = "Spread", in_out='INPUT', socket_type = 'NodeSocketFloat')
        spread_socket.default_value = 0.10000000149011612
        spread_socket.min_value = 9.999999747378752e-06
        spread_socket.max_value = 1.0
        spread_socket.subtype = 'NONE'
        spread_socket.attribute_domain = 'POINT'
        
        #Socket Count
        count_socket = nt.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketFloat')
        count_socket.default_value = 1.0
        count_socket.min_value = 9.999999747378752e-06
        count_socket.max_value = 1.0
        count_socket.subtype = 'NONE'
        count_socket.attribute_domain = 'POINT'
        
        #Socket Variation
        variation_socket = nt.interface.new_socket(name = "Variation", in_out='INPUT', socket_type = 'NodeSocketFloat')
        variation_socket.default_value = 0.0
        variation_socket.min_value = 0.0
        variation_socket.max_value = 1.0
        variation_socket.subtype = 'NONE'
        variation_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Reroute.011
        reroute_011 = nt.nodes.new("NodeReroute")
        reroute_011.name = "Reroute.011"
        #node Math.066
        math_066 = nt.nodes.new("ShaderNodeMath")
        math_066.name = "Math.066"
        math_066.operation = 'SUBTRACT'
        math_066.use_clamp = False
        #Value
        math_066.inputs[0].default_value = 1.0
        
        #node Math.067
        math_067 = nt.nodes.new("ShaderNodeMath")
        math_067.name = "Math.067"
        math_067.hide = True
        math_067.operation = 'SUBTRACT'
        math_067.use_clamp = True
        #Value
        math_067.inputs[0].default_value = 1.0
        
        #node Mix.004
        mix_004 = nt.nodes.new("ShaderNodeMix")
        mix_004.name = "Mix.004"
        mix_004.blend_type = 'MIX'
        mix_004.clamp_factor = True
        mix_004.clamp_result = False
        mix_004.data_type = 'RGBA'
        mix_004.factor_mode = 'UNIFORM'
        
        #node Math.065
        math_065 = nt.nodes.new("ShaderNodeMath")
        math_065.name = "Math.065"
        math_065.operation = 'SUBTRACT'
        math_065.use_clamp = False
        
        #node Math.064
        math_064 = nt.nodes.new("ShaderNodeMath")
        math_064.name = "Math.064"
        math_064.operation = 'DIVIDE'
        math_064.use_clamp = True
        
        #node Separate RGB.003
        separate_rgb_003 = nt.nodes.new("ShaderNodeSeparateColor")
        separate_rgb_003.name = "Separate RGB.003"
        separate_rgb_003.mode = 'RGB'
        
        #node Reroute.015
        reroute_015 = nt.nodes.new("NodeReroute")
        reroute_015.name = "Reroute.015"
        #node Reroute.022
        reroute_022 = nt.nodes.new("NodeReroute")
        reroute_022.name = "Reroute.022"
        #node Math.016
        math_016 = nt.nodes.new("ShaderNodeMath")
        math_016.name = "Math.016"
        math_016.operation = 'GREATER_THAN'
        math_016.use_clamp = False
        #Value_001
        math_016.inputs[1].default_value = 0.0
        
        #node Math.022
        math_022 = nt.nodes.new("ShaderNodeMath")
        math_022.name = "Math.022"
        math_022.operation = 'ABSOLUTE'
        math_022.use_clamp = False
        
        #node Texture Coordinate.009
        texture_coordinate_009 = nt.nodes.new("ShaderNodeTexCoord")
        texture_coordinate_009.name = "Texture Coordinate.009"
        texture_coordinate_009.from_instancer = False
        
        #node Reroute.007
        reroute_007 = nt.nodes.new("NodeReroute")
        reroute_007.name = "Reroute.007"
        #node Mix.015
        mix_015 = nt.nodes.new("ShaderNodeMix")
        mix_015.name = "Mix.015"
        mix_015.blend_type = 'MIX'
        mix_015.clamp_factor = True
        mix_015.clamp_result = False
        mix_015.data_type = 'RGBA'
        mix_015.factor_mode = 'UNIFORM'
        
        #node Reroute.016
        reroute_016 = nt.nodes.new("NodeReroute")
        reroute_016.name = "Reroute.016"
        #node Voronoi Texture
        voronoi_texture = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture.name = "Voronoi Texture"
        voronoi_texture.distance = 'EUCLIDEAN'
        voronoi_texture.feature = 'F1'
        voronoi_texture.normalize = False
        voronoi_texture.voronoi_dimensions = '3D'
        #Detail
        voronoi_texture.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture.inputs[5].default_value = 2.0
        #Randomness
        voronoi_texture.inputs[8].default_value = 1.0
        
        #node Voronoi Texture.002
        voronoi_texture_002 = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture_002.name = "Voronoi Texture.002"
        voronoi_texture_002.distance = 'EUCLIDEAN'
        voronoi_texture_002.feature = 'F1'
        voronoi_texture_002.normalize = False
        voronoi_texture_002.voronoi_dimensions = '3D'
        #Detail
        voronoi_texture_002.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture_002.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture_002.inputs[5].default_value = 2.0
        #Randomness
        voronoi_texture_002.inputs[8].default_value = 1.0
        
        #node Math.063
        math_063 = nt.nodes.new("ShaderNodeMath")
        math_063.name = "Math.063"
        math_063.operation = 'MULTIPLY'
        math_063.use_clamp = False
        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Math.060
        math_060 = nt.nodes.new("ShaderNodeMath")
        math_060.name = "Math.060"
        math_060.operation = 'GREATER_THAN'
        math_060.use_clamp = False
        
        #node Math.062
        math_062 = nt.nodes.new("ShaderNodeMath")
        math_062.name = "Math.062"
        math_062.operation = 'DIVIDE'
        math_062.use_clamp = True
        
        #node Reroute
        reroute = nt.nodes.new("NodeReroute")
        reroute.name = "Reroute"
        #node Math.061
        math_061 = nt.nodes.new("ShaderNodeMath")
        math_061.name = "Math.061"
        math_061.operation = 'SUBTRACT'
        math_061.use_clamp = False
        
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.operation = 'MULTIPLY'
        math.use_clamp = False
        
        #node Mix
        mix = nt.nodes.new("ShaderNodeMix")
        mix.name = "Mix"
        mix.blend_type = 'MIX'
        mix.clamp_factor = True
        mix.clamp_result = True
        mix.data_type = 'RGBA'
        mix.factor_mode = 'UNIFORM'
        #A_Color
        mix.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)
        
        
        #Set locations
        reroute_011.location = (-1299.0, -411.3999938964844)
        math_066.location = (-1050.0, -512.4000244140625)
        math_067.location = (-1470.0, -401.3999938964844)
        mix_004.location = (-630.0, -221.07501220703125)
        math_065.location = (-1050.0, -295.20001220703125)
        math_064.location = (-840.0, -512.4000244140625)
        separate_rgb_003.location = (-1260.0, -396.3999938964844)
        reroute_015.location = (-1719.0, -101.0)
        reroute_022.location = (-1719.0, -57.0)
        math_016.location = (-1890.0, 0.0)
        math_022.location = (-2100.0, 0.0)
        texture_coordinate_009.location = (-1890.0, -257.20001220703125)
        reroute_007.location = (-2143.0, -35.0)
        mix_015.location = (-1680.0, 0.0)
        reroute_016.location = (-879.0, -123.0)
        voronoi_texture.location = (-1260.0, 0.0)
        voronoi_texture_002.location = (-1470.0, 0.0)
        math_063.location = (-420.0, 0.0)
        group_output.location = (0.0, 0.0)
        group_input.location = (-2318.0, 0.0)
        math_060.location = (-840.0, -295.20001220703125)
        math_062.location = (-630.0, 0.0)
        reroute.location = (-1089.0, -79.0)
        math_061.location = (-840.0, 0.0)
        math.location = (-1050.0, 0.0)
        mix.location = (-210.0, 0.0)
        
        #Set dimensions
        reroute_011.width, reroute_011.height = 16.0, 100.0
        math_066.width, math_066.height = 140.0, 100.0
        math_067.width, math_067.height = 140.0, 100.0
        mix_004.width, mix_004.height = 140.0, 100.0
        math_065.width, math_065.height = 140.0, 100.0
        math_064.width, math_064.height = 140.0, 100.0
        separate_rgb_003.width, separate_rgb_003.height = 140.0, 100.0
        reroute_015.width, reroute_015.height = 16.0, 100.0
        reroute_022.width, reroute_022.height = 16.0, 100.0
        math_016.width, math_016.height = 140.0, 100.0
        math_022.width, math_022.height = 140.0, 100.0
        texture_coordinate_009.width, texture_coordinate_009.height = 140.0, 100.0
        reroute_007.width, reroute_007.height = 16.0, 100.0
        mix_015.width, mix_015.height = 140.0, 100.0
        reroute_016.width, reroute_016.height = 16.0, 100.0
        voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
        voronoi_texture_002.width, voronoi_texture_002.height = 140.0, 100.0
        math_063.width, math_063.height = 140.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        math_060.width, math_060.height = 140.0, 100.0
        math_062.width, math_062.height = 140.0, 100.0
        reroute.width, reroute.height = 16.0, 100.0
        math_061.width, math_061.height = 140.0, 100.0
        math.width, math.height = 140.0, 100.0
        mix.width, mix.height = 140.0, 100.0
        
        #initialize nt links
        #mix_015.Result -> voronoi_texture_002.Vector
        nt.links.new(mix_015.outputs[2], voronoi_texture_002.inputs[0])
        #reroute_022.Output -> voronoi_texture.Scale
        nt.links.new(reroute_022.outputs[0], voronoi_texture.inputs[2])
        #reroute_022.Output -> voronoi_texture_002.Scale
        nt.links.new(reroute_022.outputs[0], voronoi_texture_002.inputs[2])
        #reroute_011.Output -> math_060.Value
        nt.links.new(reroute_011.outputs[0], math_060.inputs[1])
        #separate_rgb_003.Red -> math_060.Value
        nt.links.new(separate_rgb_003.outputs[0], math_060.inputs[0])
        #math_065.Value -> math_064.Value
        nt.links.new(math_065.outputs[0], math_064.inputs[0])
        #reroute_011.Output -> math_066.Value
        nt.links.new(reroute_011.outputs[0], math_066.inputs[1])
        #reroute_011.Output -> math_065.Value
        nt.links.new(reroute_011.outputs[0], math_065.inputs[1])
        #math_066.Value -> math_064.Value
        nt.links.new(math_066.outputs[0], math_064.inputs[1])
        #math_060.Value -> mix_004.A
        nt.links.new(math_060.outputs[0], mix_004.inputs[6])
        #math_064.Value -> mix_004.B
        nt.links.new(math_064.outputs[0], mix_004.inputs[7])
        #reroute_016.Output -> mix_004.Factor
        nt.links.new(reroute_016.outputs[0], mix_004.inputs[0])
        #math_067.Value -> reroute_011.Input
        nt.links.new(math_067.outputs[0], reroute_011.inputs[0])
        #reroute_015.Output -> math_067.Value
        nt.links.new(reroute_015.outputs[0], math_067.inputs[1])
        #mix_004.Result -> math_063.Value
        nt.links.new(mix_004.outputs[2], math_063.inputs[1])
        #separate_rgb_003.Green -> math_065.Value
        nt.links.new(separate_rgb_003.outputs[1], math_065.inputs[0])
        #math_063.Value -> group_output.Value
        nt.links.new(math_063.outputs[0], group_output.inputs[0])
        #reroute_007.Output -> mix_015.B
        nt.links.new(reroute_007.outputs[0], mix_015.inputs[7])
        #math_016.Value -> mix_015.Factor
        nt.links.new(math_016.outputs[0], mix_015.inputs[0])
        #math_022.Value -> math_016.Value
        nt.links.new(math_022.outputs[0], math_016.inputs[0])
        #reroute_007.Output -> math_022.Value
        nt.links.new(reroute_007.outputs[0], math_022.inputs[0])
        #group_input.Count -> reroute_015.Input
        nt.links.new(group_input.outputs[4], reroute_015.inputs[0])
        #group_input.Variation -> reroute_016.Input
        nt.links.new(group_input.outputs[5], reroute_016.inputs[0])
        #group_input.Scale -> reroute_022.Input
        nt.links.new(group_input.outputs[2], reroute_022.inputs[0])
        #mix_015.Result -> voronoi_texture.Vector
        nt.links.new(mix_015.outputs[2], voronoi_texture.inputs[0])
        #group_input.Input -> reroute_007.Input
        nt.links.new(group_input.outputs[0], reroute_007.inputs[0])
        #math_061.Value -> math_062.Value
        nt.links.new(math_061.outputs[0], math_062.inputs[0])
        #math_062.Value -> math_063.Value
        nt.links.new(math_062.outputs[0], math_063.inputs[0])
        #group_input.Spread -> reroute.Input
        nt.links.new(group_input.outputs[3], reroute.inputs[0])
        #reroute.Output -> math_062.Value
        nt.links.new(reroute.outputs[0], math_062.inputs[1])
        #reroute.Output -> math_061.Value
        nt.links.new(reroute.outputs[0], math_061.inputs[0])
        #voronoi_texture_002.Color -> separate_rgb_003.Color
        nt.links.new(voronoi_texture_002.outputs[1], separate_rgb_003.inputs[0])
        #math.Value -> math_061.Value
        nt.links.new(math.outputs[0], math_061.inputs[1])
        #voronoi_texture.Distance -> math.Value
        nt.links.new(voronoi_texture.outputs[0], math.inputs[0])
        #voronoi_texture.Distance -> math.Value
        nt.links.new(voronoi_texture.outputs[0], math.inputs[1])
        #texture_coordinate_009.Generated -> mix_015.A
        nt.links.new(texture_coordinate_009.outputs[0], mix_015.inputs[6])
        #math_063.Value -> mix.Factor
        nt.links.new(math_063.outputs[0], mix.inputs[0])
        #voronoi_texture_002.Color -> mix.B
        nt.links.new(voronoi_texture_002.outputs[1], mix.inputs[7])
        #mix.Result -> group_output.Color
        nt.links.new(mix.outputs[2], group_output.inputs[1])
        #group_input.W -> voronoi_texture_002.W
        nt.links.new(group_input.outputs[1], voronoi_texture_002.inputs[1])
        #group_input.W -> voronoi_texture.W
        nt.links.new(group_input.outputs[1], voronoi_texture.inputs[1])
        return nt


