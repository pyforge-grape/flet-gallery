import flet as ft

from app import App


def main(page: ft.Page):
    page.render_views(App)


if __name__ == "__main__":
    ft.run(main)
