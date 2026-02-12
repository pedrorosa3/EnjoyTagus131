#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 131
# 62904 Pedro Rosa
# 60290 João Martins



from readingFromFiles import readRequestsFile,readScheduleFile,readSkippersFile,removeHeader
from dateTime import Date_toInt,Int_to_Hora,DayTomoroww,HourToMinutes,AfterHour
from constants import SKIPPER_ENDDATE_IDX,SKIPPER_ENDHOUR_IDX,SKIPPER_ESPECIALIZATION_IDX,SKIPPER_HOURSACUMULATED_IDX,SKIPPER_HOURWITHOUTBREAK_IDX,SKIPPER_LANGUAGE_IDX,SKIPPER_LEVEL_IDX,SKIPPER_NAME_IDX,SKIPPER_PRICEHOUR_IDX,SCHEDULE_SKIPPERSNAME_IDX  
from constants import CLIENT_ESPECIALIZATION_IDX,CLIENT_HOURS_IDX,CLIENT_LANGUAGE_IDX,CLIENT_LEVEL_IDX,CLIENT_NAME_IDX,SCHEDULE_CLENTNAME_IDX
from constants import SCHEDULE_CLENTNAME_IDX,SCHEDULE_DATE_IDX,SCHEDULE_HOUR_IDX,SCHEDULE_HOURSNAVEGATION_IDX,SCHEDULE_PRICE_IDX,SCHEDULE_SKIPPERSNAME_IDX,HEADER_DATE_IDX,HEADER_HOUR_IDX,NOT_ASSIGNED



