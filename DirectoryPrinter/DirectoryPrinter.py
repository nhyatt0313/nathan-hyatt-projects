import sys
import os

# program arguments
# 0 - DirectoryPrinter.py
# directory to begin (-path)
pathKey = "-path="
# file types to include/exclude (-ftype)
filtersKey = "-filters="
# no parameter needed to indicate inclusion
# parameter to indicate exclusion (-exclude)
excludeKey = "-exclude"

offset = 0

def validFilter(filter):
    invalid = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    startShift = 0
    endShift = len(filter)
    if filter.startswith("*"):
        startShift = 1
    if filter.endswith("*") or filter.endswith("/") or filter.endswith("\\"):
        endShift -= 1
    for i in filter[startShift : endShift]:
        if i in invalid:
            return False
    return True


def filterItem(item, filters):
    #print(f"in filterItem: item={item}, filters={filters}")
    for filter in filters:
        #print(f"checking filter: {filter}")
        if filter.endswith("/"):
            filter = filter.replace("/", "")
        if filter.startswith("*"):
            if item.endswith(filter[1:]):
                #print("returning True")
                return True
        elif filter.endswith("*"):
            if item.startswith(filter[0:-1]):
                #print("returning True")
                return True
        elif item.startswith("*") and item.endswith("*"):
            if filter[1:-1] in item:
                #print("returning True")
                return True
    #print("returning False")
    return False


def directoryPrinter(path, dirFilters, fileFilters, genFilters, include, shift=True):
    global offset
    if shift:
        offset = len(path.split("\\"))
    for item in os.listdir(path):
        if not filterItem(item, genFilters):
            if not os.path.isdir(os.path.join(path, item)) and not filterItem(item, fileFilters):
                spacing = "  " * (len(path.split("\\")) - offset)
                print(f"{spacing}{item}")
            elif not filterItem(item, dirFilters):
                spacing = "  " * (len(path.split("\\")) - offset)
                print(f"{spacing}{item}/")
                directoryPrinter(os.path.join(path, item), dirFilters, fileFilters, genFilters, include, False)


if __name__ == "__main__":
    path = "C:/"
    dirFilters = []
    fileFilters = []
    genFilters = []
    include = True
    for i in sys.argv:
        if i.startswith(pathKey):
            path = i[len(pathKey):]
            print(f"path = {path}")
        if i.startswith(filtersKey):
            strFilters = i[len(filtersKey):]
            strFilters = strFilters.replace("[", "").replace("]", "")
            allFilters = strFilters.split(",")
            for i in allFilters:
                if validFilter(i):
                    if "." in i:
                        fileFilters.append(i)
                    elif i.endswith("/") or i.endswith("\\"):
                        i = i.replace("/", "").replace("\\", "")
                        dirFilters.append(i)
                    else:
                        genFilters.append(i)
                else:
                    print(f"invalid filter: {i}")
            print(f"dirFilters = {dirFilters}")
            print(f"fileFilters = {fileFilters}")
            print(f"genFilters = {genFilters}")
        if i == excludeKey:
            include = False
            print("include toggle turned off")
    print("\n")
    directoryPrinter(path, dirFilters, fileFilters, genFilters, include)