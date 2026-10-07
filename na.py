import bpy
from .node_imp import NodeLib
from bpy.app.handlers import persistent


class Node_Info(bpy.types.PropertyGroup):
    is_noise_node: bpy.props.BoolProperty(default=False)
    bl_idname: bpy.props.StringProperty()
    dimension: bpy.props.StringProperty()
    ng_name: bpy.props.StringProperty()

def check_mat_nodes(mat):
    '''Blender 5.0 will remove use_nodes'''
    return (hasattr(mat, "use_nodes") and mat.use_nodes) and mat.node_tree and mat.node_tree.nodes

@persistent
def convert_to_nodegroup(dummy=None):
    geometrynodes, shadernodes = NodeLib.get_node_sets()
    shader_nodes = [node.__name__ for node in shadernodes]
    geometry_nodes = [node.__name__ for node in geometrynodes]

    # Process Shader Nodes
    for mat in bpy.data.materials:
        if check_mat_nodes(mat):
            search_noise_nodes(mat.node_tree, shader_nodes)

    # Process Geometry Nodes
    for obj in bpy.data.objects:
        if obj.modifiers:
            for mod in obj.modifiers:
                if mod.type == 'NODES' and mod.node_group and mod.node_group.nodes:
                    search_noise_nodes(mod.node_group, geometry_nodes)

def search_noise_nodes(node_tree , node_list):
    for node in node_tree.nodes:
        if node.type == 'GROUP':
            if not node.node_tree or not node.node_tree.nodes:
                continue
            search_noise_nodes(node.node_tree , node_list)
        if node.bl_idname in node_list:
            process_node(node_tree, node)

def search_noise_group(node_tree , nds:list , type:str = 'SHADER'):
    if not node_tree.nodes:
        return
    if type == 'SHADER':
        for node in node_tree.nodes:
            if node.type == 'GROUP':
                if not node.node_tree or not node.node_tree.nodes:
                    continue
                if hasattr(node, 'Node_Info') and node.Node_Info.is_noise_node:
                    itm = process_node_group(node_tree, node)
                    nds.append(itm)
                else:
                    search_noise_group(node.node_tree , nds , type)
            elif node.bl_idname == "NodeUndefined":
                handle_legacy_nodes()
    else:
        for node in node_tree.nodes:
            if node.type == 'GROUP':
                if not node.node_tree or not node.node_tree.nodes:
                    continue
                if hasattr(node, 'Node_Info') and node.Node_Info.is_noise_node:
                    itm = process_node_group(node_tree, node)
                    nds.append(itm)
                else:
                    search_noise_group(node.node_tree , nds , type)
            
@persistent
def convert_to_node(dummy=None):
    nds = []
    # Process Shader Nodes
    for mat in bpy.data.materials:
        if check_mat_nodes(mat):
            search_noise_group(mat.node_tree,nds)
                
    
    # Process Geometry Nodes
    for obj in bpy.data.objects:
        if obj.modifiers:
            for mod in obj.modifiers:
                if mod.type == 'NODES' and mod.node_group and mod.node_group.nodes:
                    search_noise_group(mod.node_group , nds , 'GEOMETRY')

    # Clean up unused node groups
    for nd in bpy.data.node_groups:
        if nd.users == 0:
            bpy.data.node_groups.remove(nd, do_unlink=True)

@persistent
def check_linked_nodes(dummy=None):
    """Check nodes when data is linked or appended."""
    # Check Shader Nodes
    for mat in bpy.data.materials:
        if check_mat_nodes(mat):
            for node in mat.node_tree.nodes:
                if node.type == 'GROUP':
                    if not node.node_tree or not node.node_tree.nodes:
                        continue
                    if hasattr(node, 'Node_Info') and node.Node_Info.is_noise_node:
                        process_node_group(mat.node_tree, node)
                    else:
                        search_noise_group(node.node_tree , [])

    # Check Geometry Nodes
    for obj in bpy.data.objects:
        if obj.modifiers:
            for mod in obj.modifiers:
                if mod.type == 'NODES' and mod.node_group and mod.node_group.nodes:
                    for node in mod.node_group.nodes:
                            if node.type == 'GROUP':
                                if not node.node_tree or not node.node_tree.nodes:
                                    continue
                                if hasattr(node, 'Node_Info') and node.Node_Info.is_noise_node:
                                    process_node_group(mod.node_group, node)
                                else:
                                    search_noise_group(node.node_tree , [])


# noise node to node group
def process_node(node_tree, node):
    try:
        # Determine if this is a shader or geometry node tree
        group_type = "ShaderNodeGroup" if node_tree.type == 'SHADER' else "GeometryNodeGroup"
        new_node = node_tree.nodes.new(group_type)
        new_node.node_tree = node.node_tree
        new_node.parent = node.parent
        temp_name = node.name
        new_node.label = node.label
        new_node.location = node.location
        if not hasattr(new_node, 'Node_Info'):
            return

        new_node.Node_Info.is_noise_node = True
        new_node.Node_Info.bl_idname = node.bl_idname
        new_node.Node_Info.ng_name = node.node_tree.name

        if hasattr(node, 'dimension'):
            new_node.Node_Info.dimension = node.dimension

        for input in node.inputs:
            new_input = new_node.inputs.get(input.name)
            if new_input:
                new_input.default_value = input.default_value
                if input.is_linked and input.links:
                    link_out = input.links[0].from_socket
                    node_tree.links.new(link_out, new_input)

        for output in node.outputs:
            new_output = new_node.outputs.get(output.name)
            if new_output and output.is_linked and output.links:
                for link in output.links:
                        link_in = link.to_socket
                        node_tree.links.new(new_output, link_in)

        node_tree.nodes.remove(node)
        new_node.name = temp_name

    except Exception as e:
        print(f"Error processing node {node.name}: {str(e)}")

