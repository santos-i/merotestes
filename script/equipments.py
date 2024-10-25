from math import radians, cos, sin, degrees, atan2

def defineSN(dict_serialNumbers):
    
    anemometers = []
    barometers = []
    thermohygrometers = []

    for key, value in dict_serialNumbers.items():
        try:
            value = int(value)
            if 'ANE' in key: anemometers.append(value)
            if 'BAR' in key: barometers.append(value)
            if 'TH' in key: thermohygrometers.append(value)
        
        except:pass

    return anemometers, barometers, thermohygrometers


def mean_dir_calc(seq):
    
    u = sum([cos(radians(x)) for x in seq])
    v = sum([sin(radians(x)) for x in seq])
    
    return degrees(atan2(v,u)) % 360