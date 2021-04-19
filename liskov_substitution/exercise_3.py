from datetime import datetime

from calendar import create_example_calendar
from event import Event


class Reminder(Event):
    def __init__(self, title, time):
        super().__init__(title, start=time, end=time)
        self.attendees = tuple()  # Ensure that attendees is an empty tuple

    def add_attendee(self, name):
        """Override method to prevent addition of an attendee"""
        raise NotImplementedError(f"Cannot add attendees to a Reminder")


# Create an example calendar and add a Reminder
calendar = create_example_calendar()
calendar.add_event(Reminder("Feed Sharkimedes", time=datetime(2020, 9, 20, 16, 15)))
calendar.print()


# TODO 1 - Uncomment the 2 lines below
# calendar.invite_to_all("Ernest Herringway")  # Calls add_attendee on each Event
# calendar.print()


# TODO 2 - Uncomment the 2 lines below
# calendar.remove_from_all("Me")  # Calls remove_attendee on each Event
# calendar.print()
