from datetime import datetime
from itertools import groupby
from event import Event, InvalidAttendeeOperation


class EventFormatter:
    def __init__(self, event):
        self.event = event

    def format(self):
        time = self.format_time_range()
        event_type = self.event.__class__.__name__
        left_text = f"{time}  ({event_type}) "
        lines = [f"{left_text}{self.event.title}"]
        if self.event.attendees:
            for key, value in self.event.fields().items():
                lines.append(f"{' ' * len(left_text)}{key}: {value}")
        return lines

    def format_time_range(self):
        start = self.format_time(self.event.start)
        end = self.format_time(self.event.end)
        return f"{start} - {end}"

    @staticmethod
    def format_time(time):
        return f"{time:%H:%M}"


class CalendarPrinter:
    WIDTH = 70

    def __init__(self, calendar, event_formatter=EventFormatter):
        self.calendar = calendar
        self.event_formatter = event_formatter

    def print(self):
        print()
        self.print_bar()
        self.print_line("CALENDAR".center(self.WIDTH))
        self.print_bar()
        for day, events in self.calendar.events_by_day():
            self._print_day(day, events)
        print()

    def _print_day(self, date, events):
        date_string = self.format_date(date)
        self.print_line('')
        self.print_line(date_string)
        self.print_line('-' * len(date_string))
        self.print_line('')
        for event in events:
            for line in EventFormatter(event).format():
                self.print_line(line)
            self.print_line('')
        self.print_bar()

    @staticmethod
    def format_date(date):
        return f"{date:%A %d %b, %Y}"

    @classmethod
    def print_line(cls, text):
        if len(text) > cls.WIDTH:
            text = text[:cls.WIDTH - 3] + '...'
        print(f"| {text.ljust(cls.WIDTH)} |")

    @classmethod
    def print_bar(cls):
        print(f"+{'-' * (cls.WIDTH + 2)}+")


class Calendar:
    def __init__(self, events=tuple()):
        self.events = list(events)

    def add_event(self, event):
        self.events.append(event)

    def invite_to_all(self, name):
        for event in self.events:
            try:
                event.add_attendee(name)
            except InvalidAttendeeOperation:
                print(f"Could not invite {name} to {event.__class__.__name__}: {event.title}")

    def remove_from_all(self, name):
        for event in self.events:
            try:
                event.remove_attendee(name)
            except InvalidAttendeeOperation:
                pass

    def move_all(self, timedelta):
        for event in self.events:
            event.move(timedelta)

    def print(self, printer=CalendarPrinter):
        printer(self).print()

    def events_by_day(self):
        return groupby(
            sorted(self.events, key=lambda event: event.start),
            key=lambda event: event.start.date()
        )


def create_example_calendar():
    calendar = Calendar()
    calendar.add_event(Event("Revise the Open Closed principle",
                            start=datetime(2020, 9, 19, 11),
                            end=datetime(2020, 9, 19, 13, 30),
                            attendees=['George Eeliot']))

    calendar.add_event(Event("Skiller Whale Session",
                            start=datetime(2020, 9, 20, 15),
                            end=datetime(2020, 9, 20, 16),
                            attendees=["Salmon Rushdie"]))

    calendar.add_event(Event("Learn about Orca Culture",
                            start=datetime(2020, 9, 20, 16, 30),
                            end=datetime(2020, 9, 20, 18, 30)))

    return calendar
