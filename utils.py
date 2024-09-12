import bpy

def update_dim(self, context):
        for node in self.node_tree.nodes:
            if node.type == 'TEX_NOISE':
                node.noise_dimensions = self.dimension
            elif node.type =="TEX_VORONOI":
                node.voronoi_dimensions = self.dimension
        if self.dimension=="1D":
            self.inputs['Vector'].hide = True
        else:
            self.inputs['Vector'].hide = False

        if self.dimension in ["1D","4D"]:
            self.inputs['W'].hide = False
        else:
            self.inputs['W'].hide = True


class ShaderNode(bpy.types.ShaderNodeCustomGroup):
    dimension: bpy.props.EnumProperty( name="Dimension", 
        items=[ 
        ("1D", '1D', 'Use the scalar value W as input'),
        ("2D", '2D', 'Use the 2D vector (X,Y) as input.The Z component is ignored'),
        ("3D", '3D', 'Use the 3D vector (X,Y,Z) as input'),
        ("4D", '4D', 'Use the 4D vector (X,Y,Z,W) as input'),
        ] ,
        update=update_dim,
        default="3D",
        description="Number of dimension to output noise for"
        )

    
    def draw_buttons(self, context , layout):
        if self.bl_label != "Pixelator":
            layout.prop(self, 'dimension' , text="")

    def createNodetree(self, name) :
        pass
    def getNodetree(self, name):
        if bpy.data.node_groups.find(name)==-1:
            self.createNodetree(name)
        else:
            self.node_tree=bpy.data.node_groups[name]
                   
    def addSocket(self, is_output, sockettype, name):
        if is_output==True:
            socket = self.node_tree.interface.new_socket(name, in_out='OUTPUT', socket_type=sockettype)
        else:
            socket = self.node_tree.interface.new_socket(name, in_out='INPUT', socket_type=sockettype)

        return socket
       
    def addNode(self, nodetype, attrs):
        node=self.node_tree.nodes.new(nodetype)
        for attr in attrs:
            self.value_set(node, attr, attrs[attr])
        return node
   
    def getNode(self, nodename):
        if self.node_tree.nodes.find(nodename)>-1:
            return self.node_tree.nodes[nodename]
        return None
   
    def innerLink(self, socketin, socketout):
        SI=self.node_tree.path_resolve(socketin)
        SO=self.node_tree.path_resolve(socketout)
        self.node_tree.links.new(SI, SO)
    
    def value_set(self, obj, path, value):
        if '.' in path:
            path_prop, path_attr = path.rsplit('.', 1)
            prop = obj.path_resolve(path_prop)
        else:
            prop = obj
            path_attr = path
        setattr(prop, path_attr, value)
    def free(self):
        if self.node_tree.users==1:
            bpy.data.node_groups.remove(self.node_tree, do_unlink=True)

    
        
        
            