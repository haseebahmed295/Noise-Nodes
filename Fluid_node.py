import bpy
from .utils import ShaderNode
class ShaderNodeFluid(ShaderNode):
    bl_name='Fluid Noise'
    bl_label='Fluid Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Detail 1'].default_value = 4
        self.inputs['Detail 2'].default_value = 4
        self.inputs['Scale'].default_value = 5
        self.inputs['Scale Ratio'].default_value = 1
        self.inputs['Distortion'].default_value = 1

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
        color_socket = nt.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
        color_socket.attribute_domain = 'POINT'
        
        #Socket Fac
        fac_socket = nt.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        fac_socket.subtype = 'FACTOR'
        fac_socket.default_value = 0.0
        fac_socket.min_value = 0.0
        fac_socket.max_value = 1.0
        fac_socket.attribute_domain = 'POINT'
        
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
        scale_socket.min_value = -1000.0
        scale_socket.max_value = 1000.0
        scale_socket.attribute_domain = 'POINT'
        
        #Socket Scale Ratio
        scale_ratio_socket = nt.interface.new_socket(name = "Scale Ratio", in_out='INPUT', socket_type = 'NodeSocketFloat')
        scale_ratio_socket.subtype = 'NONE'
        scale_ratio_socket.default_value = 1.0
        scale_ratio_socket.min_value = -1000.0
        scale_ratio_socket.max_value = 1000.0
        scale_ratio_socket.attribute_domain = 'POINT'
        
        #Socket Detail 1
        detail_1_socket = nt.interface.new_socket(name = "Detail 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
        detail_1_socket.subtype = 'NONE'
        detail_1_socket.default_value = 4.0
        detail_1_socket.min_value = 0.0
        detail_1_socket.max_value = 16.0
        detail_1_socket.attribute_domain = 'POINT'
        
        #Socket Detail 2
        detail_2_socket = nt.interface.new_socket(name = "Detail 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
        detail_2_socket.subtype = 'NONE'
        detail_2_socket.default_value = 4.0
        detail_2_socket.min_value = 0.0
        detail_2_socket.max_value = 16.0
        detail_2_socket.attribute_domain = 'POINT'
        
        #Socket Distortion
        distortion_socket = nt.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
        distortion_socket.subtype = 'NONE'
        distortion_socket.default_value = 1.0
        distortion_socket.min_value = -1000.0
        distortion_socket.max_value = 1000.0
        distortion_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Mix.005
        mix_005 = nt.nodes.new("ShaderNodeMix")
        mix_005.name = "Mix.005"
        mix_005.blend_type = 'SUBTRACT'
        mix_005.clamp_factor = True
        mix_005.clamp_result = False
        mix_005.data_type = 'RGBA'
        mix_005.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_005.inputs[0].default_value = 1.0
        #Factor_Vector
        mix_005.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_005.inputs[2].default_value = 0.0
        #B_Float
        mix_005.inputs[3].default_value = 0.0
        #A_Vector
        mix_005.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_005.inputs[5].default_value = (0.0, 0.0, 0.0)
        #B_Color
        mix_005.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        #A_Rotation
        mix_005.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_005.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Reroute.003
        reroute_003 = nt.nodes.new("NodeReroute")
        reroute_003.name = "Reroute.003"
        #node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.operation = 'DIVIDE'
        math_004.use_clamp = False
        #Value_002
        math_004.inputs[2].default_value = 0.5
        
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
        
        #node Reroute
        reroute = nt.nodes.new("NodeReroute")
        reroute.name = "Reroute"
        #node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.hide = True
        math_003.operation = 'POWER'
        math_003.use_clamp = False
        #Value_001
        math_003.inputs[1].default_value = 0.5
        #Value_002
        math_003.inputs[2].default_value = 0.5
        
        #node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.operation = 'MULTIPLY'
        math_002.use_clamp = False
        #Value_002
        math_002.inputs[2].default_value = 0.5
        
        #node Mix.004
        mix_004 = nt.nodes.new("ShaderNodeMix")
        mix_004.name = "Mix.004"
        mix_004.blend_type = 'MULTIPLY'
        mix_004.clamp_factor = True
        mix_004.clamp_result = False
        mix_004.data_type = 'RGBA'
        mix_004.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_004.inputs[0].default_value = 1.0
        #Factor_Vector
        mix_004.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_004.inputs[2].default_value = 0.0
        #B_Float
        mix_004.inputs[3].default_value = 0.0
        #A_Vector
        mix_004.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_004.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix_004.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_004.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Noise Texture.002
        noise_texture_002 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_002.name = "Noise Texture.002"
        noise_texture_002.noise_dimensions = '3D'
        noise_texture_002.noise_type = 'FBM'
        noise_texture_002.normalize = True
        #W
        noise_texture_002.inputs[1].default_value = 0.0
        #Roughness
        noise_texture_002.inputs[4].default_value = 0.5
        #Lacunarity
        noise_texture_002.inputs[5].default_value = 2.0
        #Offset
        noise_texture_002.inputs[6].default_value = 0.0
        #Gain
        noise_texture_002.inputs[7].default_value = 1.0
        #Distortion
        noise_texture_002.inputs[8].default_value = 0.0
        
        #node Mix.002
        mix_002 = nt.nodes.new("ShaderNodeMix")
        mix_002.name = "Mix.002"
        mix_002.blend_type = 'ADD'
        mix_002.clamp_factor = True
        mix_002.clamp_result = False
        mix_002.data_type = 'RGBA'
        mix_002.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_002.inputs[0].default_value = 1.0
        #Factor_Vector
        mix_002.inputs[1].default_value = (0.5, 0.5, 0.5)
        #A_Float
        mix_002.inputs[2].default_value = 0.0
        #B_Float
        mix_002.inputs[3].default_value = 0.0
        #A_Vector
        mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
        #B_Vector
        mix_002.inputs[5].default_value = (0.0, 0.0, 0.0)
        #A_Rotation
        mix_002.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_002.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Noise Texture.003
        noise_texture_003 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_003.name = "Noise Texture.003"
        noise_texture_003.noise_dimensions = '3D'
        noise_texture_003.noise_type = 'FBM'
        noise_texture_003.normalize = True
        #W
        noise_texture_003.inputs[1].default_value = 0.0
        #Roughness
        noise_texture_003.inputs[4].default_value = 0.5
        #Lacunarity
        noise_texture_003.inputs[5].default_value = 2.0
        #Offset
        noise_texture_003.inputs[6].default_value = 0.0
        #Gain
        noise_texture_003.inputs[7].default_value = 1.0
        #Distortion
        noise_texture_003.inputs[8].default_value = 0.0
        
        
        #Set locations
        group_output.location = (676.7249145507812, -37.44478225708008)
        mix_005.location = (-199.799560546875, 131.4398193359375)
        group_input.location = (-1491.0665283203125, -412.4112548828125)
        reroute_003.location = (-476.3770446777344, -78.57305908203125)
        math_004.location = (-703.3331298828125, -156.88624572753906)
        mix_006.location = (-718.663330078125, 68.35282897949219)
        math_001.location = (-924.088134765625, 74.92439270019531)
        math.location = (-1123.8330078125, 0.37811279296875)
        texture_coordinate.location = (-1309.598876953125, 122.64407348632812)
        reroute.location = (-1152.595458984375, -245.2519989013672)
        math_003.location = (-921.2232666015625, -375.7601318359375)
        math_002.location = (26.031099319458008, -321.9505920410156)
        mix_004.location = (26.2509765625, -136.32623291015625)
        noise_texture_002.location = (-363.82275390625, 136.32623291015625)
        mix_002.location = (238.841552734375, -6.847412109375)
        noise_texture_003.location = (463.8226318359375, -40.54779052734375)
        
        #Set dimensions
        group_output.width, group_output.height = 140.0, 100.0
        mix_005.width, mix_005.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        reroute_003.width, reroute_003.height = 16.0, 100.0
        math_004.width, math_004.height = 140.0, 100.0
        mix_006.width, mix_006.height = 140.0, 100.0
        math_001.width, math_001.height = 140.0, 100.0
        math.width, math.height = 140.0, 100.0
        texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
        reroute.width, reroute.height = 16.0, 100.0
        math_003.width, math_003.height = 140.0, 100.0
        math_002.width, math_002.height = 140.0, 100.0
        mix_004.width, mix_004.height = 140.0, 100.0
        noise_texture_002.width, noise_texture_002.height = 140.0, 100.0
        mix_002.width, mix_002.height = 140.0, 100.0
        noise_texture_003.width, noise_texture_003.height = 140.0, 100.0
        
        #initialize nt links
        #reroute_003.Output -> noise_texture_002.Vector
        nt.links.new(reroute_003.outputs[0], noise_texture_002.inputs[0])
        #mix_002.Result -> noise_texture_003.Vector
        nt.links.new(mix_002.outputs[2], noise_texture_003.inputs[0])
        #noise_texture_002.Fac -> mix_005.A
        nt.links.new(noise_texture_002.outputs[0], mix_005.inputs[6])
        #mix_005.Result -> mix_004.A
        nt.links.new(mix_005.outputs[2], mix_004.inputs[6])
        #reroute_003.Output -> mix_002.A
        nt.links.new(reroute_003.outputs[0], mix_002.inputs[6])
        #mix_004.Result -> mix_002.B
        nt.links.new(mix_004.outputs[2], mix_002.inputs[7])
        #group_input.Detail 1 -> noise_texture_002.Detail
        nt.links.new(group_input.outputs[3], noise_texture_002.inputs[3])
        #group_input.Detail 2 -> noise_texture_003.Detail
        nt.links.new(group_input.outputs[4], noise_texture_003.inputs[3])
        #noise_texture_003.Color -> group_output.Color
        nt.links.new(noise_texture_003.outputs[1], group_output.inputs[0])
        #group_input.Distortion -> mix_004.B
        nt.links.new(group_input.outputs[5], mix_004.inputs[7])
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
        #mix_006.Result -> reroute_003.Input
        nt.links.new(mix_006.outputs[2], reroute_003.inputs[0])
        #group_input.Scale -> math_004.Value
        nt.links.new(group_input.outputs[1], math_004.inputs[0])
        #group_input.Scale Ratio -> math_003.Value
        nt.links.new(group_input.outputs[2], math_003.inputs[0])
        #math_002.Value -> noise_texture_003.Scale
        nt.links.new(math_002.outputs[0], noise_texture_003.inputs[2])
        #group_input.Scale -> math_002.Value
        nt.links.new(group_input.outputs[1], math_002.inputs[0])
        #noise_texture_003.Fac -> group_output.Fac
        nt.links.new(noise_texture_003.outputs[0], group_output.inputs[1])
        #math_003.Value -> math_002.Value
        nt.links.new(math_003.outputs[0], math_002.inputs[1])
        #math_004.Value -> noise_texture_002.Scale
        nt.links.new(math_004.outputs[0], noise_texture_002.inputs[2])
        #math_003.Value -> math_004.Value
        nt.links.new(math_003.outputs[0], math_004.inputs[1])