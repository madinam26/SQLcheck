def seconds_to_time(seconds):
  """
  Преобразует количество секунд в дни, часы, минуты и секунды.

  Args:
    seconds: Количество секунд.

  Returns:
    Строка с отформатированным временем.
  """
  days = seconds // (24 * 60 * 60)
  hours = (seconds % (24 * 60 * 60)) // (60 * 60)
  minutes = (seconds % (60 * 60)) // 60
  seconds = seconds % 60
  return f'{days} days {hours} hours {minutes} minutes {seconds} seconds'

# Тестовый вызов процедуры
seconds = 123456
formatted_time = seconds_to_time(seconds)
print(formatted_time)
