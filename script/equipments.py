

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
