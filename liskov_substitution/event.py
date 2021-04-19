from datetime import datetime, timedelta


class InvalidAttendeeOperation(Exception):
    pass


class Event:
    def __init__(self, title, start: datetime, end: datetime, attendees=tuple()):
        self.title = title
        self.start = start
        self.end = end
        self.attendees = ["Me"] + list(attendees)

    def fields(self):
        """Returns a dict of attributes to describe the event"""
        return {'Attendees': ', '.join(self.attendees)}

    def move(self, delta: timedelta):
        self.start += delta
        self.end += delta

    def add_attendee(self, name):
        if '/' in name:
            raise InvalidAttendeeOperation("Name cannot contain the '/' character")
        self.attendees.append(name)

    def remove_attendee(self, name):
        try:
            self.attendees.remove(name)
        except ValueError:
            raise InvalidAttendeeOperation(f"Could not remove {name} from attendees")
