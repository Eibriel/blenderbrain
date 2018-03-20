from blenderbrain.common import check_regexs


class kn_meaning_life:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"meaning\s+of(\s+the)*\s+life"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "The meaning of life is to blend"
        ]
        return help_text


class kn_meaning_universe:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"meaning\s+of(\s+the)*\s+universe"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "The universe is here to be blended"
        ]
        return help_text


classes = [
    kn_meaning_life,
    kn_meaning_universe
]
