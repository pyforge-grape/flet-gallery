import flet as ft

from app import DesktopApp, MobileApp


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
