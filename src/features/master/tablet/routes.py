import flet as ft

from features.master.paths import MASTER
from features.master.tablet.layout import MasterLayout


def MasterRoutes():
    return [
        ft.Route(
            path=MASTER,
            component=MasterLayout,
        ),
    ]
