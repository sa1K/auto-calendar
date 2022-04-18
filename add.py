from ast import While
from datetime import datetime, timedelta, date

from setup import get_calendar_service


def main():
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()
   while True:
      try:
         date= str(input("Enter date of event: "))
         dateC= datetime.strptime(date, '%m/%d/%Y')
         break
      except ValueError:
         print("You entered your date in the wrong format. Please enter in format month/day/YYYY.")
   name=str(input("Enter name of event: "))
   startTime= str(input("Enter the time of event: "))
   timeR= datetime.strptime(startTime, '%h:%m')
   print(timeR)
   tomorrow = datetime(dateC.year, dateC.month, dateC.day, 10)+timedelta(days=1)
   print(tomorrow)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
	   body={
		   "summary": name,
		   "description": 'This is a tutorial example of automating google calendar with python',
		   "start": {"dateTime": start, "timeZone": 'America/New_York'},
		   "end": {"dateTime": end, "timeZone": 'America/New_York'},
	   }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main()
