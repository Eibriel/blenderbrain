import bpy
import random

from blenderbrain.common import check_regexs


class kn_select_random:
    def check(self, info):
        regxs = [
            r"select\s+random",
            r"select\s+some"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        bpy.ops.object.select_random(seed=random.randint(0, 99999))
        return ["Ok"]


class kn_unselect_all:
    def check(self, info):
        regxs = [
            r"unselect\s+all",
            r"select\s+none",
            r"deselect"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        bpy.ops.object.select_all(action='DESELECT')
        return ["Ok"]


class kn_select_all:
    def check(self, info):
        regxs = [
            r"select\s+all"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        bpy.ops.object.select_all(action='SELECT')
        return ["Ok"]


class kn_rotate:
    def check(self, info):
        return False

    def execute(self, info):
        pass


class kn_translate:
    def check(self, info):
        return False

    def execute(self, info):
        for obj in objects:
            print("Translate")


classes = [
    kn_select_random,
    kn_unselect_all,
    kn_select_all,
    kn_rotate,
    kn_translate
]
