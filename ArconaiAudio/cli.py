from ArconaiAudio.play import play

def main(prompt=False, show_type=None, show_name=None):
    url = "http://arconaitv.us"
    play(url, prompt=prompt, show_type=show_type, show_name=show_name)


if __name__ == "__main__":
    import sys
    prompt = False
    show_type = None
    show_name = None

    if len(sys.argv) > 1:
        prompt = "--prompt" in [val.lower() for val in sys.argv]

        if sys.argv[1].lower() == "prompt":
            prompt = True
        else:
            show_type = sys.argv[1]

        if len(sys.argv) > 2:
            show_name = sys.argv[2]

    main(prompt=prompt, show_type=show_type, show_name=show_name)
