# Processing Module

Модуль для обработки списков словарей (например, банковских транзакций).

## Описание

Модуль предоставляет две основные функции для работы со списками словарей:
- Фильтрация по значению ключа `state`
- Сортировка по дате

## Функции

### `filter_by_state(data, state='EXECUTED')`

Фильтрует список словарей по значению ключа `state`.

**Параметры:**
| Параметр | Тип | Описание | Значение по умолчанию |
|----------|-----|----------|----------------------|
| `data` | `List[Dict[str, Any]]` | Список словарей для фильтрации | Обязательный |
| `state` | `Optional[str]` | Значение для фильтрации | `'EXECUTED'` |

**Возвращает:** `List[Dict[str, Any]]` — отфильтрованный список словарей

**Пример использования:**
```python
from processing import filter_by_state

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Фильтрация по умолчанию (state='EXECUTED')
executed = filter_by_state(transactions)

# Фильтрация с другим значением
canceled = filter_by_state(transactions, "CANCELED")




Функция sort_by_date
Сортирует список словарей по ключу date.

python
from src.processing import sort_by_date

# Пример данных
data = [
    {"id": 1, "date": "2024-03-15T10:30:00"},
    {"id": 2, "date": "2024-03-20T15:45:00"},
    {"id": 3, "date": "2024-03-10T08:15:00"},
]

# Сортировка от новых к старым (по умолчанию)
result_desc = sort_by_date(data)
print(result_desc)
# [{"id": 2, "date": "2024-03-20T15:45:00"},
#  {"id": 1, "date": "2024-03-15T10:30:00"},
#  {"id": 3, "date": "2024-03-10T08:15:00"}]

# Сортировка от старых к новым
result_asc = sort_by_date(data, sort=False)
print(result_asc)
# [{"id": 3, "date": "2024-03-10T08:15:00"},
#  {"id": 1, "date": "2024-03-15T10:30:00"},
#  {"id": 2, "date": "2024-03-20T15:45:00"}]
Параметры
Параметр	Тип	Описание	Значение по умолчанию
data	List[Dict[str, Any]]	Список словарей для сортировки	Обязательный
sort	bool	True - по убыванию, False - по возрастанию	True
Возвращаемое значение
List[Dict[str, Any]] - отсортированный список словарей

Исключения
TypeError - если data не является списком

ValueError - если формат даты некорректен

🧪 Тестирование
Проект содержит полный набор тестов с использованием pytest.

Запуск тестов
bash
# Запустить все тесты
poetry run pytest

# Запустить с подробным выводом
poetry run pytest -v

# Запустить конкретный тест
poetry run pytest tests/test_processing.py::test_filter_by_state_success -v

# Запустить с отчетом о покрытии
poetry run pytest --cov=src --cov-report=html
Структура тестов
python
# Тесты для filter_by_state
test_filter_by_state_success()      # Проверка фильтрации по умолчанию
test_filter_by_canceled_state()     # Проверка фильтрации CANCELED
test_filter_by_state_no_empty_data() # Проверка пустого списка
test_filter_by_state_type_error()    # Проверка типа данных

# Тесты для sort_by_date
test_sort_date_true()               # Сортировка по убыванию
test_sort_date_false()              # Сортировка по возрастанию
test_sort_with_identical_dates()    # Одинаковые даты
test_sort_with_invalid_date_formats() # Некорректные форматы




📁 Структура проекта
text
pythonproject-praktyka/
├── src/
│   ├── __init__.py
│   ├── masks.py           # Маскировка карт и счетов
│   ├── widget.py          # Основные функции (маскировка, дата)
│   └── processing.py      # Фильтрация и сортировка
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Фикстуры pytest
│   ├── test_masks.py      # Тесты для masks.py
│   ├── test_widget.py     # Тесты для widget.py
│   └── test_processing.py # Тесты для processing.py
├── pyproject.toml         # Конфигурация Poetry
├── .gitignore            # Игнорируемые файлы
└── README.md             # Документация





1. Маскировка номера карты
python
from src.masks import get_mask_card_number

# Маскировка номера карты (16 цифр)
masked_card = get_mask_card_number("7000792289606361")
print(masked_card)
# Вывод: 7000 79** **** 6361
Формат маскировки: XXXX XX** **** XXXX

Первые 4 цифры

Следующие 2 цифры

**

****

Последние 4 цифры

2. Маскировка номера счета
python
from src.masks import get_mask_account

# Маскировка номера счета (20 цифр)
masked_account = get_mask_account("73654108430135874305")
print(masked_account)
# Вывод: **4305
Формат маскировки: **XXXX (только последние 4 цифры)

3. Универсальная маскировка карты/счета
python
from src.widget import mask_account_card

# Маскировка карты
result1 = mask_account_card("Visa Platinum 7000792289606361")
print(result1)
# Вывод: Visa Platinum 7000 79** **** 6361

# Маскировка счета
result2 = mask_account_card("Счет 73654108430135874305")
print(result2)
# Вывод: Счет **4305

# Другие примеры
print(mask_account_card("Visa Classic 6831982476737658"))
# Вывод: Visa Classic 6831 98** **** 7658

print(mask_account_card("Счет 64686473678894779589"))
# Вывод: Счет **9589
4. Преобразование даты
python
from src.widget import get_date, get_datee

# Простое преобразование (без datetime)
date1 = get_date("2024-03-11T02:26:18.671407")
print(date1)
# Вывод: 11.03.2024

# Преобразование с использованием datetime
date2 = get_datee("2024-03-11T02:26:18.671407")
print(date2)
# Вывод: 11.03.2024
5. Фильтрация транзакций по статусу
python
from src.processing import filter_by_state

transactions = [
    {"id": 414288297, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

# Фильтрация выполненных операций (по умолчанию)
executed = filter_by_state(transactions)
print(executed)
# Вывод: [{"id": 414288297, "state": "EXECUTED", ...}, 
#         {"id": 939719570, "state": "EXECUTED", ...}]

# Фильтрация отмененных операций
canceled = filter_by_state(transactions, state="CANCELED")
print(canceled)
# Вывод: [{"id": 615064591, "state": "CANCELED", ...},
#         {"id": 594226727, "state": "CANCELED", ...}]
6. Сортировка транзакций по дате
python
from src.processing import sort_by_date

# Сортировка от новых к старым (по умолчанию)
sorted_desc = sort_by_date(transactions)
print(sorted_desc)

# Сортировка от старых к новым
sorted_asc = sort_by_date(transactions, sort=False)
print(sorted_asc)