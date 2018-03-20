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
import importlib
import blender_id
import blenderbrain.brain

from bpy.props import StringProperty
from bpy.app.handlers import persistent

bl_info = {
    "name": "BlenderBrain",
    "author": "Eibriel",
    "version": (0, 0),
    "blender": (2, 79, 0),
    "location": "Text Editor > BlenderBrain text",
    "description": "Blender Assistant",
    "warning": "",
    "wiki_url": "https://github.com/Eibriel/BlenderBrain/wiki",
    "tracker_url": "https://github.com/Eibriel/BlenderBrain/issues",
    "category": "Eibriel"}


# importlib.reload(blenderbrain.commands)

# TODO
# Traceback (most recent call last):
#   File "addons/blenderbrain/__init__.py", line 57, in load_handler
#     if not (last_line == "" and last_last_line[0] != "#"):
# IndexError: string index out of range

@persistent
def load_handler(dummy):
    D = bpy.data
    if 'BlenderBrain' not in D.texts:
        return
    text = D.texts['BlenderBrain']
    if len(text.lines) > 1:
        last_last_line = text.lines[-2].body
    else:
        last_last_line = "#"
    last_line = text.lines[-1].body
    if not (last_line == "" and last_last_line[0] != "#"):
        return
    # Mark as processing
    text.from_string("{}#".format(text.as_string()))
    br = blenderbrain.brain.brain()
    br.load()
    question = last_last_line
    if question.startswith("- "):
        question = question[2:]
    answers = br.process(question)
    answer_text = "\n# ".join(answers)
    answer_text = "# {}".format(answer_text)
    new_text = "{}{}\n- ".format(text.as_string(), answer_text)

    text.from_string(new_text)


class blenderbrainCommand (bpy.types.Operator):
    """Excecute BlenderBrain Command"""
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
        bpy.ops.object.select_all(action='DESELECT')
        return {'FINISHED'}


def blenderbrain_button(self, context):
    wm = bpy.context.window_manager
    self.layout.operator("blenderbrain.command")


def register():
    bpy.app.handlers.scene_update_post.append(load_handler)
    bpy.types.INFO_HT_header.prepend(blenderbrain_button)
    bpy.utils.register_module(__name__)


def unregister():
    bpy.app.handlers.scene_update_post.remove(load_handler)
    bpy.types.INFO_HT_header.remove(blenderbrain_button)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
