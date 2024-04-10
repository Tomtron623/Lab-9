key = {"1":"4", "2":"5", "3":"6", "4":"7", "5": "8", "6":"9", "7":"1", "8":"2", "9":"3"}
def encoder(value):
    newValue = ""
    for i in range(len(value)):
        newValue += key.get(value[i])
    return newValue

key2 = {"4":"1", "5":"2", "6":"3", "7":"4", "8": "5", "9":"6", "1":"7", "2":"8", "3":"9"}
def decoder(value):
    newValue = ""
    for i in range(len(value)):
        newValue += key2.get(value[i])
    return newValue


