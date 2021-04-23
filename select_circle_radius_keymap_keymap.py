# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_select_circle_radius_keymap

import bpy


class SCRKEYMAP_KeyMap:

    _keymaps = []

    @classmethod
    def register(cls, context):
        # add new key map
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='Window')
            # add keys
            keymap_item = keymap.keymap_items.new('scr_keymap.change', 'PAGE_UP', 'PRESS')
            keymap_item.properties.mode = 'INCREASE'
            keymap_item = keymap.keymap_items.new('scr_keymap.change', 'PAGE_DOWN', 'PRESS')
            keymap_item.properties.mode = 'DECREASE'
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    SCRKEYMAP_KeyMap.register(context=bpy.context)


def unregister():
    SCRKEYMAP_KeyMap.unregister()
