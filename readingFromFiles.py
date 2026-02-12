#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 131
# 62904 Pedro Rosa
# 60290 João Martins




from constants import NUM_HEADER_LINES

def readSkippersFile(fileName):
    """
    Reads a file with a list of skippers into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a skipper listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    
    elements,header=removeHeader(fileName)
    InFile1= elements
    skippers=[]
    
    for line in InFile1:
        list_skippers=(line.rstrip().split(", "))
        list_skippers[1]=list_skippers[1].split("; ")
        list_skippers[7]=list_skippers[7].replace("(","")
        list_skippers[8]=list_skippers[8].replace(")","")


        for i in range(0,len(list_skippers[1])):
            list_skippers[1][i]=list_skippers[1][i].replace("(","").replace(")","")  
            
        skippers.append(list_skippers)
    
    
    
    return skippers




def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.
    Requires: 
    fileName is a string of a .txt file containing a list of requests
    Ensures:
    List of a list where each list correspondes to a requests listed in fileName 
    
    """
    elements,header=removeHeader(fileName)
    InFile3 = elements      
    
    requests = [] 
    for line in InFile3:
        requestData = (line.rstrip().split(", "))
        requestData[1]=(requestData[1]).split("; ")

        for i in range(0, len(requestData[1])):
            requestData[1][i]=requestData[1][i].replace("(","").replace(")","")
        requests.append(requestData)        
    
    return requests






def readScheduleFile(fileName):
    """
    Reads a file whit a schedule and give that schedule into a collection.
    Requires:
    fileName is a string of a .txt file containing list of schedule
    Ensures:
    List of a list where each list correspond to one cruser
    """
    elements,header=removeHeader(fileName)
    InFile2=elements

    schedule=[]
    for line in InFile2:
        scheduledata= (line.rstrip().split(", "))
        schedule.append(scheduledata)
       
    return schedule    














def removeHeader(filename):
    """
    Remove header from .txt file according to example provided
    Requires: File .txt accoding to example provided
    Ensures: List with the information above the header
    """
    list=[]
    header=[]
    
    try:
        file=open(filename,"r")
    except FileNotFoundError:
        print("Could not found this file")
        file.close()
    finally:
        for line in file.readlines():
            list.append(line)
        for i in (list[0:NUM_HEADER_LINES]):
            header.append(i)
            list.remove(i)
        file.close()  
        for n in range(len(header)):
            header[n]=header[n].rstrip() 
            
    return list,header














