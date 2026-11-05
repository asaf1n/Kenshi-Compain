# Контракт данных (data-contract.md)

Технический контракт полей, используемых в публикациях и справочниках проекта Kenshi Compain. Источники — игровые данные (FCS / quick.save), подтверждённые сверкой с историей кампании и внешними источниками.

## state_code уникальных NPC (usedUniquesState)

В сейве (quick.save → запись типа CAMERA) состояние уникального NPC хранится в полях `usedUniquesStateX`, где X — индекс, соответствующий записи `usedUniquesX` (String ID персонажа).

| state_code | Значение | Описание |
|------------|----------|----------|
| 0 | Мёртв (Dead) | Персонаж мёртв. Устанавливается при смерти. |
| 1 | Жив и свободен (Alive and free / Okay) | Персонаж жив и не находится в клетке. |
| 2 | В плену (Imprisoned / Kidnapped) | Персонаж пленён или похищен (в клетке). |

Подтверждение:
- Сверка с историей кампании: код 0 у всех погибших, код 2 у всех пленённых, код 1 у живых и свободных.
- FCS / код чтения usedUniques (подтверждено модератором Shidan и множеством источников): 0 = Dead, 1 = Alive and well / okay, 2 = Kidnapped or imprisoned.
- Источники: https://steamcommunity.com/app/233860/discussions/3/1751275687422260269/, https://steamcommunity.com/app/233860/discussions/0/596261972223251360/, https://wiki3.jp/kenshijp/page/605, Reddit-треды по редактированию World States.

В публикациях проекта остаётся сырой числовой `state_code` (решение из ревью). Интерпретация значений — по этой таблице.

## Другие поля

(Будут дополняться по мере необходимости.)

Источники раздела: FCS (quick.save, CAMERA), https://steamcommunity.com/app/233860/discussions/3/1751275687422260269/, https://steamcommunity.com/app/233860/discussions/0/596261972223251360/, https://wiki3.jp/kenshijp/page/605
