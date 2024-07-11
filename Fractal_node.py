import bpy
from .utils import ShaderNode
class ShaderNodeFractal(ShaderNode):
    bl_name='Fractal Noise'
    bl_label='Fractal Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Detail'].default_value = 1
        self.inputs['Scale'].default_value = 10
        self.inputs['Roughness'].default_value = 1
        self.inputs['Distortion'].default_value = 0.1
        self.inputs['From Max'].default_value = 1
        self.inputs['From Min'].default_value = 0.1

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
               #Socket Result
        result_socket = nt.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        result_socket.subtype = 'NONE'
        result_socket.default_value = 0.0
        result_socket.min_value = 0.0
        result_socket.max_value = 0.0
        result_socket.attribute_domain = 'POINT'
        
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
        detail_socket.default_value = 2.3999998569488525
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.attribute_domain = 'POINT'
        
        #Socket Roughness
        roughness_socket = nt.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
        roughness_socket.subtype = 'FACTOR'
        roughness_socket.default_value = 1.0
        roughness_socket.min_value = 0.0
        roughness_socket.max_value = 1.0
        roughness_socket.attribute_domain = 'POINT'
        
        #Socket Distortion
        distortion_socket = nt.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
        distortion_socket.subtype = 'NONE'
        distortion_socket.default_value = 1.0
        distortion_socket.min_value = -1000.0
        distortion_socket.max_value = 1000.0
        distortion_socket.attribute_domain = 'POINT'
        
        #Socket From Min
        from_min_socket = nt.interface.new_socket(name = "From Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
        from_min_socket.subtype = 'NONE'
        from_min_socket.default_value = 0.0
        from_min_socket.min_value = -10000.0
        from_min_socket.max_value = 10000.0
        from_min_socket.attribute_domain = 'POINT'
        
        #Socket From Max
        from_max_socket = nt.interface.new_socket(name = "From Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
        from_max_socket.subtype = 'NONE'
        from_max_socket.default_value = 1.0
        from_max_socket.min_value = -10000.0
        from_max_socket.max_value = 10000.0
        from_max_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Noise Texture.004
        noise_texture_004 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_004.name = "Noise Texture.004"
        noise_texture_004.noise_dimensions = '3D'
        noise_texture_004.noise_type = 'FBM'
        noise_texture_004.normalize = True
        #W
        noise_texture_004.inputs[1].default_value = 0.0
        #Lacunarity
        noise_texture_004.inputs[5].default_value = 2.0
        #Offset
        noise_texture_004.inputs[6].default_value = 0.0
        #Gain
        noise_texture_004.inputs[7].default_value = 1.0
        
        #node Separate HSV.001
        separate_hsv_001 = nt.nodes.new("ShaderNodeSeparateColor")
        separate_hsv_001.name = "Separate HSV.001"
        separate_hsv_001.mode = 'HSV'
        
        #node Map Range
        map_range = nt.nodes.new("ShaderNodeMapRange")
        map_range.name = "Map Range"
        map_range.clamp = True
        map_range.data_type = 'FLOAT'
        map_range.interpolation_type = 'LINEAR'
        #To Min
        map_range.inputs[3].default_value = 0.0
        #To Max
        map_range.inputs[4].default_value = 1.0
        #Steps
        map_range.inputs[5].default_value = 4.0
        #Vector
        map_range.inputs[6].default_value = (0.0, 0.0, 0.0)
        #From_Min_FLOAT3
        map_range.inputs[7].default_value = (0.0, 0.0, 0.0)
        #From_Max_FLOAT3
        map_range.inputs[8].default_value = (1.0, 1.0, 1.0)
        #To_Min_FLOAT3
        map_range.inputs[9].default_value = (0.0, 0.0, 0.0)
        #To_Max_FLOAT3
        map_range.inputs[10].default_value = (1.0, 1.0, 1.0)
        #Steps_FLOAT3
        map_range.inputs[11].default_value = (4.0, 4.0, 4.0)
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Clamp
        clamp = nt.nodes.new("ShaderNodeClamp")
        clamp.name = "Clamp"
        clamp.hide = True
        clamp.clamp_type = 'MINMAX'
        #Min
        clamp.inputs[1].default_value = 0.0
        #Max
        clamp.inputs[2].default_value = 1.0
        

        
        #initialize nt links
        #noise_texture_004.Color -> separate_hsv_001.Color
        nt.links.new(noise_texture_004.outputs[1], separate_hsv_001.inputs[0])
        #group_input.Vector -> noise_texture_004.Vector
        nt.links.new(group_input.outputs[0], noise_texture_004.inputs[0])
        #group_input.Scale -> noise_texture_004.Scale
        nt.links.new(group_input.outputs[1], noise_texture_004.inputs[2])
        #group_input.Detail -> noise_texture_004.Detail
        nt.links.new(group_input.outputs[2], noise_texture_004.inputs[3])
        #group_input.Distortion -> noise_texture_004.Distortion
        nt.links.new(group_input.outputs[4], noise_texture_004.inputs[8])
        #group_input.From Min -> map_range.From Min
        nt.links.new(group_input.outputs[5], map_range.inputs[1])
        #group_input.From Max -> map_range.From Max
        nt.links.new(group_input.outputs[6], map_range.inputs[2])
        #map_range.Result -> group_output.Result
        nt.links.new(map_range.outputs[0], group_output.inputs[0])
        #group_input.Roughness -> clamp.Value
        nt.links.new(group_input.outputs[3], clamp.inputs[0])
        #clamp.Result -> noise_texture_004.Roughness
        nt.links.new(clamp.outputs[0], noise_texture_004.inputs[4])
        #separate_hsv_001.Red -> map_range.Value
        nt.links.new(separate_hsv_001.outputs[0], map_range.inputs[0])


