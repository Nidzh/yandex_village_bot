from src.tgbot.handlers.start import router as _start_router
from src.tgbot.handlers.welcome import router as _welcome_router
from src.tgbot.handlers.main import router as _main_router
from src.tgbot.handlers.map import router as _map_router
from src.tgbot.handlers.program import router as _activity_router
from src.tgbot.handlers.chronicle import router as _chronicle_router
from src.tgbot.handlers.help import router as _help_router
from src.tgbot.handlers.activity import router as _program_router
from src.tgbot.handlers.transfer import router as _transfer_router
from src.tgbot.handlers.wardrobe import router as _wardrobe_router


MAIN_ROUTER = [
    _start_router,
    _welcome_router,
    _main_router,
    _map_router,
    _activity_router,
    _chronicle_router,
    _help_router,
    _program_router,
    _transfer_router,
    _wardrobe_router,
]
