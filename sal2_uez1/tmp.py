from time import sleep
 def print_countdown(date, minutes_to_midnight):
  if date == "31.12.2021":
   for minute in range(minutes_to_midnight, -1, -1):
    if minute == 0:
     print("60 seconds to midnight!")
    else:
     print(f"{minute + 1} minutes to midnight!")
    for second in range(59, -1, -1):
     if len(str(second)) > 1:
      print(f"{minute}:{second}")
     else:
      print(f"{minute}:0{second}")
     sleep(1)
     if minute == 0 and second == 0:
      print(f"{5 * '*'} Happy new year 2022! {5 * '*'}")
   else:
      print("Countdowns to 2022 can only start on new year's eve!")
