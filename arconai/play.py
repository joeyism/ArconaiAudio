#!/usr/bin/env python3
import sys
import arconai.prompt as p
import arconai.extract as extract

mpv_exists=True
try:
    import mpv
except:
    print("You need to install mpv")
    mpv_exists=False


def play(url):
    show_types = ["shows", "cable", "movies"]
    questions = [
            {
                "type": "rawlist",
                "name": "show_type",
                "message": "Pick a show type",
                "choices": show_types
            }
        ]
    answers = p.prompt(questions, style=p.style)
    show_type = answers["show_type"]

    m3u8_url = extract.run(url, show_type=show_type)
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
