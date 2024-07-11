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

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')

        self.addNode('NodeGroupInput', { 'name':'GroupInput'  })
        self.addNode('NodeGroupOutput', { 'name':'GroupOutput'  })

        separate_xyz = nt.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz.name = "Separate XYZ"
        
        #node Voronoi Texture.001
        voronoi_texture_001 = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture_001.name = "Voronoi Texture.001"
        voronoi_texture_001.distance = 'EUCLIDEAN'
        voronoi_texture_001.feature = 'F1'
        voronoi_texture_001.normalize = False
        voronoi_texture_001.voronoi_dimensions = '3D'
        #W
        voronoi_texture_001.inputs[1].default_value = 0.0
        #Detail
        voronoi_texture_001.inputs[3].default_value = 0.0
        #Roughness
        voronoi_texture_001.inputs[4].default_value = 0.5
        #Lacunarity
        voronoi_texture_001.inputs[5].default_value = 2.0
        #Smoothness
        voronoi_texture_001.inputs[6].default_value = 1.0
        #Exponent
        voronoi_texture_001.inputs[7].default_value = 0.5
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
        #Value_002
        math_030.inputs[2].default_value = 0.5
        
        #node Math.033
        math_033 = nt.nodes.new("ShaderNodeMath")
        math_033.name = "Math.033"
        math_033.hide = True
        math_033.operation = 'SUBTRACT'
        math_033.use_clamp = False
        #Value_002
        math_033.inputs[2].default_value = 0.5
        
        #node Math.032
        math_032 = nt.nodes.new("ShaderNodeMath")
        math_032.name = "Math.032"
        math_032.operation = 'DIVIDE'
        math_032.use_clamp = False
        #Value_002
        math_032.inputs[2].default_value = 0.5
        
        #node Math.034
        math_034 = nt.nodes.new("ShaderNodeMath")
        math_034.name = "Math.034"
        math_034.operation = 'MULTIPLY'
        math_034.use_clamp = False
        #Value_002
        math_034.inputs[2].default_value = 0.5
        
        #node Math.035
        math_035 = nt.nodes.new("ShaderNodeMath")
        math_035.name = "Math.035"
        math_035.hide = True
        math_035.operation = 'FRACT'
        math_035.use_clamp = False
        #Value_001
        math_035.inputs[1].default_value = 0.5
        #Value_002
        math_035.inputs[2].default_value = 0.5
        
        #node Math.036
        math_036 = nt.nodes.new("ShaderNodeMath")
        math_036.name = "Math.036"
        math_036.hide = True
        math_036.operation = 'SUBTRACT'
        math_036.use_clamp = False
        #Value_002
        math_036.inputs[2].default_value = 0.5
        
        #node Math.037
        math_037 = nt.nodes.new("ShaderNodeMath")
        math_037.name = "Math.037"
        math_037.operation = 'DIVIDE'
        math_037.use_clamp = False
        #Value_002
        math_037.inputs[2].default_value = 0.5
        
        #node Math.038
        math_038 = nt.nodes.new("ShaderNodeMath")
        math_038.name = "Math.038"
        math_038.operation = 'MULTIPLY'
        math_038.use_clamp = False
        #Value_002
        math_038.inputs[2].default_value = 0.5
        
        #node Math.039
        math_039 = nt.nodes.new("ShaderNodeMath")
        math_039.name = "Math.039"
        math_039.hide = True
        math_039.operation = 'FRACT'
        math_039.use_clamp = False
        #Value_001
        math_039.inputs[1].default_value = 0.5
        #Value_002
        math_039.inputs[2].default_value = 0.5
        
        #node Math.040
        math_040 = nt.nodes.new("ShaderNodeMath")
        math_040.name = "Math.040"
        math_040.hide = True
        math_040.operation = 'SUBTRACT'
        math_040.use_clamp = False
        #Value_002
        math_040.inputs[2].default_value = 0.5
        
        #node Math.041
        math_041 = nt.nodes.new("ShaderNodeMath")
        math_041.name = "Math.041"
        math_041.operation = 'DIVIDE'
        math_041.use_clamp = False
        #Value_002
        math_041.inputs[2].default_value = 0.5
        
        #node Reroute.002
        reroute_002 = nt.nodes.new("NodeReroute")
        reroute_002.name = "Reroute.002"
        #node Math.031
        math_031 = nt.nodes.new("ShaderNodeMath")
        math_031.name = "Math.031"
        math_031.hide = True
        math_031.operation = 'FRACT'
        math_031.use_clamp = False
        #Value_001
        math_031.inputs[1].default_value = 0.5
        #Value_002
        math_031.inputs[2].default_value = 0.5
        
        #node Combine XYZ.001
        combine_xyz_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz_001.name = "Combine XYZ.001"

        
        self.addSocket(False, 'NodeSocketVector', 'Vector').hide_value = True

        self.addSocket(False, 'NodeSocketFloat', 'Scale')

        self.addSocket(True, 'NodeSocketColor', 'Color')
        self.addSocket(True, 'NodeSocketFloat', 'Fac')
        self.addSocket(True, 'NodeSocketVector', 'Voxel Position')
        self.addSocket(True, 'NodeSocketVector', 'Voxel Vector')


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
        #voronoi_texture_001.Distance -> output_1.Input

        self.innerLink('nodes["GroupInput"].outputs[0]' , 'nodes["Reroute"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[1]' , 'nodes["Reroute.014"].inputs[0]')
        self.innerLink('nodes["Voronoi Texture.001"].outputs[1]' , 'nodes["GroupOutput"].inputs[0]')
        self.innerLink('nodes["Voronoi Texture.001"].outputs[0]' , 'nodes["GroupOutput"].inputs[1]')
        self.innerLink('nodes["Combine XYZ"].outputs[0]' , 'nodes["GroupOutput"].inputs[2]')
        self.innerLink('nodes["Combine XYZ.001"].outputs[0]' , 'nodes["GroupOutput"].inputs[3]')
