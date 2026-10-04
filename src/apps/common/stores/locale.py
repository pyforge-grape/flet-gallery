from dataclasses import dataclass

import flet as ft

from apps.common.i18n.types import Locale


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
