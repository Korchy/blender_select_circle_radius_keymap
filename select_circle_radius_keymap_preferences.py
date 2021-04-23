# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_select_circle_radius_keymap

from bpy.types import AddonPreferences
from bpy.props import IntProperty
from bpy.utils import register_class, unregister_class


class SCR_KEYMAP_preferences(AddonPreferences):
    bl_idname = __package__

    change_value: IntProperty(
        name='Change on',
        default=4
    )

    def draw(self, context):
        self.layout.prop(self, 'change_value')


def register():
    register_class(SCR_KEYMAP_preferences)


def unregister():
    unregister_class(SCR_KEYMAP_preferences)
