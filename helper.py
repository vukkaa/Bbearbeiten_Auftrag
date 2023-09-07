from dataclasses import dataclass
import datetime

items = []


@dataclass
class Item:
    text: str
    date: datetime
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')

    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    items.append(Item(text, date))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
