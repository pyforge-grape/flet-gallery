from apps.common.stores.locale import LocaleContext, LocaleStore


def StoreProviders(content):
    providers = [
        (LocaleContext, LocaleStore("en-US")),
    ]

    for context, store in reversed(providers):
        content = context(store, lambda c=content: c)

    return content
