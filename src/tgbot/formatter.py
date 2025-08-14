def _B(_: str) -> str:
    return f"<b>{_}</b>"


def _I(_: str) -> str:
    return f"<i>{_}</i>"


def _U(_: str) -> str:
    return f"<u>{_}</u>"


def _M(_: str) -> str:
    return f"<code>{_}</code>"


def _C(_: str) -> str:
    return f"<pre>{_}</pre>"


def _Q(_: str) -> str:
    return f"<blockquote>{_}</blockquote>"


def _S(_: str) -> str:
    return f"<tg-spoiler>{_}</tg-spoiler>"


def _A(_: str, url: str) -> str:
    return f'<a href="{url}">{_}</a>'
