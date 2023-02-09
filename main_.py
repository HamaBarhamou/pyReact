#!/usr/bin/python3
"""
    React for python programming
"""
def main():
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
            menu_node,
        ]
    )
    APP = render(app, indent=2)

    print(APP)
    
if __name__ == "__main__":
    main()