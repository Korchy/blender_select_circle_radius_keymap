# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_select_circle_radius_keymap

from . import select_circle_radius_keymap_ops
from . import select_circle_radius_keymap_preferences
from . import select_circle_radius_keymap_keymap
from .addon import Addon


bl_info = {
    'name': 'Select Circle Radius KeyMap',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 92, 0),
    'location': '3D Viewport',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-select-circle-radius-keymap/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-select-circle-radius-keymap/',
    'description': 'KeyMap for convenient changing the radius of the Select Circle tool'
}


def register():
    if not Addon.dev_mode():
        select_circle_radius_keymap_preferences.register()
        select_circle_radius_keymap_ops.register()
        select_circle_radius_keymap_keymap.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        select_circle_radius_keymap_keymap.unregister()
        select_circle_radius_keymap_ops.unregister()
        select_circle_radius_keymap_preferences.unregister()


if __name__ == '__main__':
    register()
