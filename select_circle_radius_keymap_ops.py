# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_select_circle_radius_keymap

from bl_ui.space_toolsystem_common import ToolSelectPanelHelper
from bpy.props import EnumProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class SCR_KEYMAP_OT_change(Operator):
    bl_idname = 'scr_keymap.change'
    bl_label = 'SCR KeyMap: increase'
    bl_description = 'Change Select Circle Radius'
    bl_options = {'REGISTER'}

    mode: EnumProperty(
        name='mode',
        items=[
            ('INCREASE', 'Increase', 'Increase'),
            ('DECREASE', 'Decrease', 'Decrease')
        ],
        default='INCREASE'
    )

    def execute(self, context):
        tool = ToolSelectPanelHelper.tool_active_from_context(context=context)
        if tool.idname == 'builtin.select_circle':
            props = tool.operator_properties('view3d.select_circle')
            value = context.preferences.addons[__package__].preferences.change_value
            if self.mode == 'INCREASE':
                props.radius += value
            elif self.mode == 'DECREASE':
                props.radius -= value
        return {'FINISHED'}


def register():
    register_class(SCR_KEYMAP_OT_change)


def unregister():
    unregister_class(SCR_KEYMAP_OT_change)
