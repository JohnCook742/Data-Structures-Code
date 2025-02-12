from abc import ABC, abstractmethod

class Bag(ABC):

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
