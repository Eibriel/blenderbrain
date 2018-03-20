from blenderbrain.common import check_regexs

general_info = {
    "blender": ["Blender is the free and open source 3D creation suite.", "It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering,", "compositing and motion tracking, even video editing and game creation."],
    "frame": ["Frame is"],
    "sample": ["Sample is"],
    "vertex": ["Vertex is"],
    "keyframe": ["Keyframe is"],
    "ray tracing": ["Ray Tracing is"],
    "render": ["Render is"],
    "subsurface scattering": ["Subsurface Scattering is"]
}


class kn_what_is:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"what\s+is"])
        if re_test:
            return True
        return False

    def entities(self, info):
        re_test = check_regexs(info["question"], [r"what\s+is\s+((a|the)\s+)(?P<thing>.+)"], True)
        if re_test:
            return re_test.group('thing')
        else:
            return ""

    def execute(self, info):
        thing_name = self.entities(info)
        if thing_name.endswith("?"):
            thing_name = thing_name[:-1]
        help_text = ["I don't know what a \"{}\" is".format(thing_name)]

        if thing_name.lower() in general_info:
            help_text = general_info[thing_name.lower()]
        return help_text


classes = [
    kn_what_is,
]
