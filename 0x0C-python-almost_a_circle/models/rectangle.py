#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width  # private attribute
        self.__height = height  # private attribute
        
        self.__x = x  # private attribute
        self.__y = y  # private attribute
        
    @property
    def private_width(self):
        return self.__width
    
    @private_width.setter
    def private_width(self, value):
        self.__width = value
    
    @property
    def private_height(self):
        return self.__height
    
    @private_height.setter
    def private_height(self, value):
        self.__height = value
    
    
    @property
    def private_x(self):
        return self.__x
    
    @private_x.setter
    def private_x(self, value):
        self.__x = value
        
    @property
    def private_y(self):
        return self.__y
    
    @private_y.setter
    def private_y(self, value):
        self.__y = value