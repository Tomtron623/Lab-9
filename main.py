key = {"1":"4", "2":"5", "3":"6", "4":"7", "5": "8", "6":"9", "7":"1", "8":"2", "9":"3"}
def encoder(value):
    newValue = ""
    for i in range(len(value)):
        newValue += key.get(value[i])
    return newValue