# node group to noise node
def process_node_group(node_tree, node):
    try:
        if not hasattr(node, 'Node_Info'):
            return

        new_node = node_tree.nodes.new(node.Node_Info.bl_idname)
        new_node.parent = node.parent
        new_node.location = node.location
        temp_name = node.name
        new_node.label = node.label
        ng_name = node.Node_Info.ng_name
        if hasattr(new_node, 'dimension') and node.Node_Info.dimension:
            new_node.dimension = node.Node_Info.dimension

        for input in node.inputs:
            new_input = new_node.inputs.get(input.name)
            if new_input:
                new_input.default_value = input.default_value
                if input.is_linked and input.links:
                    link_out = input.links[0].from_socket
                    node_tree.links.new(link_out, new_input)

        for output in node.outputs:
            new_output = new_node.outputs.get(output.name)
            if new_output and output.is_linked and output.links:
                for link in output.links:
                    if hasattr(link, 'to_socket'):
                        link_in = link.to_socket
                        node_tree.links.new(new_output, link_in)
        node_tree.nodes.remove(node)
        new_node.name = temp_name
        return (new_node.node_tree ,ng_name)

    except Exception as e:
        print(f"Error processing node group {node.name}: {str(e)}")

def replace_legacy_node(node_tree, node , shadernode_id):
    new_node = node_tree.nodes.new(shadernode_id)
    new_node.location = node.location
    new_node.label = node.label
    temp_name = node.name  # Preserve name directly

    # Copy inputs
    for input in node.inputs:
        new_input = new_node.inputs.get(input.name)
        if new_input:
            new_input.default_value = input.default_value
            if input.is_linked and input.links:
                link_out = input.links[0].from_socket
                node_tree.links.new(link_out, new_input)

    # Copy outputs
    for output in node.outputs:
        new_output = new_node.outputs.get(output.name)
        if new_output and output.is_linked and output.links:
            for link in output.links:
                    link_in = link.to_socket
                    node_tree.links.new(new_output, link_in)

    node_tree.nodes.remove(node)
    new_node.name = temp_name

def handle_legacy_nodes():
    from .nodes.utils import ShaderNode
    _, shadernodes = NodeLib.get_node_sets()
    dynamic_classes = []
    # Register dynamic classes
    for shadernode in shadernodes:
        # Define default methods if not present in original node
        def default_init(self, context):
            pass

        def default_createNodetree(self, name):
            node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
            return node_tree

        # Get init and createNodetree methods from original node, or use defaults
        init_method = getattr(shadernode, 'init', default_init)
        createNodetree_method = getattr(
            shadernode, 'createNodetree', default_createNodetree)

        # Create dynamic class inheriting from ShaderNode
        class_dict = {
            'bl_idname': shadernode.bl_label,
            'bl_label': shadernode.bl_label,
            'init': init_method,
            'createNodetree': createNodetree_method
        }
        DynamicSubClass = type(shadernode.bl_label, (ShaderNode,), class_dict)

        
        bpy.utils.register_class(DynamicSubClass)
        dynamic_classes.append(DynamicSubClass)

    # Process materials
    for mat in bpy.data.materials:
        if check_mat_nodes(mat):
            for node in mat.node_tree.nodes:
                for shadernode in shadernodes:
                    if node.bl_idname == shadernode.bl_label or node.bl_idname == "NodeUndefined":
                        replace_legacy_node(
                            mat.node_tree, node, shadernode.__name__)
                        break

    # Unregister dynamic classes
    for _class in dynamic_classes:
        bpy.utils.unregister_class(_class)


def ng_register():
    # Register the Node_Info class and attach it to both ShaderNodeGroup and GeometryNodeGroup
    if not hasattr(bpy.types.ShaderNodeGroup, 'Node_Info'):
        bpy.utils.register_class(Node_Info)
        bpy.types.ShaderNodeGroup.Node_Info = bpy.props.PointerProperty(
            type=Node_Info)
        bpy.types.GeometryNodeGroup.Node_Info = bpy.props.PointerProperty(
            type=Node_Info)

    # Register handlers
    if convert_to_nodegroup not in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.append(convert_to_nodegroup)
    if convert_to_node not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(convert_to_node)
    if convert_to_node not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(convert_to_node)
    if bpy.app.version >= (4, 3, 0):
        if check_linked_nodes not in bpy.app.handlers.blend_import_post:
            bpy.app.handlers.blend_import_post.append(check_linked_nodes)

    # Register timer for initial conversion
    if not bpy.app.timers.is_registered(convert_to_node):
        bpy.app.timers.register(convert_to_node, first_interval=0.1)


def ng_unregister():
    # Run conversion before unregistering
    convert_to_nodegroup()

    # Clean up handlers
    if convert_to_nodegroup in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.remove(convert_to_nodegroup)
    if convert_to_node in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(convert_to_node)
    if convert_to_node in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(convert_to_node)
    if bpy.app.version >= (4, 3, 0):
        if check_linked_nodes in bpy.app.handlers.blend_import_post:
            bpy.app.handlers.blend_import_post.remove(check_linked_nodes)
    if bpy.app.timers.is_registered(convert_to_node):
        bpy.app.timers.unregister(convert_to_node)

    # Note: We deliberately do NOT unregister Node_Info here
    # This ensures properties persist in the .blend file
