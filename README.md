# Successful-customer-banking

***Всем привет! Меня зовут Кристина Рожкова. Я учусь в online школе [sky.pro](https://sky.pro/#giftpopup) на phyton разработчика. Данный проект является выполнением домашнего задания на втором курсе.***
![фото](https://drive.google.com/file/d/1cNTOJoptHGbSHMw2KLAotzH3SIAwncqy/view?usp=sharing)

Контекст проекта следующий:

*IT-отдел крупного банка делает новые фичи для личного кабинета клиента. Вам доверили реализовать этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.*
*Вы будете работать над проектом на протяжении вЫсех домашних заданий этого курса.*

---
## Установка

1. Клонирование репозитория по [HTTPS](https://github.com/Kristina-Rozhkova/Successful-customer-banking.git)
2. Все зависимости описаны в файле **peproject.toml**, все исключения добавлены в **.gitignore** установку необходимо
начать с:
```
poetry install
```
---
## Использование

**Пакет src содержит следующие модули:**
- [masks.py](src/masks.py)
- [widget.py](src/widget.py)
- [processing.py](src/processing.py)
- [generators.py](src/generators.py)
- [decorators.py](src/decorators.py)
- [utils.py](src/utils.py)
- [external_api.py](src/external_api.py)


**Пакет data содержит следующие файлы:**
-[operations.json](data/operations.json) - для использования в модуле utils.py.
-[operations1.json](data/operations1.json) - для использования в модуле external_api.py.

**Файл .env.txt содержится в пакете src**

---

**Содержание модулей и примеры работы функций пакета src**

1. **masks.py:**
- `def get_mask_card_number()` - *Функция маскирует номера принимаемых карт*

  *Пример работы функции:*

  ```7000792289606361     # входной аргумент```

  ```7000 79** **** 6361  # выход функции```


- `def get_mask_account()` - *Функция маскирует номера принимаемых счетов*

  *Пример работы функции:*

  ```73654108430135874305  # входной аргумент```

  ```**4305  # выход функции```

2. **widget.py**
- `def mask_account_card()` - *Функция принимает номер карты или счета и маскирует его, в зависимости от принятых данных*

  *Пример работы функции:*

  `# Пример для карты`

  `Visa Platinum 7000792289606361  # входной аргумент`

  `Visa Platinum 7000 79** **** 6361  # выход функции`

  `# Пример для счета`

  `Счет 73654108430135874305  # входной аргумент`

  `Счет **4305  # выход функции`


- `def get_date()` - *Функция принимает строковые данные содержащие текущую дату и выводит в удобном формате*

  *Пример работы функции:*

  `"2024-03-11T02:26:18.671407" # входной аргумент`

  `"11.03.2024" # выход функции`

3. **processing.py**

- `def filter_by_state()` - *Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению*

  *Пример работы функции:*

  `# Выход функции со статусом по умолчанию 'EXECUTED'`

  `[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]`

  `# Выход функции, если вторым аргументов передано 'CANCELED'`

  `[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`

  `# пример входных данных` 
  
  `[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`


- `def sort_by_date()` - *Функция должна возвращать новый список, отсортированный по дате (date)*

  *Пример работы функции:*  

  `# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)`
  
  `[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]`
  
  `# Пример входных данных`

  `[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`

4. **generators.py**

Этот модуль содержит функции, реализующие генераторы для обработки данных.

- `def filter_by_currency()` - *Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).*
  
  *Пример использования функции:*

  ` usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(3):
      print(next(usd_transactions)) `

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }


- `def transaction_descriptions()` - *Функция-генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди*

    *Пример использования функции:*

    `descriptions = transaction_descriptions(transactions)
     for _ in range(5):
        print(next(descriptions))`

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

- `def card_number_generator()` - *Функция-генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.*

    *Пример использования функции:*

    `for card_number in card_number_generator(1, 5):
     print(card_number)`

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005


5. **decorators.py**

Этот модуль используется для размещения декораторов.

- `def log()` - *Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.*

Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль):

