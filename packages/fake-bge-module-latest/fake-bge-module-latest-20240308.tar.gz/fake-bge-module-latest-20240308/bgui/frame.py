import sys
import typing
import bgui.widget

GenericType = typing.TypeVar("GenericType")


class Frame(bgui.widget.Widget):
    children = None
    ''' '''

    on_active = None
    ''' '''

    on_click = None
    ''' '''

    on_hover = None
    ''' '''

    on_mouse_enter = None
    ''' '''

    on_mouse_exit = None
    ''' '''

    on_release = None
    ''' '''

    parent = None
    ''' '''

    position = None
    ''' '''

    size = None
    ''' '''

    system = None
    ''' '''

    theme_options = None
    ''' '''

    theme_section = None
    ''' '''

    def add_animation(self, animation):
        ''' 

        '''
        pass

    def move(self, position, time, callback):
        ''' 

        '''
        pass
