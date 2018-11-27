total_rain = 0
day_count = 0

new_rain = float(input('How much rain today?\t'))
  
while True:
    if new_rain == 9999:
        break
    elif new_rain >= 0:
        total_rain = total_rain + new_rain
        day_count = day_count + 1
    new_rain = float(input("Average:\t" + str(total_rain/day_count) + '\tHow much rain today?\t'))
        
