from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.creat_dirs()