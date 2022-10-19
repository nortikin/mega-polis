import bpy
from bpy.props import IntProperty, EnumProperty

#from collections import namedtuple
from sverchok.node_tree import SverchCustomTreeNode
from sverchok.data_structure import updateNode
from sverchok.utils.dummy_nodes import add_dummy


#Megapolis Dependencies
from megapolis.dependencies import pandas as pd

if pd is None:
    add_dummy('SvMegapolisCorrelationIndex', 'Correlation Index', 'pandas')
else:
    class SvMegapolisCorrelationIndex(bpy.types.Node, SverchCustomTreeNode):
        """
        Triggers: Correlation Index
        Tooltip: Correlates a Dataframe at index of X and y features 
        """
        bl_idname = 'SvMegapolisCorrelationIndex'
        bl_label = 'Correlation Index'
        bl_icon = 'MESH_DATA'
        

        def sv_init(self, context):
            # inputs
            self.inputs.new('SvStringsSocket', "Dataframe")
            self.inputs.new('SvStringsSocket', "Index Feature X")
            self.inputs.new('SvStringsSocket', "Index Feature y")
           
            #outputs
            self.outputs.new('SvStringsSocket', "Correlation Index")

        def process(self):
            if not self.inputs["Dataframe"].is_linked or not self.inputs["Index Feature X"].is_linked or not self.inputs["Index Feature y"].is_linked:
                return
            self.dataframe = self.inputs["Dataframe"].sv_get(deepcopy = False)
            self.feature_x = self.inputs["Index Feature X"].sv_get(deepcopy = False)
            self.feature_y = self.inputs["Index Feature y"].sv_get(deepcopy = False)
          
            df = self.dataframe
            index_feature_x= self.feature_x[0][0]
            index_feature_y = self.feature_y[0][0]

            iat = df.iat[index_feature_x,index_feature_y]

            corr_at  = [iat]
            
            #Outputs

            self.outputs["Correlation Index"].sv_set(corr_at)

def register():
    if pd is not None:
        bpy.utils.register_class(SvMegapolisCorrelationIndex)

def unregister():
    if pd is not None:
        bpy.utils.unregister_class(SvMegapolisCorrelationIndex)
