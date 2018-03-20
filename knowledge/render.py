import bpy

from blenderbrain.common import check_regexs


class kn_render:
    def check(self, info):
        regxs = [
            r"^render$"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        return ["I'm sorry. I can't render"]


class kn_enable_motion_blur:
    def check(self, info):
        regxs = [
            r"enable\s+motion\s+blur"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        bpy.data.scenes["Scene"].render.use_motion_blur = True
        return ["Motion Blur enabled"]


class kn_disable_motion_blur:
    def check(self, info):
        regxs = [
            r"disable\s+motion\s+blur"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        bpy.data.scenes["Scene"].render.use_motion_blur = False
        return ["Motion Blur enabled"]


class kn_set_render_size:
    def check(self, info):
        regxs = [
            r"^set\s+render\s+size\s+to\s+"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def entities(self, info):
        re_test = check_regexs(info["question"], [r"^set\s+render\s+size\s+to\s+(?P<thing>.+)$"], True)
        if re_test:
            return re_test.group('thing')
        else:
            return ""

    def execute(self, info):
        thing_name = self.entities(info)
        resolution_value = None
        if thing_name == "half":
            resolution_value = 50
        elif thing_name == "quarter":
            resolution_value = 25
        if resolution_value is not None:
            bpy.data.scenes["Scene"].render.resolution_percentage = resolution_value
            return ["Resolution Percentage set to {}%".format(resolution_value)]
        else:
            return ["Cant set the Resolution Percentage to {}".format(thing_name)]


class kn_describe_render:
    def check(self, info):
        regxs = [
            r"^(describe\s+)?render(\s+set+ings)?$"
        ]
        re_test = check_regexs(info["question"], regxs)
        if re_test:
            return True
        return False

    def execute(self, info):
        msg = []
        for scene in bpy.data.scenes:
            scene_name = scene.name
            scene_render_engine = scene.render.engine
            output_width = scene.render.resolution_x
            output_height = scene.render.resolution_y
            resolution_percentage = scene.render.resolution_percentage
            using_motion_blur = scene.render.use_motion_blur
            render_device = scene.cycles.device
            using_shading = scene.cycles.shading_system
            sample_method = scene.cycles.progressive
            #
            msg.append(scene_name)
            msg.append("  Render Engine:     {}".format(scene_render_engine))
            if resolution_percentage == 100:
                data = {
                    "width": output_width,
                    "height": output_height
                }
                msg.append("  Output resolution: {width}x{height}".format(**data))
            else:
                scaled_width = int(output_width * (resolution_percentage / 100))
                scaled_height = int(output_height * (resolution_percentage / 100))
                data = {
                    "scaled_width": scaled_width,
                    "scaled_height": scaled_height,
                    "resolution_percentage": resolution_percentage,
                    "width": output_width,
                    "height": output_height
                }
                msg.append("  Output resolution: {scaled_width}x{scaled_height} scaled ({resolution_percentage}% of {width}x{height})".format(**data))
            if using_motion_blur:
                msg.append("Motion Blur enabled")
            if scene_render_engine == "CYCLES":
                msg.append("  Render Device: {}".format(render_device))
                if using_shading and render_device == "CPU":
                    msg.append("  Using Open Shading Language")
        return msg


classes = [
    kn_enable_motion_blur,
    kn_disable_motion_blur,
    kn_set_render_size,
    kn_describe_render,
    kn_render
]
