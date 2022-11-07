from tkinter import messagebox, filedialog
from collections import defaultdict
from collections import Counter
import os

class restaurentException(Exception):
        pass

def getTopMenu(filename):
    
    eaterList = []
    foodMenuList = []

    try:
        file = open(filename, 'r')

        for eachLine in file:
            if(eachLine == "\n"):
                continue
            if(":" not in eachLine):
                raise restaurentException("Error: The Log file format is incorrect. ':' is missing.")
            lineSet = eachLine.split(":")
            if(lineSet[0].startswith("e") & lineSet[1].startswith("fm")):
                eaterList.append(lineSet[0])
                foodMenuList.append(lineSet[1][:-1])
                if('' in eaterList):
                    raise restaurentException("Error: The Log file format is incorrect. Some eater_id(s) is/are not logged.")
                if('' in foodMenuList):
                    raise restaurentException("Error: The Log file format is incorrect. Some foodMenu_id(s) is/are not logged.")
            else:
                raise restaurentException("Error: The Log file format is incorrect. The Id format is invalid.")
        
        dinerDict = defaultdict(list)
        for key, value in zip(eaterList, foodMenuList):
            dinerDict[key].append(value)

        for key in dinerDict:
            if(len(dinerDict[key]) != len(set(dinerDict[key]))):
                foodMnenuItems = ','.join(dinerDict[key])
                raise restaurentException("Error: 2 or more instance of the same diner is logged.eaterId: "+key+" foodmenuIds: "+ foodMnenuItems)
        
        result = [item for items, c in Counter(foodMenuList).most_common()
                                        for item in [items] * c]
        topMenu = ""
        i = 0
        currentElement = ""
        for element in result:
            if i>2:
                break
            if element == currentElement:
                continue
            topMenu = topMenu+element+'\n'
            i+=1
            currentElement = element
        file.close()
        return topMenu
        

    except restaurentException as e:
        print(e)
        #messagebox.showerror('Log File Error', e)

    except Exception as e:
        print(e)
        #messagebox.showerror('File Error', e)

if __name__ == "__main__":
    print("Please provide the log file")
    filename = filedialog.askopenfilename(initialdir="/Restaurant App",title="Select File",
        filetypes=[('text files', '*.txt')])
    filename = os.path.basename(filename).split('/')[-1]
    topMenu = getTopMenu(filename)
    print(topMenu)
    if topMenu:
        messagebox.showinfo("Top 3 Menu", topMenu)
