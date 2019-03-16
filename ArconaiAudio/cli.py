from ArconaiAudio.play import play

def main(search=False, show_type=None, show_name=None):
    url = "http://arconaitv.us"
    play(url, search=search, show_type=show_type, show_name=show_name)


if __name__ == "__main__":
    import sys
    search = True #TODO: when inquirer==2.5.2, set this to False
    show_type = None
    show_name = None
    input_args = sys.argv.copy()

    if len(input_args) > 1:
        for i, val in enumerate(input_args):
            if "--search" in val.lower():
                search = True
                input_args.pop(i)
                break

    if len(input_args) > 1:
        show_type = input_args[1]

        if len(input_args) > 2:
            show_name = input_args[2]

    main(search=search, show_type=show_type, show_name=show_name)
