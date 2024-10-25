def time_string(hour, min, time):
    if time == 12:
        if hour >= 12:
            if int((hour-12)/10) == 0:
                if int(min/10) == 0:
                    print(f'0{hour-12}:0{min}pm')
                else:
                    print(f'0{hour-12}:{min}pm')
            else:
                if int(min/10) == 0:
                    print(f'{hour}:0{min}pm')
                else:
                    print(f'{hour}:{min}pm')
        else:
            if int(hour/10) == 0:
                if int(min/10) == 0:
                    print(f'0{hour}:0{min}am')
                else:
                    print(f'0{hour}:{min}am')
            else:
                if int(min/10) == 0:
                    print(f'{hour}:0{min}am')
                else:
                    print(f'{hour}:{min}am')
    elif time == 24:
        if int(hour/10) == 0:
                if int(min/10) == 0:
                    print(f'0{hour}:0{min}')
                else:
                    print(f'0{hour}:{min}')
        else:
                if int(min/10) == 0:
                    print(f'{hour}:0{min}')
                else:
                    print(f'{hour}:{min}')
bro = int(input())
bro1 = int(input())
bro2 = int(input())
print(time_string(bro,bro1,bro2))
