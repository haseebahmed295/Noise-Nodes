
import bpy
from ..utils import ShaderNode


class ShaderNodeHex(ShaderNode):
    bl_label = "Hex Noise"
    bl_icon = "NONE"

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + "_node_tree")
        

    def createNodetree(self, name):
        """Initialize Hexagon Noise node group"""
        nt = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = name)

        nt.color_tag = 'TEXTURE'
        nt.description = ""
        nt.default_group_node_width = 140
        # hexagon_noise_1 interface

        # Socket Random Color
        random_color_socket = nt.interface.new_socket(name="Random Color", in_out='OUTPUT', socket_type='NodeSocketColor')
        random_color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        random_color_socket.attribute_domain = 'POINT'
        random_color_socket.default_input = 'VALUE'
        random_color_socket.structure_type = 'AUTO'

        # Socket Grid Lines
        grid_lines_socket = nt.interface.new_socket(name="Grid Lines", in_out='OUTPUT', socket_type='NodeSocketFloat')
        grid_lines_socket.default_value = 0.0
        grid_lines_socket.min_value = -3.4028234663852886e+38
        grid_lines_socket.max_value = 3.4028234663852886e+38
        grid_lines_socket.subtype = 'NONE'
        grid_lines_socket.attribute_domain = 'POINT'
        grid_lines_socket.default_input = 'VALUE'
        grid_lines_socket.structure_type = 'AUTO'

        # Socket Distance to Edge
        distance_to_edge_socket = nt.interface.new_socket(name="Distance to Edge", in_out='OUTPUT', socket_type='NodeSocketFloat')
        distance_to_edge_socket.default_value = 0.0
        distance_to_edge_socket.min_value = -3.4028234663852886e+38
        distance_to_edge_socket.max_value = 3.4028234663852886e+38
        distance_to_edge_socket.subtype = 'NONE'
        distance_to_edge_socket.attribute_domain = 'POINT'
        distance_to_edge_socket.default_input = 'VALUE'
        distance_to_edge_socket.structure_type = 'AUTO'

        # Socket Cell Center Vector
        cell_center_vector_socket = nt.interface.new_socket(name="Cell Center Vector", in_out='OUTPUT', socket_type='NodeSocketVector')
        cell_center_vector_socket.default_value = (0.0, 0.0, 0.0)
        cell_center_vector_socket.min_value = -3.4028234663852886e+38
        cell_center_vector_socket.max_value = 3.4028234663852886e+38
        cell_center_vector_socket.subtype = 'NONE'
        cell_center_vector_socket.attribute_domain = 'POINT'
        cell_center_vector_socket.default_input = 'VALUE'
        cell_center_vector_socket.structure_type = 'AUTO'

        # Socket Vector
        vector_socket = nt.interface.new_socket(name="Vector", in_out='INPUT', socket_type='NodeSocketVector')
        vector_socket.default_value = (0.0, 0.0, 0.0)
        vector_socket.min_value = -10000.0
        vector_socket.max_value = 10000.0
        vector_socket.subtype = 'NONE'
        vector_socket.attribute_domain = 'POINT'
        vector_socket.hide_value = True
        vector_socket.default_input = 'VALUE'
        vector_socket.structure_type = 'AUTO'

        # Socket Scale
        scale_socket = nt.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
        scale_socket.default_value = 5.0
        scale_socket.min_value = -3.4028234663852886e+38
        scale_socket.max_value = 3.4028234663852886e+38
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        scale_socket.default_input = 'VALUE'
        scale_socket.structure_type = 'AUTO'

        # Socket Line Thickness
        line_thickness_socket = nt.interface.new_socket(name="Line Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
        line_thickness_socket.default_value = 0.07999999821186066
        line_thickness_socket.min_value = -3.4028234663852886e+38
        line_thickness_socket.max_value = 3.4028234663852886e+38
        line_thickness_socket.subtype = 'NONE'
        line_thickness_socket.attribute_domain = 'POINT'
        line_thickness_socket.default_input = 'VALUE'
        line_thickness_socket.structure_type = 'AUTO'

        # Socket Smoothness
        smoothness_socket = nt.interface.new_socket(name="Smoothness", in_out='INPUT', socket_type='NodeSocketFloat')
        smoothness_socket.default_value = 0.019999999552965164
        smoothness_socket.min_value = -3.4028234663852886e+38
        smoothness_socket.max_value = 3.4028234663852886e+38
        smoothness_socket.subtype = 'NONE'
        smoothness_socket.attribute_domain = 'POINT'
        smoothness_socket.default_input = 'VALUE'
        smoothness_socket.structure_type = 'AUTO'

        # Initialize hexagon_noise_1 nodes

        # Node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        group_input.show_options = True

        # Node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.show_options = True
        group_output.is_active_output = True

        # Node Vector Math
        vector_math = nt.nodes.new("ShaderNodeVectorMath")
        vector_math.label = "P"
        vector_math.name = "Vector Math"
        vector_math.show_options = True
        vector_math.operation = 'SCALE'

        # Node Combine XYZ.001
        combine_xyz_001 = nt.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz_001.label = "H"
        combine_xyz_001.name = "Combine XYZ.001"
        combine_xyz_001.show_options = True
        # X
        combine_xyz_001.inputs[0].default_value = 0.5
        # Y
        combine_xyz_001.inputs[1].default_value = 0.8660249710083008
        # Z
        combine_xyz_001.inputs[2].default_value = 0.0

        # Node Vector Math.002
        vector_math_002 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_002.label = "Vector A"
        vector_math_002.name = "Vector Math.002"
        vector_math_002.show_options = True
        vector_math_002.operation = 'WRAP'

        # Node Vector Math.003
        vector_math_003 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_003.name = "Vector Math.003"
        vector_math_003.hide = True
        vector_math_003.show_options = True
        vector_math_003.operation = 'SUBTRACT'

        # Node Vector Math.004
        vector_math_004 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_004.label = "Vector B"
        vector_math_004.name = "Vector Math.004"
        vector_math_004.show_options = True
        vector_math_004.operation = 'WRAP'

        # Node Vector Math.005
        vector_math_005 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_005.name = "Vector Math.005"
        vector_math_005.show_options = True
        vector_math_005.operation = 'DOT_PRODUCT'

        # Node Vector Math.006
        vector_math_006 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_006.name = "Vector Math.006"
        vector_math_006.show_options = True
        vector_math_006.operation = 'DOT_PRODUCT'

        # Node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.show_options = True
        math.operation = 'GREATER_THAN'
        math.use_clamp = False

        # Node Mix
        mix = nt.nodes.new("ShaderNodeMix")
        mix.label = "C = (x,y)"
        mix.name = "Mix"
        mix.show_options = True
        mix.blend_type = 'MIX'
        mix.clamp_factor = True
        mix.clamp_result = False
        mix.data_type = 'VECTOR'
        mix.factor_mode = 'UNIFORM'

        # Node Vector Math.007
        vector_math_007 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_007.name = "Vector Math.007"
        vector_math_007.show_options = True
        vector_math_007.operation = 'ABSOLUTE'

        # Node Separate XYZ
        separate_xyz = nt.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz.name = "Separate XYZ"
        separate_xyz.show_options = True

        # Node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.show_options = True
        math_001.operation = 'MULTIPLY_ADD'
        math_001.use_clamp = False
        # Value_001
        math_001.inputs[1].default_value = 0.8660249710083008

        # Node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.show_options = True
        math_002.operation = 'MULTIPLY'
        math_002.use_clamp = False
        # Value_001
        math_002.inputs[1].default_value = 0.5

        # Node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.show_options = True
        math_003.operation = 'MAXIMUM'
        math_003.use_clamp = False

        # Node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.show_options = True
        math_004.operation = 'MULTIPLY'
        math_004.use_clamp = False
        # Value_001
        math_004.inputs[1].default_value = 2.0

        # Node Map Range
        map_range = nt.nodes.new("ShaderNodeMapRange")
        map_range.name = "Map Range"
        map_range.show_options = True
        map_range.clamp = True
        map_range.data_type = 'FLOAT'
        map_range.interpolation_type = 'SMOOTHSTEP'
        # To Min
        map_range.inputs[3].default_value = 0.0
        # To Max
        map_range.inputs[4].default_value = 1.0

        # Node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.hide = True
        math_006.show_options = True
        math_006.operation = 'SUBTRACT'
        math_006.use_clamp = True
        # Value
        math_006.inputs[0].default_value = 1.0

        # Node Group Input.001
        group_input_001 = nt.nodes.new("NodeGroupInput")
        group_input_001.name = "Group Input.001"
        group_input_001.show_options = True

        # Node Math.007
        math_007 = nt.nodes.new("ShaderNodeMath")
        math_007.name = "Math.007"
        math_007.show_options = True
        math_007.operation = 'ADD'
        math_007.use_clamp = True

        # Node Vector Math.008
        vector_math_008 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_008.name = "Vector Math.008"
        vector_math_008.show_options = True
        vector_math_008.operation = 'SUBTRACT'

        # Node Reroute.001
        reroute_001 = nt.nodes.new("NodeReroute")
        reroute_001.name = "Reroute.001"
        reroute_001.show_options = True
        reroute_001.socket_idname = "NodeSocketVector"
        # Node White Noise Texture
        white_noise_texture = nt.nodes.new("ShaderNodeTexWhiteNoise")
        white_noise_texture.name = "White Noise Texture"
        white_noise_texture.show_options = True
        white_noise_texture.show_texture = True
        white_noise_texture.noise_dimensions = '3D'

        # Node Combine XYZ.002
        combine_xyz_002 = nt.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz_002.label = "H"
        combine_xyz_002.name = "Combine XYZ.002"
        combine_xyz_002.show_options = True
        # X
        combine_xyz_002.inputs[0].default_value = -0.5
        # Y
        combine_xyz_002.inputs[1].default_value = -0.8660249710083008
        # Z
        combine_xyz_002.inputs[2].default_value = 0.0

        # Node Vector Math.009
        vector_math_009 = nt.nodes.new("ShaderNodeVectorMath")
        vector_math_009.name = "Vector Math.009"
        vector_math_009.show_options = True
        vector_math_009.operation = 'SNAP'
        # Vector_001
        vector_math_009.inputs[1].default_value = (0.0010000000474974513, 0.0010000000474974513, 0.0)

        # Node Math.008
        math_008 = nt.nodes.new("ShaderNodeMath")
        math_008.name = "Math.008"
        math_008.hide = True
        math_008.show_options = True
        math_008.operation = 'GREATER_THAN'
        math_008.use_clamp = False
        # Value_001
        math_008.inputs[1].default_value = 0.0

        # Node Math.009
        math_009 = nt.nodes.new("ShaderNodeMath")
        math_009.name = "Math.009"
        math_009.show_options = True
        math_009.operation = 'ABSOLUTE'
        math_009.use_clamp = False

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

        # Set locations
        nt.nodes["Group Input"].location = (-1264.6180419921875, -109.26416015625)
        nt.nodes["Group Output"].location = (3560.0849609375, 26.52273941040039)
        nt.nodes["Vector Math"].location = (-177.8655242919922, -10.820605278015137)
        nt.nodes["Combine XYZ.001"].location = (-328.01580810546875, -524.6202392578125)
        nt.nodes["Vector Math.002"].location = (346.96038818359375, -122.26448822021484)
        nt.nodes["Vector Math.003"].location = (166.2872314453125, -473.59027099609375)
        nt.nodes["Vector Math.004"].location = (361.42059326171875, -431.75140380859375)
        nt.nodes["Vector Math.005"].location = (777.4835205078125, -273.66656494140625)
        nt.nodes["Vector Math.006"].location = (779.1595458984375, -509.830078125)
        nt.nodes["Math"].location = (1089.3564453125, -326.22210693359375)
        nt.nodes["Mix"].location = (1323.9345703125, 13.915637016296387)
        nt.nodes["Vector Math.007"].location = (1566.5166015625, -62.860877990722656)
        nt.nodes["Separate XYZ"].location = (1738.7086181640625, -86.08895111083984)
        nt.nodes["Math.001"].location = (2184.91650390625, 196.69430541992188)
        nt.nodes["Math.002"].location = (1965.876953125, 109.22880554199219)
        nt.nodes["Math.003"].location = (2432.7587890625, 23.7506103515625)
        nt.nodes["Math.004"].location = (2629.27685546875, 10.037023544311523)
        nt.nodes["Map Range"].location = (3175.019287109375, 241.3290557861328)
        nt.nodes["Math.006"].location = (2949.351806640625, 282.8285217285156)
        nt.nodes["Group Input.001"].location = (2690.306884765625, 295.07293701171875)
        nt.nodes["Math.007"].location = (2952.077392578125, 232.96322631835938)
        nt.nodes["Vector Math.008"].location = (1653.9976806640625, -366.8586120605469)
        nt.nodes["Reroute.001"].location = (939.9117431640625, -41.952674865722656)
        nt.nodes["White Noise Texture"].location = (2013.5396728515625, -353.23724365234375)
        nt.nodes["Combine XYZ.002"].location = (-327.4054260253906, -755.772216796875)
        nt.nodes["Vector Math.009"].location = (1833.60009765625, -381.1334533691406)
        nt.nodes["Math.008"].location = (-677.17578125, 130.44845581054688)
        nt.nodes["Math.009"].location = (-855.4929809570312, 83.4824447631836)
        nt.nodes["Texture Coordinate.001"].location = (-1032.07568359375, 141.39450073242188)
        nt.nodes["Mix.006"].location = (-459.50653076171875, 146.86044311523438)

        # Set dimensions
        nt.nodes["Group Input"].width  = 140.0
        nt.nodes["Group Input"].height = 100.0

        nt.nodes["Group Output"].width  = 140.0
        nt.nodes["Group Output"].height = 100.0

        nt.nodes["Vector Math"].width  = 140.0
        nt.nodes["Vector Math"].height = 100.0

        nt.nodes["Combine XYZ.001"].width  = 140.0
        nt.nodes["Combine XYZ.001"].height = 100.0

        nt.nodes["Vector Math.002"].width  = 140.0
        nt.nodes["Vector Math.002"].height = 100.0

        nt.nodes["Vector Math.003"].width  = 140.0
        nt.nodes["Vector Math.003"].height = 100.0

        nt.nodes["Vector Math.004"].width  = 140.0
        nt.nodes["Vector Math.004"].height = 100.0

        nt.nodes["Vector Math.005"].width  = 140.0
        nt.nodes["Vector Math.005"].height = 100.0

        nt.nodes["Vector Math.006"].width  = 140.0
        nt.nodes["Vector Math.006"].height = 100.0

        nt.nodes["Math"].width  = 140.0
        nt.nodes["Math"].height = 100.0

        nt.nodes["Mix"].width  = 140.0
        nt.nodes["Mix"].height = 100.0

        nt.nodes["Vector Math.007"].width  = 140.0
        nt.nodes["Vector Math.007"].height = 100.0

        nt.nodes["Separate XYZ"].width  = 140.0
        nt.nodes["Separate XYZ"].height = 100.0

        nt.nodes["Math.001"].width  = 140.0
        nt.nodes["Math.001"].height = 100.0

        nt.nodes["Math.002"].width  = 140.0
        nt.nodes["Math.002"].height = 100.0

        nt.nodes["Math.003"].width  = 140.0
        nt.nodes["Math.003"].height = 100.0

        nt.nodes["Math.004"].width  = 140.0
        nt.nodes["Math.004"].height = 100.0

        nt.nodes["Map Range"].width  = 140.0
        nt.nodes["Map Range"].height = 100.0

        nt.nodes["Math.006"].width  = 140.0
        nt.nodes["Math.006"].height = 100.0

        nt.nodes["Group Input.001"].width  = 140.0
        nt.nodes["Group Input.001"].height = 100.0

        nt.nodes["Math.007"].width  = 140.0
        nt.nodes["Math.007"].height = 100.0

        nt.nodes["Vector Math.008"].width  = 140.0
        nt.nodes["Vector Math.008"].height = 100.0

        nt.nodes["Reroute.001"].width  = 12.5
        nt.nodes["Reroute.001"].height = 100.0

        nt.nodes["White Noise Texture"].width  = 140.0
        nt.nodes["White Noise Texture"].height = 100.0

        nt.nodes["Combine XYZ.002"].width  = 140.0
        nt.nodes["Combine XYZ.002"].height = 100.0

        nt.nodes["Vector Math.009"].width  = 140.0
        nt.nodes["Vector Math.009"].height = 100.0

        nt.nodes["Math.008"].width  = 134.1873016357422
        nt.nodes["Math.008"].height = 100.0

        nt.nodes["Math.009"].width  = 134.1873016357422
        nt.nodes["Math.009"].height = 100.0

        nt.nodes["Texture Coordinate.001"].width  = 134.1873016357422
        nt.nodes["Texture Coordinate.001"].height = 100.0

        nt.nodes["Mix.006"].width  = 134.1873016357422
        nt.nodes["Mix.006"].height = 100.0


        # Initialize hexagon_noise_1 links

        # group_input.Scale -> vector_math.Scale
        nt.links.new(
            nt.nodes["Group Input"].outputs[1],
            nt.nodes["Vector Math"].inputs[3]
        )
        # vector_math.Vector -> vector_math_002.Vector
        nt.links.new(
            nt.nodes["Vector Math"].outputs[0],
            nt.nodes["Vector Math.002"].inputs[0]
        )
        # vector_math.Vector -> vector_math_003.Vector
        nt.links.new(
            nt.nodes["Vector Math"].outputs[0],
            nt.nodes["Vector Math.003"].inputs[0]
        )
        # combine_xyz_001.Vector -> vector_math_003.Vector
        nt.links.new(
            nt.nodes["Combine XYZ.001"].outputs[0],
            nt.nodes["Vector Math.003"].inputs[1]
        )
        # vector_math_003.Vector -> vector_math_004.Vector
        nt.links.new(
            nt.nodes["Vector Math.003"].outputs[0],
            nt.nodes["Vector Math.004"].inputs[0]
        )
        # combine_xyz_001.Vector -> vector_math_002.Vector
        nt.links.new(
            nt.nodes["Combine XYZ.001"].outputs[0],
            nt.nodes["Vector Math.002"].inputs[1]
        )
        # combine_xyz_001.Vector -> vector_math_004.Vector
        nt.links.new(
            nt.nodes["Combine XYZ.001"].outputs[0],
            nt.nodes["Vector Math.004"].inputs[1]
        )
        # vector_math_002.Vector -> vector_math_005.Vector
        nt.links.new(
            nt.nodes["Vector Math.002"].outputs[0],
            nt.nodes["Vector Math.005"].inputs[0]
        )
        # vector_math_002.Vector -> vector_math_005.Vector
        nt.links.new(
            nt.nodes["Vector Math.002"].outputs[0],
            nt.nodes["Vector Math.005"].inputs[1]
        )
        # vector_math_004.Vector -> vector_math_006.Vector
        nt.links.new(
            nt.nodes["Vector Math.004"].outputs[0],
            nt.nodes["Vector Math.006"].inputs[0]
        )
        # vector_math_004.Vector -> vector_math_006.Vector
        nt.links.new(
            nt.nodes["Vector Math.004"].outputs[0],
            nt.nodes["Vector Math.006"].inputs[1]
        )
        # vector_math_006.Value -> math.Value
        nt.links.new(
            nt.nodes["Vector Math.006"].outputs[1],
            nt.nodes["Math"].inputs[1]
        )
        # vector_math_005.Value -> math.Value
        nt.links.new(
            nt.nodes["Vector Math.005"].outputs[1],
            nt.nodes["Math"].inputs[0]
        )
        # vector_math_002.Vector -> mix.A
        nt.links.new(
            nt.nodes["Vector Math.002"].outputs[0],
            nt.nodes["Mix"].inputs[4]
        )
        # math.Value -> mix.Factor
        nt.links.new(
            nt.nodes["Math"].outputs[0],
            nt.nodes["Mix"].inputs[0]
        )
        # mix.Result -> vector_math_007.Vector
        nt.links.new(
            nt.nodes["Mix"].outputs[1],
            nt.nodes["Vector Math.007"].inputs[0]
        )
        # vector_math_007.Vector -> separate_xyz.Vector
        nt.links.new(
            nt.nodes["Vector Math.007"].outputs[0],
            nt.nodes["Separate XYZ"].inputs[0]
        )
        # separate_xyz.Y -> math_001.Value
        nt.links.new(
            nt.nodes["Separate XYZ"].outputs[1],
            nt.nodes["Math.001"].inputs[0]
        )
        # separate_xyz.X -> math_002.Value
        nt.links.new(
            nt.nodes["Separate XYZ"].outputs[0],
            nt.nodes["Math.002"].inputs[0]
        )
        # math_002.Value -> math_001.Value
        nt.links.new(
            nt.nodes["Math.002"].outputs[0],
            nt.nodes["Math.001"].inputs[2]
        )
        # separate_xyz.X -> math_003.Value
        nt.links.new(
            nt.nodes["Separate XYZ"].outputs[0],
            nt.nodes["Math.003"].inputs[0]
        )
        # math_001.Value -> math_003.Value
        nt.links.new(
            nt.nodes["Math.001"].outputs[0],
            nt.nodes["Math.003"].inputs[1]
        )
        # math_003.Value -> math_004.Value
        nt.links.new(
            nt.nodes["Math.003"].outputs[0],
            nt.nodes["Math.004"].inputs[0]
        )
        # group_input_001.Line Thickness -> math_006.Value
        nt.links.new(
            nt.nodes["Group Input.001"].outputs[2],
            nt.nodes["Math.006"].inputs[1]
        )
        # math_006.Value -> map_range.From Min
        nt.links.new(
            nt.nodes["Math.006"].outputs[0],
            nt.nodes["Map Range"].inputs[1]
        )
        # group_input_001.Smoothness -> math_007.Value
        nt.links.new(
            nt.nodes["Group Input.001"].outputs[3],
            nt.nodes["Math.007"].inputs[1]
        )
        # math_006.Value -> math_007.Value
        nt.links.new(
            nt.nodes["Math.006"].outputs[0],
            nt.nodes["Math.007"].inputs[0]
        )
        # math_007.Value -> map_range.From Max
        nt.links.new(
            nt.nodes["Math.007"].outputs[0],
            nt.nodes["Map Range"].inputs[2]
        )
        # map_range.Result -> group_output.Grid Lines
        nt.links.new(
            nt.nodes["Map Range"].outputs[0],
            nt.nodes["Group Output"].inputs[1]
        )
        # math_004.Value -> group_output.Distance to Edge
        nt.links.new(
            nt.nodes["Math.004"].outputs[0],
            nt.nodes["Group Output"].inputs[2]
        )
        # reroute_001.Output -> vector_math_008.Vector
        nt.links.new(
            nt.nodes["Reroute.001"].outputs[0],
            nt.nodes["Vector Math.008"].inputs[0]
        )
        # vector_math.Vector -> reroute_001.Input
        nt.links.new(
            nt.nodes["Vector Math"].outputs[0],
            nt.nodes["Reroute.001"].inputs[0]
        )
        # mix.Result -> vector_math_008.Vector
        nt.links.new(
            nt.nodes["Mix"].outputs[1],
            nt.nodes["Vector Math.008"].inputs[1]
        )
        # white_noise_texture.Color -> group_output.Random Color
        nt.links.new(
            nt.nodes["White Noise Texture"].outputs[1],
            nt.nodes["Group Output"].inputs[0]
        )
        # math_004.Value -> map_range.Value
        nt.links.new(
            nt.nodes["Math.004"].outputs[0],
            nt.nodes["Map Range"].inputs[0]
        )
        # combine_xyz_002.Vector -> vector_math_004.Vector
        nt.links.new(
            nt.nodes["Combine XYZ.002"].outputs[0],
            nt.nodes["Vector Math.004"].inputs[2]
        )
        # combine_xyz_002.Vector -> vector_math_002.Vector
        nt.links.new(
            nt.nodes["Combine XYZ.002"].outputs[0],
            nt.nodes["Vector Math.002"].inputs[2]
        )
        # vector_math_004.Vector -> mix.B
        nt.links.new(
            nt.nodes["Vector Math.004"].outputs[0],
            nt.nodes["Mix"].inputs[5]
        )
        # mix.Result -> group_output.Cell Center Vector
        nt.links.new(
            nt.nodes["Mix"].outputs[1],
            nt.nodes["Group Output"].inputs[3]
        )
        # vector_math_009.Vector -> white_noise_texture.Vector
        nt.links.new(
            nt.nodes["Vector Math.009"].outputs[0],
            nt.nodes["White Noise Texture"].inputs[0]
        )
        # vector_math_008.Vector -> vector_math_009.Vector
        nt.links.new(
            nt.nodes["Vector Math.008"].outputs[0],
            nt.nodes["Vector Math.009"].inputs[0]
        )
        # math_008.Value -> mix_006.Factor
        nt.links.new(
            nt.nodes["Math.008"].outputs[0],
            nt.nodes["Mix.006"].inputs[0]
        )
        # texture_coordinate_001.Generated -> mix_006.A
        nt.links.new(
            nt.nodes["Texture Coordinate.001"].outputs[0],
            nt.nodes["Mix.006"].inputs[6]
        )
        # math_009.Value -> math_008.Value
        nt.links.new(
            nt.nodes["Math.009"].outputs[0],
            nt.nodes["Math.008"].inputs[0]
        )
        # mix_006.Result -> vector_math.Vector
        nt.links.new(
            nt.nodes["Mix.006"].outputs[2],
            nt.nodes["Vector Math"].inputs[0]
        )
        # group_input.Vector -> mix_006.B
        nt.links.new(
            nt.nodes["Group Input"].outputs[0],
            nt.nodes["Mix.006"].inputs[7]
        )
        # group_input.Vector -> math_009.Value
        nt.links.new(
            nt.nodes["Group Input"].outputs[0],
            nt.nodes["Math.009"].inputs[0]
        )

        return nt


