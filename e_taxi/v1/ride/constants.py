import enum


class ChoiceAdapter(enum.IntEnum):

    @classmethod
    def choices(self):
        return ((item.value, item.name.replace("_", " ")) for item in self)

    @classmethod
    def values(self):
        return [item.vale for item in self]


class UserTypes(ChoiceAdapter):
    """ gender type choices"""

    USER = 101
    DRIVER = 102


class RideStatus(ChoiceAdapter):
    """ gender type choices"""

    requested = 101
    accepted = 102
    in_progress = 103
    completed = 104
    cancelled = 105


