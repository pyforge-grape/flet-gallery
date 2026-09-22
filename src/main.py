import flet as ft

from apps.factory import create_app


def main(page: ft.Page):
    page.adaptive = True

    app = create_app(page)
    page.render_views(app)


if __name__ == "__main__":
    ft.run(main)
