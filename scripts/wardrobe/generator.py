from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def generate_number_images(
    template_path: str,
    font_path: str,
    out_dir: str,
    start: int = 1,
    end: int = 1000,
    color: str = "#b3332a",
    padding_px: int = 0,
    max_text_fraction: float = 0.7,
    min_font_size: int = 8,
    max_font_size: int | None = None,
    jpeg_quality: int = 95,
) -> None:
    """
    Рисует числа от start до end по центру шаблона JPG и сохраняет JPEG-файлы.
    - template_path: путь к шаблону JPG/PNG (фон).
    - font_path: путь к .ttf/.otf шрифту.
    - out_dir: папка для результата.
    - color: цвет текста (hex, например "#b3332a").
    - padding_px: внутренние отступы от краёв (если нужно).
    - max_text_fraction: доля от меньшей стороны изображения, под которую подгоняется текст.
    - min_font_size / max_font_size: границы подбора размера шрифта.
    - jpeg_quality: качество сохраняемого JPEG (1..95).
    """
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    base_img = Image.open(template_path).convert("RGB")
    W, H = base_img.size

    # Область, в которую должен поместиться текст
    box_w = max(1, W - 2 * padding_px)
    box_h = max(1, H - 2 * padding_px)
    target = int(min(box_w, box_h) * max_text_fraction)

    # Если верхняя граница размера шрифта не задана — ставим “разумный” предел
    if max_font_size is None:
        max_font_size = max(12, int(target * 2))

    def fit_font_size(text: str) -> ImageFont.FreeTypeFont:
        # Быстрый подбор размера шрифта бинарным поиском
        lo, hi = min_font_size, max_font_size
        best = ImageFont.truetype(font_path, size=lo)
        while lo <= hi:
            mid = (lo + hi) // 2
            f = ImageFont.truetype(font_path, size=mid)
            # Черновой канвас для измерения
            tmp = Image.new("RGB", (W, H))
            d = ImageDraw.Draw(tmp)
            # Точное измерение реального bbox текста
            bbox = d.textbbox((0, 0), text, font=f)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            if tw <= box_w and th <= box_h and max(tw, th) <= target:
                best = f
                lo = mid + 1
            else:
                hi = mid - 1
        return best

    for n in range(start, end + 1):
        img = base_img.copy()
        draw = ImageDraw.Draw(img)

        text = str(n)
        font = fit_font_size(text)

        # Высчитываем точный bbox для аккуратного центрирования
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Центр кадра
        cx, cy = W / 2, H / 2
        # Координаты так, чтобы центр текста совпал с центром кадра
        x = cx - tw / 2 - bbox[0]
        y = cy - th / 2 - bbox[1]

        draw.text((x, y), text, font=font, fill=color)

        out_path = out / f"wardrobe_{n}.jpg"
        img.save(out_path, "JPEG", quality=jpeg_quality, subsampling="4:2:0")

    print(f"Готово! Изображения сохранены в: {out.resolve()}")


generate_number_images(
    template_path="template.jpg",
    font_path="YS Display-Regular.ttf",
    out_dir="./wardrobe",
    start=1,
    end=1000,
    color="#b3332a",
    padding_px=0,          # без отступов
    max_text_fraction=0.4  # текст занимает ~70% меньшей стороны
)
