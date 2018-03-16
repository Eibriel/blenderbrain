# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import json
import asyncio
import requests
import blender_id

from bpy.props import StringProperty

bl_info = {
    "name": "BlenderBrain",
    "author": "Eibriel",
    "version": (0, 0),
    "blender": (2, 78, 0),
    "location": "View3D > Info Header",
    "description": "Artificial Intelligence for Blender",
    "warning": "",
    "wiki_url": "https://github.com/Eibriel/BlenderBrain/wiki",
    "tracker_url": "https://github.com/Eibriel/BlenderBrain/issues",
    "category": "Eibriel"}


class blenderbrainCommand (bpy.types.Operator):
    """Send command to BlenderBrain"""
    bl_idname = "blenderbrain.command"
    bl_label = "BlenderBrain"
    bl_options = {"REGISTER", "UNDO"}

    # invert = bpy.props.BoolProperty(name="Invert", default=False)

    @classmethod
    def poll(cls, context):
        epoll = True
        return epoll

    def execute(self, context):
        scn = context.scene
        return {'FINISHED'}


def input_update_loop(self, loop, context):
    wm = bpy.context.window_manager
    if not blender_id.is_logged_in():
        wm.blenderbrain_response = "First you need to login with Blender ID"
        return

    username = blender_id.get_active_profile().username
    username_name = username.split("@")[0]

    headers = {'user-agent': 'rDany', 'Content-Type': 'application/json'}
    post_data = {
        'question': wm.blenderbrain_input,
        'username': username
    }
    r = requests.post("http://0.0.0.0:5000/blenderbrain_api", data=json.dumps(post_data), headers=headers)
    # print (r.text)
    r_json = r.json()
    wm.blenderbrain_response = r_json["output"]["text"][0]
    loop.stop()


def on_input_update(self, context):
    loop = asyncio.get_event_loop()

    # Schedule a call to hello_world()
    loop.call_soon(input_update_loop, self, loop, context)

    # Blocking call interrupted by loop.stop()
    loop.run_forever()
    loop.close()


def blenderbrain_input(self, context):
    wm = bpy.context.window_manager
    self.layout.prop(wm, "blenderbrain_input", text="", icon="SPACE2")
    self.layout.label(text=wm.blenderbrain_response)


def register():
    bpy.types.WindowManager.blenderbrain_input = StringProperty(name="BlenderBrain input", description="Input field for BlenderBrain", default="", options={'HIDDEN', 'SKIP_SAVE'}, update=on_input_update)
    bpy.types.WindowManager.blenderbrain_response = StringProperty(name="BlenderBrain response", description="Response from BlenderBrain", default="", options={'HIDDEN', 'SKIP_SAVE'})

    bpy.types.INFO_HT_header.prepend(blenderbrain_input)
    bpy.utils.register_module(__name__)


def unregister():
    bpy.types.INFO_HT_header.remove(blenderbrain_input)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
