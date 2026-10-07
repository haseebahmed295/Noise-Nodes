import bpy
import bl_ui
from bpy.app.translations import pgettext_iface as iface_

from .translations import langs
from .node_imp import NodeLib
from .icons import Icon
from .na import ng_register , ng_unregister
from .override import enable_override_node_wrangler , disable_override_node_wrangler


bl_info = {
    "name": "Noise Nodes",
    "description": "Advanced Noise Nodes for Blender's Shader and Geometry Nodes",
    "author": "haseebahmad295",
    "version": (0, 6, 0),
    "blender": (4, 0, 0),
    "location": "Node Editor > Add Menu",
    "warning": "This addon is still in development",
    "doc_url": "https://github.com/haseebahmed295/Noise-Nodes",
    "tracker_url": "https://github.com/haseebahmed295/Noise-Nodes/issues",
    "category": "Node",
}

class NODE_MT_category_noise(bpy.types.Menu):
    bl_idname = "NODE_MT_category_noise"
    bl_label = "Noise Nodes"
    bl_description = "Advanced noise generation nodes"

    @classmethod
    def poll(cls, context):
        """Only show menu in supported node editors"""
        return context.space_data.tree_type in {"ShaderNodeTree", "GeometryNodeTree"}

    def draw(self, context):
        layout = self.layout
        geometry_nodes, shader_nodes = NodeLib.get_node_sets()

        # Determine active node tree type
        node_classes = (
            shader_nodes
            if context.space_data.tree_type == "ShaderNodeTree"
            else geometry_nodes
        )

        if not node_classes:
            layout.label(text="No nodes available", icon="ERROR")
            return

        # Draw nodes with separators for better organization
        for node_class in sorted(node_classes, key=lambda x: x.bl_label):
            props = layout.operator(
                "node.add_node",
                text=iface_(node_class.bl_label),
                icon_value=Icon.get_icon(node_class.bl_label),
            )
            props.type = node_class.__name__
            props.use_transform = True



def menu_draw(self, context):
    """Draw menu entry if conditions are met"""
    if NODE_MT_category_noise.poll(context):
        self.layout.menu(NODE_MT_category_noise.bl_idname)


def register():

        # Register icons and classes
        Icon.register_icons()
        bpy.utils.register_class(NODE_MT_category_noise)

        # Add to menus
        bpy.types.NODE_MT_shader_node_add_all.append(menu_draw)
        bpy.types.NODE_MT_geometry_node_add_all.append(menu_draw)

        # Register node classes
        geometry_nodes, shader_nodes = NodeLib.get_node_sets()
        for cls in geometry_nodes + shader_nodes:
            bpy.utils.register_class(cls)

        # Register translations
        bpy.app.translations.register(__name__, langs)
        try:
            ng_register()
        except Exception as e:
            print(f"Noide Node Registration failed: {e}")
        try:
            enable_override_node_wrangler()
        except:
            pass


def unregister():
        try:
            disable_override_node_wrangler()
        except:
            pass
        # try:
        ng_unregister()
        # except Exception as e:
        #     print(f"Noide Node Unregistration failed: {e}")

        # Unregister nodes
        geometry_nodes, shader_nodes = NodeLib.get_node_sets()
        for cls in geometry_nodes + shader_nodes:
            bpy.utils.unregister_class(cls)

        # Remove from menus
        bpy.types.NODE_MT_shader_node_add_all.remove(menu_draw)
        bpy.types.NODE_MT_geometry_node_add_all.remove(menu_draw)

        # Unregister classes
        Icon.unregister_icons()
        bpy.utils.unregister_class(NODE_MT_category_noise)


        # Cleanup
        bpy.app.translations.unregister(__name__)

    

if __name__ == "__main__":
    register()
