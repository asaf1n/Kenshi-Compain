# Спецификация реализации (Sol) — Картография Kenshi Compain

## Контекст и целевые файлы
Реализация выполняется моделью **Sol** (`gpt-6.1-sol`) в ветке `feature/cartography`.
- Документ решения: `docs/adr/0001-cartography.md`
- Замечания архитектурного аудита: `orchestrate_workflow/plans/cartography/architecture_review.md` (AR-01–AR-07)
- Целевые файлы для создания:
  1. `tools/cartography.py`
  2. `tests/test_cartography.py`
  3. `sites/map/index.html`

## Требования к реализации

### 1. `tools/cartography.py`
- Константы:
  - `MIN_COORD = -147456.0`, `MAX_COORD = 147456.0`
  - `RASTER_PIXEL_SIZE = 1152.0`, `RASTER_GRID_SIZE = 256`, `ZONE_SIZE = 4608.0`
  - `REGION_DISPLAY_NAMES = {"The Iron Trail": "Железный шельф"}`
- Координатные функции:
  - `world_to_svg(x: float, z: float) -> tuple[float, float] | None`: возвращает `(svg_x, svg_y)` в диапазоне `[0, 256]`. Возвращает `None` при выходе за границы `[-147456.0, 147456.0)` или невалидных числах (NaN, Inf).
  - `svg_to_world(svg_x: float, svg_y: float) -> tuple[float, float] | None`: обратное преобразование.
  - `world_to_grid(x: float, z: float) -> tuple[int, int] | None`: возвращает `(px, py)` с инверсией строки: `px = floor(svg_x)`, `py = 255 - floor(svg_y)`.
  - `grid_to_world_center(px: int, py: int) -> tuple[float, float]`: центр ячейки растра.
- Идентификация регионов:
  - Сопоставление строго по `name_en` / `sid` / `index`.
  - Функция `get_region_display_name(name_en: str, default_ru: str = "") -> str`: возвращает «Железный шельф» для `The Iron Trail`.
- Канонический граф 4-связного соседства 69 регионов:
  - Словарь `ADJACENCY_GRAPH: dict[str, list[str]]`, проверенный по растру `areasmap.tga`.
  - Функция `are_regions_adjacent(reg_a_en: str, reg_b_en: str) -> bool`.
  - Контрольные проверки: Floodlands—Rebirth: True, Skinner's Roam—Deadlands: True, Rebirth—Deadlands: False, Arm of Okran—Deadlands: False, Raptor Island: 0 соседей.
- Анализ коридоров:
  - Функция `compare_corridors(...)` с расчётом расстояний, проверкой соседства и дисклеймером: «Схематический коридор ориентиров. Прямые линии не являются проходимым маршрутом».
- Экспорт SVG:
  - Формирование валидного SVG с подписями: `world_ref_id`, `snapshot_id`, `branch_id`, `game_time`, маркер «Картографическая схема Kenshi», дисклеймер.
- Генератор сводки для компаньона:
  - Форматированный markdown со статусом отряда, списком коридоров и дисклеймером.

### 2. `tests/test_cartography.py`
- Модульные тесты `unittest`, запускаемые командой `python -m unittest tests/test_cartography.py`:
  1. `test_coordinates`: 7 контрольных точек (Скуин, Хаб, Безродный, Край Мира, Ровная лагуна, Стоат, Катун) с их `instance_id` попадают в свои регионы и координаты SVG без зеркалирования.
  2. `test_raster_invariants`: сумма RLE = 65536, граничные координаты, обратимость формул, центры ячеек, контрольные соседства (включая Пойма—Возрождение, Скорняков край—Гиблые земли; отсутствие Возрождение—Гиблые земли, Рука Окрана—Гиблые земли).
  3. `test_snapshot_integrity`: 30 персонажей текущего выпуска без склейки дубликатов имён, проверка `snapshot_id`, `world_ref_id`, `branch_id`.
  4. `test_semantics`: `resolution_status` не даёт «исследован», линия коридора не получает «проверен» или «проходим».
  5. `test_branches_mismatch`: несовпадающие `world_ref_id` или `snapshot_id` вызывают предупреждение.
  6. `test_export_stamps`: сгенерированный SVG содержит все обязательные подписи и дисклеймер.
  7. `test_iron_trail_display`: The Iron Trail во всех представлениях и экспортах выводится как «Железный шельф».

### 3. `sites/map/index.html`
- Автономный одностраничный веб-интерфейс:
  - Без внешних CDN (чистый HTML5, CSS3, Vanilla JS).
  - Работает локально по `file://` и через http-сервер.
  - Масштабирование (wheel) и панорамирование (drag) векторной карты SVG.
  - Интеграция векторных контуров 69 регионов (из `docs/reference/regions_map.svg`).
  - Локации: маркеры по типам, поиск по имени, фильтрация по типу и региону, **скрытие секретных локаций (`is_secret=true`) по умолчанию** с чекбоксом показа.
  - Персонажи и группы: цветовая индикация статусов разрешения (`in_location`, `near_location`, `in_region`), всплывающий список бойцов, скрытие персонажей со статусом `unknown` с карты (с сохранением в боковом списке).
  - Сравнение коридоров Главы XI (Пойма -> Гиблые земли через Возрождение и через Край Мира) с проверкой смежности регионов.
  - Экспорт в SVG.
  - Кнопка «Копировать сводку для чата».
  - Встроенный baseline текущего выпуска + возможность загрузки файлов через Drag-and-Drop / File input.
