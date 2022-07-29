import os

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print('download caption: ', url)

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError as e:
                print('Error in download caption: ', e)
                continue

            text_file = open(utils.get_caption_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break



