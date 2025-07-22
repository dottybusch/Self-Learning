def hours_to_seconds(hours):
    seconds = hours * 60 * 60
    return round(seconds)

def hours_to_minutes(hours):
    minutes = hours * 60
    return round(minutes)

def seconds_to_minutes(seconds):

    if seconds % 60 == 0:
        minutes = seconds / 60
        print(str(round(minutes)) + " Minutes")
    else:
        modmins = round((seconds - (seconds % 60)) / 60)
        mod = seconds % 60
        print(str(modmins) + " Minutes " + str(mod) + " Seconds")
    return(seconds / 60)

def seconds_to_hours(seconds):


    if seconds % (60*60) == 0:
        hours = seconds / (60*60)
        print(str(round(hours)) + " Hours")
    else:
        modhrs = round((seconds - (seconds % (60*60))) / (60*60))
        mod = seconds % (60*60)
        if mod % 60 == 0:
            modmins = round(mod / 60)
        else:
            modmins = round((mod - (mod % 60)) / 60)
            modsecs = mod % 60
        print(str(modhrs) + " Hour " + str(modmins) + " Minutes " + str(modsecs)
               + " Seconds")
    return(seconds / (60*60))
