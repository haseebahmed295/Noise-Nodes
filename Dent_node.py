import bpy
from .utils import ShaderNode
class ShaderNodeDent(ShaderNode):
    bl_name='Dent Noise'
    bl_label='Dent Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Detail'].default_value = 0
        self.inputs['Scale'].default_value = 5
        self.inputs['Distortion'].default_value = 0

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
               #Socket Value
        value_socket = nt.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        value_socket.subtype = 'NONE'
        value_socket.default_value = 0.0
        value_socket.min_value = 0.0
        value_socket.max_value = 0.0
        value_socket.attribute_domain = 'POINT'
        
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
        
        #Socket Detail
        detail_socket = nt.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
        detail_socket.subtype = 'NONE'
        detail_socket.default_value = 0.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.attribute_domain = 'POINT'
        
        #Socket Distortion
        distortion_socket = nt.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
        distortion_socket.subtype = 'NONE'
        distortion_socket.default_value = 0.0
        distortion_socket.min_value = -1000.0
        distortion_socket.max_value = 1000.0
        distortion_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Noise Texture.008
        noise_texture_008 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_008.name = "Noise Texture.008"
        noise_texture_008.noise_dimensions = '3D'
        noise_texture_008.noise_type = 'FBM'
        noise_texture_008.normalize = True
        #W
        noise_texture_008.inputs[1].default_value = 0.0
        #Roughness
        noise_texture_008.inputs[4].default_value = 0.5
        #Lacunarity
        noise_texture_008.inputs[5].default_value = 2.0
        #Offset
        noise_texture_008.inputs[6].default_value = 0.0
        #Gain
        noise_texture_008.inputs[7].default_value = 1.0
        
        #node Mix.008
        mix_008 = nt.nodes.new("ShaderNodeMix")
        mix_008.name = "Mix.008"
        mix_008.blend_type = 'SUBTRACT'
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
        #B_Color
        mix_008.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        #A_Rotation
        mix_008.inputs[8].default_value = (0.0, 0.0, 0.0)
        #B_Rotation
        mix_008.inputs[9].default_value = (0.0, 0.0, 0.0)
        
        #node Separate RGB.003
        separate_rgb_003 = nt.nodes.new("ShaderNodeSeparateColor")
        separate_rgb_003.name = "Separate RGB.003"
        separate_rgb_003.mode = 'RGB'
        
        #node Math.058
        math_058 = nt.nodes.new("ShaderNodeMath")
        math_058.name = "Math.058"
        math_058.operation = 'MAXIMUM'
        math_058.use_clamp = False
        #Value_002
        math_058.inputs[2].default_value = 0.5
        
        #node Math.060
        math_060 = nt.nodes.new("ShaderNodeMath")
        math_060.name = "Math.060"
        math_060.operation = 'ABSOLUTE'
        math_060.use_clamp = False
        #Value_001
        math_060.inputs[1].default_value = 0.5
        #Value_002
        math_060.inputs[2].default_value = 0.5
        
        #node Math.061
        math_061 = nt.nodes.new("ShaderNodeMath")
        math_061.name = "Math.061"
        math_061.operation = 'ABSOLUTE'
        math_061.use_clamp = False
        #Value_001
        math_061.inputs[1].default_value = 0.5
        #Value_002
        math_061.inputs[2].default_value = 0.5
        
        #node Math.062
        math_062 = nt.nodes.new("ShaderNodeMath")
        math_062.name = "Math.062"
        math_062.operation = 'ABSOLUTE'
        math_062.use_clamp = False
        #Value_001
        math_062.inputs[1].default_value = 0.5
        #Value_002
        math_062.inputs[2].default_value = 0.5
        
        #node Math.063
        math_063 = nt.nodes.new("ShaderNodeMath")
        math_063.name = "Math.063"
        math_063.operation = 'MULTIPLY'
        math_063.use_clamp = False
        #Value_001
        math_063.inputs[1].default_value = 2.0
        #Value_002
        math_063.inputs[2].default_value = 0.5
        
        #node Math.064
        math_064 = nt.nodes.new("ShaderNodeMath")
        math_064.name = "Math.064"
        math_064.operation = 'MAXIMUM'
        math_064.use_clamp = False
        #Value_002
        math_064.inputs[2].default_value = 0.5
        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Math.065
        math_065 = nt.nodes.new("ShaderNodeMath")
        math_065.name = "Math.065"
        math_065.operation = 'POWER'
        math_065.use_clamp = False
        #Value_001
        math_065.inputs[1].default_value = 2.5
        #Value_002
        math_065.inputs[2].default_value = 0.5
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"

        
        #initialize nt links
        #noise_texture_008.Color -> mix_008.A
        nt.links.new(noise_texture_008.outputs[1], mix_008.inputs[6])
        #separate_rgb_003.Red -> math_060.Value
        nt.links.new(separate_rgb_003.outputs[0], math_060.inputs[0])
        #mix_008.Result -> separate_rgb_003.Color
        nt.links.new(mix_008.outputs[2], separate_rgb_003.inputs[0])
        #math_058.Value -> math_064.Value
        nt.links.new(math_058.outputs[0], math_064.inputs[0])
        #separate_rgb_003.Green -> math_062.Value
        nt.links.new(separate_rgb_003.outputs[1], math_062.inputs[0])
        #separate_rgb_003.Blue -> math_061.Value
        nt.links.new(separate_rgb_003.outputs[2], math_061.inputs[0])
        #math_064.Value -> math_063.Value
        nt.links.new(math_064.outputs[0], math_063.inputs[0])
        #math_060.Value -> math_058.Value
        nt.links.new(math_060.outputs[0], math_058.inputs[0])
        #math_062.Value -> math_058.Value
        nt.links.new(math_062.outputs[0], math_058.inputs[1])
        #math_061.Value -> math_064.Value
        nt.links.new(math_061.outputs[0], math_064.inputs[1])
        #math_063.Value -> math_065.Value
        nt.links.new(math_063.outputs[0], math_065.inputs[0])
        #group_input.Vector -> noise_texture_008.Vector
        nt.links.new(group_input.outputs[0], noise_texture_008.inputs[0])
        #group_input.Scale -> noise_texture_008.Scale
        nt.links.new(group_input.outputs[1], noise_texture_008.inputs[2])
        #math_065.Value -> group_output.Value
        nt.links.new(math_065.outputs[0], group_output.inputs[0])
        #group_input.Detail -> noise_texture_008.Detail
        nt.links.new(group_input.outputs[2], noise_texture_008.inputs[3])
        #group_input.Distortion -> noise_texture_008.Distortion
        nt.links.new(group_input.outputs[3], noise_texture_008.inputs[8])


