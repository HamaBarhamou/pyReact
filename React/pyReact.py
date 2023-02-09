def createElement(element, children, **kwargs):
    """
    cette fonction permet de creer un element dans le dom
    :param element:
    :param children:
    :param kwargs:
    :return:
    """
    element = document.createElement(element)
    for child in children:
        element.appendChild(child)
    for key, value in kwargs.items():
        element.setAttribute(key, value)
    return element

def div(children, **kwargs):
    return createElement('div', children, **kwargs)

def span(children, **kwargs):
    return createElement('span', children, **kwargs)

def h1(children, **kwargs):
    return createElement('h1', children, **kwargs)

def h2(children, **kwargs):
    return createElement('h2', children, **kwargs)

def h3(children, **kwargs):
    return createElement('h3', children, **kwargs)

def h4(children, **kwargs):
    return createElement('h4', children, **kwargs)

def h5(children, **kwargs):
    return createElement('h5', children, **kwargs)

def h6(children, **kwargs):
    return createElement('h6', children, **kwargs)

def p(children, **kwargs):
    return createElement('p', children, **kwargs)

""" class BaseComponent:
    pass

class Component:
    pass

class React:
    
    def createElement():
        pass
        """