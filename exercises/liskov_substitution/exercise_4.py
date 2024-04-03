from datetime import datetime, date, timedelta

from calendar import create_example_calendar
from event import Event


class AllDayEvent(Event):
    def __init__(self, title, date, attendees=tuple()):
        self.title = title
        self.start = datetime(date.year, date.month, date.day, 0, 0)
        self.end = datetime(date.year, date.month, date.day, 23, 59)
        self.attendees = ["Me"] + list(attendees)

    def move(self, delta):
        pass  # AllDayEvents should always go from the start to end of a day


calendar = create_example_calendar()

calendar.add_event(AllDayEvent("Very Long Event", date=date(2020, 9, 21)))

# TODO: Uncomment this line moving all events forward by 23 hours
# calendar.move_all(timedelta(hours=23))

calendar.print()
