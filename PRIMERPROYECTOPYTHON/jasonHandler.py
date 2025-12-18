import json

#Lee y carga el archivo JSON
def readJson(file):
    try: 
        f = open(file, 'r', encoding='utf-8')
        data = json.load(f)
        f.close()
        return data
    except:
        return []

#Escribe y guarda el archivo JSON
def saveData(file, data):
    f = open(file, 'w', encoding='utf-8')
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()

#Guarda el contador en el archivo JSON
def saveCounter(file, counter):
    f = open(file, 'w', encoding='utf-8')
    json.dump(counter, f)
    f.close()

#Lee el contador del archivo JSON
def readCounter(file):
    f = open(file, 'r', encoding='utf-8')
    counter = json.load(f)
    f.close()
    return counter