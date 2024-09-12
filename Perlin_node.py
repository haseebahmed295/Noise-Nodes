import bpy
from .utils import ShaderNode
class ShaderNodePerlin(ShaderNode):
    bl_name='Perlin Noise'
    bl_label='Perlin Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):        
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Scale'].default_value = 8
        self.inputs['Detail'].default_value = 10
        self.inputs['Dimension'].default_value = 0
        self.inputs['Lacunarity'].default_value = 2
        self.inputs['Offset'].default_value = 0
        self.inputs['Gain'].default_value = 60
        self.inputs['Min'].default_value = 0
        self.inputs['Max'].default_value = 1
        self.inputs['W'].hide = True

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
        
        nt.color_tag = 'NONE'
        nt.description = ""

        #nt interface
        #Socket 2 Vec
        _2_vec_socket = nt.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        _2_vec_socket.default_value = 0.0
        _2_vec_socket.min_value = -3.4028234663852886e+38
        _2_vec_socket.max_value = 3.4028234663852886e+38
        _2_vec_socket.subtype = 'NONE'
        _2_vec_socket.attribute_domain = 'POINT'
        
        #Socket Vector
        vector_socket = nt.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = -3.4028234663852886e+38
        vector_socket.max_value = 3.4028234663852886e+38
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
        detail_socket.default_value = 15.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 15.0
        detail_socket.subtype = 'NONE'
        detail_socket.attribute_domain = 'POINT'
        
        #Socket Dimension
        dimension_socket = nt.interface.new_socket(name = "Dimension", in_out='INPUT', socket_type = 'NodeSocketFloat')
        dimension_socket.default_value = 0.0
        dimension_socket.min_value = 0.0
        dimension_socket.max_value = 1000.0
        dimension_socket.subtype = 'NONE'
        dimension_socket.attribute_domain = 'POINT'
        
        #Socket Lacunarity
        lacunarity_socket = nt.interface.new_socket(name = "Lacunarity", in_out='INPUT', socket_type = 'NodeSocketFloat')
        lacunarity_socket.default_value = 2.0
        lacunarity_socket.min_value = 0.0
        lacunarity_socket.max_value = 1000.0
        lacunarity_socket.subtype = 'NONE'
        lacunarity_socket.attribute_domain = 'POINT'
        
        #Socket Offset
        offset_socket = nt.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
        offset_socket.default_value = 0.0
        offset_socket.min_value = -1000.0
        offset_socket.max_value = 1000.0
        offset_socket.subtype = 'NONE'
        offset_socket.attribute_domain = 'POINT'
        
        #Socket Gain
        gain_socket = nt.interface.new_socket(name = "Gain", in_out='INPUT', socket_type = 'NodeSocketFloat')
        gain_socket.default_value = 90.0
        gain_socket.min_value = 0.0
        gain_socket.max_value = 1000.0
        gain_socket.subtype = 'NONE'
        gain_socket.attribute_domain = 'POINT'
        
        #Socket Min
        min_socket = nt.interface.new_socket(name = "Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
        min_socket.default_value = 0.0
        min_socket.min_value = -10000.0
        min_socket.max_value = 10000.0
        min_socket.subtype = 'NONE'
        min_socket.attribute_domain = 'POINT'
        
        #Socket Max
        max_socket = nt.interface.new_socket(name = "Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
        max_socket.default_value = 1.0
        max_socket.min_value = -10000.0
        max_socket.max_value = 10000.0
        max_socket.subtype = 'NONE'
        max_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Musgrave Texture
        musgrave_texture = nt.nodes.new("ShaderNodeTexNoise")
        musgrave_texture.name = "Musgrave Texture"
        musgrave_texture.noise_dimensions = '3D'
        musgrave_texture.noise_type = 'RIDGED_MULTIFRACTAL'
        musgrave_texture.normalize = False
        #Distortion
        musgrave_texture.inputs[8].default_value = 0.0
        
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
        
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.hide = True
        math.operation = 'MINIMUM'
        math.use_clamp = False
        #Value_001
        math.inputs[1].default_value = 14.0
        
        #node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.hide = True
        math_001.operation = 'SUBTRACT'
        math_001.use_clamp = False
        
        #node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.hide = True
        math_002.operation = 'GREATER_THAN'
        math_002.use_clamp = False
        #Value_001
        math_002.inputs[1].default_value = 1.0
        
        #node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.hide = True
        math_003.operation = 'MAXIMUM'
        math_003.use_clamp = False
        #Value_001
        math_003.inputs[1].default_value = -9.999999747378752e-06
        
        #node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.hide = True
        math_004.operation = 'MULTIPLY'
        math_004.use_clamp = False
        #Value_001
        math_004.inputs[1].default_value = -1.0
        
        #node Math.005
        math_005 = nt.nodes.new("ShaderNodeMath")
        math_005.name = "Math.005"
        math_005.hide = True
        math_005.operation = 'POWER'
        math_005.use_clamp = False
        
        #node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.hide = True
        math_006.operation = 'MAXIMUM'
        math_006.use_clamp = False
        #Value_001
        math_006.inputs[1].default_value = -9.999999747378752e-06
        
        
        #Set locations
        group_output.location = (0.0, 0.0)
        group_input.location = (-771.8055419921875, 0.0)
        musgrave_texture.location = (-518.1944580078125, 0.0)
        map_range.location = (-253.61111450195312, 0.0)
        math.location = (-518.1944580078125, -320.0)
        math_001.location = (-518.1944580078125, -360.0)
        math_002.location = (-518.1944580078125, -400.0)
        math_003.location = (-518.1944580078125, -520.0)
        math_004.location = (-518.1944580078125, -480.0)
        math_005.location = (-518.1944580078125, -440.0)
        math_006.location = (-518.1944580078125, -560.0)
        
        #Set dimensions
        group_output.width, group_output.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        musgrave_texture.width, musgrave_texture.height = 150.0, 100.0
        map_range.width, map_range.height = 140.0, 100.0
        math.width, math.height = 140.0, 100.0
        math_001.width, math_001.height = 140.0, 100.0
        math_002.width, math_002.height = 140.0, 100.0
        math_003.width, math_003.height = 140.0, 100.0
        math_004.width, math_004.height = 140.0, 100.0
        math_005.width, math_005.height = 140.0, 100.0
        math_006.width, math_006.height = 140.0, 100.0
        
        #initialize nt links
        #musgrave_texture.Fac -> map_range.Value
        nt.links.new(musgrave_texture.outputs[0], map_range.inputs[0])
        #map_range.Result -> group_output.2 Vec
        nt.links.new(map_range.outputs[0], group_output.inputs[0])
        #group_input.Vector -> musgrave_texture.Vector
        nt.links.new(group_input.outputs[0], musgrave_texture.inputs[0])
        #group_input.W -> musgrave_texture.W
        nt.links.new(group_input.outputs[1], musgrave_texture.inputs[1])
        #group_input.Scale -> musgrave_texture.Scale
        nt.links.new(group_input.outputs[2], musgrave_texture.inputs[2])
        #group_input.Offset -> musgrave_texture.Offset
        nt.links.new(group_input.outputs[6], musgrave_texture.inputs[6])
        #group_input.Gain -> musgrave_texture.Gain
        nt.links.new(group_input.outputs[7], musgrave_texture.inputs[7])
        #group_input.Min -> map_range.From Min
        nt.links.new(group_input.outputs[8], map_range.inputs[1])
        #group_input.Max -> map_range.From Max
        nt.links.new(group_input.outputs[9], map_range.inputs[2])
        #group_input.Detail -> math_001.Value
        nt.links.new(group_input.outputs[3], math_001.inputs[0])
        #math_001.Value -> math.Value
        nt.links.new(math_001.outputs[0], math.inputs[0])
        #math.Value -> musgrave_texture.Detail
        nt.links.new(math.outputs[0], musgrave_texture.inputs[3])
        #group_input.Detail -> math_002.Value
        nt.links.new(group_input.outputs[3], math_002.inputs[0])
        #math_002.Value -> math_001.Value
        nt.links.new(math_002.outputs[0], math_001.inputs[1])
        #group_input.Dimension -> math_003.Value
        nt.links.new(group_input.outputs[4], math_003.inputs[0])
        #math_003.Value -> math_004.Value
        nt.links.new(math_003.outputs[0], math_004.inputs[0])
        #math_004.Value -> math_005.Value
        nt.links.new(math_004.outputs[0], math_005.inputs[1])
        #math_005.Value -> musgrave_texture.Roughness
        nt.links.new(math_005.outputs[0], musgrave_texture.inputs[4])
        #group_input.Lacunarity -> math_006.Value
        nt.links.new(group_input.outputs[5], math_006.inputs[0])
        #math_006.Value -> math_005.Value
        nt.links.new(math_006.outputs[0], math_005.inputs[0])
        #math_006.Value -> musgrave_texture.Lacunarity
        nt.links.new(math_006.outputs[0], musgrave_texture.inputs[5])
        return nt


