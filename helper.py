from dataclasses import dataclass
import datetime
import operator


items = []


@dataclass
class Item:
    text: str
    date: datetime.date
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now().date()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")

    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    items.append(Item(text, date))

    # Sortierung Datum
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
