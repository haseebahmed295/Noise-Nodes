import bpy
from .utils import ShaderNode
class ShaderNodeVoxel(ShaderNode):
    bl_name='Voxel Noise'
    bl_label='Voxel Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')

        self.inputs['Scale'].default_value = 5
        self.inputs['W'].hide = True

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
	
        
        nt.color_tag = 'TEXTURE'
        nt.description = ""

        #nt interface
        #Socket Color
        color_socket = nt.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
        color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        color_socket.attribute_domain = 'POINT'
        
        #Socket Fac
        fac_socket = nt.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        fac_socket.default_value = 0.0
        fac_socket.min_value = -3.4028234663852886e+38
        fac_socket.max_value = 3.4028234663852886e+38
        fac_socket.subtype = 'NONE'
        fac_socket.attribute_domain = 'POINT'
        
        #Socket Voxel Position
        voxel_position_socket = nt.interface.new_socket(name = "Voxel Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
        voxel_position_socket.default_value = (0.0, 0.0, 0.0)
        voxel_position_socket.min_value = -3.4028234663852886e+38
        voxel_position_socket.max_value = 3.4028234663852886e+38
        voxel_position_socket.subtype = 'NONE'
        voxel_position_socket.attribute_domain = 'POINT'
        
        #Socket Voxel Vector
        voxel_vector_socket = nt.interface.new_socket(name = "Voxel Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
        voxel_vector_socket.default_value = (0.0, 0.0, 0.0)
        voxel_vector_socket.min_value = -3.4028234663852886e+38
        voxel_vector_socket.max_value = 3.4028234663852886e+38
        voxel_vector_socket.subtype = 'NONE'
        voxel_vector_socket.attribute_domain = 'POINT'
        
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
        w_socket.hide_value = False
        
        #Socket Scale
        scale_socket = nt.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
        scale_socket.default_value = 0.0
        scale_socket.min_value = -3.4028234663852886e+38
        scale_socket.max_value = 3.4028234663852886e+38
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node GroupInput
        groupinput = nt.nodes.new("NodeGroupInput")
        groupinput.name = "GroupInput"
        
        #node GroupOutput
        groupoutput = nt.nodes.new("NodeGroupOutput")
        groupoutput.name = "GroupOutput"
        groupoutput.is_active_output = True
        
        #node Separate XYZ
        separate_xyz = nt.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz.name = "Separate XYZ"
        
        #node Voronoi Texture.001
        voronoi_texture_001 = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture_001.name = "Voronoi Texture.001"
        voronoi_texture_001.distance = 'EUCLIDEAN'
        voronoi_texture_001.feature = 'F1'
        voronoi_texture_001.normalize = False
        voronoi_texture_001.voronoi_dimensions = '3D'
        #Detail
        voronoi_texture_001.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture_001.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture_001.inputs[5].default_value = 2.0
        #Randomness
        voronoi_texture_001.inputs[8].default_value = 1.0
        
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
        
        #node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.operation = 'GREATER_THAN'
        math_001.use_clamp = False
        #Value_001
        math_001.inputs[1].default_value = 0.0
        
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.operation = 'ABSOLUTE'
        math.use_clamp = False
        
        #node Texture Coordinate
        texture_coordinate = nt.nodes.new("ShaderNodeTexCoord")
        texture_coordinate.name = "Texture Coordinate"
        texture_coordinate.from_instancer = False
        
        #node Reroute.014
        reroute_014 = nt.nodes.new("NodeReroute")
        reroute_014.name = "Reroute.014"
        #node Combine XYZ
        combine_xyz = nt.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz.name = "Combine XYZ"
        
        #node Reroute.001
        reroute_001 = nt.nodes.new("NodeReroute")
        reroute_001.name = "Reroute.001"
        #node Math.030
        math_030 = nt.nodes.new("ShaderNodeMath")
        math_030.name = "Math.030"
        math_030.operation = 'MULTIPLY'
        math_030.use_clamp = False
        
        #node Math.033
        math_033 = nt.nodes.new("ShaderNodeMath")
        math_033.name = "Math.033"
        math_033.hide = True
        math_033.operation = 'SUBTRACT'
        math_033.use_clamp = False
        
        #node Math.032
        math_032 = nt.nodes.new("ShaderNodeMath")
        math_032.name = "Math.032"
        math_032.operation = 'DIVIDE'
        math_032.use_clamp = False
        
        #node Math.034
        math_034 = nt.nodes.new("ShaderNodeMath")
        math_034.name = "Math.034"
        math_034.operation = 'MULTIPLY'
        math_034.use_clamp = False
        
        #node Math.035
        math_035 = nt.nodes.new("ShaderNodeMath")
        math_035.name = "Math.035"
        math_035.hide = True
        math_035.operation = 'FRACT'
        math_035.use_clamp = False
        
        #node Math.036
        math_036 = nt.nodes.new("ShaderNodeMath")
        math_036.name = "Math.036"
        math_036.hide = True
        math_036.operation = 'SUBTRACT'
        math_036.use_clamp = False
        
        #node Math.037
        math_037 = nt.nodes.new("ShaderNodeMath")
        math_037.name = "Math.037"
        math_037.operation = 'DIVIDE'
        math_037.use_clamp = False
        
        #node Math.038
        math_038 = nt.nodes.new("ShaderNodeMath")
        math_038.name = "Math.038"
        math_038.operation = 'MULTIPLY'
        math_038.use_clamp = False
        
        #node Math.039
        math_039 = nt.nodes.new("ShaderNodeMath")
        math_039.name = "Math.039"
        math_039.hide = True
        math_039.operation = 'FRACT'
        math_039.use_clamp = False
        
        #node Math.040
        math_040 = nt.nodes.new("ShaderNodeMath")
        math_040.name = "Math.040"
        math_040.hide = True
        math_040.operation = 'SUBTRACT'
        math_040.use_clamp = False
        
        #node Math.041
        math_041 = nt.nodes.new("ShaderNodeMath")
        math_041.name = "Math.041"
        math_041.operation = 'DIVIDE'
        math_041.use_clamp = False
        
        #node Reroute.002
        reroute_002 = nt.nodes.new("NodeReroute")
        reroute_002.name = "Reroute.002"
        #node Math.031
        math_031 = nt.nodes.new("ShaderNodeMath")
        math_031.name = "Math.031"
        math_031.hide = True
        math_031.operation = 'FRACT'
        math_031.use_clamp = False
        
        #node Combine XYZ.001
        combine_xyz_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz_001.name = "Combine XYZ.001"
        
        
        #Set locations
        groupinput.location = (-2318.0, 0.0)
        groupoutput.location = (0.0, 0.0)
        separate_xyz.location = (-1470.0, 0.0)
        voronoi_texture_001.location = (-210.0, 0.0)
        reroute.location = (-2143.0, -35.0)
        mix_006.location = (-1680.0, 0.0)
        math_001.location = (-1890.0, 0.0)
        math.location = (-2100.0, 0.0)
        texture_coordinate.location = (-1890.0, -293.20001220703125)
        reroute_014.location = (-1929.0, -57.0)
        combine_xyz.location = (-420.0, 0.0)
        reroute_001.location = (-1719.0, -57.0)
        math_030.location = (-1260.0, 0.0)
        math_033.location = (-840.0, -5.0)
        math_032.location = (-630.0, 0.0)
        math_034.location = (-1260.0, -434.3999938964844)
        math_035.location = (-1050.0, -438.370361328125)
        math_036.location = (-840.0, -431.1111145019531)
        math_037.location = (-630.0, -434.3999938964844)
        math_038.location = (-1260.0, -217.1999969482422)
        math_039.location = (-1050.0, -303.0617370605469)
        math_040.location = (-840.0, -242.3851776123047)
        math_041.location = (-630.0, -217.1999969482422)
        reroute_002.location = (-1299.0, -132.35000610351562)
        math_031.location = (-1050.0, -5.0)
        combine_xyz_001.location = (-210.0, -439.6000061035156)
        
        #Set dimensions
        groupinput.width, groupinput.height = 140.0, 100.0
        groupoutput.width, groupoutput.height = 140.0, 100.0
        separate_xyz.width, separate_xyz.height = 140.0, 100.0
        voronoi_texture_001.width, voronoi_texture_001.height = 140.0, 100.0
        reroute.width, reroute.height = 16.0, 100.0
        mix_006.width, mix_006.height = 140.0, 100.0
        math_001.width, math_001.height = 140.0, 100.0
        math.width, math.height = 140.0, 100.0
        texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
        reroute_014.width, reroute_014.height = 16.0, 100.0
        combine_xyz.width, combine_xyz.height = 140.0, 100.0
        reroute_001.width, reroute_001.height = 16.0, 100.0
        math_030.width, math_030.height = 140.0, 100.0
        math_033.width, math_033.height = 140.0, 100.0
        math_032.width, math_032.height = 140.0, 100.0
        math_034.width, math_034.height = 140.0, 100.0
        math_035.width, math_035.height = 140.0, 100.0
        math_036.width, math_036.height = 140.0, 100.0
        math_037.width, math_037.height = 140.0, 100.0
        math_038.width, math_038.height = 140.0, 100.0
        math_039.width, math_039.height = 140.0, 100.0
        math_040.width, math_040.height = 140.0, 100.0
        math_041.width, math_041.height = 140.0, 100.0
        reroute_002.width, reroute_002.height = 16.0, 100.0
        math_031.width, math_031.height = 140.0, 100.0
        combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
        
        #initialize nt links
        #combine_xyz.Vector -> voronoi_texture_001.Vector
        nt.links.new(combine_xyz.outputs[0], voronoi_texture_001.inputs[0])
        #reroute_014.Output -> voronoi_texture_001.Scale
        nt.links.new(reroute_014.outputs[0], voronoi_texture_001.inputs[2])
        #math_001.Value -> mix_006.Factor
        nt.links.new(math_001.outputs[0], mix_006.inputs[0])
        #math.Value -> math_001.Value
        nt.links.new(math.outputs[0], math_001.inputs[0])
        #reroute.Output -> math.Value
        nt.links.new(reroute.outputs[0], math.inputs[0])
        #mix_006.Result -> separate_xyz.Vector
        nt.links.new(mix_006.outputs[2], separate_xyz.inputs[0])
        #reroute_014.Output -> reroute_001.Input
        nt.links.new(reroute_014.outputs[0], reroute_001.inputs[0])
        #reroute_002.Output -> math_030.Value
        nt.links.new(reroute_002.outputs[0], math_030.inputs[1])
        #separate_xyz.X -> math_030.Value
        nt.links.new(separate_xyz.outputs[0], math_030.inputs[0])
        #reroute_001.Output -> reroute_002.Input
        nt.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
        #reroute_002.Output -> math_032.Value
        nt.links.new(reroute_002.outputs[0], math_032.inputs[1])
        #math_032.Value -> combine_xyz.X
        nt.links.new(math_032.outputs[0], combine_xyz.inputs[0])
        #math_030.Value -> math_031.Value
        nt.links.new(math_030.outputs[0], math_031.inputs[0])
        #math_031.Value -> math_033.Value
        nt.links.new(math_031.outputs[0], math_033.inputs[1])
        #math_033.Value -> math_032.Value
        nt.links.new(math_033.outputs[0], math_032.inputs[0])
        #math_030.Value -> math_033.Value
        nt.links.new(math_030.outputs[0], math_033.inputs[0])
        #math_034.Value -> math_035.Value
        nt.links.new(math_034.outputs[0], math_035.inputs[0])
        #math_035.Value -> math_036.Value
        nt.links.new(math_035.outputs[0], math_036.inputs[1])
        #math_036.Value -> math_037.Value
        nt.links.new(math_036.outputs[0], math_037.inputs[0])
        #math_034.Value -> math_036.Value
        nt.links.new(math_034.outputs[0], math_036.inputs[0])
        #math_038.Value -> math_039.Value
        nt.links.new(math_038.outputs[0], math_039.inputs[0])
        #math_039.Value -> math_040.Value
        nt.links.new(math_039.outputs[0], math_040.inputs[1])
        #math_040.Value -> math_041.Value
        nt.links.new(math_040.outputs[0], math_041.inputs[0])
        #math_038.Value -> math_040.Value
        nt.links.new(math_038.outputs[0], math_040.inputs[0])
        #separate_xyz.Y -> math_038.Value
        nt.links.new(separate_xyz.outputs[1], math_038.inputs[0])
        #reroute_002.Output -> math_038.Value
        nt.links.new(reroute_002.outputs[0], math_038.inputs[1])
        #reroute_002.Output -> math_034.Value
        nt.links.new(reroute_002.outputs[0], math_034.inputs[1])
        #reroute_002.Output -> math_037.Value
        nt.links.new(reroute_002.outputs[0], math_037.inputs[1])
        #reroute_002.Output -> math_041.Value
        nt.links.new(reroute_002.outputs[0], math_041.inputs[1])
        #separate_xyz.Z -> math_034.Value
        nt.links.new(separate_xyz.outputs[2], math_034.inputs[0])
        #math_037.Value -> combine_xyz.Z
        nt.links.new(math_037.outputs[0], combine_xyz.inputs[2])
        #math_041.Value -> combine_xyz.Y
        nt.links.new(math_041.outputs[0], combine_xyz.inputs[1])
        #math_031.Value -> combine_xyz_001.X
        nt.links.new(math_031.outputs[0], combine_xyz_001.inputs[0])
        #math_039.Value -> combine_xyz_001.Y
        nt.links.new(math_039.outputs[0], combine_xyz_001.inputs[1])
        #math_035.Value -> combine_xyz_001.Z
        nt.links.new(math_035.outputs[0], combine_xyz_001.inputs[2])
        #reroute.Output -> mix_006.B
        nt.links.new(reroute.outputs[0], mix_006.inputs[7])
        #texture_coordinate.Generated -> mix_006.A
        nt.links.new(texture_coordinate.outputs[0], mix_006.inputs[6])
        #groupinput.Vector -> reroute.Input
        nt.links.new(groupinput.outputs[0], reroute.inputs[0])
        #groupinput.Scale -> reroute_014.Input
        nt.links.new(groupinput.outputs[2], reroute_014.inputs[0])
        #voronoi_texture_001.Color -> groupoutput.Color
        nt.links.new(voronoi_texture_001.outputs[1], groupoutput.inputs[0])
        #voronoi_texture_001.Distance -> groupoutput.Fac
        nt.links.new(voronoi_texture_001.outputs[0], groupoutput.inputs[1])
        #combine_xyz.Vector -> groupoutput.Voxel Position
        nt.links.new(combine_xyz.outputs[0], groupoutput.inputs[2])
        #combine_xyz_001.Vector -> groupoutput.Voxel Vector
        nt.links.new(combine_xyz_001.outputs[0], groupoutput.inputs[3])
        #groupinput.W -> voronoi_texture_001.W
        nt.links.new(groupinput.outputs[1], voronoi_texture_001.inputs[1])
        return nt