Если filename задан, логи записываются в указанный файл.

Если filename не задан, логи выводятся в консоль.

Логирование должно включать:

Имя функции и результат выполнения при успешной операции.

Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.

**Пример использования декоратора**

`@log(filename="mylog.txt")
 def my_function(x, y):
     return x + y
 my_function(1, 2)`


6. **utils.py**

Этот модуль используется для работы с json-файлами.

- `def get_financial_transactions()` - *Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.*

Если файл пустой, содержит не список или не найден, функция возвращает пустой список. Функцию поместите в модуль utils.
Файл с данными о финансовых транзациях operations.json размещен в директории *data* в корне проекта.

Ссылка на файл: [operations.json](https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view?usp=sharing).


7. **external_api.py**

Этот модуль используется для взаимодействия с внешними серверами по API-ключу.

- `get_transaction_amount()` - *Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.*

Если транзакция в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.

Для конвертации валюты использовалось Exchange Rates Data API: https://apilayer.com/exchangerates_data-api. 

---


## Тестирование:

**Пакет tests содержит следующие модули:**
-[conftest.py](tests/conftest.py)
-[test_masks.py](tests/test_masks.py)
-[test_processing.py](tests/test_processing.py)
-[test_widget.py](tests/test_widget.py)
-[test_generators.py](tests/test_generators.py)
-[test_decorators.py](tests/test_generators.py)
-[test_utils.py](tests/test_utils.py)
-[test_external_api.py](tests/test_external_api.py)

---

**Содержание модулей:**

1. **conftest.py:**

Модуль содержит фикстуры с выходными данными для последующих тестов.

- Фикстуры для модуля test_mask.py:

`def card_number()` - *Функция выводит замаскированный номер карты*

`def account_number()` - *Функция выводит замаскированный номер счета*

- Фикстуры для модуля widget.py:

`def length_card():` - *Функция выводит варианты неправильно набранного номера **карты** с учетом его необходимой длины*

`def length_account():` - *Функция выводит варианты неправильно набранного номера **счета** с учетом его необходимой длины*

`def without_data_for_mask():` - *Функция выводит случай, когда пользователь не ввел никаких данных о номере карты или счета*

`def datas():` - *Функция выводит отформатированную дату в виде, привычную пользователю (например, 11.03.2024)*

`def get_date_invalid():` - *Функция выводит случай, когда пользователь не ввел никаких данных о дате*

- Фикстуры для модуля processing.py:

`def list_of_dicts():` - *Функция выводит входные данные в виде списка словарей для последующей проверки рабочих модулей*

`def test_filter_canceled():` - *Функция выводит результат работы функции, которая фильтрует список словарей по ключу "state" со значением **"CANCELED"***

`def test_filter_executed()` - *Функция выводит результат работы функции, которая фильтрует список словарей по ключу "state" со значением **"EXECUTED"***

`def date_sort():` - *Функция выводит результат работы функции, которая сортирует список словарей по возрастанию или убыванию(по умолчанию)*

- Фикстуры для модуля generators.py:

`def transaction()` - *Функция выводит входные данные в виде списка транзакций*

`def usd_filtered()` - *Функция возвращает отфильтрованный список транзакций по коду валюты **"USD"***

`def rub_filtered()` - *Функция возвращает отфильтрованный список транзакций по коду валюты **"RUB"***

`def clear_transaction()` - *Функция выводит входные данные в качестве пустого списка транзакций*

`def card_numbers_from_one_to_five()` *Функция возвращает результат работы функции **card_numbers**: первые 5 номеров карт*

2. **test_masks.py:**

Модуль проверяет работу функций из рабочего модуля **masks.py**.

`def test_get_mask_card_number(card_number):` - *Функция проверяет работу функции **get_mask_card_number***

`def test_get_mask_account(account_number):` - *Функция проверяет работу функции **get_mask_account***

3. **test_widget.py**

Модуль проверяет работу функций из модуля **widget.py**.

