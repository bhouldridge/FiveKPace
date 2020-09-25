# 5000m times to per mile and per killometer times
import math

def fivek_pace(total_time):#input time must be in form 'mm:ss'
    total_time = str(total_time)
    if total_time[2] != ':' :
        print('Error, input needs to be in the form "mm:ss"')
    else:     
        minutes = int(total_time[0:2])
        seconds = int(total_time[3:5])
        total_seconds =  (minutes * 60) + seconds
        kilometer_seconds_total = total_seconds / 5
        kilometer_min = math.floor(kilometer_seconds_total / 60) 
        kilometer_sec = str(round(kilometer_seconds_total % 60))
        mile_seconds_total = total_seconds / 3.11
        mile_min = math.floor(mile_seconds_total / 60)
        mile_sec = str(round(mile_seconds_total % 60))
        if len(kilometer_sec) == 1:
            kilometer_sec = '0' + kilometer_sec 
        if len(mile_sec) == 1:
            mile_sec = '0' + mile_sec
        print("Your kilometer pace is {}:{} \nYour mile pace is {}:{}".format(kilometer_min, kilometer_sec, mile_min, mile_sec))
        
        
def fivek_split_to_pace(split_time, distance):#split_time in form 'm:ss', and distance either '1600m' or '1k'
    if split_time[1] != ':' :
        print('Error, split_time input needs to be in the form "m:ss"')
    elif distance == '1600m':
        seconds_in = int(split_time[2:4]) + int(split_time[0]) * 60
        seconds_for_5k = int(seconds_in * 5000 / 1600)
        seconds_out = int(seconds_for_5k % 60)
        minutes_out = int((seconds_for_5k - seconds_out) / 60)
        print('Your 5k time would be {}:{}'.format(minutes_out, seconds_out))
    elif distance == '1k':
        seconds_in = int(split_time[2:4]) + int(split_time[0]) * 60
        seconds_for_5k = int(seconds_in * 5)
        seconds_out = int(seconds_for_5k % 60)
        minutes_out = int((seconds_for_5k - seconds_out) / 60)
        print('Your 5k time would be {}:{}'.format(minutes_out, seconds_out))
    else:   
        print('Error, distanve needs to be either "1600m" or "1k".')