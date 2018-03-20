import bpy
import random
import datetime

from blenderbrain.common import check_regexs
from blenderbrain.common import calculate_age


class kn_help:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"help"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "Help"
        ]
        return help_text


class kn_who_father:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"who\s+is\s+your\s+(father|dad)"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "My father is Ton Roosendaal"
        ]
        return help_text


class kn_how_old:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"how\s+old", r"your\s+age"])
        if re_test:
            return True
        return False

    def execute(self, info):
        age = calculate_age(datetime.datetime(1993, 1, 2))
        help_text = [
            "I was born January 2nd 1993, so I'm {} years old".format(age)
        ]
        return help_text


class kn_what_are_doing:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"what\s+are\s+you\s+doing", r"what\s+do\s+you\s+do"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "I'm refreshing the UI",
            "I'm counting vertices",
            "I'm reading what you write",
            "I'm waiting for your orders",
            "I'm doing some complex math"
        ]
        return [random.choice(help_text)]


class kn_where_are_you:
    def check(self, info):
        regs = [
            r"where\s+are\s+you",
            r"(blender\s+)?location"
        ]
        re_test = check_regexs(info["question"], regs)
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "Blender location: {}".format(bpy.app.binary_path)
        ]
        return help_text


class kn_are_male_female:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"are\s+you\s+(a\s+)?(male|boy|female|girl|gal)"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "I'm not quite sure how to answer that. I'm software",
            "I'm just a bunch of bits.",
            "I'm just ones and zeros",
            "I'm just a software'"
        ]
        return [random.choice(help_text)]


class kn_are_what_name:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"what\s+is\s+your\s+name"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "My name is Blender"
        ]
        return help_text


class kn_who_are_you:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"(who|what)\s+are\s+you"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "I'm your friendly free software Blender"
        ]
        return help_text


class kn_version:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"(blender\s+)?version"])
        if re_test:
            return True
        return False

    def execute(self, info):
        data = [
            bpy.app.version_string,
            bpy.app.build_branch.decode("UTF-8"),
            bpy.app.version_cycle,
            bpy.app.build_platform.decode("UTF-8"),
            bpy.app.build_system.decode("UTF-8")
        ]
        help_text = [
            "Blender Version: {} {} {} {} {}".format(*data),
            "  Alembic: {}".format(bpy.app.alembic),
            "  FFMPEG: {}".format(bpy.app.ffmpeg),
            "  OCIO: {}".format(bpy.app.ocio),
            "  OIIO: {}".format(bpy.app.oiio),
            "  OpenVDB: {}".format(bpy.app.openvdb),
            "  SDL: {}".format(bpy.app.sdl),
        ]
        return help_text


class kn_temp:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"temp(oral)?(\s+folder)?"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "Temp folder: {}".format(bpy.app.tempdir)
        ]
        return help_text


classes = [
    kn_temp,
    kn_version,
    kn_help,
    kn_how_old,
    kn_who_father,
    kn_what_are_doing,
    kn_where_are_you,
    kn_are_male_female,
    kn_are_what_name,
    kn_who_are_you
]
