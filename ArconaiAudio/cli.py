from ArconaiAudio.play import play

def main(search=False, show_type=None, show_name=None):
    url = "http://arconaitv.us"
    play(url, search=search, show_type=show_type, show_name=show_name)


if __name__ == "__main__":
    import sys
    search = True
    show_type = None
    show_name = None

    if len(sys.argv) > 1:
        search = "--search" in [val.lower() for val in sys.argv]

        if sys.argv[1].lower() == "search":
            search = True
        else:
            show_type = sys.argv[1]

        if len(sys.argv) > 2:
            show_name = sys.argv[2]

    main(search=search, show_type=show_type, show_name=show_name)
