import bpy
from .utils import ShaderNode
class ShaderNodeRegular(ShaderNode):
    bl_name='Regular Noise'
    bl_label='Regular Noise'
    bl_icon='NONE'
 
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Scale'].default_value = 5
        self.inputs['Fix Range'].default_value = 1
        self.inputs['Detail'].default_value = 5
        self.inputs['W'].hide = True

    def createNodetree(self, name):
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
        detail_socket.default_value = 5.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.subtype = 'NONE'
        detail_socket.attribute_domain = 'POINT'
        
        #Socket Fix Range
        fix_range_socket = nt.interface.new_socket(name = "Fix Range", in_out='INPUT', socket_type = 'NodeSocketFloat')
        fix_range_socket.default_value = 1.0
        fix_range_socket.min_value = 0.0
        fix_range_socket.max_value = 1.0
        fix_range_socket.subtype = 'NONE'
        fix_range_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.operation = 'ADD'
        math.use_clamp = False
        
        #node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.operation = 'MULTIPLY'
        math_003.use_clamp = False
        #Value_001
        math_003.inputs[1].default_value = 7.0
        
        #node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.operation = 'ADD'
        math_004.use_clamp = False
        #Value_001
        math_004.inputs[1].default_value = 1.0
        
        #node Reroute
        reroute = nt.nodes.new("NodeReroute")
        reroute.name = "Reroute"
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.operation = 'DIVIDE'
        math_001.use_clamp = False
        
        #node Musgrave Texture
        musgrave_texture = nt.nodes.new("ShaderNodeTexNoise")
        musgrave_texture.name = "Musgrave Texture"
        musgrave_texture.noise_dimensions = '3D'
        musgrave_texture.noise_type = 'FBM'
        musgrave_texture.normalize = False
        #Roughness
        musgrave_texture.inputs[4].default_value = 0.999993085861206
        #Lacunarity
        musgrave_texture.inputs[5].default_value = 2.0
        #Distortion
        musgrave_texture.inputs[8].default_value = 0.0
        
        #node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.operation = 'MULTIPLY'
        math_002.use_clamp = False
        #Value_001
        math_002.inputs[1].default_value = 4.0
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Math.005
        math_005 = nt.nodes.new("ShaderNodeMath")
        math_005.name = "Math.005"
        math_005.hide = True
        math_005.operation = 'MINIMUM'
        math_005.use_clamp = False
        #Value_001
        math_005.inputs[1].default_value = 14.0
        
        #node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.hide = True
        math_006.operation = 'SUBTRACT'
        math_006.use_clamp = False
        #Value_001
        math_006.inputs[1].default_value = 1.0
        
        #node Clamp
        clamp = nt.nodes.new("ShaderNodeClamp")
        clamp.name = "Clamp"
        clamp.hide = True
        clamp.clamp_type = 'MINMAX'
        #Min
        clamp.inputs[1].default_value = 0.0
        #Max
        clamp.inputs[2].default_value = 1.0
        
        #node Math.007
        math_007 = nt.nodes.new("ShaderNodeMath")
        math_007.name = "Math.007"
        math_007.hide = True
        math_007.operation = 'MULTIPLY'
        math_007.use_clamp = False
        
        
        #Set locations
        math.location = (-420.0, 0.0)
        math_003.location = (-630.0, -312.20001220703125)
        math_004.location = (-420.0, -312.20001220703125)
        reroute.location = (-879.0, -236.94166564941406)
        group_output.location = (0.0, 0.0)
        math_001.location = (-210.0, 0.0)
        musgrave_texture.location = (-840.0, 0.0)
        math_002.location = (-630.0, -95.0)
        group_input.location = (-1470.0, -135.94166564941406)
        math_005.location = (-1050.0, -65.05000305175781)
        math_006.location = (-1260.0, -65.05000305175781)
        clamp.location = (-840.0, -353.3999938964844)
        math_007.location = (-630.0, 0.0)
        
        #Set dimensions
        math.width, math.height = 140.0, 100.0
        math_003.width, math_003.height = 140.0, 100.0
        math_004.width, math_004.height = 140.0, 100.0
        reroute.width, reroute.height = 16.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0
        math_001.width, math_001.height = 140.0, 100.0
        musgrave_texture.width, musgrave_texture.height = 140.0, 100.0
        math_002.width, math_002.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        math_005.width, math_005.height = 140.0, 100.0
        math_006.width, math_006.height = 140.0, 100.0
        clamp.width, clamp.height = 140.0, 100.0
        math_007.width, math_007.height = 140.0, 100.0
        
        #initialize nt links
        #math.Value -> math_001.Value
        nt.links.new(math.outputs[0], math_001.inputs[0])
        #math_001.Value -> group_output.Value
        nt.links.new(math_001.outputs[0], group_output.inputs[0])
        #reroute.Output -> math_002.Value
        nt.links.new(reroute.outputs[0], math_002.inputs[0])
        #reroute.Output -> math_003.Value
        nt.links.new(reroute.outputs[0], math_003.inputs[0])
        #math_002.Value -> math.Value
        nt.links.new(math_002.outputs[0], math.inputs[1])
        #math_003.Value -> math_004.Value
        nt.links.new(math_003.outputs[0], math_004.inputs[0])
        #math_004.Value -> math_001.Value
        nt.links.new(math_004.outputs[0], math_001.inputs[1])
        #group_input.Fix Range -> reroute.Input
        nt.links.new(group_input.outputs[4], reroute.inputs[0])
        #group_input.Vector -> musgrave_texture.Vector
        nt.links.new(group_input.outputs[0], musgrave_texture.inputs[0])
        #group_input.Scale -> musgrave_texture.Scale
        nt.links.new(group_input.outputs[2], musgrave_texture.inputs[2])
        #group_input.Detail -> math_006.Value
        nt.links.new(group_input.outputs[3], math_006.inputs[0])
        #math_006.Value -> math_005.Value
        nt.links.new(math_006.outputs[0], math_005.inputs[0])
        #math_005.Value -> musgrave_texture.Detail
        nt.links.new(math_005.outputs[0], musgrave_texture.inputs[3])
        #math_007.Value -> math.Value
        nt.links.new(math_007.outputs[0], math.inputs[0])
        #musgrave_texture.Fac -> math_007.Value
        nt.links.new(musgrave_texture.outputs[0], math_007.inputs[0])
        #group_input.Detail -> clamp.Value
        nt.links.new(group_input.outputs[3], clamp.inputs[0])
        #clamp.Result -> math_007.Value
        nt.links.new(clamp.outputs[0], math_007.inputs[1])
        #group_input.W -> musgrave_texture.W
        nt.links.new(group_input.outputs[1], musgrave_texture.inputs[1])
        return nt

