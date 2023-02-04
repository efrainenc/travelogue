

def generate_calendar_for_dates(start_date, end_date):
  # Calculate the number of days in the range
  num_days = (end_date - start_date).days + 1
  # Generate the calendar rows
  calendar = []
  for i in range(0, num_days, 7):
    week = []
    for j in range(7):
      day = start_date + timedelta(days=i + j)
      if day <= end_date:
        week.append(day)
    calendar.append(week)

  return calendar
