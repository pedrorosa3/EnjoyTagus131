#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 131
# 62904 Pedro Rosa
# 60290 João Martins
from dateTime import FileNameToHour,FileNameToSpecification,AfterHour
from readingFromFiles import readRequestsFile,readScheduleFile,readSkippersFile,removeHeader
from scheduling import updateSchedule
from writingToFiles import writeScheduleFile,writeSkippersFile
from constants import HEADER_DATE_IDX,HEADER_HOUR_IDX,HEADER_SPECIFICATION
import sys


skippers=sys.argv[1]
schedule=sys.argv[2]
requests=sys.argv[3]

def assign(skippersFileName, scheduleFileName, requestsFileName):
    """
    Runs the enjoyTagus application.

    Requires:
    skippersFileName is a str with the name of a .txt file containing a list
    of skippers, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of cruises assigned to skippers as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested;
    these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the updated list of cruises assigned
    to skippers and the updated list of skippers, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    skippersXXhYY.txt, where XXhYY represents the time and date 30 minutes
    after the time and date indicated in the files skippersFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    elements,header=removeHeader(skippersFileName)
    elements,header2=removeHeader(scheduleFileName)
    elements,header3=removeHeader(requestsFileName)
    previousDate=header[HEADER_DATE_IDX]
    previousHour=header[HEADER_HOUR_IDX]
    skippers=readSkippersFile(skippersFileName)
    requests=readRequestsFile(requestsFileName)
    schedule=readScheduleFile(scheduleFileName)
    skippers_new,schedule_new=updateSchedule(skippers,schedule,requests,previousDate,previousHour,header[HEADER_HOUR_IDX])
    InFile1=writeSkippersFile(skippers_new,header,skippersFileName)
    header_new=AfterHour(header[HEADER_HOUR_IDX])
    header_new1=header[HEADER_SPECIFICATION]
    header_new2=header2[HEADER_SPECIFICATION]
    header_new3=header3[HEADER_SPECIFICATION]
    InFile2=writeScheduleFile(schedule_new,header,scheduleFileName)
    if header[HEADER_HOUR_IDX]!= FileNameToHour(skippersFileName)or header[HEADER_HOUR_IDX]!= FileNameToHour(requestsFileName) or header[HEADER_HOUR_IDX]!= FileNameToHour(scheduleFileName) or\
        header_new1!= FileNameToSpecification(skippersFileName) or  header_new3!= FileNameToSpecification(requestsFileName) or  header_new2!= FileNameToSpecification(scheduleFileName):
        raise Exception("Input file error: scope or time inconsistency between name and header in file <name of file>.")
    else:
        return InFile1,InFile2
    

print(assign(skippers,schedule,requests))
    


    

    


        

