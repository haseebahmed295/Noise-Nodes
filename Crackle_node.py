import bpy
from .utils import ShaderNode
class ShaderNodeCrackle(ShaderNode):
    bl_name='Crackle Noise'
    bl_label='Crackle Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Detail'].default_value = 5
        self.inputs['Scale'].default_value = 5
        self.inputs['Range'].default_value = 0.5
        self.inputs['W'].hide = True

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
        
        nt.color_tag = 'NONE'
        nt.description = ""

        #nt interface
        #Socket Color
        color_socket = nt.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
        color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        color_socket.attribute_domain = 'POINT'
        
        #Socket Fac
        fac_socket = nt.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        fac_socket.default_value = 0.0
        fac_socket.min_value = 0.0
        fac_socket.max_value = 0.0
        fac_socket.subtype = 'NONE'
        fac_socket.attribute_domain = 'POINT'
        
        #Socket Vector
        vector_socket = nt.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = 0.0
        vector_socket.max_value = 1.0
        vector_socket.subtype = 'NONE'
        vector_socket.attribute_domain = 'POINT'
        vector_socket.hide_value = True
        
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
        scale_socket.min_value = -1000.0
        scale_socket.max_value = 1000.0
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        
        #Socket Detail
        detail_socket = nt.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
        detail_socket.default_value = 5.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.subtype = 'NONE'
        detail_socket.attribute_domain = 'POINT'
        
        #Socket Range
        range_socket = nt.interface.new_socket(name = "Range", in_out='INPUT', socket_type = 'NodeSocketFloat')
        range_socket.default_value = 0.5
        range_socket.min_value = 0.0
        range_socket.max_value = 3.4028234663852886e+38
        range_socket.subtype = 'NONE'
        range_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Mix.007
        mix_007 = nt.nodes.new("ShaderNodeMix")
        mix_007.name = "Mix.007"
        mix_007.blend_type = 'SUBTRACT'
        mix_007.clamp_factor = True
        mix_007.clamp_result = False
        mix_007.data_type = 'RGBA'
        mix_007.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_007.inputs[0].default_value = 1.0
        #B_Color
        mix_007.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        
        #node Mix.008
        mix_008 = nt.nodes.new("ShaderNodeMix")
        mix_008.name = "Mix.008"
        mix_008.blend_type = 'MULTIPLY'
        mix_008.clamp_factor = True
        mix_008.clamp_result = False
        mix_008.data_type = 'RGBA'
        mix_008.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_008.inputs[0].default_value = 1.0
        
        #node Mix.014
        mix_014 = nt.nodes.new("ShaderNodeMix")
        mix_014.name = "Mix.014"
        mix_014.blend_type = 'MULTIPLY'
        mix_014.clamp_factor = True
        mix_014.clamp_result = False
        mix_014.data_type = 'RGBA'
        mix_014.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_014.inputs[0].default_value = 1.0
        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Reroute.003
        reroute_003 = nt.nodes.new("NodeReroute")
        reroute_003.name = "Reroute.003"
        #node Math.007
        math_007 = nt.nodes.new("ShaderNodeMath")
        math_007.name = "Math.007"
        math_007.operation = 'POWER'
        math_007.use_clamp = False
        
        #node Reroute.002
        reroute_002 = nt.nodes.new("NodeReroute")
        reroute_002.name = "Reroute.002"
        #node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.operation = 'GREATER_THAN'
        math_004.use_clamp = False
        #Value_001
        math_004.inputs[1].default_value = 0.0
        
        #node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.operation = 'ABSOLUTE'
        math_006.use_clamp = False
        
        #node Texture Coordinate.001
        texture_coordinate_001 = nt.nodes.new("ShaderNodeTexCoord")
        texture_coordinate_001.name = "Texture Coordinate.001"
        texture_coordinate_001.from_instancer = False
        
        #node Mix.006
        mix_006 = nt.nodes.new("ShaderNodeMix")
        mix_006.name = "Mix.006"
        mix_006.blend_type = 'MIX'
        mix_006.clamp_factor = True
        mix_006.clamp_result = False
        mix_006.data_type = 'RGBA'
        mix_006.factor_mode = 'UNIFORM'
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Math.016
        math_016 = nt.nodes.new("ShaderNodeMath")
        math_016.name = "Math.016"
        math_016.operation = 'MULTIPLY'
        math_016.use_clamp = False
        #Value_001
        math_016.inputs[1].default_value = 10.0
        
        #node Math.018
        math_018 = nt.nodes.new("ShaderNodeMath")
        math_018.name = "Math.018"
        math_018.operation = 'POWER'
        math_018.use_clamp = False
        #Value_001
        math_018.inputs[1].default_value = 4.0
        
        #node Noise Texture.005
        noise_texture_005 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_005.name = "Noise Texture.005"
        noise_texture_005.noise_dimensions = '3D'
        noise_texture_005.noise_type = 'FBM'
        noise_texture_005.normalize = True
        #Roughness
        noise_texture_005.inputs[4].default_value = 0.5
        #Lacunarity
        noise_texture_005.inputs[5].default_value = 2.0
        #Distortion
        noise_texture_005.inputs[8].default_value = 0.0
        
        #node Separate RGB.002
        separate_rgb_002 = nt.nodes.new("ShaderNodeSeparateColor")
        separate_rgb_002.name = "Separate RGB.002"
        separate_rgb_002.mode = 'RGB'
        
        #node Math.005
        math_005 = nt.nodes.new("ShaderNodeMath")
        math_005.name = "Math.005"
        math_005.operation = 'POWER'
        math_005.use_clamp = False
        
        #node Math.017
        math_017 = nt.nodes.new("ShaderNodeMath")
        math_017.name = "Math.017"
        math_017.operation = 'POWER'
        math_017.use_clamp = False
        
        #node Combine RGB
        combine_rgb = nt.nodes.new("ShaderNodeCombineColor")
        combine_rgb.name = "Combine RGB"
        combine_rgb.mode = 'RGB'
        
        
        #Set locations
        mix_007.location = (-47.364013671875, -28.9608154296875)
        mix_008.location = (164.960205078125, -11.03729248046875)
        mix_014.location = (338.26611328125, -6.556396484375)
        group_output.location = (1399.126708984375, 56.21197509765625)
        reroute_003.location = (-307.2171630859375, -123.05186462402344)
        math_007.location = (718.314453125, -28.3140869140625)
        reroute_002.location = (-932.8892822265625, -304.4244689941406)
        math_004.location = (-704.3819580078125, 15.75190258026123)
        math_006.location = (-904.1268310546875, -58.794376373291016)
        texture_coordinate_001.location = (-1089.8927001953125, 63.47160720825195)
        mix_006.location = (-498.9571533203125, 9.180338859558105)
        group_input.location = (-1271.5714111328125, -293.7167663574219)
        math_016.location = (87.45454406738281, -228.89926147460938)
        math_018.location = (-427.25982666015625, -296.3743896484375)
        noise_texture_005.location = (-239.151611328125, -89.97918701171875)
        separate_rgb_002.location = (516.0333251953125, 12.352848052978516)
        math_005.location = (717.56689453125, 131.79165649414062)
        math_017.location = (894.8026733398438, 5.226926326751709)
        combine_rgb.location = (1107.0928955078125, 99.53492736816406)
        
        #Set dimensions
        mix_007.width, mix_007.height = 140.0, 100.0
        mix_008.width, mix_008.height = 140.0, 100.0
        mix_014.width, mix_014.height = 140.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0
        reroute_003.width, reroute_003.height = 16.0, 100.0
        math_007.width, math_007.height = 140.0, 100.0
        reroute_002.width, reroute_002.height = 16.0, 100.0
        math_004.width, math_004.height = 140.0, 100.0
        math_006.width, math_006.height = 140.0, 100.0
        texture_coordinate_001.width, texture_coordinate_001.height = 140.0, 100.0
        mix_006.width, mix_006.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        math_016.width, math_016.height = 140.0, 100.0
        math_018.width, math_018.height = 140.0, 100.0
        noise_texture_005.width, noise_texture_005.height = 140.0, 100.0
        separate_rgb_002.width, separate_rgb_002.height = 140.0, 100.0
        math_005.width, math_005.height = 140.0, 100.0
        math_017.width, math_017.height = 140.0, 100.0
        combine_rgb.width, combine_rgb.height = 140.0, 100.0
        
        #initialize nt links
        #noise_texture_005.Color -> mix_007.A
        nt.links.new(noise_texture_005.outputs[1], mix_007.inputs[6])
        #mix_007.Result -> mix_008.A
        nt.links.new(mix_007.outputs[2], mix_008.inputs[6])
        #mix_008.Result -> mix_014.A
        nt.links.new(mix_008.outputs[2], mix_014.inputs[6])
        #mix_007.Result -> mix_008.B
        nt.links.new(mix_007.outputs[2], mix_008.inputs[7])
        #mix_014.Result -> separate_rgb_002.Color
        nt.links.new(mix_014.outputs[2], separate_rgb_002.inputs[0])
        #separate_rgb_002.Red -> math_005.Value
        nt.links.new(separate_rgb_002.outputs[0], math_005.inputs[0])
        #group_input.Detail -> noise_texture_005.Detail
        nt.links.new(group_input.outputs[3], noise_texture_005.inputs[3])
        #separate_rgb_002.Green -> math_005.Value
        nt.links.new(separate_rgb_002.outputs[1], math_005.inputs[1])
        #separate_rgb_002.Blue -> math_007.Value
        nt.links.new(separate_rgb_002.outputs[2], math_007.inputs[1])
        #separate_rgb_002.Green -> math_007.Value
        nt.links.new(separate_rgb_002.outputs[1], math_007.inputs[0])
        #separate_rgb_002.Blue -> math_017.Value
        nt.links.new(separate_rgb_002.outputs[2], math_017.inputs[0])
        #separate_rgb_002.Red -> math_017.Value
        nt.links.new(separate_rgb_002.outputs[0], math_017.inputs[1])
        #math_005.Value -> combine_rgb.Red
        nt.links.new(math_005.outputs[0], combine_rgb.inputs[0])
        #math_007.Value -> combine_rgb.Green
        nt.links.new(math_007.outputs[0], combine_rgb.inputs[1])
        #math_017.Value -> combine_rgb.Blue
        nt.links.new(math_017.outputs[0], combine_rgb.inputs[2])
        #reroute_002.Output -> mix_006.B
        nt.links.new(reroute_002.outputs[0], mix_006.inputs[7])
        #math_004.Value -> mix_006.Factor
        nt.links.new(math_004.outputs[0], mix_006.inputs[0])
        #texture_coordinate_001.Generated -> mix_006.A
        nt.links.new(texture_coordinate_001.outputs[0], mix_006.inputs[6])
        #math_006.Value -> math_004.Value
        nt.links.new(math_006.outputs[0], math_004.inputs[0])
        #reroute_002.Output -> math_006.Value
        nt.links.new(reroute_002.outputs[0], math_006.inputs[0])
        #mix_006.Result -> reroute_003.Input
        nt.links.new(mix_006.outputs[2], reroute_003.inputs[0])
        #group_input.Vector -> reroute_002.Input
        nt.links.new(group_input.outputs[0], reroute_002.inputs[0])
        #reroute_003.Output -> noise_texture_005.Vector
        nt.links.new(reroute_003.outputs[0], noise_texture_005.inputs[0])
        #group_input.Scale -> noise_texture_005.Scale
        nt.links.new(group_input.outputs[2], noise_texture_005.inputs[2])
        #group_input.Range -> math_018.Value
        nt.links.new(group_input.outputs[4], math_018.inputs[0])
        #math_016.Value -> mix_014.B
        nt.links.new(math_016.outputs[0], mix_014.inputs[7])
        #combine_rgb.Color -> group_output.Color
        nt.links.new(combine_rgb.outputs[0], group_output.inputs[0])
        #math_018.Value -> math_016.Value
        nt.links.new(math_018.outputs[0], math_016.inputs[0])
        #math_007.Value -> group_output.Fac
        nt.links.new(math_007.outputs[0], group_output.inputs[1])
        #group_input.W -> noise_texture_005.W
        nt.links.new(group_input.outputs[1], noise_texture_005.inputs[1])
        return nt