def updateSchedule(skippers, schedule, requests, previousDate, previousHour, startHourHeader):
	"""
        Update cruises' schedule assigning the cruises requested given
        to the skippers given taking into account a previous schedule.
	
	Requires:
	skippers is a list of lists with the structure as in the output of
	readingFromFiles.readSkipersFile concerning the previous update time;
	schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
	requests is a list of lists with the structure as in the output of 
	readingFromFiles.readRequestsFile concerning the current update time;
	date is string in format DD:MM:YYYY with the previous update date;
	hour is string in format HH:MN: with the previous update hour;
	Ensures:
	a list of cruises, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	(omitted here for the sake of readability).
	"""
	
	

	to_delete = []
	for k in range(0, len(schedule)):
		
		if Date_toInt(schedule[k][SCHEDULE_DATE_IDX]) < Date_toInt(previousDate):
			to_delete.append(k)
		elif Date_toInt(schedule[k][SCHEDULE_DATE_IDX])+Date_toInt(schedule[k][SCHEDULE_HOUR_IDX])+HourToMinutes(schedule[k][SCHEDULE_HOURSNAVEGATION_IDX]) <= Date_toInt(previousDate)+Date_toInt(previousHour):
			to_delete.append(k)

	for k in sorted(to_delete, reverse=True):
		del(schedule[k])

	

	not_assigned = []
	for i in range(len(requests)):
		skippers_available=[]
		for n in range(len(skippers)):
			
			
			
			if skippers[n][SKIPPER_LEVEL_IDX]==requests[i][CLIENT_LEVEL_IDX] and \
			skippers[n][SKIPPER_ESPECIALIZATION_IDX]==requests[i][CLIENT_ESPECIALIZATION_IDX] and \
			(skippers[n][SKIPPER_LANGUAGE_IDX][0] in requests[i][CLIENT_LANGUAGE_IDX]or \
			skippers[n][SKIPPER_LANGUAGE_IDX][1] in requests[i][CLIENT_LANGUAGE_IDX] or\
			skippers[n][SKIPPER_LANGUAGE_IDX][2] in requests[i][CLIENT_LANGUAGE_IDX] or\
			skippers[n][SKIPPER_LANGUAGE_IDX][3] in requests[i][CLIENT_LANGUAGE_IDX]) and \
				int(skippers[n][SKIPPER_HOURSACUMULATED_IDX])+int(requests[i][CLIENT_HOURS_IDX]) <= int(skippers[n][SKIPPER_HOURWITHOUTBREAK_IDX]):

				if Date_toInt(skippers[n][SKIPPER_ENDHOUR_IDX])+HourToMinutes(requests[i][CLIENT_HOURS_IDX])<=2000 :
					skippers_available.append(skippers[n])
					skippers_available.sort(key=lambda skippers_available: (skippers_available[SKIPPER_ENDHOUR_IDX],skippers_available[SKIPPER_PRICEHOUR_IDX],\
						skippers_available[SKIPPER_HOURSACUMULATED_IDX],skippers_available[SKIPPER_NAME_IDX]))
				else:
					
					skippers_available.append([skippers[n][SKIPPER_NAME_IDX],skippers[n][SKIPPER_LANGUAGE_IDX],skippers[n][SKIPPER_LEVEL_IDX],skippers[n][SKIPPER_PRICEHOUR_IDX],\
						skippers[n][SKIPPER_ESPECIALIZATION_IDX],\
						skippers[n][SKIPPER_HOURWITHOUTBREAK_IDX],skippers[n][SKIPPER_HOURSACUMULATED_IDX],DayTomoroww(skippers[n][SKIPPER_ENDDATE_IDX]),"08:00"])

					
					skippers_available.sort(key=lambda skippers_available: (skippers_available[SKIPPER_ENDHOUR_IDX],skippers_available[SKIPPER_PRICEHOUR_IDX],\
						skippers_available[SKIPPER_HOURSACUMULATED_IDX],skippers_available[SKIPPER_NAME_IDX]))

		if len(skippers_available)==0: 
			
			not_assigned.append([previousDate,NOT_ASSIGNED,requests[i][CLIENT_NAME_IDX]])
		else:

			if Date_toInt(skippers_available[0][SKIPPER_ENDDATE_IDX]) == Date_toInt(schedule[0][SCHEDULE_DATE_IDX]) and\
				 Date_toInt(skippers_available[0][SKIPPER_ENDHOUR_IDX]) < Date_toInt(AfterHour(startHourHeader)):

				skippers_available[0][SKIPPER_ENDHOUR_IDX] = AfterHour(startHourHeader)
			
			schedule.append([skippers_available[0][SKIPPER_ENDDATE_IDX],skippers_available[0][SKIPPER_ENDHOUR_IDX],requests[i][CLIENT_HOURS_IDX],\
				skippers_available[0][SKIPPER_NAME_IDX],int(skippers_available[0][SKIPPER_PRICEHOUR_IDX])*int(requests[i][CLIENT_HOURS_IDX]),requests[i][CLIENT_NAME_IDX]])

			schedule_new_element=[skippers_available[0][SKIPPER_ENDDATE_IDX],skippers_available[0][SKIPPER_ENDHOUR_IDX],requests[i][CLIENT_HOURS_IDX],\
				skippers_available[0][SKIPPER_NAME_IDX],int(skippers_available[0][SKIPPER_PRICEHOUR_IDX])*int(requests[i][CLIENT_HOURS_IDX]),requests[i][CLIENT_NAME_IDX]]

			
			skippers_available[0][SKIPPER_HOURSACUMULATED_IDX]=int(skippers_available[0][SKIPPER_HOURSACUMULATED_IDX])+int(schedule_new_element[SCHEDULE_HOURSNAVEGATION_IDX])
			skippers_available[0][SKIPPER_ENDDATE_IDX]=""+schedule_new_element[SCHEDULE_DATE_IDX]
			skippers_available[0][SKIPPER_ENDHOUR_IDX]=Int_to_Hora(Date_toInt(schedule_new_element[SCHEDULE_HOUR_IDX])+(int(schedule_new_element[SCHEDULE_HOURSNAVEGATION_IDX])*100)) +""
			
			for k in range(0, len(skippers)):
				if skippers[k][SKIPPER_NAME_IDX] == skippers_available[0][SKIPPER_NAME_IDX]:
						skippers[k]=skippers_available[0]
						

			
			
	schedule.sort(key=lambda schedule: (schedule[SCHEDULE_DATE_IDX],schedule[SCHEDULE_HOUR_IDX],schedule[SCHEDULE_SKIPPERSNAME_IDX]))

	for i in range(0, len(not_assigned)):
		schedule.insert(i, not_assigned[i])	                              

	return skippers,schedule
			
			




		
	


	











