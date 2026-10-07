import bpy
from ..utils import ShaderNode


class ShaderNodeContour(ShaderNode):
    bl_label = "Contour Noise"
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
        # contour_noise_1 interface

        # Socket Lines
        lines_socket = nt.interface.new_socket(name="Lines", in_out='OUTPUT', socket_type='NodeSocketFloat')
        lines_socket.default_value = 0.0
        lines_socket.min_value = -3.4028234663852886e+38
        lines_socket.max_value = 3.4028234663852886e+38
        lines_socket.subtype = 'NONE'
        lines_socket.attribute_domain = 'POINT'
        lines_socket.default_input = 'VALUE'
        lines_socket.structure_type = 'AUTO'

        # Socket Bands
        bands_socket = nt.interface.new_socket(name="Bands", in_out='OUTPUT', socket_type='NodeSocketFloat')
        bands_socket.default_value = 0.0
        bands_socket.min_value = -3.4028234663852886e+38
        bands_socket.max_value = 3.4028234663852886e+38
        bands_socket.subtype = 'NONE'
        bands_socket.attribute_domain = 'POINT'
        bands_socket.default_input = 'VALUE'
        bands_socket.structure_type = 'AUTO'

        # Socket Terraces
        terraces_socket = nt.interface.new_socket(name="Terraces", in_out='OUTPUT', socket_type='NodeSocketFloat')
        terraces_socket.default_value = 0.0
        terraces_socket.min_value = -3.4028234663852886e+38
        terraces_socket.max_value = 3.4028234663852886e+38
        terraces_socket.subtype = 'NONE'
        terraces_socket.attribute_domain = 'POINT'
        terraces_socket.default_input = 'VALUE'
        terraces_socket.structure_type = 'AUTO'

        # Socket Vector
        vector_socket = nt.interface.new_socket(name="Vector", in_out='INPUT', socket_type='NodeSocketVector')
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = -3.4028234663852886e+38
        vector_socket.max_value = 3.4028234663852886e+38
        vector_socket.subtype = 'NONE'
        vector_socket.attribute_domain = 'POINT'
        vector_socket.hide_value = True
        vector_socket.default_input = 'VALUE'
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
        scale_socket.default_value = 3.0
        scale_socket.min_value = 0.0
        scale_socket.max_value = 1000.0
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        scale_socket.default_input = 'VALUE'
        scale_socket.structure_type = 'AUTO'

        # Socket Density
        density_socket = nt.interface.new_socket(name="Density", in_out='INPUT', socket_type='NodeSocketFloat')
        density_socket.default_value = 10.0
        density_socket.min_value = 0.0
        density_socket.max_value = 100.0
        density_socket.subtype = 'NONE'
        density_socket.attribute_domain = 'POINT'
        density_socket.default_input = 'VALUE'
        density_socket.structure_type = 'AUTO'

        # Socket Line Width
        line_width_socket = nt.interface.new_socket(name="Line Width", in_out='INPUT', socket_type='NodeSocketFloat')
        line_width_socket.default_value = 0.5
        line_width_socket.min_value = -1.0
        line_width_socket.max_value = 0.9990000128746033
        line_width_socket.subtype = 'NONE'
        line_width_socket.attribute_domain = 'POINT'
        line_width_socket.default_input = 'VALUE'
        line_width_socket.structure_type = 'AUTO'

        # Socket Detail
        detail_socket = nt.interface.new_socket(name="Detail", in_out='INPUT', socket_type='NodeSocketFloat')
        detail_socket.default_value = 2.0
        detail_socket.min_value = 0.0
        detail_socket.max_value = 5.0
        detail_socket.subtype = 'NONE'
        detail_socket.attribute_domain = 'POINT'
        detail_socket.default_input = 'VALUE'
        detail_socket.structure_type = 'AUTO'

        # Socket Roughness
        roughness_socket = nt.interface.new_socket(name="Roughness", in_out='INPUT', socket_type='NodeSocketFloat')
        roughness_socket.default_value = 0.5
        roughness_socket.min_value = 0.0
        roughness_socket.max_value = 1.0
        roughness_socket.subtype = 'FACTOR'
        roughness_socket.attribute_domain = 'POINT'
        roughness_socket.default_input = 'VALUE'
        roughness_socket.structure_type = 'AUTO'

        # Initialize contour_noise_1 nodes

        # Node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        group_input.show_options = True

        # Node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.show_options = True
        group_output.is_active_output = True

        # Node Noise Texture
        noise_texture = nt.nodes.new("ShaderNodeTexNoise")
        noise_texture.name = "Noise Texture"
        noise_texture.show_options = True
        noise_texture.show_texture = True
        noise_texture.noise_dimensions = '4D'
        noise_texture.noise_type = 'FBM'
        noise_texture.normalize = True
        # Lacunarity
        noise_texture.inputs[5].default_value = 2.0
        # Offset
        noise_texture.inputs[6].default_value = 0.0
        # Gain
        noise_texture.inputs[7].default_value = 1.0
        # Distortion
        noise_texture.inputs[8].default_value = 0.0

        # Node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.show_options = True
        math.operation = 'MULTIPLY'
        math.use_clamp = False
        # Value_002
        math.inputs[2].default_value = 0.5

        # Node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.show_options = True
        math_001.operation = 'SINE'
        math_001.use_clamp = False
        # Value_001
        math_001.inputs[1].default_value = 0.5
        # Value_002
        math_001.inputs[2].default_value = 0.5

        # Node Map Range
        map_range = nt.nodes.new("ShaderNodeMapRange")
        map_range.name = "Map Range"
        map_range.show_options = True
        map_range.clamp = True
        map_range.data_type = 'FLOAT'
        map_range.interpolation_type = 'LINEAR'
        # From Max
        map_range.inputs[2].default_value = 1.0
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

        # Node Group Input.001
        group_input_001 = nt.nodes.new("NodeGroupInput")
        group_input_001.name = "Group Input.001"
        group_input_001.show_options = True

        # Node Map Range.001
        map_range_001 = nt.nodes.new("ShaderNodeMapRange")
        map_range_001.name = "Map Range.001"
        map_range_001.show_options = True
        map_range_001.clamp = True
        map_range_001.data_type = 'FLOAT'
        map_range_001.interpolation_type = 'LINEAR'
        # From Min
        map_range_001.inputs[1].default_value = -1.0
        # From Max
        map_range_001.inputs[2].default_value = 1.0
        # To Min
        map_range_001.inputs[3].default_value = 0.0
        # To Max
        map_range_001.inputs[4].default_value = 1.0
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

        # Node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.show_options = True
        math_002.operation = 'SUBTRACT'
        math_002.use_clamp = False
        # Value
        math_002.inputs[0].default_value = 1.0
        # Value_002
        math_002.inputs[2].default_value = 0.5

        # Node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.show_options = True
        math_003.operation = 'MULTIPLY'
        math_003.use_clamp = False
        # Value_002
        math_003.inputs[2].default_value = 0.5

        # Node Group Input.002
        group_input_002 = nt.nodes.new("NodeGroupInput")
        group_input_002.name = "Group Input.002"
        group_input_002.show_options = True
        group_input_002.outputs[0].hide = True
        group_input_002.outputs[1].hide = True
        group_input_002.outputs[2].hide = True
        group_input_002.outputs[4].hide = True
        group_input_002.outputs[5].hide = True
        group_input_002.outputs[6].hide = True
        group_input_002.outputs[7].hide = True

        # Node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.show_options = True
        math_004.operation = 'FLOOR'
        math_004.use_clamp = False
        # Value_001
        math_004.inputs[1].default_value = 0.5
        # Value_002
        math_004.inputs[2].default_value = 0.5

        # Node Math.005
        math_005 = nt.nodes.new("ShaderNodeMath")
        math_005.name = "Math.005"
        math_005.show_options = True
        math_005.operation = 'DIVIDE'
        math_005.use_clamp = False
        # Value_002
        math_005.inputs[2].default_value = 0.5

        # Node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.show_options = True
        math_006.operation = 'MULTIPLY'
        math_006.use_clamp = False
        # Value_001
        math_006.inputs[1].default_value = 10.0
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
        # B_Color
        mix_006.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
        # A_Rotation
        mix_006.inputs[8].default_value = (0.0, 0.0, 0.0)
        # B_Rotation
        mix_006.inputs[9].default_value = (0.0, 0.0, 0.0)

        # Set locations
        nt.nodes["Group Input"].location = (-1229.950927734375, -219.00698852539062)
        nt.nodes["Group Output"].location = (981.6458129882812, 54.68791961669922)
        nt.nodes["Noise Texture"].location = (-214.2169952392578, -8.20745849609375)
        nt.nodes["Math"].location = (49.16997528076172, 12.767206192016602)
        nt.nodes["Math.001"].location = (237.78311157226562, 12.75494384765625)
        nt.nodes["Map Range"].location = (444.6038513183594, 6.3438720703125)
        nt.nodes["Group Input.001"].location = (26.80753517150879, -163.14974975585938)
        nt.nodes["Map Range.001"].location = (458.1055603027344, -340.66961669921875)
        nt.nodes["Math.002"].location = (632.3165893554688, -223.1692352294922)
        nt.nodes["Math.003"].location = (235.99789428710938, 393.7946472167969)
        nt.nodes["Group Input.002"].location = (-79.86508178710938, 268.5232849121094)
        nt.nodes["Math.004"].location = (440.38568115234375, 384.65875244140625)
        nt.nodes["Math.005"].location = (626.6856079101562, 287.61541748046875)
        nt.nodes["Math.006"].location = (-705.92236328125, -71.61913299560547)
        nt.nodes["Math.007"].location = (-769.1712646484375, 221.17147827148438)
        nt.nodes["Math.008"].location = (-947.4884643554688, 174.20550537109375)
        nt.nodes["Texture Coordinate.001"].location = (-1124.0711669921875, 232.11752319335938)
        nt.nodes["Mix.006"].location = (-551.5020751953125, 237.58349609375)

        # Set dimensions
        nt.nodes["Group Input"].width  = 140.0
        nt.nodes["Group Input"].height = 100.0

        nt.nodes["Group Output"].width  = 140.0
        nt.nodes["Group Output"].height = 100.0

        nt.nodes["Noise Texture"].width  = 160.0
        nt.nodes["Noise Texture"].height = 100.0

        nt.nodes["Math"].width  = 140.0
        nt.nodes["Math"].height = 100.0

        nt.nodes["Math.001"].width  = 140.0
        nt.nodes["Math.001"].height = 100.0

        nt.nodes["Map Range"].width  = 140.0
        nt.nodes["Map Range"].height = 100.0

        nt.nodes["Group Input.001"].width  = 140.0
        nt.nodes["Group Input.001"].height = 100.0

        nt.nodes["Map Range.001"].width  = 140.0
        nt.nodes["Map Range.001"].height = 100.0

        nt.nodes["Math.002"].width  = 140.0
        nt.nodes["Math.002"].height = 100.0

        nt.nodes["Math.003"].width  = 140.0
        nt.nodes["Math.003"].height = 100.0

        nt.nodes["Group Input.002"].width  = 140.0
        nt.nodes["Group Input.002"].height = 100.0

        nt.nodes["Math.004"].width  = 140.0
        nt.nodes["Math.004"].height = 100.0

        nt.nodes["Math.005"].width  = 140.0
        nt.nodes["Math.005"].height = 100.0

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


        # Initialize contour_noise_1 links

        # noise_texture.Factor -> math.Value
        nt.links.new(
            nt.nodes["Noise Texture"].outputs[0],
            nt.nodes["Math"].inputs[0]
        )
        # math.Value -> math_001.Value
        nt.links.new(
            nt.nodes["Math"].outputs[0],
            nt.nodes["Math.001"].inputs[0]
        )
        # math_001.Value -> map_range.Value
        nt.links.new(
            nt.nodes["Math.001"].outputs[0],
            nt.nodes["Map Range"].inputs[0]
        )
        # group_input.Scale -> noise_texture.Scale
        nt.links.new(
            nt.nodes["Group Input"].outputs[2],
            nt.nodes["Noise Texture"].inputs[2]
        )
        # group_input.Roughness -> noise_texture.Roughness
        nt.links.new(
            nt.nodes["Group Input"].outputs[6],
            nt.nodes["Noise Texture"].inputs[4]
        )
        # group_input_001.Line Width -> map_range.From Min
        nt.links.new(
            nt.nodes["Group Input.001"].outputs[4],
            nt.nodes["Map Range"].inputs[1]
        )
        # map_range.Result -> group_output.Lines
        nt.links.new(
            nt.nodes["Map Range"].outputs[0],
            nt.nodes["Group Output"].inputs[0]
        )
        # group_input.Detail -> noise_texture.Detail
        nt.links.new(
            nt.nodes["Group Input"].outputs[5],
            nt.nodes["Noise Texture"].inputs[3]
        )
        # math_006.Value -> math.Value
        nt.links.new(
            nt.nodes["Math.006"].outputs[0],
            nt.nodes["Math"].inputs[1]
        )
        # math_001.Value -> map_range_001.Value
        nt.links.new(
            nt.nodes["Math.001"].outputs[0],
            nt.nodes["Map Range.001"].inputs[0]
        )
        # map_range_001.Result -> math_002.Value
        nt.links.new(
            nt.nodes["Map Range.001"].outputs[0],
            nt.nodes["Math.002"].inputs[1]
        )
        # math_002.Value -> group_output.Bands
        nt.links.new(
            nt.nodes["Math.002"].outputs[0],
            nt.nodes["Group Output"].inputs[1]
        )
        # group_input_002.Density -> math_003.Value
        nt.links.new(
            nt.nodes["Group Input.002"].outputs[3],
            nt.nodes["Math.003"].inputs[1]
        )
        # math_003.Value -> math_004.Value
        nt.links.new(
            nt.nodes["Math.003"].outputs[0],
            nt.nodes["Math.004"].inputs[0]
        )
        # math_004.Value -> math_005.Value
        nt.links.new(
            nt.nodes["Math.004"].outputs[0],
            nt.nodes["Math.005"].inputs[0]
        )
        # group_input_002.Density -> math_005.Value
        nt.links.new(
            nt.nodes["Group Input.002"].outputs[3],
            nt.nodes["Math.005"].inputs[1]
        )
        # noise_texture.Factor -> math_003.Value
        nt.links.new(
            nt.nodes["Noise Texture"].outputs[0],
            nt.nodes["Math.003"].inputs[0]
        )
        # group_input.Density -> math_006.Value
        nt.links.new(
            nt.nodes["Group Input"].outputs[3],
            nt.nodes["Math.006"].inputs[0]
        )
        # math_005.Value -> group_output.Terraces
        nt.links.new(
            nt.nodes["Math.005"].outputs[0],
            nt.nodes["Group Output"].inputs[2]
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
        # mix_006.Result -> noise_texture.Vector
        nt.links.new(
            nt.nodes["Mix.006"].outputs[2],
            nt.nodes["Noise Texture"].inputs[0]
        )
        # group_input.W -> noise_texture.W
        nt.links.new(
            nt.nodes["Group Input"].outputs[1],
            nt.nodes["Noise Texture"].inputs[1]
        )

        return nt

