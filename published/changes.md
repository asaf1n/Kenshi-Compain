# Изменения снимка

- **Предыдущий снимок:** Day 135, 10:49 (`sha256-781b398192623ce34bf974bf2bd1baffa960fe8b2300cb6c72002c130cb4a03d`)
- **Текущий снимок:** Day 135, 10:49 (`sha256-a9cff462de1f539da1aaa9b314edf6244e966ccdb1c6844d77850e0b6be382ba`)

## Ключевые изменения

- Изменений в отслеживаемых категориях не зафиксировано.

## Счётчики

| Показатель | Значение |
|---|---|
| `base_storage_changes` | 0 |
| `characters_after` | 30 |
| `characters_before` | 30 |
| `common` | 30 |
| `diplomacy_changes` | 0 |
| `equipment_changes` | 0 |
| `health_changes` | 0 |
| `inventory_changes` | 0 |
| `job_changes` | 0 |
| `joined` | 0 |
| `left` | 0 |
| `prosthetic_changes` | 0 |
| `skill_changes` | 0 |
| `supply_changes` | 0 |
| `transfers` | 0 |
| `world_changes` | 0 |
| `world_state_changes` | 0 |

## Промежуточные снимки

События предыдущих переходов цепочки; файлы дельт остаются в конвертере, их содержание приведено здесь.

<a id="snapshot-447fd171e4d3"></a>
### Day 132, 06:03 (sha256-447fd171)

- Казна: 36516 -> 61953 (+25437)
- Смена статуса: Вик unconscious=False, Зелёный палец unconscious=False, Мью unconscious=False, Седая тень coma=False, Седая тень unconscious=False
- Изменены отношения с фракциями (1): Болотники

<a id="snapshot-31ce3e1ccaf4"></a>
### Day 132, 11:15 (sha256-31ce3e1c)

- Изменены конечности и протезы: Зелёный палец: left_leg None -> lost
- Казна: 61953 -> 58866 (-3087)
- Смена статуса: Зелёный палец incapacitated=True

<a id="snapshot-fcbf8aa46af0"></a>
### Day 132, 23:02 (sha256-fcbf8aa4)

- Изменены конечности и протезы: Зелёный палец: left_leg lost -> {'level': 95, 'name': 'Нога разведчика (левая)', 'sid': '96020-Newwworld.mod'}
- Казна: 58866 -> 40426 (-18440)
- Смена статуса: Зелёный палец incapacitated=False

<a id="snapshot-5fde6a27cf9d"></a>
### Day 133, 06:03 (sha256-5fde6a27)

- Казна: 40426 -> 51802 (+11376)

<a id="snapshot-52c72c49b5a1"></a>
### Day 134, 10:49 (sha256-52c72c49)

- Сменили отряд (2): Вынос мозга, Флик
- Казна: 51802 -> 9347 (-42455)

<a id="snapshot-1316eacab478"></a>
### Day 134, 16:54 (sha256-1316eaca)

- Казна: 9347 -> 4941 (-4406)
- Смена статуса: Зелёный палец coma=True, Зелёный палец unconscious=True
- Изменены отношения с фракциями (1): Болотники

<a id="snapshot-487bd5b4d5f7"></a>
### Day 134, 20:46 (sha256-487bd5b4)

- Казна: 4941 -> 4791 (-150)
- Смена статуса: Зелёный палец coma=False, Зелёный палец unconscious=False

<a id="snapshot-474d819db915"></a>
### Day 135, 10:49 (sha256-474d819d)

- Казна: 4791 -> 1585 (-3206)

## Несравниваемые категории

- position: географические координаты подключаются профильным артефактом в задаче 02
- property: здания и собственность не сравниваются в kenshi-session-diff/5
- research: дерево исследований не сравнивается в kenshi-session-diff/5
