#!/usr/bin/env python3
import sys
from ArconaiAudio import prompt, extract

mpv_exists=True
try:
    import mpv
except:
    print("You need to install mpv")
    mpv_exists=False


def play(url, search=False, show_type=None, show_name=None):
    if show_type is None:
        show_type = prompt.get_show_type()

    m3u8_url = extract.run(url, show_type=show_type, show_name=show_name, search=search)
    if mpv_exists:
        while True:
            player = mpv.MPV(video=False, input_default_bindings=True, input_vo_keyboard=True)
            print("Playing {}".format(m3u8_url))
            player.play(m3u8_url)
            player.wait_for_playback()

            m3u8_url = extract.run(url, show_type=show_type)
    else:
        bashCommand = "mpv {} --no-video".format(m3u8_url)
        print("Running ")
        print(bashCommand)
        import subprocess
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        output, error = process.communicate()
        print(output, error)
