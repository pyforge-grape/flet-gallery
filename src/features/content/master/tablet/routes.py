import flet as ft

from features.content.master.paths import MASTER
from features.content.master.tablet.layout import MasterLayout


def MasterRoutes():
    return [
        ft.Route(
            path=MASTER,
            component=MasterLayout,
        ),
    ]
