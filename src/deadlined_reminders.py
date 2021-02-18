from abc import ABCMeta, abstractmethod
from collections.abc import Iterable

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
   
    def is_due(self):
        pass

# ABCMeta is the Meta Class which can be used to implement our Abstract base class
# abstractmethod is a decorator
