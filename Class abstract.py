# Class abstract instance nya class
# memaksa class untuk menginplementasikan methodnya
# abc = abstact base class

from abc import ABC, abstractmethod

# class python
class Button(ABC):  # BUTTON INI INHERIT ABC JADI CLASS ABSTRACT

    def __init__(self,set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):

    def click(self):
        print("Go to: {}".format(self.link))

    @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link

tombol1 = PushButton("www.facebook.com")
tombol1.click()
