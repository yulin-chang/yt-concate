from .step import Step

from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([find.yt for find in data])  # set方式去除重複(關鍵字多次出現於同一部影片)
        print("download counts of videos: ", len(yt_set))

        cou = 1
        for yt in yt_set:  # yt = find.yt
            if utils.video_file_exists(yt):  # 已下載過的影片不需重新下載(雖然下列pytube亦會自動略過已下載的)
                print(f'find existing video file: {yt.url} ,skipping')
                continue

            print(f'download videos(No: {cou}): {yt.url}')
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
            cou += 1

        return data
