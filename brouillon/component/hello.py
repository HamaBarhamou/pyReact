

def Welcome(props):
    ele = ("", {}, [props, menu_item('hama','barhamou')])
    return ele

def menu_item(href, text):
    return ("li", {}, [("a", {"href": href}, [text])])


def menu(items):
    return ("ul", {}, [menu_item(href, text) for href, text in items])
