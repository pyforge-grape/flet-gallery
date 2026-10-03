import flet as ft

from apps.desktop.app import DesktopApp
from apps.mobile.app import MobileApp
from apps.tablet.app import TabletApp


def create_app():
    page = ft.context.page

    page.adaptive = True

    assert page.platform is not None
    assert page.width is not None

    if page.platform.is_desktop():
        return DesktopApp

    if page.platform.is_mobile() and page.width >= 768:
        return TabletApp

    return MobileApp
