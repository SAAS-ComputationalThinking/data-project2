total_rain = 0
day_count = 0


new_rain = float(input('How much rain today?\t'))

    
while True:
    if new_rain == 9999:
        break
    elif new_rain >= 0:
        total_rain = total_rain + new_rain
        day_count = day_count + 1
        print("Average:\t", total_rain/day_count)
    new_rain = float(input('How much rain today?\t'))
        
