import bpy
from .utils import ShaderNode
class ShaderNodeWavy(ShaderNode):
    bl_name='Wavy Noise'
    bl_label='Wavy Noise'
    bl_icon='NONE'

    # ('NodeSocketBool', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketShader', 'NodeSocketFloat', 'NodeSocketColor')
    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Scale'].default_value = 5
        self.inputs['Detail'].default_value = 5
        self.inputs['Line Thickness'].default_value = 2
        self.inputs['Dimension'].default_value = 0
        self.inputs['W'].hide = True

    def createNodetree(self, name) :
        nt = self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
        
        nt.color_tag = 'NONE'
        nt.description = ""

        #nt interface
        #Socket Mask
        mask_socket = nt.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
        mask_socket.default_value = 0.0
        mask_socket.min_value = -3.4028234663852886e+38
        mask_socket.max_value = 3.4028234663852886e+38
        mask_socket.subtype = 'NONE'
        mask_socket.attribute_domain = 'POINT'
        
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
        scale_socket.default_value = 8.399999618530273
        scale_socket.min_value = -1000.0
        scale_socket.max_value = 1000.0
        scale_socket.subtype = 'NONE'
        scale_socket.attribute_domain = 'POINT'
        
        #Socket Detail
        detail_socket = nt.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
        detail_socket.default_value = 7.800000190734863
        detail_socket.min_value = 0.0
        detail_socket.max_value = 16.0
        detail_socket.subtype = 'NONE'
        detail_socket.attribute_domain = 'POINT'
        
        #Socket LineThickness
        linethickness_socket = nt.interface.new_socket(name = "Line Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
        linethickness_socket.default_value = 0.0
        linethickness_socket.min_value = -3.4028234663852886e+38
        linethickness_socket.max_value = 3.4028234663852886e+38
        linethickness_socket.subtype = 'NONE'
        linethickness_socket.attribute_domain = 'POINT'
        
        #Socket Dimension
        dimension_socket = nt.interface.new_socket(name = "Dimension", in_out='INPUT', socket_type = 'NodeSocketFloat')
        dimension_socket.default_value = 0.0
        dimension_socket.min_value = 0.0
        dimension_socket.max_value = 1000.0
        dimension_socket.subtype = 'NONE'
        dimension_socket.attribute_domain = 'POINT'
        
        
        #initialize nt nodes
        #node Musgrave Texture
        musgrave_texture = nt.nodes.new("ShaderNodeTexNoise")
        musgrave_texture.name = "Musgrave Texture"
        musgrave_texture.noise_dimensions = '3D'
        musgrave_texture.noise_type = 'MULTIFRACTAL'
        musgrave_texture.normalize = False
        #Lacunarity
        musgrave_texture.inputs[5].default_value = 1.0
        #Distortion
        musgrave_texture.inputs[8].default_value = 0.0
        
        #node ColorRamp
        colorramp = nt.nodes.new("ShaderNodeValToRGB")
        colorramp.name = "ColorRamp"
        colorramp.color_ramp.color_mode = 'RGB'
        colorramp.color_ramp.hue_interpolation = 'NEAR'
        colorramp.color_ramp.interpolation = 'CONSTANT'
        
        #initialize color ramp elements
        colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
        colorramp_cre_0 = colorramp.color_ramp.elements[0]
        colorramp_cre_0.position = 0.0
        colorramp_cre_0.alpha = 1.0
        colorramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

        colorramp_cre_1 = colorramp.color_ramp.elements.new(0.5045453906059265)
        colorramp_cre_1.alpha = 1.0
        colorramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)

        
        #node Group Output
        group_output = nt.nodes.new("NodeGroupOutput")
        group_output.name = "Group Output"
        group_output.is_active_output = True
        
        #node Math
        math = nt.nodes.new("ShaderNodeMath")
        math.name = "Math"
        math.operation = 'COMPARE'
        math.use_clamp = False
        #Value_002
        math.inputs[2].default_value = 0.0
        
        #node Group Input
        group_input = nt.nodes.new("NodeGroupInput")
        group_input.name = "Group Input"
        
        #node Math.001
        math_001 = nt.nodes.new("ShaderNodeMath")
        math_001.name = "Math.001"
        math_001.hide = True
        math_001.operation = 'MINIMUM'
        math_001.use_clamp = False
        #Value_001
        math_001.inputs[1].default_value = 14.0
        
        #node Math.002
        math_002 = nt.nodes.new("ShaderNodeMath")
        math_002.name = "Math.002"
        math_002.hide = True
        math_002.operation = 'SUBTRACT'
        math_002.use_clamp = False
        #Value_001
        math_002.inputs[1].default_value = 1.0
        
        #node Clamp
        clamp = nt.nodes.new("ShaderNodeClamp")
        clamp.name = "Clamp"
        clamp.hide = True
        clamp.clamp_type = 'MINMAX'
        #Min
        clamp.inputs[1].default_value = 0.0
        #Max
        clamp.inputs[2].default_value = 1.0
        
        #node Math.003
        math_003 = nt.nodes.new("ShaderNodeMath")
        math_003.name = "Math.003"
        math_003.hide = True
        math_003.operation = 'MULTIPLY'
        math_003.use_clamp = False
        
        #node Math.004
        math_004 = nt.nodes.new("ShaderNodeMath")
        math_004.name = "Math.004"
        math_004.hide = True
        math_004.operation = 'SUBTRACT'
        math_004.use_clamp = True
        #Value
        math_004.inputs[0].default_value = 1.0
        
        #node Math.005
        math_005 = nt.nodes.new("ShaderNodeMath")
        math_005.name = "Math.005"
        math_005.hide = True
        math_005.operation = 'ADD'
        math_005.use_clamp = False
        
        #node Math.006
        math_006 = nt.nodes.new("ShaderNodeMath")
        math_006.name = "Math.006"
        math_006.hide = True
        math_006.operation = 'MAXIMUM'
        math_006.use_clamp = False
        #Value_001
        math_006.inputs[1].default_value = -9.999999747378752e-06
        
        #node Math.007
        math_007 = nt.nodes.new("ShaderNodeMath")
        math_007.name = "Math.007"
        math_007.hide = True
        math_007.operation = 'MULTIPLY'
        math_007.use_clamp = False
        #Value_001
        math_007.inputs[1].default_value = -1.0
        
        #node Math.008
        math_008 = nt.nodes.new("ShaderNodeMath")
        math_008.name = "Math.008"
        math_008.hide = True
        math_008.operation = 'POWER'
        math_008.use_clamp = False
        #Value
        math_008.inputs[0].default_value = 1.0
        
        #node Bright/Contrast
        bright_contrast = nt.nodes.new("ShaderNodeBrightContrast")
        bright_contrast.name = "Bright/Contrast"
        #Bright
        bright_contrast.inputs[1].default_value = 0.0
        
        #node Mix
        mix = nt.nodes.new("ShaderNodeMix")
        mix.name = "Mix"
        mix.blend_type = 'MIX'
        mix.clamp_factor = True
        mix.clamp_result = False
        mix.data_type = 'RGBA'
        mix.factor_mode = 'UNIFORM'
        
        #node Hue Saturation Value
        hue_saturation_value = nt.nodes.new("ShaderNodeHueSaturation")
        hue_saturation_value.name = "Hue Saturation Value"
        #Hue
        hue_saturation_value.inputs[0].default_value = 0.5
        #Saturation
        hue_saturation_value.inputs[1].default_value = 1.0
        #Value
        hue_saturation_value.inputs[2].default_value = 0.0
        #Fac
        hue_saturation_value.inputs[3].default_value = 1.0
        #Color
        hue_saturation_value.inputs[4].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        
        #node Hue Saturation Value.001
        hue_saturation_value_001 = nt.nodes.new("ShaderNodeHueSaturation")
        hue_saturation_value_001.name = "Hue Saturation Value.001"
        #Hue
        hue_saturation_value_001.inputs[0].default_value = 0.5
        #Saturation
        hue_saturation_value_001.inputs[1].default_value = 1.0
        #Value
        hue_saturation_value_001.inputs[2].default_value = 1.0
        #Fac
        hue_saturation_value_001.inputs[3].default_value = 1.0
        #Color
        hue_saturation_value_001.inputs[4].default_value = (1.0, 1.0, 1.0, 1.0)
        
        
        #Set locations
        musgrave_texture.location = (-319.5953674316406, 35.24851989746094)
        colorramp.location = (-35.19441604614258, -79.08134460449219)
        group_output.location = (1101.0281982421875, 73.40489196777344)
        math.location = (380.554931640625, 177.0710906982422)
        group_input.location = (-873.1984252929688, -208.5149383544922)
        math_001.location = (-319.5953674316406, -284.75146484375)
        math_002.location = (-319.5953674316406, -324.75146484375)
        clamp.location = (-319.5953674316406, 75.24851989746094)
        math_003.location = (-319.5953674316406, 115.24851989746094)
        math_004.location = (-319.5953674316406, 155.24851989746094)
        math_005.location = (-319.5953674316406, 195.24851989746094)
        math_006.location = (-319.5953674316406, -442.5599670410156)
        math_007.location = (-319.5953674316406, -402.5599365234375)
        math_008.location = (-319.5953674316406, -364.75146484375)
        bright_contrast.location = (-24.859228134155273, 432.16552734375)
        mix.location = (178.04879760742188, 432.65887451171875)
        hue_saturation_value.location = (-29.928512573242188, 298.6106262207031)
        hue_saturation_value_001.location = (-26.235519409179688, 123.8736572265625)
        
        #Set dimensions
        musgrave_texture.width, musgrave_texture.height = 150.0, 100.0
        colorramp.width, colorramp.height = 240.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0
        math.width, math.height = 140.0, 100.0
        group_input.width, group_input.height = 140.0, 100.0
        math_001.width, math_001.height = 140.0, 100.0
        math_002.width, math_002.height = 140.0, 100.0
        clamp.width, clamp.height = 140.0, 100.0
        math_003.width, math_003.height = 140.0, 100.0
        math_004.width, math_004.height = 140.0, 100.0
        math_005.width, math_005.height = 140.0, 100.0
        math_006.width, math_006.height = 140.0, 100.0
        math_007.width, math_007.height = 140.0, 100.0
        math_008.width, math_008.height = 140.0, 100.0
        bright_contrast.width, bright_contrast.height = 140.0, 100.0
        mix.width, mix.height = 140.0, 100.0
        hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
        hue_saturation_value_001.width, hue_saturation_value_001.height = 150.0, 100.0
        
        #initialize nt links
        #group_input.Vector -> musgrave_texture.Vector
        nt.links.new(group_input.outputs[0], musgrave_texture.inputs[0])
        #group_input.Scale -> musgrave_texture.Scale
        nt.links.new(group_input.outputs[2], musgrave_texture.inputs[2])
        #math.Value -> group_output.Mask
        nt.links.new(math.outputs[0], group_output.inputs[0])
        #colorramp.Color -> math.Value
        nt.links.new(colorramp.outputs[0], math.inputs[0])
        #group_input.Detail -> math_002.Value
        nt.links.new(group_input.outputs[3], math_002.inputs[0])
        #math_002.Value -> math_001.Value
        nt.links.new(math_002.outputs[0], math_001.inputs[0])
        #math_001.Value -> musgrave_texture.Detail
        nt.links.new(math_001.outputs[0], musgrave_texture.inputs[3])
        #math_005.Value -> colorramp.Fac
        nt.links.new(math_005.outputs[0], colorramp.inputs[0])
        #math_003.Value -> math_005.Value
        nt.links.new(math_003.outputs[0], math_005.inputs[0])
        #group_input.Detail -> math_004.Value
        nt.links.new(group_input.outputs[3], math_004.inputs[1])
        #math_004.Value -> math_005.Value
        nt.links.new(math_004.outputs[0], math_005.inputs[1])
        #musgrave_texture.Fac -> math_003.Value
        nt.links.new(musgrave_texture.outputs[0], math_003.inputs[0])
        #group_input.Detail -> clamp.Value
        nt.links.new(group_input.outputs[3], clamp.inputs[0])
        #clamp.Result -> math_003.Value
        nt.links.new(clamp.outputs[0], math_003.inputs[1])
        #group_input.Dimension -> math_006.Value
        nt.links.new(group_input.outputs[5], math_006.inputs[0])
        #math_007.Value -> math_008.Value
        nt.links.new(math_007.outputs[0], math_008.inputs[1])
        #math_008.Value -> musgrave_texture.Roughness
        nt.links.new(math_008.outputs[0], musgrave_texture.inputs[4])
        #math_006.Value -> math_007.Value
        nt.links.new(math_006.outputs[0], math_007.inputs[0])
        #bright_contrast.Color -> mix.Factor
        nt.links.new(bright_contrast.outputs[0], mix.inputs[0])
        #hue_saturation_value.Color -> mix.A
        nt.links.new(hue_saturation_value.outputs[0], mix.inputs[6])
        #hue_saturation_value_001.Color -> mix.B
        nt.links.new(hue_saturation_value_001.outputs[0], mix.inputs[7])
        #math_005.Value -> bright_contrast.Color
        nt.links.new(math_005.outputs[0], bright_contrast.inputs[0])
        #group_input.LineThickness -> bright_contrast.Contrast
        nt.links.new(group_input.outputs[4], bright_contrast.inputs[2])
        #mix.Result -> math.Value
        nt.links.new(mix.outputs[2], math.inputs[1])
        #group_input.W -> musgrave_texture.W
        nt.links.new(group_input.outputs[1], musgrave_texture.inputs[1])
        return nt



