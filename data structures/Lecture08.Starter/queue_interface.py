from abc import ABC, abstractmethod

class Stack(ABC):

  @abstractmethod
  def push(self, value):
    pass

  @abstractmethod
  def dequeue(self, value):
    pass

  @abstractmethod
  def peek(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass