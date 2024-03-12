import json

class Config:
    def __init__(self,filePath):
        self.filePath = filePath
        self.jsonData = {}

    def readLucy(self):
        data = open(self.filePath,"r",encoding="utf-8").readlines()
        reader = Reader(data)
        self.jsonData,error = reader.makeJson()
        if error is None:
            return self.jsonData
        else:
            return None
    def writeLucy(self):
        writer = Writer(self.jsonData)
        writer.makeSpc(self.filePath)

class Reader:
    def __init__(self,chunks):
        self.chips = [chunk.strip() for chunk in chunks if chunk.strip()]
        self.jsonData = {}
    
    def makeJson(self):
        state = ""
        currentKey = ""
        for chip in self.chips:
            if chip[-1] == "{" and "connection" in chip:
                keyWords = [w for w in chip.split(" ") if w.strip() and w not in ["{","connection"]]
                if len(keyWords) == 0:
                    return self.jsonData,Exception("not a valid spc file, error while adding key")
                currentKey = keyWords[0][1:-1]
                self.jsonData[currentKey] = {}
                state = "opened"
            elif state == "opened" and "}" not in chip:
                keyWords = [w.strip() for w in chip.split("=",1) if w.strip()]
                if len(keyWords) != 2:
                    return self.jsonData,Exception("not a valid spc file, error while adding value")
                if keyWords[1][0] == "[":
                    valueData = json.loads(keyWords[1])
                else:
                    valueData = keyWords[1][1:-1]
                self.jsonData[currentKey][keyWords[0]] = valueData
            elif chip == "}":
                state = "closed"
        return self.jsonData,None

class Writer:
    def __init__(self,jsonData):
        self.jsonData = jsonData
    
    def makeSpc(self,filePath):
        fileString = ""
        for conName in self.jsonData:
            fileString += f'connection "{conName}"' + " {\n"
            for keyName,valueName in self.jsonData[conName].items():
                fileString += f"  {keyName} = "
                if type(valueName) == list:
                    fileString += json.dumps(valueName)
                else:
                    fileString += f'"{valueName}"'
                fileString += "\n"
            fileString += "}\n\n"
        spcFile = open(filePath,"w")
        spcFile.write(fileString)
        spcFile.close()
