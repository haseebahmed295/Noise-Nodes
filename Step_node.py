import bpy
from .utils import ShaderNode
class ShaderNodeStep(ShaderNode):
    bl_name='Step Noise'
    bl_label='Step Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Scale'].default_value = 5
        self.inputs['Detail'].default_value = 0
        self.inputs['Distortion'].default_value = 0
        self.inputs['min'].default_value = 0
        self.inputs['max'].default_value = 1
        self.inputs['Steps'].default_value = 6
        self.inputs['W'].hide = True

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')

        
        nt.color_tag = 'NONE'
        nt.description = ""

        #nt interface
        #Socket Value
        value_socket = nt.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        value_socket.default_value = 0.0
        value_socket.min_value = 0.0
        value_socket.max_value = 0.0
        value_socket.subtype = 'NONE'
        value_socket.attribute_domain = 'POINT'
        
        #Socket Color
        color_socket = nt.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
        color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        color_socket.attribute_domain = 'POINT'
        
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
        scale_socket.default_value = 8.59999942779541
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
        
        #Socket min
        min_socket = nt.interface.new_socket(name = "min", in_out='INPUT', socket_type = 'NodeSocketFloat')
        min_socket.default_value = 0.0
        min_socket.min_value = 0.0
        min_socket.max_value = 1.0
        min_socket.subtype = 'NONE'
        min_socket.attribute_domain = 'POINT'
        
        #Socket max
        max_socket = nt.interface.new_socket(name = "max", in_out='INPUT', socket_type = 'NodeSocketFloat')
        max_socket.default_value = 1.0
        max_socket.min_value = 0.0
        max_socket.max_value = 1.0
        max_socket.subtype = 'NONE'
        max_socket.attribute_domain = 'POINT'
        
        #Socket Steps
        steps_socket = nt.interface.new_socket(name = "Steps", in_out='INPUT', socket_type = 'NodeSocketInt')
        steps_socket.default_value = 0
        steps_socket.min_value = -2147483648
        steps_socket.max_value = 2147483647
        steps_socket.subtype = 'NONE'
        steps_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Noise Texture.002
        noise_texture_002 = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture_002.name = "Noise Texture.002"
        noise_texture_002.noise_dimensions = '3D'
        noise_texture_002.noise_type = 'FBM'
        noise_texture_002.normalize = True
        #Roughness
        noise_texture_002.inputs[4].default_value = 0.6399999856948853
        #Lacunarity
        noise_texture_002.inputs[5].default_value = 2.0
        
        #node Map Range
        map_range = nt.nodes.new("ShaderNodeMapRange")
        map_range.name = "Map Range"
        map_range.clamp = True
        map_range.data_type = 'FLOAT'
        map_range.interpolation_type = 'STEPPED'
        #To Min
        map_range.inputs[3].default_value = 0.0
        #To Max
        map_range.inputs[4].default_value = 1.0
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
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
        
        #node Reroute.001
        reroute_001 = nt.nodes.new("NodeReroute")
        reroute_001.name = "Reroute.001"
        #node Reroute.002
        reroute_002 = nt.nodes.new("NodeReroute")
        reroute_002.name = "Reroute.002"
        #node Reroute.003
        reroute_003 = nt.nodes.new("NodeReroute")
        reroute_003.name = "Reroute.003"
        #node Map Range.002
        map_range_002 = nt.nodes.new("ShaderNodeMapRange")
        map_range_002.name = "Map Range.002"
        map_range_002.clamp = True
        map_range_002.data_type = 'FLOAT_VECTOR'
        map_range_002.interpolation_type = 'STEPPED'
        #To_Min_FLOAT3
        map_range_002.inputs[9].default_value = (0.0, 0.0, 0.0)
        #To_Max_FLOAT3
        map_range_002.inputs[10].default_value = (1.0, 1.0, 1.0)
        
        #node Reroute.004
        reroute_004 = nt.nodes.new("NodeReroute")
        reroute_004.name = "Reroute.004"
        #node Reroute.005
        reroute_005 = nt.nodes.new("NodeReroute")
        reroute_005.name = "Reroute.005"
        #node Reroute.006
        reroute_006 = nt.nodes.new("NodeReroute")
        reroute_006.name = "Reroute.006"
        
        #Set locations
        noise_texture_002.location = (-1431.6282958984375, 167.54891967773438)
        map_range.location = (-412.4046325683594, 246.48764038085938)
        group_input.location = (-2846.39208984375, -582.8417358398438)
        group_output.location = (697.471435546875, 18.066408157348633)
        math_016.location = (-1981.6282958984375, 167.54891967773438)
        math_022.location = (-2256.62841796875, 167.54891967773438)
        texture_coordinate_009.location = (-2770.266357421875, -11.848047256469727)
        reroute_007.location = (-2369.84130859375, -242.9477081298828)
        mix_015.location = (-1706.6282958984375, 167.54891967773438)
        reroute_001.location = (-1071.86328125, -529.1859130859375)
        reroute_002.location = (-1071.86328125, -565.1859130859375)
        reroute_003.location = (-1071.86328125, -601.1859130859375)
        map_range_002.location = (-403.24005126953125, -137.3367919921875)
        reroute_004.location = (-1708.7164306640625, -341.7425842285156)
        reroute_005.location = (-1708.7164306640625, -372.7425842285156)
        reroute_006.location = (-1708.7164306640625, -310.7425842285156)
        
        #Set dimensions
        noise_texture_002.width, noise_texture_002.height = 140.0, 100.0
        map_range.width, map_range.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0
        math_016.width, math_016.height = 140.0, 100.0
        math_022.width, math_022.height = 140.0, 100.0
        texture_coordinate_009.width, texture_coordinate_009.height = 140.0, 100.0
        reroute_007.width, reroute_007.height = 16.0, 100.0
        mix_015.width, mix_015.height = 140.0, 100.0
        reroute_001.width, reroute_001.height = 16.0, 100.0
        reroute_002.width, reroute_002.height = 16.0, 100.0
        reroute_003.width, reroute_003.height = 16.0, 100.0
        map_range_002.width, map_range_002.height = 140.0, 100.0
        reroute_004.width, reroute_004.height = 16.0, 100.0
        reroute_005.width, reroute_005.height = 16.0, 100.0
        reroute_006.width, reroute_006.height = 16.0, 100.0
        
        #initialize nt links
        #reroute_006.Output -> noise_texture_002.Scale
        nt.links.new(reroute_006.outputs[0], noise_texture_002.inputs[2])
        #reroute_004.Output -> noise_texture_002.Detail
        nt.links.new(reroute_004.outputs[0], noise_texture_002.inputs[3])
        #noise_texture_002.Fac -> map_range.Value
        nt.links.new(noise_texture_002.outputs[0], map_range.inputs[0])
        #reroute_003.Output -> map_range.Steps
        nt.links.new(reroute_003.outputs[0], map_range.inputs[5])
        #reroute_002.Output -> map_range.From Max
        nt.links.new(reroute_002.outputs[0], map_range.inputs[2])
        #map_range.Result -> group_output.Value
        nt.links.new(map_range.outputs[0], group_output.inputs[0])
        #reroute_007.Output -> mix_015.B
        nt.links.new(reroute_007.outputs[0], mix_015.inputs[7])
        #math_016.Value -> mix_015.Factor
        nt.links.new(math_016.outputs[0], mix_015.inputs[0])
        #math_022.Value -> math_016.Value
        nt.links.new(math_022.outputs[0], math_016.inputs[0])
        #reroute_007.Output -> math_022.Value
        nt.links.new(reroute_007.outputs[0], math_022.inputs[0])
        #texture_coordinate_009.Generated -> mix_015.A
        nt.links.new(texture_coordinate_009.outputs[0], mix_015.inputs[6])
        #group_input.Vector -> reroute_007.Input
        nt.links.new(group_input.outputs[0], reroute_007.inputs[0])
        #mix_015.Result -> noise_texture_002.Vector
        nt.links.new(mix_015.outputs[2], noise_texture_002.inputs[0])
        #reroute_001.Output -> map_range.From Min
        nt.links.new(reroute_001.outputs[0], map_range.inputs[1])
        #group_input.min -> reroute_001.Input
        nt.links.new(group_input.outputs[5], reroute_001.inputs[0])
        #group_input.max -> reroute_002.Input
        nt.links.new(group_input.outputs[6], reroute_002.inputs[0])
        #group_input.Steps -> reroute_003.Input
        nt.links.new(group_input.outputs[7], reroute_003.inputs[0])
        #reroute_003.Output -> map_range_002.Steps
        nt.links.new(reroute_003.outputs[0], map_range_002.inputs[5])
        #reroute_002.Output -> map_range_002.From Max
        nt.links.new(reroute_002.outputs[0], map_range_002.inputs[2])
        #reroute_001.Output -> map_range_002.From Min
        nt.links.new(reroute_001.outputs[0], map_range_002.inputs[1])
        #group_input.Detail -> reroute_004.Input
        nt.links.new(group_input.outputs[3], reroute_004.inputs[0])
        #group_input.Distortion -> reroute_005.Input
        nt.links.new(group_input.outputs[4], reroute_005.inputs[0])
        #group_input.Scale -> reroute_006.Input
        nt.links.new(group_input.outputs[2], reroute_006.inputs[0])
        #reroute_005.Output -> noise_texture_002.Distortion
        nt.links.new(reroute_005.outputs[0], noise_texture_002.inputs[8])
        #reroute_001.Output -> map_range_002.From Min
        nt.links.new(reroute_001.outputs[0], map_range_002.inputs[7])
        #reroute_002.Output -> map_range_002.From Max
        nt.links.new(reroute_002.outputs[0], map_range_002.inputs[8])
        #reroute_003.Output -> map_range_002.Steps
        nt.links.new(reroute_003.outputs[0], map_range_002.inputs[11])
        #noise_texture_002.Color -> map_range_002.Vector
        nt.links.new(noise_texture_002.outputs[1], map_range_002.inputs[6])
        #map_range_002.Vector -> group_output.Color
        nt.links.new(map_range_002.outputs[1], group_output.inputs[1])
        #group_input.W -> noise_texture_002.W
        nt.links.new(group_input.outputs[1], noise_texture_002.inputs[1])
        return nt


