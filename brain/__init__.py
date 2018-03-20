import os
import importlib.util


class brain:
    def __init__(self):
        self.commands = []

    def load(self):
        this_path = os.path.abspath(__file__)
        this_path = os.path.split(this_path)[0]
        this_path = os.path.split(this_path)[0]
        this_path = os.path.join(this_path, "knowledge")
        for f in os.listdir(this_path):
            path = os.path.join(this_path, f)
            if os.path.isfile(path):
                spec = importlib.util.spec_from_file_location("blenderbrain.knowledge", path)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
                for knowledge_class in foo.classes:
                    self.commands.append(knowledge_class())

    def process(self, question):
        info = {
            "question": ""
        }
        if question.startswith(": "):
            question = question[2:]
        info["question"] = question
        for command in self.commands:
            if command.check(info):
                return command.execute(info)
        return ["I don't understand"]
