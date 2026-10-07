
import bpy
from ..utils import ShaderNode


class ShaderNodeCellular(ShaderNode):
    bl_label = "Cellular Noise"
    bl_icon = "NONE"

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + "_node_tree")
        self.inputs["W"].hide = True
        

    def createNodetree(self, name):
        """Initialize Noise node group"""
        nt = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = name)

        nt.color_tag = 'TEXTURE'
        nt.description = ""
        nt.default_group_node_width = 140
        # cellular_noise_1 interface

        # Socket Factor
        factor_socket = nt.interface.new_socket(name="Factor", in_out='OUTPUT', socket_type='NodeSocketFloat')
        factor_socket.default_value = 0.0
        factor_socket.min_value = -3.4028234663852886e+38
        factor_socket.max_value = 3.4028234663852886e+38
        factor_socket.subtype = 'NONE'
        factor_socket.attribute_domain = 'POINT'
        factor_socket.default_input = 'VALUE'
        factor_socket.structure_type = 'AUTO'

        # Socket Border
        border_socket = nt.interface.new_socket(name="Border", in_out='OUTPUT', socket_type='NodeSocketFloat')
        border_socket.default_value = 0.0
        border_socket.min_value = -3.4028234663852886e+38
        border_socket.max_value = 3.4028234663852886e+38
        border_socket.subtype = 'NONE'
        border_socket.attribute_domain = 'POINT'
        border_socket.default_input = 'VALUE'
        border_socket.structure_type = 'AUTO'

        # Socket Color
        color_socket = nt.interface.new_socket(name="Color", in_out='OUTPUT', socket_type='NodeSocketColor')
        color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        color_socket.attribute_domain = 'POINT'
        color_socket.default_input = 'VALUE'
        color_socket.structure_type = 'AUTO'

        # Socket Position
        position_socket = nt.interface.new_socket(name="Position", in_out='OUTPUT', socket_type='NodeSocketVector')
        position_socket.default_value = (0.0, 0.0, 0.0)
        position_socket.min_value = -3.4028234663852886e+38
        position_socket.max_value = 3.4028234663852886e+38
        position_socket.subtype = 'NONE'
        position_socket.attribute_domain = 'POINT'
        position_socket.default_input = 'VALUE'
        position_socket.structure_type = 'AUTO'

        # Socket Vector
        vector_socket = nt.interface.new_socket(name="Vector", in_out='INPUT', socket_type='NodeSocketVector')
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = -3.4028234663852886e+38
        vector_socket.max_value = 3.4028234663852886e+38
        vector_socket.subtype = 'XYZ'
        vector_socket.attribute_domain = 'POINT'
        vector_socket.hide_value = True
        vector_socket.structure_type = 'AUTO'

        # Socket W
        w_socket = nt.interface.new_socket(name="W", in_out='INPUT', socket_type='NodeSocketFloat')
        w_socket.default_value = 1.0
        w_socket.min_value = -1000.0
        w_socket.max_value = 1000.0
        w_socket.subtype = 'NONE'
        w_socket.attribute_domain = 'POINT'
        w_socket.default_input = 'VALUE'
        w_socket.structure_type = 'AUTO'

        # Socket Scale
        scale_socket = nt.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
        scale_socket.default_value = 5.0
        scale_socket.min_value = 0.0
        scale_socket.max_value = 1000.0
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        scale_socket.default_input = 'VALUE'
        scale_socket.structure_type = 'AUTO'

        # Socket Distortion
        distortion_socket = nt.interface.new_socket(name="Distortion", in_out='INPUT', socket_type='NodeSocketFloat')
        distortion_socket.default_value = 0.0
        distortion_socket.min_value = 0.0
        distortion_socket.max_value = 10.0
        distortion_socket.subtype = 'NONE'
        distortion_socket.attribute_domain = 'POINT'
        distortion_socket.default_input = 'VALUE'
        distortion_socket.structure_type = 'AUTO'

        # Socket Randomness
        randomness_socket = nt.interface.new_socket(name="Randomness", in_out='INPUT', socket_type='NodeSocketFloat')
        randomness_socket.default_value = 0.5
        randomness_socket.min_value = 0.0
        randomness_socket.max_value = 1.0
        randomness_socket.subtype = 'FACTOR'
        randomness_socket.attribute_domain = 'POINT'
        randomness_socket.default_input = 'VALUE'
        randomness_socket.structure_type = 'AUTO'

        # Socket Border Width
        border_width_socket = nt.interface.new_socket(name="Border Width", in_out='INPUT', socket_type='NodeSocketFloat')
        border_width_socket.default_value = 0.019999999552965164
        border_width_socket.min_value = 0.0
        border_width_socket.max_value = 2.0
        border_width_socket.subtype = 'NONE'
        border_width_socket.attribute_domain = 'POINT'
        border_width_socket.default_input = 'VALUE'
        border_width_socket.structure_type = 'AUTO'

        # Socket Smothness
        smothness_socket = nt.interface.new_socket(name="Smothness", in_out='INPUT', socket_type='NodeSocketFloat')
        smothness_socket.default_value = 0.0
        smothness_socket.min_value = 0.0
        smothness_socket.max_value = 2.0
        smothness_socket.subtype = 'NONE'
        smothness_socket.attribute_domain = 'POINT'
        smothness_socket.default_input = 'VALUE'
        smothness_socket.structure_type = 'AUTO'

        # Initialize cellular_noise_1 nodes

        # Node Voronoi Texture
        voronoi_texture = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture.name = "Voronoi Texture"
        voronoi_texture.show_options = True
        voronoi_texture.show_texture = True
        voronoi_texture.distance = 'EUCLIDEAN'
        voronoi_texture.feature = 'F1'
        voronoi_texture.normalize = False
        voronoi_texture.voronoi_dimensions = '4D'
        # Detail
        voronoi_texture.inputs[3].default_value = 0.0
        # Roughness
        voronoi_texture.inputs[4].default_value = 0.5
        # Lacunarity
        voronoi_texture.inputs[5].default_value = 2.0
        # Smoothness
        voronoi_texture.inputs[6].default_value = 1.0
        # Exponent
        voronoi_texture.inputs[7].default_value = 0.5

        # Node Voronoi Texture.001
        voronoi_texture_001 = nt.nodes.new("ShaderNodeTexVoronoi")
        voronoi_texture_001.name = "Voronoi Texture.001"
        voronoi_texture_001.show_options = True
        voronoi_texture_001.distance = 'EUCLIDEAN'
        voronoi_texture_001.feature = 'F2'
        voronoi_texture_001.normalize = False
        voronoi_texture_001.voronoi_dimensions = '4D'
        # Detail
        voronoi_texture_001.inputs[3].default_value = 0.0
        # Roughness
        voronoi_texture_001.inputs[4].default_value = 0.5
        # Lacunarity
        voronoi_texture_001.inputs[5].default_value = 2.0
        # Smoothness
        voronoi_texture_001.inputs[6].default_value = 1.0
        # Exponent
        voronoi_texture_001.inputs[7].default_value = 0.5

        # Node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.show_options = True
        math.operation = 'SUBTRACT'
        math.use_clamp = False
        # Value_002
        math.inputs[2].default_value = 0.5

        # Node Noise Texture
        noise_texture = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture.name = "Noise Texture"
        noise_texture.show_options = True
        noise_texture.noise_dimensions = '4D'
        noise_texture.noise_type = 'FBM'
        noise_texture.normalize = True
        # Scale
        noise_texture.inputs[2].default_value = 5.0
        # Detail
        noise_texture.inputs[3].default_value = 2.0
        # Roughness
        noise_texture.inputs[4].default_value = 0.5
        # Lacunarity
        noise_texture.inputs[5].default_value = 2.0
        # Offset
        noise_texture.inputs[6].default_value = 0.0
        # Gain
        noise_texture.inputs[7].default_value = 1.0
        # Distortion
        noise_texture.inputs[8].default_value = 0.0

        # Node Vector Math
        vector_math = nt.nodes.new("ShaderNodeVectorMath")
        vector_math.name = "Vector Math"
        vector_math.show_options = True
        vector_math.operation = 'ADD'
        # Vector_002
        vector_math.inputs[2].default_value = (0.0, 0.0, 0.0)
        # Scale
        vector_math.inputs[3].default_value = 1.0

        # Node Vector Math.003
        vector_math_003 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_003.name = "Vector Math.003"
        vector_math_003.show_options = True
        vector_math_003.operation = 'SUBTRACT'
        # Vector_001
        vector_math_003.inputs[1].default_value = (0.5, 0.5, 0.5)
        # Vector_002
        vector_math_003.inputs[2].default_value = (0.0, 0.0, 0.0)
        # Scale
        vector_math_003.inputs[3].default_value = 1.0

        # Node Vector Math.004
        vector_math_004 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_004.name = "Vector Math.004"
        vector_math_004.show_options = True
        vector_math_004.operation = 'SCALE'
        # Vector_001
        vector_math_004.inputs[1].default_value = (0.0, 0.0, 0.0)
        # Vector_002
        vector_math_004.inputs[2].default_value = (0.0, 0.0, 0.0)

        # Node Map Range
        map_range = nt.nodes.new("ShaderNodeMapRange")
        map_range.name = "Map Range"
        map_range.show_options = True
        map_range.clamp = False
        map_range.data_type = 'FLOAT'
        map_range.interpolation_type = 'LINEAR'
        # From Min
        map_range.inputs[1].default_value = 0.0
        # From Max
        map_range.inputs[2].default_value = 0.6000000238418579
        # To Min
        map_range.inputs[3].default_value = 0.0
        # To Max
        map_range.inputs[4].default_value = 1.0
        # Steps
        map_range.inputs[5].default_value = 4.0
        # Vector
        map_range.inputs[6].default_value = (0.0, 0.0, 0.0)
        # From_Min_FLOAT3
        map_range.inputs[7].default_value = (0.0, 0.0, 0.0)
        # From_Max_FLOAT3
        map_range.inputs[8].default_value = (1.0, 1.0, 1.0)
        # To_Min_FLOAT3
        map_range.inputs[9].default_value = (0.0, 0.0, 0.0)
        # To_Max_FLOAT3
        map_range.inputs[10].default_value = (1.0, 1.0, 1.0)
        # Steps_FLOAT3
        map_range.inputs[11].default_value = (4.0, 4.0, 4.0)

        # Node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.show_options = True
        group_output.is_active_output = True

        # Node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        group_input.show_options = True
        group_input.outputs[5].hide = True

        # Node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.show_options = True
        math_002.operation = 'POWER'
        math_002.use_clamp = False
        # Value_001
        math_002.inputs[1].default_value = 0.3499999940395355
        # Value_002
        math_002.inputs[2].default_value = 0.5

        # Node Map Range.001
        map_range_001 = nt.nodes.new("ShaderNodeMapRange")
        map_range_001.name = "Map Range.001"
        map_range_001.show_options = True
        map_range_001.clamp = True
        map_range_001.data_type = 'FLOAT'
        map_range_001.interpolation_type = 'SMOOTHSTEP'
        # To Min
        map_range_001.inputs[3].default_value = 1.0
        # To Max
        map_range_001.inputs[4].default_value = 0.0
        # Steps
        map_range_001.inputs[5].default_value = 4.0
        # Vector
        map_range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
        # From_Min_FLOAT3
        map_range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
        # From_Max_FLOAT3
        map_range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
        # To_Min_FLOAT3
        map_range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
        # To_Max_FLOAT3
        map_range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
        # Steps_FLOAT3
        map_range_001.inputs[11].default_value = (4.0, 4.0, 4.0)

        # Node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.show_options = True
        math_001.operation = 'ADD'
        math_001.use_clamp = False
        # Value_002
        math_001.inputs[2].default_value = 0.5

        # Node Group Input.002
        group_input_002 = nt.nodes.new("NodeGroupInput")
        group_input_002.name = "Group Input.002"
        group_input_002.show_options = True

        # Node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.show_options = True
        math_003.operation = 'ADD'
        math_003.use_clamp = False
        # Value_001
        math_003.inputs[1].default_value = 1.0
        # Value_002
        math_003.inputs[2].default_value = 0.5

        # Node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.show_options = True
        math_004.operation = 'MAXIMUM'
        math_004.use_clamp = False
        # Value_001
        math_004.inputs[1].default_value = 0.0010000000474974513
        # Value_002
        math_004.inputs[2].default_value = 0.5

        # Node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.show_options = True
        math_006.operation = 'ADD'
        math_006.use_clamp = False
        # Value_001
        math_006.inputs[1].default_value = 0.9990000128746033
        # Value_002
        math_006.inputs[2].default_value = 0.5

        # Node Math.007
        math_007 = nt.nodes.new("ShaderNodeMath")
        math_007.name = "Math.007"
        math_007.hide = True
        math_007.show_options = True
        math_007.operation = 'GREATER_THAN'
        math_007.use_clamp = False
        # Value_001
        math_007.inputs[1].default_value = 0.0
        # Value_002
        math_007.inputs[2].default_value = 0.5

        # Node Math.008
        math_008 = nt.nodes.new("ShaderNodeMath")
        math_008.name = "Math.008"
        math_008.show_options = True
        math_008.operation = 'ABSOLUTE'
        math_008.use_clamp = False
        # Value_001
        math_008.inputs[1].default_value = 0.5
        # Value_002
        math_008.inputs[2].default_value = 0.5

        # Node Texture Coordinate.001
        texture_coordinate_001 = nt.nodes.new("ShaderNodeTexCoord")
        texture_coordinate_001.name = "Texture Coordinate.001"
        texture_coordinate_001.hide = True
        texture_coordinate_001.show_options = True
        texture_coordinate_001.from_instancer = False

        # Node Mix.006
        mix_006 = nt.nodes.new("ShaderNodeMix")
        mix_006.name = "Mix.006"
        mix_006.show_options = True
        mix_006.blend_type = 'MIX'
        mix_006.clamp_factor = True
        mix_006.clamp_result = False
        mix_006.data_type = 'RGBA'
        mix_006.factor_mode = 'UNIFORM'
        # Factor_Vector
        mix_006.inputs[1].default_value = (0.5, 0.5, 0.5)
        # A_Float
        mix_006.inputs[2].default_value = 0.0
        # B_Float
        mix_006.inputs[3].default_value = 0.0
        # A_Vector
        mix_006.inputs[4].default_value = (0.0, 0.0, 0.0)
        # B_Vector
        mix_006.inputs[5].default_value = (0.0, 0.0, 0.0)
        # A_Rotation
        mix_006.inputs[8].default_value = (0.0, 0.0, 0.0)
        # B_Rotation
        mix_006.inputs[9].default_value = (0.0, 0.0, 0.0)

        # Set locations
        nt.nodes["Voronoi Texture"].location = (373.842041015625, 328.46575927734375)
        nt.nodes["Voronoi Texture.001"].location = (360.50921630859375, -130.42166137695312)
        nt.nodes["Math"].location = (753.1743774414062, 178.99639892578125)
        nt.nodes["Noise Texture"].location = (-721.063232421875, -29.26068115234375)
        nt.nodes["Vector Math"].location = (94.21235656738281, 330.56011962890625)
        nt.nodes["Vector Math.003"].location = (-462.22882080078125, 146.02944946289062)
        nt.nodes["Vector Math.004"].location = (-210.6414031982422, 153.8640594482422)
        nt.nodes["Map Range"].location = (971.3658447265625, 226.1817626953125)
        nt.nodes["Group Output"].location = (2139.863037109375, 89.3709716796875)
        nt.nodes["Group Input"].location = (-1257.157958984375, 5.803216934204102)
        nt.nodes["Math.002"].location = (1222.596435546875, 232.7285614013672)
        nt.nodes["Map Range.001"].location = (1466.7109375, -41.68879699707031)
        nt.nodes["Math.001"].location = (1259.3392333984375, -262.21807861328125)
        nt.nodes["Group Input.002"].location = (707.45263671875, -127.80023193359375)
        nt.nodes["Math.003"].location = (1209.074462890625, 60.080711364746094)
        nt.nodes["Math.004"].location = (1016.4873046875, -368.3545837402344)
        nt.nodes["Math.006"].location = (941.9755859375, -73.69654846191406)
        nt.nodes["Math.007"].location = (-722.597412109375, 314.8002624511719)
        nt.nodes["Math.008"].location = (-900.9146728515625, 267.834228515625)
        nt.nodes["Texture Coordinate.001"].location = (-1077.497314453125, 325.7463073730469)
        nt.nodes["Mix.006"].location = (-477.18267822265625, 407.1900329589844)

        # Set dimensions
        nt.nodes["Voronoi Texture"].width  = 160.0
        nt.nodes["Voronoi Texture"].height = 100.0

        nt.nodes["Voronoi Texture.001"].width  = 160.0
        nt.nodes["Voronoi Texture.001"].height = 100.0

        nt.nodes["Math"].width  = 140.0
        nt.nodes["Math"].height = 100.0

        nt.nodes["Noise Texture"].width  = 160.0
        nt.nodes["Noise Texture"].height = 100.0

        nt.nodes["Vector Math"].width  = 141.71084594726562
        nt.nodes["Vector Math"].height = 100.0

        nt.nodes["Vector Math.003"].width  = 140.0
        nt.nodes["Vector Math.003"].height = 100.0

        nt.nodes["Vector Math.004"].width  = 140.0
        nt.nodes["Vector Math.004"].height = 100.0

        nt.nodes["Map Range"].width  = 140.0
        nt.nodes["Map Range"].height = 100.0

        nt.nodes["Group Output"].width  = 140.0
        nt.nodes["Group Output"].height = 100.0

        nt.nodes["Group Input"].width  = 140.0
        nt.nodes["Group Input"].height = 100.0

        nt.nodes["Math.002"].width  = 140.0
        nt.nodes["Math.002"].height = 100.0

        nt.nodes["Map Range.001"].width  = 140.0
        nt.nodes["Map Range.001"].height = 100.0

        nt.nodes["Math.001"].width  = 140.0
        nt.nodes["Math.001"].height = 100.0

        nt.nodes["Group Input.002"].width  = 140.0
        nt.nodes["Group Input.002"].height = 100.0

        nt.nodes["Math.003"].width  = 140.0
        nt.nodes["Math.003"].height = 100.0

        nt.nodes["Math.004"].width  = 140.0
        nt.nodes["Math.004"].height = 100.0

        nt.nodes["Math.006"].width  = 140.0
        nt.nodes["Math.006"].height = 100.0

        nt.nodes["Math.007"].width  = 140.0
        nt.nodes["Math.007"].height = 100.0

        nt.nodes["Math.008"].width  = 140.0
        nt.nodes["Math.008"].height = 100.0

        nt.nodes["Texture Coordinate.001"].width  = 140.0
        nt.nodes["Texture Coordinate.001"].height = 100.0

        nt.nodes["Mix.006"].width  = 140.0
        nt.nodes["Mix.006"].height = 100.0


        # Initialize cellular_noise_1 links

        # noise_texture.Color -> vector_math_003.Vector
        nt.links.new(
            nt.nodes["Noise Texture"].outputs[1],
            nt.nodes["Vector Math.003"].inputs[0]
        )
        # vector_math_003.Vector -> vector_math_004.Vector
        nt.links.new(
            nt.nodes["Vector Math.003"].outputs[0],
            nt.nodes["Vector Math.004"].inputs[0]
        )
        # vector_math_004.Vector -> vector_math.Vector
        nt.links.new(
            nt.nodes["Vector Math.004"].outputs[0],
            nt.nodes["Vector Math"].inputs[1]
        )
        # vector_math.Vector -> voronoi_texture.Vector
        nt.links.new(
            nt.nodes["Vector Math"].outputs[0],
            nt.nodes["Voronoi Texture"].inputs[0]
        )
        # vector_math.Vector -> voronoi_texture_001.Vector
        nt.links.new(
            nt.nodes["Vector Math"].outputs[0],
            nt.nodes["Voronoi Texture.001"].inputs[0]
        )
        # voronoi_texture_001.Distance -> math.Value
        nt.links.new(
            nt.nodes["Voronoi Texture.001"].outputs[0],
            nt.nodes["Math"].inputs[0]
        )
        # voronoi_texture.Distance -> math.Value
        nt.links.new(
            nt.nodes["Voronoi Texture"].outputs[0],
            nt.nodes["Math"].inputs[1]
        )
        # math.Value -> map_range.Value
        nt.links.new(
            nt.nodes["Math"].outputs[0],
            nt.nodes["Map Range"].inputs[0]
        )
        # math_002.Value -> group_output.Factor
        nt.links.new(
            nt.nodes["Math.002"].outputs[0],
            nt.nodes["Group Output"].inputs[0]
        )
        # group_input.Distortion -> vector_math_004.Scale
        nt.links.new(
            nt.nodes["Group Input"].outputs[3],
            nt.nodes["Vector Math.004"].inputs[3]
        )
        # group_input.Scale -> voronoi_texture.Scale
        nt.links.new(
            nt.nodes["Group Input"].outputs[2],
            nt.nodes["Voronoi Texture"].inputs[2]
        )
        # group_input.Scale -> voronoi_texture_001.Scale
        nt.links.new(
            nt.nodes["Group Input"].outputs[2],
            nt.nodes["Voronoi Texture.001"].inputs[2]
        )
        # group_input.Randomness -> voronoi_texture.Randomness
        nt.links.new(
            nt.nodes["Group Input"].outputs[4],
            nt.nodes["Voronoi Texture"].inputs[8]
        )
        # group_input.Randomness -> voronoi_texture_001.Randomness
        nt.links.new(
            nt.nodes["Group Input"].outputs[4],
            nt.nodes["Voronoi Texture.001"].inputs[8]
        )
        # group_input.Vector -> noise_texture.Vector
        nt.links.new(
            nt.nodes["Group Input"].outputs[0],
            nt.nodes["Noise Texture"].inputs[0]
        )
        # voronoi_texture.Color -> group_output.Color
        nt.links.new(
            nt.nodes["Voronoi Texture"].outputs[1],
            nt.nodes["Group Output"].inputs[2]
        )
        # map_range.Result -> math_002.Value
        nt.links.new(
            nt.nodes["Map Range"].outputs[0],
            nt.nodes["Math.002"].inputs[0]
        )
        # math_003.Value -> map_range_001.Value
        nt.links.new(
            nt.nodes["Math.003"].outputs[0],
            nt.nodes["Map Range.001"].inputs[0]
        )
        # math_001.Value -> map_range_001.From Max
        nt.links.new(
            nt.nodes["Math.001"].outputs[0],
            nt.nodes["Map Range.001"].inputs[2]
        )
        # map_range_001.Result -> group_output.Border
        nt.links.new(
            nt.nodes["Map Range.001"].outputs[0],
            nt.nodes["Group Output"].inputs[1]
        )
        # map_range.Result -> math_003.Value
        nt.links.new(
            nt.nodes["Map Range"].outputs[0],
            nt.nodes["Math.003"].inputs[0]
        )
        # math_004.Value -> math_001.Value
        nt.links.new(
            nt.nodes["Math.004"].outputs[0],
            nt.nodes["Math.001"].inputs[1]
        )
        # group_input_002.Smothness -> math_004.Value
        nt.links.new(
            nt.nodes["Group Input.002"].outputs[6],
            nt.nodes["Math.004"].inputs[0]
        )
        # group_input_002.Border Width -> math_006.Value
        nt.links.new(
            nt.nodes["Group Input.002"].outputs[5],
            nt.nodes["Math.006"].inputs[0]
        )
        # math_006.Value -> map_range_001.From Min
        nt.links.new(
            nt.nodes["Math.006"].outputs[0],
            nt.nodes["Map Range.001"].inputs[1]
        )
        # math_006.Value -> math_001.Value
        nt.links.new(
            nt.nodes["Math.006"].outputs[0],
            nt.nodes["Math.001"].inputs[0]
        )
        # voronoi_texture.Position -> group_output.Position
        nt.links.new(
            nt.nodes["Voronoi Texture"].outputs[2],
            nt.nodes["Group Output"].inputs[3]
        )
        # math_007.Value -> mix_006.Factor
        nt.links.new(
            nt.nodes["Math.007"].outputs[0],
            nt.nodes["Mix.006"].inputs[0]
        )
        # texture_coordinate_001.Generated -> mix_006.A
        nt.links.new(
            nt.nodes["Texture Coordinate.001"].outputs[0],
            nt.nodes["Mix.006"].inputs[6]
        )
        # math_008.Value -> math_007.Value
        nt.links.new(
            nt.nodes["Math.008"].outputs[0],
            nt.nodes["Math.007"].inputs[0]
        )
        # group_input.Vector -> math_008.Value
        nt.links.new(
            nt.nodes["Group Input"].outputs[0],
            nt.nodes["Math.008"].inputs[0]
        )
        # group_input.Vector -> mix_006.B
        nt.links.new(
            nt.nodes["Group Input"].outputs[0],
            nt.nodes["Mix.006"].inputs[7]
        )
        # mix_006.Result -> vector_math.Vector
        nt.links.new(
            nt.nodes["Mix.006"].outputs[2],
            nt.nodes["Vector Math"].inputs[0]
        )
        # group_input.W -> noise_texture.W
        nt.links.new(
            nt.nodes["Group Input"].outputs[1],
            nt.nodes["Noise Texture"].inputs[1]
        )
        # group_input.W -> voronoi_texture.W
        nt.links.new(
            nt.nodes["Group Input"].outputs[1],
            nt.nodes["Voronoi Texture"].inputs[1]
        )
        # group_input.W -> voronoi_texture_001.W
        nt.links.new(
            nt.nodes["Group Input"].outputs[1],
            nt.nodes["Voronoi Texture.001"].inputs[1]
        )

        return nt


