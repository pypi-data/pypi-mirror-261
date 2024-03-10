from jinja2 import Template


def foo():
    template = Template('Hello {{ name }}!')
    return template.render(name='foo')


def bar():
    template = Template('Hello {{ name }}!')
    return template.render(name='bar')
