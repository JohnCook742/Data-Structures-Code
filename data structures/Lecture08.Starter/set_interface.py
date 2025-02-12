from abc import ABC, abstractmethod

class Set(ABC):

  @abstractmethod
  def add(self, value):
    pass

  @abstractmethod
  def remove(self, value):
    pass

  @abstractmethod
  def contains(self, value):
    pass

  @abstractmethod
  def size(self):
    pass