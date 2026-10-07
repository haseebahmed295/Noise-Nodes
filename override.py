import bpy

#Node wrangle Crtl + T override to make noise nodes recongized as texture nodes
def enable_override_node_wrangler():
    if not "node_wrangler" in bpy.context.preferences.addons:
        return
    from node_wrangler import operators # type: ignore 
    operators.get_texture_node_types = lambda:[
        "ShaderNodeTexBrick",
        "ShaderNodeTexChecker",
        "ShaderNodeTexEnvironment",
        "ShaderNodeTexGabor",
        "ShaderNodeTexGradient",
        "ShaderNodeTexIES",
        "ShaderNodeTexImage",
        "ShaderNodeTexMagic",
        "ShaderNodeTexMusgrave",
        "ShaderNodeTexNoise",
        "ShaderNodeTexPointDensity",
        "ShaderNodeTexSky",
        "ShaderNodeTexVoronoi",
        "ShaderNodeTexWave",
        "ShaderNodeTexWhiteNoise",
        "ShaderNodeCrackle",
        "ShaderNodeCranal",
        "ShaderNodeDent",
        "ShaderNodeDots",
        "ShaderNodeFluid",
        "ShaderNodeFractal",
        "ShaderNodePerlin",
        "ShaderNodePixelator",
        "ShaderNodeRegular",
        "ShaderNodeScratches",
        "ShaderNodeStep",
        "ShaderNodeStreaks",
        "ShaderNodeVoxel",
        "ShaderNodeWavy",
        "ShaderNodeHex",
        "ShaderNodeContour",
        "ShaderNodeCellular"
    ]

def disable_override_node_wrangler():
    if not "node_wrangler" in bpy.context.preferences.addons:
        return
    from node_wrangler import operators # type: ignore 
    operators.get_texture_node_types = lambda:[
        "ShaderNodeTexBrick",
        "ShaderNodeTexChecker",
        "ShaderNodeTexEnvironment",
        "ShaderNodeTexGabor",
        "ShaderNodeTexGradient",
        "ShaderNodeTexIES",
        "ShaderNodeTexImage",
        "ShaderNodeTexMagic",
        "ShaderNodeTexMusgrave",
        "ShaderNodeTexNoise",
        "ShaderNodeTexPointDensity",
        "ShaderNodeTexSky",
        "ShaderNodeTexVoronoi",
        "ShaderNodeTexWave",
        "ShaderNodeTexWhiteNoise"
    ]