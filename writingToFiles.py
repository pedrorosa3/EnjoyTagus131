#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 131
# 62904 Pedro Rosa
# 60290 João Martins


from dateTime import Date_toInt,Int_to_Hora,AfterHour,DayTomoroww
from dateTime import intToTime
from readingFromFiles import removeHeader,readRequestsFile,readScheduleFile,readSkippersFile
from constants import HEADER_DATE_IDX,HEADER_HOUR_IDX
from scheduling import updateSchedule


#FUNÇÃO SCHEDULE - WRITE

def writeScheduleFile(schedule, header, fileName):
    """
    Writes a collection of scheduled cruises into a file.

    Requires:
    schedule is a list with the structure as in the output of
    scheduling.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the cruises in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the cruises as ordered head to tail in schedule.
    """
    

    elements,header=removeHeader(fileName)
    hours_name=AfterHour(header[HEADER_HOUR_IDX]).replace(":","h")
    hours=AfterHour(header[HEADER_HOUR_IDX])
    if hours=="08:00":
        
        day=DayTomoroww(header[HEADER_DATE_IDX])
    else:

        day=header[HEADER_DATE_IDX]

    fileName="schedule"+hours_name+".txt"
    header="Company:\n"+"Tagus Sailing\n"+"Day: \n"+day+"\n"+"Time:\n"+hours+"\n"+"Schedule:\n"






    InFile2=open(fileName,"w",encoding="utf-8")



    InFile2.write(header)
    for line_idx, text in enumerate(schedule):
        if line_idx > 0:
            InFile2.write("\n")
        for x in text:
            if str(x) == text[-1]:
                InFile2.write(x)
                continue
            x = str(x)+", "
            InFile2.write(x)


    InFile2.close()
    return InFile2     



def writeSkippersFile(skippers, header, fileName):
    """
    Writes a collection of skippers into a file
    Requires: 
    skippers is a list  representing the skippers;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:Writes a file with the header and the list of requests as in the examples provided.
    """
    
    skippers.sort()        

    
    

    elements,header=removeHeader(fileName)
    hours_name=AfterHour(header[HEADER_HOUR_IDX]).replace(":","h")
    hours=AfterHour(header[HEADER_HOUR_IDX])
    if hours=="08:00" :
        
        day=DayTomoroww(header[HEADER_DATE_IDX])
    else:

        day=header[HEADER_DATE_IDX]

    fileName="skippers"+hours_name+".txt"
    header="Company:\n"+"Tagus Sailing\n"+"Day: \n"+day+"\n"+"Time:\n"+hours+"\n"+"Skippers:\n"




    InFile1=open(fileName,"w",encoding="utf-8")



    InFile1.write(header)
    for line_idx, text in enumerate(skippers):
        if line_idx > 0:
            InFile1.write("\n")
        for x in text:
                     
            if type(x)==list:
                    
                    x=str(x).replace(',', ';').replace("'", '').replace('[', '(').replace(']', ')') + ', '
                    InFile1.write(x)
            else:
                if str(x) == text[-2]:
                    x = "(" + str(x)
                elif str(x) == text[-1]:
                    x = str(x) + ")"
                    InFile1.write(x)
                    continue

                x = str(x)+", "
                InFile1.write(x)


    InFile1.close()
    return InFile1



