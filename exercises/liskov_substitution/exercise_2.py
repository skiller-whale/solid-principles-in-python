from datetime import datetime, date

from calendar import create_example_calendar
from event import Event

"""
HINTS:
-----

1. For AllDayEvent to be substituable, it will need `start` and `end` datetime
   attributes. These could be set to 00:00 and 23:59 for the provided date.

2. To convert a date into a datetime, you can use something like the following code.
   It takes a date, `t`, and creates a datetime instance for
   that day at 15:45.

   converted = datetime(t.year, t.month, t.day, 15, 45)
"""

class AllDayEvent(Event):
    def __init__(self, title, date: date, attendees=tuple()):
        self.title = title
        self.date = date
        self.attendees = ["Me"] + list(attendees)

    def move(self, timedelta):
        pass  # AllDayEvents should always go from the start to end of a day


calendar = create_example_calendar()

calendar.add_event(AllDayEvent("Very Long Event", date=date(2020, 9, 21)))

calendar.print()
