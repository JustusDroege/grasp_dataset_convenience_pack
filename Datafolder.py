import os
import DataInfo
import DataPoint

"""
Datafolder class. Expected arg is a normpath : str
"""
class Datafolder:
    def __init__(self, location) -> None:
        self.location = location

        #get files, full paths
        self.files = self.GetFiles(self, self.location)
        self.filenames = self.GetFilenames(self.files)

        # misc info about data
        self.info = self.GetRange(self.filenames)

        # store data points
        m = self.GetDataPoints()

        self.datapoints = m[0]
        self.incomplete = m[1]

    @staticmethod
    def GetFiles(self, location : str) -> list:
        return [os.path.join(location, f) for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]

    def GetFilenames(self, files : list) -> list:
        filenames = []
        for f in files:
            filenames.append(f.split('/')[-1])
        return filenames

    def GetRange(self, filenames : list) -> DataInfo:
        d_f = c_f = g_f = False
        
        highest = 0
        lowest = 100000
        zfill = 0

        # prefix
        prefix = ""

        #init suffices
        sd, sc, sg = "", "", ""

        def ExtractFileInfo(filename : str):
            prefix = ""
            digits = ""
            suffix = ""

            for s in filename:
                if(s == "."):
                    break
                if(s.isdigit() == False and digits == ""):
                    prefix += s
                elif(str(s).isdigit()):
                    digits += s
                else:
                    suffix += s
            
            return prefix, digits, suffix

        for i in range(len(filenames)):
            if((d_f and c_f and g_f) == False):
                if(".tiff" in filenames[i] and d_f == False):
                    info = ExtractFileInfo(filenames[i].replace(".tiff", ""))
                    if(prefix == ""):
                        prefix = info[0]
                       
                    sd = info[2]
                    if(int(info[1]) > highest):
                        highest = int(info[1].zfill(len(info[1])))
                    if(int(info[1]) < lowest):
                        lowest = int(info[1].zfill(len(info[1])))
                    if(zfill == 0):
                        zfill = len(info[1])

                    d_f = True

                if(".png" in filenames[i] and c_f == False):
                    info = ExtractFileInfo(filenames[i].replace(".png", ""))
                    if(prefix == ""):
                        prefix = info[0]

                    sc = info[2]
                    if(int(info[1]) > highest):
                        highest = int(info[1].zfill(len(info[1])))
                    if(int(info[1]) < lowest):
                        lowest = int(info[1].zfill(len(info[1])))
                    if(zfill == 0):
                        zfill = len(info[1])

                    c_f = True
                if(".txt" in filenames[i] and g_f == False):
                    info = ExtractFileInfo(filenames[i].replace(".txt", ""))
                    if(prefix == ""):
                        prefix = info[0]

                    sg = info[2]
                    if(int(info[1]) > highest):
                        highest = int(info[1].zfill(len(info[1])))
                    if(int(info[1]) < lowest):
                        lowest = int(info[1].zfill(len(info[1])))
                    if(zfill == 0):
                        zfill = len(info[1])
                    g_f = True
                

            # run that loop
            else:
                filename = ""
                if(".tiff" in filenames[i]):
                    filename = filenames[i].replace(".tiff", "")
                if(".png" in filenames[i]):
                    filename = filenames[i].replace(".png", "")
                    
                if(".txt" in filenames[i]):
                    filename = filenames[i].replace(".txt", "")
                    
                digit = ExtractFileInfo(filename)[1].zfill(zfill)
                if(int(digit) > highest):
                    highest = int(digit)
                if(int(digit) < lowest):
                    lowest = int(digit)

        return DataInfo.DataInfo(lowest, highest, zfill, prefix, sd, sc, sg)

    def GetDataPoints(self) -> list:
        data = []
        incompletes = []
        def FindCorrespondance(digit : str):
            d = ""
            c = ""
            g = ""
            for file in self.files:
                if(digit in file):
                    if(".tiff" in file and d == ""):
                        d = file
                        
                    elif(".png" in file and c == ""):
                        c = file
                        
                    elif(".txt" in file and g == ""):
                        g = file
            
            return d,c,g

        for i in range(self.info.data_start, self.info.data_end):
            digit = str(i).zfill(self.info.zfill)
            depth, color, grasps = FindCorrespondance(digit)
            if not depth == "" and not color == "" and not grasps == "":
                data.append(DataPoint.DataPoint(depth, color, grasps))
            else:
                incompletes.append(DataPoint.DataPoint(depth, color, grasps))
        
        return data, incompletes






