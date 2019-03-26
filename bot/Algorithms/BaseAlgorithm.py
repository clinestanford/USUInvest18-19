
import abc


class BaseAlgorithm(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getOrder(self):
    	pass
        