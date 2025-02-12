from abc import ABC, abstractmethod

class Map(ABC):

  @abstractmethod
  def add(self, key, value):
    pass

  @abstractmethod
  def remove(self, key):
    pass

  @abstractmethod
  def update_value(self, key, value):
    pass

  @abstractmethod
  def get_value(self, key):
    pass

  @abstractmethod
  def get_keys(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass