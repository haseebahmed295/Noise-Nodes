import bpy
from .utils import ShaderNode
class ShaderNodeCranal(ShaderNode):
    bl_name='Cranal Noise'
    bl_label='Cranal Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Scale'].default_value = 5
        self.inputs['W'].hide = True

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')

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
        detail_socket.default_value = 0.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.subtype = 'NONE'
        detail_socket.attribute_domain = 'POINT'
        
        #Socket Distortion
        distortion_socket = nt.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
        distortion_socket.default_value = 0.0
        distortion_socket.min_value = -1000.0
        distortion_socket.max_value = 1000.0
        distortion_socket.subtype = 'NONE'
        distortion_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Separate RGB.002
        separate_rgb_002 = nt.nodes.new("ShaderNodeSeparateColor")
        separate_rgb_002.name = "Separate RGB.002"
        separate_rgb_002.mode = 'RGB'
        
        #node Math.018
        math_018 = nt.nodes.new("ShaderNodeMath")
        math_018.name = "Math.018"
        math_018.hide = True
        math_018.operation = 'ABSOLUTE'
        math_018.use_clamp = False
        
        #node Math.020
        math_020 = nt.nodes.new("ShaderNodeMath")
        math_020.name = "Math.020"
        math_020.hide = True
        math_020.operation = 'ABSOLUTE'
        math_020.use_clamp = False
        
        #node Math.019
        math_019 = nt.nodes.new("ShaderNodeMath")
        math_019.name = "Math.019"
        math_019.hide = True
        math_019.operation = 'ABSOLUTE'
        math_019.use_clamp = False
        
        #node Math.008
        math_008 = nt.nodes.new("ShaderNodeMath")
        math_008.name = "Math.008"
        math_008.hide = True
        math_008.operation = 'MULTIPLY'
        math_008.use_clamp = False
        
        #node Math.017
        math_017 = nt.nodes.new("ShaderNodeMath")
        math_017.name = "Math.017"
        math_017.hide = True
        math_017.operation = 'MULTIPLY'
        math_017.use_clamp = False
        
        #node Math.021
        math_021 = nt.nodes.new("ShaderNodeMath")
        math_021.name = "Math.021"
        math_021.hide = True
        math_021.operation = 'POWER'
        math_021.use_clamp = False
        #Value_001
        math_021.inputs[1].default_value = 0.20000000298023224
        
        #node Mix.006
        mix_006 = nt.nodes.new("ShaderNodeMix")
        mix_006.name = "Mix.006"
        mix_006.blend_type = 'SUBTRACT'
        mix_006.clamp_factor = True
        mix_006.clamp_result = False
        mix_006.data_type = 'RGBA'
        mix_006.factor_mode = 'UNIFORM'
        #Factor_Float
        mix_006.inputs[0].default_value = 1.0
        #B_Color
        mix_006.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        
        #node Noise Texture.006
        noise_texture_006 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_006.name = "Noise Texture.006"
        noise_texture_006.noise_dimensions = '3D'
        noise_texture_006.noise_type = 'FBM'
        noise_texture_006.normalize = True
        #Roughness
        noise_texture_006.inputs[4].default_value = 0.5
        #Lacunarity
        noise_texture_006.inputs[5].default_value = 2.0
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        
        #Set locations
        separate_rgb_002.location = (-30.37060546875, 42.99603271484375)
        math_018.location = (130.0, 30.0)
        math_020.location = (130.0, -10.0)
        math_019.location = (130.0, -50.0)
        math_008.location = (250.0, 10.0)
        math_017.location = (250.0, -30.0)
        math_021.location = (350.0, -10.0)
        mix_006.location = (-190.0, 50.0)
        noise_texture_006.location = (-350.0, 50.0)
        group_input.location = (-550.0, -0.0)
        group_output.location = (550.0, -0.0)
        
        #Set dimensions
        separate_rgb_002.width, separate_rgb_002.height = 140.0, 100.0
        math_018.width, math_018.height = 140.0, 100.0
        math_020.width, math_020.height = 140.0, 100.0
        math_019.width, math_019.height = 140.0, 100.0
        math_008.width, math_008.height = 140.0, 100.0
        math_017.width, math_017.height = 140.0, 100.0
        math_021.width, math_021.height = 140.0, 100.0
        mix_006.width, mix_006.height = 140.0, 100.0
        noise_texture_006.width, noise_texture_006.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0
        
        #initialize nt links
        #noise_texture_006.Color -> mix_006.A
        nt.links.new(noise_texture_006.outputs[1], mix_006.inputs[6])
        #separate_rgb_002.Red -> math_018.Value
        nt.links.new(separate_rgb_002.outputs[0], math_018.inputs[0])
        #mix_006.Result -> separate_rgb_002.Color
        nt.links.new(mix_006.outputs[2], separate_rgb_002.inputs[0])
        #math_008.Value -> math_017.Value
        nt.links.new(math_008.outputs[0], math_017.inputs[0])
        #separate_rgb_002.Green -> math_020.Value
        nt.links.new(separate_rgb_002.outputs[1], math_020.inputs[0])
        #separate_rgb_002.Blue -> math_019.Value
        nt.links.new(separate_rgb_002.outputs[2], math_019.inputs[0])
        #math_018.Value -> math_008.Value
        nt.links.new(math_018.outputs[0], math_008.inputs[0])
        #math_020.Value -> math_008.Value
        nt.links.new(math_020.outputs[0], math_008.inputs[1])
        #math_019.Value -> math_017.Value
        nt.links.new(math_019.outputs[0], math_017.inputs[1])
        #math_017.Value -> math_021.Value
        nt.links.new(math_017.outputs[0], math_021.inputs[0])
        #group_input.Vector -> noise_texture_006.Vector
        nt.links.new(group_input.outputs[0], noise_texture_006.inputs[0])
        #math_021.Value -> group_output.Value
        nt.links.new(math_021.outputs[0], group_output.inputs[0])
        #group_input.Scale -> noise_texture_006.Scale
        nt.links.new(group_input.outputs[2], noise_texture_006.inputs[2])
        #group_input.Detail -> noise_texture_006.Detail
        nt.links.new(group_input.outputs[3], noise_texture_006.inputs[3])
        #group_input.Distortion -> noise_texture_006.Distortion
        nt.links.new(group_input.outputs[4], noise_texture_006.inputs[8])
        #group_input.W -> noise_texture_006.W
        nt.links.new(group_input.outputs[1], noise_texture_006.inputs[1])
        return nt




