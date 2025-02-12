from abc import ABC, abstractmethod

class List(ABC):

  @abstractmethod
  def add(self, value):
    pass

  @abstractmethod
  def add_front(self, value):
    pass

  @abstractmethod
  def insert_at(self, value, index):
    pass

  @abstractmethod
  def remove(self, value):
    pass

  @abstractmethod
  def remove_index(self, index):
    pass

  @abstractmethod
  def get_value_at(self, index):
    pass

  @abstractmethod
  def contains(self, value):
    pass

  @abstractmethod
  def update_at(self, index, value):
    pass

  @abstractmethod
  def size(self):
    pass