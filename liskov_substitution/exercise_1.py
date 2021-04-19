from datetime import datetime

from calendar import Calendar
from event import Event


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
                         start=datetime(2020, 9, 20, 16),
                         end=datetime(2020, 9, 20, 18, 30)))


# TODO: Define a subclass of Event called Meeting, which has a `location` attribute
...


# calendar.add_event(
#     Meeting("Important Discussions",
#             start=datetime(2020, 9, 21, 17, 0),
#             end=datetime(2020, 9, 21, 17, 45, 0),
#             location="Main Room",
#             attendees=["Sealion Dion"]))


calendar.print()
