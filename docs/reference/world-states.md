# World States, Town Overrides и уникальные NPC (Kenshi Vanilla)

Источники: игровые данные через FCS/Web FCS (приоритет), Kenshi Wiki (kenshi.fandom.com), kenshi.zone research notes, Steam guides, сообщества. При расхождениях указаны оба. Русские названия по справочнику Kenshi_RU_EN.md; английское в скобках при первом упоминании.

## Механика World States

World States — система учёта состояния уникальных NPC (жив и свободен / пленён / мёртв). Изменения затрагивают Town Overrides (полная замена поселения) и Homeless Spawns (патрули/рейды в зонах). «Жив» означает жив и свободен. Пленение и смерть в большинстве условий эквивалентны («не жив»). Некоторые условия различают: 7 записей используют только imprisoned (включая Феникса, Эсату, Тенгу, Лонгена, королев Улья); 26 — только смерть. Вербовка не считается исчезновением. Приоритет override: наибольшее число условий; при равенстве — первый в списке. Изменения применяются при загрузке зоны. [kenshi.zone World States notes; Kenshi Wiki World States]

Игрок не может полностью уничтожить большинство фракций: остаются remnants, отдельные поселения (Holy Farms, Tengu's Vault, Spring, Last Stand и т.д.). [Kenshi Wiki; kenshi.zone]

## Проверки

1. **Пленение vs смерть (Феникс / Бугристый Холм / Святые военные базы)**: Эквивалентны для большинства. Сдача Феникса (Holy Lord Phoenix) живым Эсате (Esata the Stone Golem) триггерит те же эффекты, что и смерть: Бугристый холм (Blister Hill) разрушается (или переходит к Flotsam/Outlaws при условиях), Святые военные базы (Holy Military Bases) становятся Deadhive Overrun (Fogmen), появляются Fogmen nests в Окранов залив (Okran's Gulf). [Kenshi Wiki Holy Lord Phoenix, Holy Military Base/Fogmen; kenshi.zone Phoenix]

2. **Мёртвый NPC сданный за награду (Летящий Бык / Flying Bull) vs живой (Призрак / Ghost)**: Оба устанавливают флаг «не жив и свободен». Для Flying Bull (Летящий Бык): New Kralia (Новая Кралия) становится руинами при imprisoned/dead. Для Ghost (Призрак): патрули Berserkers halved/broken. Сдача тела даёт 50% награды, но World State тот же. [Kenshi Wiki Flying Bull, Ghost; bounty guides]

3. **Deadhive override**: Deadhive (Мёртвый улей) — Fogmen (туманники), Hivers, потерявшие связь с королевой/феромонами. При смерти/пленении Western/Southern Hive Queen: Hive villages → Deadhive Overrun. При Phoenix dead/imprisoned: Holy Military Bases → Fogmen ruins + nests в Okran's Gulf. Связь: теория сообщества — Fogmen = Hive без королевы. [kenshi.zone Deadhive; Kenshi Wiki Fogmen, Deadhive Overrun]

4. **Файлы rebirth.mod, Dialogue.mod, Newwworld.mod, __world reactions*.mod, __Mourn.mod**: Часть Vanilla base data (gamedata). Загружаются по умолчанию в FCS вместе с gamedata.base. Не пользовательские моды. [Steam community discussions; FCS behavior]

## Уникальные NPC, связанные с World States

### Святая Нация (Holy Nation)
- **Святой Лорд Феникс (Holy Lord Phoenix)**: Blister Hill. Награда ~100k (Shek/UC/Flotsam/Rebel). Не вербуем. Смерть/пленение: Blister Hill ruins (или Flotsam если Moll alive + Seta/Valtena gone), Holy Military Bases → Deadhive, reduced HN patrols, Fogmen в Okran's Gulf, Wrath of God raids. [Wiki; kenshi.zone]
- **Верховный Инквизитор Сета (High Inquisitor Seta)**: Stack. Награда 40k. Смерть/пленение: Stack/Bad Teeth → Shek (если Esata) или Kral's Chosen (если Flying Bull) или ruins. [ISK Mogul; Wiki]
- **Верховный Инквизитор Вальтена (High Inquisitor Valtena)**: Okran's Shield. Смерть/пленение: Okran's Shield → UC/Shek/Reavers/ruins в зависимости от лидеров. [Wiki]

### Союзные Города (United Cities) и Traders Guild
- **Император Тенгу (Emperor Tengu)**: Heft/Tengu's Vault. Смерть/пленение: многие города half-destroyed/prosperous (Empire Peasants), Samurai Rogues. [kenshi.zone]
- Nobles (Lady Sanda, Tsugi, Merin, Lords Inaba etc.): влияют на specific towns (Bark, Heng и т.д.).
- **Лонген (Longen)**: Traders Guild. Влияет на prosperous overrides.

### Королевство Шек (Shek Kingdom)
- **Эсата Каменный Голем (Esata the Stone Golem)**: Admag. Награда 100k. Смерть/пленение: Admag → Berserkers, Squin new leader (Mukai), Kamikaze patrols. [Wiki]
- **Мукаи Гора (Mukai the Mountain)**: Squin override.
- **Летящий Бык (Flying Bull)**: New Kralia. Награда 30k. Alive free: takeovers Stack/Bad Teeth/Squin в определённых условиях.
- **Призрак (Ghost)**: Berserker Village. Награда 10k. Death: reduced patrols; alive + Seta gone: patrols в Okran's Gulf; can take Admag/Squin.

### Другие
- **Молл (Moll)**: Flotsam Ninjas. Alive: can take Blister Hill/Rebirth.
- **Баян (Bayan)**: диалоги по bounty/альянсам.
- Bugmaster (Бугристый Холм / Arach): death destroys location, Meitou sabre.
- Hive Queens, Tinfist, Crab Queen, Valamon, Boss Simion, Shade, Big Gray/Grim, Yabuta, Screamer/Ponk, King Gurgler и др. — см. списки в kenshi.zone и Wiki.

Таблица ключевых (сокращённо; полный в источниках):

| NPC | Фракция | Место | Награда | Эффект при gone |
|-----|---------|-------|---------|-----------------|
| Phoenix | HN | Blister Hill | 100k | Blister ruins, Deadhive bases, Wrath of God |
| Esata | Shek | Admag | 100k | Admag Berserkers, Squin Mukai |
| Tengu | UC | Heft | - | UC towns prosperous/half-destroyed |
| Flying Bull | Kral's Chosen | New Kralia | 30k | New Kralia ruins; takeovers if alive |
| Ghost | Berserkers | Berserker Village | 10k | Reduced patrols |

## Town Overrides

Типы: Destroyed (руины), Faction takeover, Prosperous (часто Empire Peasants), Half-destroyed, Malnourished/Famine. 117+ towns, 234 versions. Игрок buildings обычно сохраняются. [kenshi.zone Town Overrides]

Примеры:
- Bad Teeth: half-destroyed / destroyed / Shek / Kral's Chosen / UC (по условиям Phoenix/Seta/Esata/Flying Bull/Tengu).
- Stack: Shek (Esata) / Kral's (Flying Bull) / ruins.
- Holy Military Base: Deadhive при Phoenix gone.
- Squin: new leader / Kral's / Berserkers / destroyed.
- Admag: Berserkers при Esata gone.
- Hive villages: Deadhive Overrun при Queen gone.
- UC towns (Heng, Bark etc.): зависят от Tengu + nobles + slavers.

## Рейды и события

- **Гнев Божий (Wrath of God)**: при Phoenix gone. Recurring HN assault на player outposts (или towns). Led by Seta (bugged variants). До 80+ units. Постоянный риск. [Kenshi Wiki Wrath of God]
- Другие: Challenger of the Undefeated (Bugmaster related), Hive attacks и т.д. Некоторые never-ending.

## Связанные диалоги

- Молл (Moll): Flotsam takeover options.
- Эсата: комментарии о HN collapse.
- Баян: bounty turn-ins, alliances, suggestions по Shek enemies (Berserkers etc.).
- Феникс: questline Holy Nation Route (Seto etc.).

Источники: Kenshi Wiki (World_States, individual NPC/Town pages), kenshi.zone (world-states, town-overrides, deadhive, phoenix, berserkers), ISK Mogul guides, Steam bounty lists. Данные Vanilla; моды (Reactive World и др.) отброшены.