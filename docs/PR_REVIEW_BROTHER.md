# Рев'ю ПРів (task_00 — task_04)

Нижче тільки баги, помилкова логіка та зайві коментарі. Чистота коду поки не оцінювалась.

---

## PR #3 — Task 00

- По суті ОК: невелика зміна в `task_00.md`, тести task00 проходять.

---

## PR #4 — Task 01

**Баги / логіка**

1. **`json_store.py`** — для дати використовується `datetime.strptime(..., "%Y-%m-%d")`. Він повертає **`datetime`**, а в моделях очікується **`date`** (`Entry.day`, `State.start_date`). Треба брати лише дату: **`.date()`**, наприклад:
   - `day=datetime.strptime(entry["date"], "%Y-%m-%d").date()`
   - `start_date=datetime.strptime(data["start_date"], "%Y-%m-%d").date()`

2. **`json_store.py`** — зараз усі `minutes` у записах і `daily_target_minutes` / `bonus_threshold_minutes` у schedule поставлені в **1**. Через це дані з фікстури (наприклад, "2h", "32m") не відповідають реальності, і подальша логіка (/status, дедлайн тощо) буде неправильною. Треба парсити duration з JSON (наприклад, простим хелпером у цьому ж модулі, як у підказці в task_01).

**Зайві коментарі**

3. **`domain/models.py`** — залишено закоментований рядок `#raise NotImplementedError` після `return total`. Його варто видалити.

4. **`json_store.py`** — коментарі типу `# TODO implement after parse_duration_to_minutes` — якщо вже реалізував парсинг (наприклад, у task_02), можна або використати той парсер, або прибрати TODO.

---

## PR #5 — Task 02

**Логіка**

1. **`parse_duration_to_minutes`** — для рядка типу **`"1h "`** (пробіл після `h`) після обробки годин залишається `raw = " "`. Далі `"m" in raw` → False, а `raw.strip()` не порожній тільки якщо там щось крім пробілів. Для `" "` буде `""`, тож ValueError не кидається, і результат коректний. Якщо з’являться формати на кшталт `"1h 30m"` з пробілами — перевір на кількох варіантах, щоб не відрізати зайве.

2. **`parse_log_command`** — якщо команда не починається з `/log` або `/logy` (наприклад, користувач надіслав просто "2h"), буде `ValueError("Unknown command")`. Це ок, якщо ми очікуємо тільки ці два варіанти.

**Зайві коментарі**

3. **`domain/models.py`** — знову залишений `#raise NotImplementedError` після `return total`. Краще видалити.

---

## PR #6 — Task 03

**Баги / логіка**

1. **`json_store.py` — `load()`: повернення `state` у гілці `else`**  
   У блоці `else:` ти робиш `state = State(...)` всередині `with open(...)`, а **`return state`** стоїть уже після блоку `else` (на одному рівні з `if/else`). Тобто після виходу з `with` змінна `state` ще в області видимості, і повертається правильний об’єкт. Але якщо колись винесеш `return` всередину `else`, треба буде повертати саме той `state` — зараз логіка коректна, просто варто мати на увазі.

2. **`save()` — якщо `state.start_date` є `None`**  
   У моделі `State.start_date` має тип `date | None`. У `save()` викликається `state.start_date.isoformat()`. Якщо `start_date is None`, буде **AttributeError**. Варто або перевіряти `if state.start_date is not None` і тоді писати в JSON, або в описі формату зафіксувати, що при збереженні ми завжди очікуємо задану дату (і тоді не створювати State з `start_date=None` для збереження).

3. **Збереження `duration` у `entries`**  
   Зараз duration формується як `f"{e.minutes//60}h{e.minutes%60}m"` або `f"{e.minutes}m"`. Для значень на кшталт 90 хвилин вийде "1h30m" — це узгоджується з тим, що очікує `parse_duration_to_minutes` при читанні. Ок.

**Зайві коментарі**

4. **`domain/models.py`** — знову той самий закоментований `#raise NotImplementedError` — варто прибрати в цій гілці разом з іншими змінами.

---

## PR #7 — Task 04

**Логіка**

1. **`compute_status`: "done" має рахуватися лише з `start_date`**  
   У таску сказано: *"Done minutes: sum of logged minutes **since start_date**"*. Зараз робиться:
   `done_minutes = sum(entry.minutes for entry in state.entries)`  
   Тобто враховуються **всі** записи. Правильно — тільки ті, де **`entry.day >= state.start_date`** (і варто врахувати випадок, коли `state.start_date is None` — тоді або рахувати всі записи, або 0, залежно від того, як ти визначиш семантику). Наприклад:
   - `done_minutes = sum(e.minutes for e in state.entries if state.start_date is not None and e.day >= state.start_date)`  
   або окрема перевірка на `None` і потім фільтр по даті.

2. **`compute_status`: нескінченний цикл при `daily_target_minutes == 0`**  
   Якщо в `state.schedule.daily_target_minutes` буде 0 (наприклад, порожній дефолтний state у task_03), то в циклі `remaining_work -= state.schedule.daily_target_minutes` ніколи не зменшить `remaining_work`, і цикл буде нескінченним. Варто на початку перевірити: якщо `state.schedule.daily_target_minutes <= 0`, то або вважати deadline = today / не рахувати дни, або одразу виходити з циклу з якимось дефолтним дедлайном.

3. **Дедлайн: чи рахувати сьогодні як workday**  
   Зараз ти починаєш з `expected_deadline_date = today` і одразу робиш `expected_deadline_date += timedelta(days=1)`, тобто проекція йде з **завтра**. Для "days left" це часто прийнятно (сьогодні вже не "залишилось"). Якщо в таску очікується "перший день, коли план виконано" — поточна логіка теж виглядає розумно. Залишаю лише як зауваження.

**Зайві коментарі**

4. У **`handlers.py`** імпорт `datetime` здається не використаним (використовується лише `date`). Можна прибрати з імпортів, щоб не залишати зайве.

5. **`domain/models.py`** — знову той самий `#raise NotImplementedError` після `return total` — варто видалити.

---

## Підсумок

- **Task 00**: ок.
- **Task 01**: обов’язково виправити тип дати (`.date()`) і не хардкодити minutes у 1; прибрати `#raise NotImplementedError` і зайві TODO.
- **Task 02**: прибрати закоментований `#raise NotImplementedError`.
- **Task 03**: обробити `start_date is None` у `save()`; прибрати закоментований рядок у models.
- **Task 04**: фільтрувати `done_minutes` по `start_date`; захиститися від `daily_target_minutes == 0` у циклі; прибрати зайвий імпорт і закоментований код у models.

Якщо хочеш, можу окремо сформулювати короткі коментарі під конкретні файли/рядки для вставки в GitHub review.
