def add_time(start, duration, *args):
  start = start.split()
  time_indicator = start[1]
  [starth, startmin] = start[0].split(":")
  [durationh, durationmin] = duration.split(":")

  weekdays = [
    "Monday",  
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
  ]

  text = ""
  n = 0
  weekday = ""

  new_hours = int(starth) + int(durationh)
  new_min = int(startmin) + int(durationmin)

  if new_min >= 60:
    new_hours += 1
    new_min = new_min % 60
  
  new_min = f"0{new_min}" if len(str(new_min)) == 1 else new_min
   

  if new_hours >= 12:
    # a is how many 12 in new_hours, b is a remainder of division
    a, b = divmod(new_hours, 12)
    new_hours = b if b else new_hours // a
    
    if a > 1:
      if time_indicator == "PM":
        n = ((a - 1) // 2) + 1
      else:
        n = a // 2
    elif a == 1:
      if time_indicator == "PM":
        n = 1
    
    if a > 0 and a % 2 != 0:
      time_indicator = "AM" if time_indicator == "PM" else "PM"
  else:
    n == 0

  new_time = f"{new_hours}{':'}{new_min} {time_indicator}"

  if args:
    day = f"{args[0].title()}"
    if n > 0:
      index = weekdays.index(day)
      index += n % 7
      if n > 6:
        index = index - 7
      weekday = weekdays[index]
    else:
      index = weekdays.index(day)
      weekday = weekdays[index]
    
    new_time += f", {weekday}"

  if n > 1:
    text = f" ({n} days later)"
    new_time += text
  elif n == 1:
    text = " (next day)"
    new_time += text
  
  return new_time


