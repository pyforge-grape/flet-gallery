import flet as ft

from features.master.mobile.layout import MasterLayout
from features.master.paths import MASTER


def MasterRoutes():
    return [
        ft.Route(
            path=MASTER,
            component=MasterLayout,
        ),
    ]
