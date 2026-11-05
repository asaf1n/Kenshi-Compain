# Изменения снимка

- **Предыдущий снимок:** Day 133, 06:03 (`sha256-5fde6a27cf9da521976599fd176b5bceab85a8bf236d3afe0856f14066024e52`)
- **Текущий снимок:** Day 133, 06:03 (`sha256-41a5855f649cf436624adbdefdc8901e082f0ddeb1e039ff319de150e29147f8`)

## Ключевые изменения

- **Изменения здоровья:** у 3 участников

## Счётчики

| Показатель | Значение |
|---|---|
| `base_storage_changes` | 0 |
| `characters_after` | 30 |
| `characters_before` | 30 |
| `common` | 30 |
| `diplomacy_changes` | 0 |
| `equipment_changes` | 0 |
| `health_changes` | 3 |
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

## Здоровье и состояние

- Вьючный бык (`ps:1856201216`): parts.Живот.bandage: 20.46 -> 20.38 (-0.08); parts.Живот.flesh: 190.54 -> 190.63 (+0.09); parts.Левая лапа.bandage: 23.62 -> 23.58 (-0.04); parts.Левая лапа.flesh: 81.88 -> 81.92 (+0.04)
- Седая тень (`ps:706176768`): parts.Голова.bandage: 21.85 -> 21.83 (-0.02); parts.Голова.flesh: 58.15 -> 58.17 (+0.02)
- Флик (`ps:1106567424`): parts.Грудь.bandage: 66.06 -> 66.04 (-0.02); parts.Грудь.flesh: 8.94 -> 8.96 (+0.02); parts.Грудь.stun: 12.07 -> 12.06 (-0.01); parts.Живот.bandage: 11.84 -> 11.83 (-0.01); parts.Живот.flesh: 63.16 -> 63.17 (+0.01); parts.Живот.stun: 3.63 -> 3.61 (-0.02); parts.Левая нога.stun: 5.28 -> 5.25 (-0.03); parts.Левая рука.stun: 2.19 -> 2.16 (-0.03); parts.Правая рука.bandage: 43.02 -> 43.01 (-0.01); parts.Правая рука.flesh: 31.98 -> 31.99 (+0.01)

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

## Несравниваемые категории

- position: географические координаты подключаются профильным артефактом в задаче 02
- property: здания и собственность не сравниваются в kenshi-session-diff/5
- research: дерево исследований не сравнивается в kenshi-session-diff/5
