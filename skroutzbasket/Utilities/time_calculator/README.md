First of all you need to import datetime<br>

<h4>Days from today</h4>
Returns the date after given days. If true is passed, hence will be calculated backwords

<h5>Example 1:</h5>
If you need to get the date after one week

```python
days_hence(7)
```

<h5>Example 2:</h5>
If you need to get the date before 5 days

```python
calculate_back = True
days_hence(5, calculate_back)
```

<h4>Ensure age of at least 18 years old.</h4>h4>
<h5>Example 1:</h5>
Find if the given birthdate is adult. Default adult years are 18.

```python
sample_date = datetime.date(1987, 8, 13)
is_adult(sample_date)
```

If the given date is over 18 years old, returns True else False
<h5>Example 2:</h5>

```python
sample_date = datetime.date(1987, 8, 13)
adult_years = 21
is_adult(sample_date, adult_years)
```

In some countries adultd age differs, so pass the years you need