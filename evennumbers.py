def print_even_numbers():
  """
  Выводит четные числа от 1 до 10.
  """
  for i in range(1, 11):
    if i % 2 == 0:
      print(i, end=", ")

# Тестовый вызов процедуры
print_even_numbers()
