import flet as ft

from features.content.settings.paths import SETTINGS
from features.content.settings.tablet.layout import SettingsLayout


def SettingsRoutes():
    return [
        ft.Route(
            path=SETTINGS,
            component=SettingsLayout,
        ),
    ]
