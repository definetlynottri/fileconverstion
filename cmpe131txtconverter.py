import json
import csv
import xml

def convertFile(FileLink, formatLetter):
    if(formatLetter == 'c'):
        convertCSV(FileLink)
    if(formatLetter == 'x'):
        convertXML(FileLink)
    if(formatLetter == 'j'):
        convertJSON(FileLink)

def convertJSON(FileLink):
    #creats dictionary for lines of text
    textdictionary= {}

    # opens file and filters extra spaces from text
    # puts filtered words in dictionary
    with open(FileLink) as x:
        for line in x:
            command, description = line.strip().split(None,1)
            textdictionary[command] = description.strip()

    #creates new json file
    jsonFile= open('txttojson.json', "x")

    #dumps words from dictionary created from txt file into json file
    json.dump(textdictionary, jsonFile, indent= 4, sort_keys= False)
    jsonFile.close

    print("json success")


def convertCSV(FileLink):
    open(r'texttocsv.csv', 'x')
    rowsdict= []

    with open(FileLink) as x:
        for line in x:
            linelist= line.split()
            rowsdict.append(linelist)
    print(rowsdict)
    with open(r'texttocsv.csv', 'w') as x:
        writer= csv.writer(x)
        writer.writerows(rowsdict)
        print ("csv success")

def convertRow(headers, row):
    s = '<row id="{row[0]}">\n'
    for header, item in zip(headers, row):
        s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
    return s + '</row>'

def convertXML(FileLink):
    open(r'texttoxml.xml','x')
    with open('texttocsv.csv', 'r') as f:
        r = csv.reader(f)
        headers = next(r)
        xml = '<data>\n'
        for row in r:
            xml += convertRow(headers, row) + '\n'
    xml += '</data>'
    with open('texttoxml.xml',  "w") as x:
        x.write(xml);
    print("xml success")
   

convertFile(r'C:\Users\tritt\Downloads\testfile.txt', 'j')
convertFile(r'C:\Users\tritt\Downloads\testfile.txt', 'c')
convertFile(r'C:\Users\tritt\Downloads\testfile.txt', 'x')
