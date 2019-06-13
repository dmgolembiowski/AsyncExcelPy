#!/usr/bin/env python3.7
from __future__ import annotations

class Value:
    def __init__(
            self,
            Id=''
            Val=None,
            Input='',
            Row=0,
            Col='',
            **kwargs):
        
        self._internal = {
                'val': Val,
                'input': Input,
                'row': Row,
                'col': Col,
                'id': Id}
        
        self._val = self._internal['val']
        self._input = self._internal['input']
        self._row = self._internal['row']
        self._col = self._internal['col']
        self._id = self._internal['id']
        self.__dict__.update(kwargs)

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, Val):
        self._internal['val'] = Val

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, Input):
        self._internal['input'] = Input

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, Row):
        self._internal['row'] = Row

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, Col):
        self._internal['col'] = Col

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, Id):
        self._internal['id'] = Id

    def __un__(self):
        return self._internal

    @staticmethod
    def __nu__(attrs: dict):
        return Value.__init__(**attrs)

    def __repr__(self):
        return str(self._internal)

class Sheet(dict):

    def __init__(self):
        super().__init__()
    
    '''
    def __setitem(self):
        pass
    '''

class Mapper:
    def __init__(self):
        self._sheet = {}

    @property
    def sheet(self):
        return self._sheet

    
