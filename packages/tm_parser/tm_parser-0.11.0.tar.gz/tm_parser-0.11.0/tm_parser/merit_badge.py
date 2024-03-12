from itertools import chain

from more_itertools import chunked

from .utils import get_date, parse_merit_badge


def split_badge(item):
    """some merit badges are too long like "Emergency Preparedness* 06/20/22"
    fortunately these are all longer than 22 characters, so we split them at the *"""
    if len(item) > 23:
        output = list(item.rsplit(" ", 1))
        return output
    return [item]


def get_full_merit_badges(lines):
    """take a stream of merit badge lines from a pdf"""
    output = chain.from_iterable([split_badge(m) for m in lines])
    data = []
    for item, date_str in chunked(output, 2):
        badge = parse_merit_badge(item)
        data.append(
            MeritBadge(
                name=badge.get("name"),
                date=get_date(date_str),
                eagle_required=badge.get("eagle_required"),
                version=badge.get("version"),
            )
        )
    return data


class MeritBadge:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.date = kwargs.get("date")
        self.eagle_required = kwargs.get("eagle_required")
        self.version = kwargs.get("version")

    def __str__(self):
        return f"{self.name} earned on {self.date} (E: {self.eagle_required})"