`def test_mask_account_card(numb, expected):` - *Функция тестирует работу функции **mask_account_card***
Для данной функции создана фикстура с параметризацией для проверки ожидаемого и фактического результата рабочей функции, где numb - значение, которое вводит пользователь, а expected - ожидаемое значение в результате работы рабочей функции.

`def test_mask_account_card_length_of_card(length_card):` - *Функция проверяет работу функции **mask_account_card** в случае, когда длина **счета** не соответствует ожидаемой*

`def test_mask_account_card_length_of_account(length_account):` - *Функция проверяет работу функции **mask_account_card** в случае, когда длина **номера карты** не соответствует ожидаемой*

`def test_mask_account_card_without_data(without_data_for_mask):` - *Функция проверяет работу функции **mask_account_card** в случае, когда пользователь ничего не ввел, т.е. ввел пустое значение*

`def test_get_date(datas, expected_data):` - *Функция проверяет работу функции **get_date***
Для данной функции создана фикстура с параметризацией для проверки ожидаемого и фактического результата работы рабочей функции, где datas - значение, получаемое пользовательским вводом, а expected_data - ожидаемое значение в результате работы рабочей функции.

`def test_get_date_missing_data(get_date_invalid)` - *Функция проверяет работу функции **get_date** в случае, когда пользователь не ввел никакое значение*

4. **test_processing.py**

Модуль проверяет работу функций из модуля **processing.py**.

`def test_filter_by_state_executed(list_of_dicts, test_filter_executed)` - *Функция проверяет работу функции **filter_by_state** со значением **'EXECUTED'** по ключу 'state'*

`def test_filter_by_state_canceled(list_of_dicts, test_filter_canceled)` - *Функция проверяет работу функции **filter_by_state** со значением **'CANCELED'** по ключу 'state'*

`def test_sort_by_date(list_of_dicts, date_sort)` - *Функция проверяет работу функции **sort_by_date***

5. **test_generators.py**

Модуль проверяет работу функций из модуля **generators.py**.

`def test_filter_by_currency_usd()` - *Функция проверяет работу функции **filter_by_currency** со значением **"USD"** по ключу **"code"***

`def test_filter_by_currency_rub`- *Функция проверяет работу функции **filter_by_currency** со значением **"RUB"** по ключу **"code"***

`def test_filter_by_currency_incorrect()` - *Функция проверяет работу функции **filter_by_currency** в случае, когда указанного пользователем значения не нашлось в списке не нашлось*

`def test_filter_by_currency_with_clear_transaction()` - *Функция проверяет работу функции **filter_by_currency** в случае, когда на вход подается пустой список транзакций*

`def test_transaction_descriptions()` - *Функция проверяет корректность работы функции **transaction_descriptions**. На вход подается основной список транзакций и отфильтрованные списки транзакций со значениями **"USD"** или **"RUB***

`def test_transaction_descriptions_with_clear_list()` - *Функция проверяет работу функции **transaction_descriptions** в случае, когда на вход подается пустой список транзакций*

`def test_card_number_generator()` - *Функция проверяет корректность работы функции **card_number_generator***

6. **test_decorators.py**

Модуль проверяет работу функций из модуля **decorators.py**.

`def test_log_success` - *Функция проверяет работу декоратора в случае успешного выполнения*

`def test_log_error` - *Функция проверяет работу декоратора в случае выпадения ошибки*


7. **test_utils.py**

Модуль проверяет работу функций из модуля **utils.py**.

`def test_get_financial_transactions_success()` - *Функция проверяет успешное открытие файла и работу функции.*

`def test_get_financial_transactions_not_found()` - *Функция проверяет результат функции при ненайденном пути.*

`test_get_financial_transactions_clear()` - *Функция проверяет результат функции, если файл пустой.*

`def test_get_financial_transactions_not_list():` - *Функция проверяет результат функции, если файл содержит не список.*

---


## Документация:

Для получения дополнительной информации обратитесь к [документации](//README.md).

## Лицензия:

Этот проект лицензирован по лицензии MIT.
