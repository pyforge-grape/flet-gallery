import flet as ft

from desktop_app import DesktopApp
from mobile_app import MobileApp


def main(page: ft.Page):
    app = {
        ft.PagePlatform.ANDROID: MobileApp,
        ft.PagePlatform.IOS: MobileApp,
        ft.PagePlatform.WINDOWS: DesktopApp,
        ft.PagePlatform.MACOS: DesktopApp,
    }[page.platform]

    page.render_views(app)


if __name__ == "__main__":
    ft.run(main)
