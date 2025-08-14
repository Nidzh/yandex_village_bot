from pathlib import Path


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Create a new FastAPI app module.")
    parser.add_argument("name", help="Name of the app to create")
    parser.add_argument("--base-dir", default="src/apps", help="Base directory for the apps")
    args = parser.parse_args()

    base_path = Path(args.base_dir) / args.name

    # Структура приложения
    files = [
        "__init__.py",
        "api.py",
        "constants.py",
        "exceptions.py",
        "models.py",
        "repository.py",
        "schemas.py",
        "service.py",
    ]

    # Создание директории приложения
    base_path.mkdir(parents=True, exist_ok=True)

    # Создание файлов
    for file in files:
        file_path = base_path / file
        if not file_path.exists():
            file_path.touch()
            print(f"Created: {file_path}")

    _fill_files(base_path, args)  # Заполнение файлов
    _register_routes(args)  # Регистрация роутера

    print(f"App '{args.name}' created successfully at {base_path}")


def _register_routes(args):
    router_file = Path(args.base_dir) / 'router.py'

    # Считываем содержимое файла
    with router_file.open("r") as rf:
        lines = rf.readlines()

    import_line = f"from src.apps.{args.name}.api import router as _{args.name}_router\n"
    registration_line = f"router.include_router(_{args.name}_router, prefix='/{args.name}', tags=['{args.name.capitalize()}'])\n"

    # Проверяем наличие импорта и строки регистрации, чтобы избежать дубликатов
    if import_line not in lines:
        for i, line in enumerate(lines):
            if line.startswith("from ") and "import router as" in line:
                lines.insert(i, import_line)
                break
        else:
            lines.insert(0, import_line)

    # Вставляем строку регистрации в конце, перед закрытием маршрутов
    if registration_line not in lines:
        for i, line in enumerate(lines):
            if line.strip().startswith("router = APIRouter()"):
                lines.insert(i + 2, registration_line)
                break
        else:
            lines.append(registration_line)

    # Записываем обновлённый файл
    with router_file.open("w") as rf:
        rf.writelines(lines)

    print(f"Router updated: {router_file}")


def _fill_files(base_path, args):
    file = base_path / "api.py"
    file.write_text(f"""from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {{"app": "{args.name}"}}
""")

    file = base_path / "exceptions.py"
    file.write_text(f"""from src.core.exceptions import APPException


class {args.name.capitalize()}Error(APPException):
    status_code = 400
    detail = 'Ошибка приложения {args.name}'
    type = '{args.name}.error'
""")

    file = base_path / "models.py"
    file.write_text(f"""from sqlalchemy.orm import Mapped, mapped_column

from src.core.model import Base


class {args.name.capitalize()}(Base, Base.TimestampsMixin, Base.IsDeletedMixin):
    __tablename__ = '{args.name}'

    id: Mapped[int] = mapped_column(primary_key=True, comment='Id')
""")

    file = base_path / "service.py"
    file.write_text(f"""from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.{args.name}.models import {args.name.capitalize()}
from src.apps.{args.name}.repository import {args.name.capitalize()}Repository


class {args.name.capitalize()}Service:
    def __init__(self, session: AsyncSession = None):
        self.repo = {args.name.capitalize()}Repository(session=session, model={args.name.capitalize()})
""")

    file = base_path / "repository.py"
    file.write_text(f"""from src.core.repository import BaseRepository


class {args.name.capitalize()}Repository(BaseRepository):
    ...
""")

    file = base_path / "schemas.py"
    file.write_text(f"""from pydantic import Field

from src.core.schema import CustomBaseModel


class {args.name.capitalize()}Schema(CustomBaseModel):
    id: int = Field(..., description='Id')
""")
