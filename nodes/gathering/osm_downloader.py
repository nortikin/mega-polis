import bpy
from bpy.props import BoolProperty, EnumProperty

from collections import namedtuple
from sverchok.node_tree import SverchCustomTreeNode
from sverchok.data_structure import updateNode
from sverchok.utils.dummy_nodes import add_dummy


#Megapolis Dependencies
from megapolis.dependencies import osmnx as ox
import shutil

Download_method = namedtuple('DownloadMethod', ['Address', 'Place','Point','Bbox'])
DOWNLOADMETHOD = Download_method('Address', 'Place','Point','Bbox')
downloadmethod_items = [(i, i, '') for i in DOWNLOADMETHOD]



if ox is None:
    add_dummy('SvMegapolisOSMDownloader', 'OSM Downloader', 'osmx')
else:
    class SvMegapolisOSMDownloader(bpy.types.Node, SverchCustomTreeNode):
        """
        Triggers: OSM Downloader
        Tooltip: Download an Open Streetmap file
        """
        bl_idname = 'SvMegapolisOSMDownloader'
        bl_label = 'OSM Downloader'
        bl_icon = 'MESH_DATA'
        

        # Hide Interactive Sockets
        def update_sockets(self, context):
            """ need to do UX transformation before updating node"""
            def set_hide(sock, status):
                if sock.hide_safe != status:
                    sock.hide_safe = status

            if self.download_method in DOWNLOADMETHOD.Address:
                set_hide(self.inputs['Address'], False)
                set_hide(self.inputs['Tags'], False)
                set_hide(self.inputs['Folder'], False)


                set_hide(self.inputs['Distance'], False)

                set_hide(self.inputs['Place'], True)
                
                set_hide(self.inputs['Coordinate_X'], True)
                set_hide(self.inputs['Coordinate_Y'], True)

                set_hide(self.inputs['North'], True)
                set_hide(self.inputs['South'], True)
                set_hide(self.inputs['East'], True)
                set_hide(self.inputs['West'], True)

            elif self.download_method in DOWNLOADMETHOD.Place:
                set_hide(self.inputs['Address'], True)
                set_hide(self.inputs['Tags'], False)
                set_hide(self.inputs['Folder'], False)


                set_hide(self.inputs['Distance'], True)

                set_hide(self.inputs['Place'], False)
                
                set_hide(self.inputs['Coordinate_X'], True)
                set_hide(self.inputs['Coordinate_Y'], True)

                set_hide(self.inputs['North'], True)
                set_hide(self.inputs['South'], True)
                set_hide(self.inputs['East'], True)
                set_hide(self.inputs['West'], True)

            elif self.download_method in DOWNLOADMETHOD.Point:
                set_hide(self.inputs['Address'], True)
                set_hide(self.inputs['Tags'], False)
                set_hide(self.inputs['Folder'], False)


                set_hide(self.inputs['Distance'], False)

                set_hide(self.inputs['Place'], True)
                
                set_hide(self.inputs['Coordinate_X'], False)
                set_hide(self.inputs['Coordinate_Y'], False)

                set_hide(self.inputs['North'], True)
                set_hide(self.inputs['South'], True)
                set_hide(self.inputs['East'], True)
                set_hide(self.inputs['West'], True)


            else:
                set_hide(self.inputs['Address'], True)
                set_hide(self.inputs['Tags'], False)
                set_hide(self.inputs['Folder'], False)


                set_hide(self.inputs['Distance'], True)

                set_hide(self.inputs['Place'], True)
                
                set_hide(self.inputs['Coordinate_X'], True)
                set_hide(self.inputs['Coordinate_Y'], True)

                set_hide(self.inputs['North'], False)
                set_hide(self.inputs['South'], False)
                set_hide(self.inputs['East'], False)
                set_hide(self.inputs['West'], False)

            updateNode(self,context)

        #Blender Properties Buttons

        download: BoolProperty(
            name="download",
            description="Run the Node to Download",
            default=False,
            update=update_sockets)
        
        buildings: BoolProperty(
            name="buildings",
            description="Download Building Information",
            default=False,
            update=update_sockets)
        

        download_method: EnumProperty(
            name='download_method', items=downloadmethod_items,
            default="Address",
            description='Choose an OSM Download Method', 
            update=update_sockets)


        def sv_init(self, context):
            
            # inputs
            self.inputs.new('SvStringsSocket', "Address")
            self.inputs.new('SvStringsSocket', "Place")
           
            
            self.inputs.new('SvStringsSocket', "Coordinate_X")
            self.inputs.new('SvStringsSocket', "Coordinate_Y")
           
            self.inputs.new('SvStringsSocket', "North")
            self.inputs.new('SvStringsSocket', "South")
            self.inputs.new('SvStringsSocket', "East")
            self.inputs.new('SvStringsSocket', "West")
           

            self.inputs['Place'].hide_safe = True 
            
            self.inputs['Coordinate_X'].hide_safe = True 
            self.inputs['Coordinate_Y'].hide_safe = True 
            self.inputs['North'].hide_safe = True 
            self.inputs['South'].hide_safe = True 
            self.inputs['East'].hide_safe = True 
            self.inputs['West'].hide_safe = True 
            
            self.inputs.new('SvStringsSocket', "Tags")
            self.inputs.new('SvStringsSocket', "Distance")
            self.inputs.new('SvStringsSocket', "Folder")
           


            # outputs

            self.outputs.new('SvStringsSocket', "Output_Message")
            
            
        def draw_buttons(self,context, layout):
            layout.prop(self, 'download')
            layout.prop(self, 'buildings')
            layout.prop(self, 'download_method', expand=True)

        def draw_buttons_ext(self, context, layout):
            self.draw_buttons(context, layout)

        def process(self):
             
            if self.download_method in DOWNLOADMETHOD.Address:
                if not self.inputs["Address"].is_linked:
                    return
                self.address = self.inputs["Address"].sv_get(deepcopy = False)
                self.distance = self.inputs["Distance"].sv_get(deepcopy = False)


            elif self.download_method in DOWNLOADMETHOD.Place:
                if not self.inputs["Place"].is_linked:
                    return
                self.place = self.inputs["Place"].sv_get(deepcopy = False)

            elif self.download_method in DOWNLOADMETHOD.Point:
                if not self.inputs["Coordinate_X"].is_linked and not self.inputs["Coordinate_Y"].is_linked:
                    return
                self.coordinate_x = self.inputs["Coordinate_X"].sv_get(deepcopy = False)
                self.coordinate_y = self.inputs["Coordinate_Y"].sv_get(deepcopy = False)
                self.distance = self.inputs["Distance"].sv_get(deepcopy = False)

            else:
                if not self.inputs["North"].is_linked and not self.inputs["South"].is_linked and not self.inputs["East"].is_linked and not self.inputs["West"].is_linked  :
                    return
                self.north = self.inputs["North"].sv_get(deepcopy = False)
                self.south = self.inputs["South"].sv_get(deepcopy = False)
                self.east = self.inputs["East"].sv_get(deepcopy = False)
                self.west = self.inputs["West"].sv_get(deepcopy = False)

            self.tags = self.inputs["Tags"].sv_get(deepcopy = False)
            self.folder = self.inputs["Folder"].sv_get(deepcopy = False)

            


            if len(self.tags) > 1:
                tags = tags[0][0]
                tag = tags.split(",")

                dict = {}

                keys = []

                values = []
             
                #print(tag)

                for i in tag:
                    s= i.split(":")
                    k = keys.append(s[0])
                    v = values.append(s[1])
                #for i in tag:
                #    i.split(":")
                #    keys.append(i[0])
                #    values.append(i[1])
                    
                for i in range(len(keys)):
                    dict[keys[i]] = values[i]
            else:
                s= self.tags.split(":")
                dictionary = {s[0]:s[1]}
            
            message = []


            if self.buildings == True:
                dictionary["building"] = True
            
            if download_method in DOWNLOADMETHOD.Address:
                buildings = ox.geometries_from_address(self.address, dictionary, self.distance)
                buildings = buildings.loc[:,buildings.columns.str.contains('addr:|geometry')]
                buildings.to_file(f"{self.folder}{self.address}", driver='GPKG')
                #shutil.make_archive(place, 'zip', place)
                message = "Downloaded {0}{1}".format(self.folder,self.address)
                

            elif download_method in DOWNLOADMETHOD.Place:
                buildings = ox.geometries_from_place(self.place, dictionary)
                buildings = buildings.loc[:,buildings.columns.str.contains('addr:|geometry')]
                buildings.to_file(f"{self.folder}{self.place}", driver='GPKG')
                #shutil.make_archive(place, 'zip', place)
                message = "Downloaded {0}{1}".format(self.folder,self.place)
                

            elif download_method in DOWNLOADMETHOD.Point:
                point = (float(self.coordinate_x),float(self.coordinate_y))
                buildings = ox.geometries_from_point(self.point, dictionary, self.distance)
                buildings = buildings.loc[:,buildings.columns.str.contains('addr:|geometry')]
                buildings.to_file(f"{self.folder}{point}", driver='GPKG')
                #shutil.make_archive(place, 'zip', place)
                message = "Downloaded {0}{1}".format(self.folder,self.point)
                

            else:
                bbox = f'{self.north}_{self.south}_{self.east}_{self.west}'
                buildings = ox.geometries_from_bbox(self.north,self.south,self.east,self.west, dictionary)
                buildings = buildings.loc[:,buildings.columns.str.contains('addr:|geometry')]
                buildings.to_file(f"{self.folder}{bbox}", driver='GPKG')
                #shutil.make_archive(place, 'zip', place)
                message = "Downloaded {0}{1}".format(self.folder,bbox)
            
            ## Output
            self.outputs["Output_Message"].sv_set(message)
            
def register():
    if ox is not None:
        bpy.utils.register_class(SvMegapolisOSMDownloader)

def unregister():
    if ox is not None:
        bpy.utils.unregister_class(SvMegapolisOSMDownloader)
