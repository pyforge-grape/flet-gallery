import flet as ft

from features.content.master.desktop.layout import MasterLayout
from features.content.master.paths import MASTER


def MasterRoutes():
    return [
        ft.Route(
            path=MASTER,
            component=MasterLayout,
        ),
    ]
