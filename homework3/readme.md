# Задание 3
1. Соберите данные о погоде в разных городах мира за последниймесяц. Используйте открытые источники данных, такие как API погодныхсервисов или веб-скрейпинг.
2. Выведете график изменения температуры в разных городах, график распределения температуры. 
3. Сохранить результаты в HDFS
4. Выгрузить результаты из HDFS на локальный компьютер

## Загрузка данных с сайта

Сайт <https://meteostat.net>

<https://dev.meteostat.net/python/#installation>
```
# создаем и активируем среду
python -m venv venv
venv\Scripts\activate

# ставим пакет
pip install meteostat
```

Файл homework3.py - загрузка данных с сайта, координаты с сайта

<https://time-in.ru/coordinates/russia>

python homework3.py

## Загрузка данных в superset
+ Data - Upload csv to database
```
SELECT * from temperatures;
```

Преобразуем даты
```
ALTER TABLE temperatures ADD COLUMN date_temp DATE;
UPDATE temperatures SET date_temp = TO_DATE(time,'YYYY-MM-DD');
```

## Создать диаграммы
### Графики изменения температур
```
SELECT date_temp, tavg, city FROM temperatures;
CREATE CHART - Line Chart
X-axis  - date_temp - Month
Dimensions - city
Metrics - Simple - AVG(tavg)
```

### Графики распределения температур
```
SELECT tavg, city FROM temperatures;
CREATE CHART - Line Chart
X-axis  - date_temp - Month
Dimensions - city
Metrics - Simple - AVG(tavg)
```

## Создаем диаграмму
Результат в файле 

графики-температур-2024-09-19T06-00-03.249Z.pdf


