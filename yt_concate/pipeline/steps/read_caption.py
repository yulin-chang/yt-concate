import os
from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}  # key: caption_file, value: captions dir
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}  # key: caption_str, value: time_str
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                is_time_line = False
                time_str = None
                caption_str = None
                for line in f:
                    if '-->' in line:
                        is_time_line = True
                        time_str = line.strip()
                        continue
                    if is_time_line:
                        caption_str = line.strip()
                        captions[caption_str] = time_str
                        is_time_line = False
            data[caption_file] = captions
        pprint(data)
        return data



