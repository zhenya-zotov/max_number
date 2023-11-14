list_enter = [1.0,-3.0,0.1,-5]
#return: 150.0

def maxNumber(list_numbers: list):
    tmpMin = list_numbers[0]
    tmpMax = list_numbers[0]
    
    mins = []
    maxs = []
    
    for i in list_numbers[1:]:
        mins.append(tmpMin - i)
        maxs.append(tmpMax - i)
        
        mins.append(tmpMin + i)
        maxs.append(tmpMax + i)
        
        mins.append(tmpMin * i)
        maxs.append(tmpMax * i)
        
        if i != 0:
            mins.append(tmpMin / i)
            maxs.append(tmpMax / i)
        
        tmpMin = min(min(mins), min(maxs))
        tmpMax = max(max(mins), max(maxs))
    return tmpMax

print(maxNumber(list_enter))
