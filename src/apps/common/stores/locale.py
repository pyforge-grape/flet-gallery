from dataclasses import dataclass
from typing import Literal

import flet as ft

Locale = Literal[
    "en-US",
    "ja-JP",
]


@ft.observable
@dataclass
class LocaleStore:
    locale: Locale

    def set_locale(self, locale: Locale):
        self.locale = locale


LocaleContext = ft.create_context(
    LocaleStore(
        locale="en-US",
    ),
)


def use_locale_store() -> LocaleStore:
    return ft.use_context(LocaleContext)
