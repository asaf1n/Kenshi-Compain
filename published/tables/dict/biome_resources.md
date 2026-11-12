# Словарь колонок таблицы biome_resources.csv

- Назначение: Ресурсы и климат регионов
- Ключ сортировки: biome_sid
- Ключи соединения: biome_sid

## Нормативные примечания

- Локальные пятна кнопки «Разведка» в рантайме вычисляются процедурным шумом и в сохранение не записываются.

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `biome_sid` | sid записи BIOME_GROUP (тип 95) |
| `name_en` | Название региона (en) |
| `name_ru` | Название региона (ru) |
| `color_index` | Цветовой код региона на карте (`index`) |
| `locations_total` | Всего стационарных локаций в регионе по справочнику мира (`world_reference.json`) |
| `locations_discovered` | Открыто локаций игроком (`discovered = true` в `quick.save`) |
| `player_buildings_count` | Число верхнеуровневых построек и рудных точек игрока в регионе |
| `player_mining_nodes` | Уже разрабатываемые игроком рудные точки (`MINING`) в регионе с их `resource_mult` |
| `climate_arid` | Доля засушливого климата (`arid` из ENVIRONMENT_RESOURCES) |
| `climate_green` | Доля зелёного климата (`green` из ENVIRONMENT_RESOURCES) |
| `climate_swamp` | Доля болотного климата (`swamp` из ENVIRONMENT_RESOURCES) |
| `farming_min` | Минимальное плодородие почвы в регионе (`farming min`) |
| `farming_mult` | Максимальный множитель плодородия почвы (`farming mult`) |
| `farming_altitude_min` | Нижняя граница высоты плодородия (`farming altitude min`) |
| `farming_altitude_max` | Верхняя граница высоты плодородия (`farming altitude max`) |
| `water_min` | Минимальный уровень грунтовых вод (`water min`) |
| `water_mult` | Максимальный множитель грунтовых вод (`water mult`) |
| `water_altitude_min` | Нижняя граница высоты грунтовых вод (`water altitude min`) |
| `water_altitude_max` | Верхняя граница высоты грунтовых вод (`water altitude max`) |
| `farm_water_usage` | Множитель расхода воды фермами в регионе (`farm water usage`) |
| `iron_mult` | Множитель железной руды в регионе (`iron mult`) |
| `copper_mult` | Множитель медной руды в регионе (`copper mult`) |
| `stone_mult` | Множитель камня в регионе (`stone mult`) |
| `stone_noise_cutoff` | Порог Perlin-шума пятен камня (`stone noise cutoff`; меньше — крупнее пятна) |
| `carbon_mult` | Множитель углерода/топлива (`carbon mult`) |
| `wind_speed_min` | Минимальная скорость ветра по сезонам региона (`wind speed min` из WEATHER) |
| `wind_speed_max` | Максимальная скорость ветра по сезонам региона (`wind speed max` из WEATHER) |
| `wind_speed_weighted_avg` | Средневзвешенная скорость ветра по длительности сезонов и вероятностям погоды |
| `acidic_ground` | Кислотность почвы (`acidic ground`, 0..1: обжигает ноги без обуви) |
| `acidic_water` | Кислотность воды (`acidic water`, 0..1) |
| `weather_affect_codes` | Коды погодных угроз в сезонах региона (`affect type` из WEATHER и WEATHER_EFFECT) |
| `weather_hazards` | Расшифровка погодных угроз (1 песчаная буря, 2 кислотный дождь, 3 жара/лучи, 4 газ; сопоставимо с `races.csv`) |

[← К оглавлению таблиц](../index.md)
