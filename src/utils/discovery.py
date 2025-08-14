import importlib

from loguru import logger


class ModelDiscovery:
    """
    Утилита для динамического обнаружения и загрузки классов моделей,
    которые наследуют указанный базовый класс из набора Python-модулей, расположенных в структуре директорий проекта.
    Используется модулем Alembic для автоматического отслеживания изменений в моделях SQLAlchemy.
    """

    def __init__(self, root_path, base_class):
        self.root_path = root_path
        self.base_class = base_class

    def _find_model_classes(self, module):
        """
        Поиск классов моделей в модуле.
        """
        model_classes = []
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, self.base_class) and attribute != self.base_class:
                model_classes.append(attribute)
        return model_classes

    def load_models(self):
        """
        Загрузка всех моделей из файлов model.py в указанной директории.
        """
        models = []
        for file in self.root_path.rglob("models.py"):
            relative_path = file.relative_to(self.root_path.parent.parent)
            module_path = ".".join(relative_path.with_suffix("").parts)
            module = importlib.import_module(module_path)
            models.extend(self._find_model_classes(module))

        logger.info(f"Модели из {self.root_path} успешно импортированы")
        return models
