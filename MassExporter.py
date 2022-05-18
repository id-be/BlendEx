import os
import bpy

models = bpy.data.meshes

#    set a custom directory here, otherwise will 
#    default to wherever the .blend file is.

dir = os.getcwd()

#    puts it all in a subfolder titled "models" within dir.

mod_folder = dir + '\\' + 'models'

if not os.path.isdir(mod_folder):
    os.mkdir(mod_folder)

for mod in models:
    my_path = mod_folder + '\\' + str(mod.name) + '.ply'
    bpy.ops.export_mesh.ply(filepath=my_path)