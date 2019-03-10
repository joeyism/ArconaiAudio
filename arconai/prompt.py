#!/usr/bin/python3
import os

from PyInquirer import style_from_dict, Token, prompt, Separator
from tqdm import tqdm

from arconai.driver import driver

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

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



def prompt_for_shows(show_url_map):
    questions = [
            {
                "type": "checkbox",
                "qmark": "?",
                "name": "show_name",
                "message": "Pick a show:",
                "choices": [ {"name": show_name} for show_name in show_url_map.keys()]
            }
        ]
    answers = prompt(questions, style=style)
    selected_show_name = answers["show_name"][0]
    url = show_url_map[selected_show_name]
    return url


if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    sys.stderr.write(url)
    print(prompt_for_shows(get_shows(url)))
