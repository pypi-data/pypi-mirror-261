import abc
from typing import List

from hydromill.message.message import Message


class PublisherInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "publish") and callable(subclass.publish)

    @abc.abstractmethod
    def publish(self, topic: str, messages: List[Message]):
        """ """
        raise NotImplementedError


class SubscriberInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "subscribe") and callable(subclass.subscribe)

    @abc.abstractmethod
    def subscribe(self, topic: str):
        """ """
        raise NotImplementedError
