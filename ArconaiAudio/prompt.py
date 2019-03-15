#!/usr/bin/python3
import os

import inquirer
from tqdm import tqdm
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from ArconaiAudio.driver import driver

def get_show_type():
    show_types = ["shows", "cable", "movies"]
    questions = [
      inquirer.List("show_type",
                    message="Pick a show type",
                    choices=show_types,
                ),
    ]
    answers = inquirer.prompt(questions)
    show_type = answers["show_type"]
    return show_type


def get_shows(url, show_type="shows", verbose=True):
    driver.get(url)
    show_url_map = []
    shows = driver.find_element_by_id(show_type)
    iterator = tqdm(enumerate(shows.find_elements_by_class_name("box-content")), desc="Extracting shows") if verbose else enumerate(shows.find_elements_by_class_name("box-content"))
    for i, show in iterator:
        if i == 0:
            continue
        try:
            show_section = show.find_element_by_xpath(".//*")
            show_name = show_section.text
            show_url = show_section.get_attribute("href")
            if len(show_name) > 1:
                show_url_map.append((show_name, show_url))
        except:
            pass
    return dict(show_url_map)


def prompt_for_shows(show_url_map, search=False):
    if search:
        return prompt_for_shows_input(show_url_map)
    else:
        return prompt_for_shows_select(show_url_map)

def prompt_for_shows_select(show_url_map):
    questions = [
      inquirer.List("show_name",
                    message="Pick a show:",
                    choices=show_url_map.keys()
                ),
    ]
    answers = inquirer.prompt(questions)
    selected_show_name = answers["show_name"]
    url = show_url_map[selected_show_name]
    return url

def divide(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def _print_shows(shows, no_of_columns=4):
    l = list(shows)
    while len(l) % no_of_columns != 0:
        l.append(" ")

    split = int(len(l)/no_of_columns)
    l_split = list(divide(l, split))
    for row in l_split:
        print(("{:<30s}" * no_of_columns).format(*row))

def prompt_for_shows_input(show_url_map):
    _print_shows(show_url_map.keys())
    show_completer = WordCompleter(show_url_map.keys())
    selected_show_name = prompt("Pick a show: ", completer=show_completer)
    return show_url_map[selected_show_name]


if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    sys.stderr.write(url)
    print(prompt_for_shows(get_shows(url)))
