from datetime import UTC, datetime
from typing import Annotated

from pydantic import BeforeValidator


def return_int_or_none(value: any) -> int | None:
    """Преобразует объект в int или возвращает None."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def return_datetime_or_none(value: any) -> datetime | None:
    """Преобразует unixtime мс в datetime или возвращает None."""
    if isinstance(value, datetime):
        return value
    try:
        return datetime.utcfromtimestamp(value / 1000)
    except (TypeError, ValueError):
        try:
            return datetime.strptime(value, "%d.%m.%Y %H:%M:%S").replace(tzinfo=UTC)
        except (TypeError, ValueError):
            return None


def return_str_or_none(value: any) -> str | None:
    """Преобразует объект в str или возвращает None."""
    try:
        if isinstance(value, list):
            return ", ".join([str(i) for i in value])
        return str(value)
    except (TypeError, ValueError):
        return None


def return_locale_str_or_none(value: any) -> str | None:
    """Преобразует объект в локализованную строку (по умолчанию rus) или возвращает None."""
    if isinstance(value, str):
        return value
    elif isinstance(value, dict):
        if value.get("rus"):
            return value.get("rus")
        elif value.get("eng"):
            return value.get("eng")
    return None


def collect_full_name(value: any, model):
    if value is not None:
        return value
    else:
        name = model.data.get("name", "")
        surname = model.data.get("surname", "")
        father_name = model.data.get("father_name", "")
        full_name = " ".join(filter(None, [surname, name, father_name]))
        return full_name or None


ToInt = Annotated[int | None, BeforeValidator(return_int_or_none)]
ToStr = Annotated[str | None, BeforeValidator(return_str_or_none)]
ToDatetime = Annotated[datetime | None, BeforeValidator(return_datetime_or_none)]
ToLocaleStr = Annotated[str | None, BeforeValidator(return_locale_str_or_none)]
FullNameCollector = Annotated[str | None, BeforeValidator(return_locale_str_or_none), BeforeValidator(collect_full_name)]
