#!/usr/bin/python3
"""
    React for python programming
"""
from hotmetal import render
from brouillon.component.hello import Welcome, menu, menu_item


prop="ISSAKA HAMA Barhamou"
menu_node = menu(
    [
        ("/home/", "Home"),
        ("/blog/", "Blog"),
    ]
)

app = (
    "div",
    {},
    [
        Welcome(prop),
        menu_item("www.google.com", "faite une recherche"),
        Welcome(prop),
    ]
)
APP = render(app, indent=2)

print(APP)