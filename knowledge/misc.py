from blenderbrain.common import check_regexs


class kn_ok:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"ok"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "Ok!"
        ]
        return help_text


class kn_nice:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"(nice|cool)"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            ":)"
        ]
        return help_text


class kn_hi:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"(^|\s+)(hi|hello|hola|chiao)"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "Ready to blend?"
        ]
        return help_text


class kn_bye:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"((good)?bye|chau|see\s+you)"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "Blend you later!"
        ]
        return help_text


class kn_yes:
    def check(self, info):
        re_test = check_regexs(info["question"], [r"(off?\s+course|yes|sure)"])
        if re_test:
            return True
        return False

    def execute(self, info):
        help_text = [
            "That's the spirit"
        ]
        return help_text


classes = [
    kn_ok,
    kn_nice,
    kn_hi,
    kn_bye,
    kn_yes
]
