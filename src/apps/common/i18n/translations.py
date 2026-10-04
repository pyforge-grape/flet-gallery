from apps.common.i18n.locales import en_US, ja_JP
from apps.common.i18n.types import Locale, Translation, TranslationKey

_TRANSLATIONS: dict[Locale, Translation] = {
    "en-US": en_US.TRANSLATION,
    "ja-JP": {**en_US.TRANSLATION, **ja_JP.TRANSLATION},
}


def use_translation(locale: Locale):
    translation = _TRANSLATIONS[locale]

    def t(key: TranslationKey) -> str:
        return translation[key]

    return t
