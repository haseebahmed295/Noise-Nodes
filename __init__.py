
from .Voxel_node import ShaderNodeVoxel
from .Cranal_node import ShaderNodeCranal
from .Pixelator_node import ShaderNodePixelator
from .Scratches_node import ShaderNodeScratches
from .Dots_node import ShaderNodeDots
from .Regular_node import ShaderNodeRegular
from .Dent_node import ShaderNodeDent
from .Fractal_node import ShaderNodeFractal
from .Streaks_node import ShaderNodeStreaks
from .Fluid_node import ShaderNodeFluid
from .Crackle_node import ShaderNodeCrackle
from .Perlin_node import ShaderNodePerlin
from .Step_node import ShaderNodeStep
from .Wavy_node import ShaderNodeWavy
import bl_ui
import bpy


import bpy,nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
from bpy.types import Menu
from bl_ui import node_add_menu


bl_info = {
    "name": "Noise Nodes",
    "description": "Advance Noise Nodes For blender",
    "author": "haseebahmad295",
    "version": (0, 3, 0),
    "blender": (4, 0, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }
    




class ExtraNodesCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return (context.space_data.tree_type == 'ShaderNodeTree' and
                context.scene.render.engine in ['BLENDER_EEVEE', 'CYCLES'])



nodes = [
    ShaderNodeVoxel,
    ShaderNodeCranal,
    ShaderNodePixelator,
    ShaderNodeScratches,
    ShaderNodeDots,
    ShaderNodeRegular,
    ShaderNodeStreaks,
    ShaderNodeFractal,
    ShaderNodeDent,
    ShaderNodeFluid,
    ShaderNodeCrackle,
    ShaderNodePerlin,
    ShaderNodeStep,
    ShaderNodeWavy
]

node_categories = [
    ExtraNodesCategory("SH_NoiseNodes", "NoiseNodes", items=[node.__name__ for node in nodes]),
    ]

class NODE_MT_category_shader_noise(bpy.types.Menu):
    bl_idname = "NODE_MT_category_shader_noise"
    bl_label = "Noise Nodes"

    def draw(self, context):
        layout = self.layout
        for cls in nodes:
            bl_ui.node_add_menu.add_node_type(layout, cls.__name__)
        bl_ui.node_add_menu.draw_assets_for_catalog(layout, self.bl_label)

def menu_draw(self, context):
    layout = self.layout
    layout.menu("NODE_MT_category_shader_noise")

def register():
    bpy.utils.register_class(NODE_MT_category_shader_noise)
    bpy.types.NODE_MT_shader_node_add_all.append(menu_draw)
    nodeitems_utils.register_node_categories("NOISE_NODES", node_categories)
    
    for cls in nodes:
        bpy.utils.register_class(cls)
    
def unregister():
    bpy.utils.unregister_class(NODE_MT_category_shader_noise)
    bpy.types.NODE_MT_shader_node_add_all.remove(menu_draw)
    nodeitems_utils.unregister_node_categories("NOISE_NODES")
    
    for cls in nodes:
        bpy.utils.unregister_class(cls)