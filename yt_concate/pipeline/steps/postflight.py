from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
        if inputs['clean_up_download']:
            utils.delete_dirs()
