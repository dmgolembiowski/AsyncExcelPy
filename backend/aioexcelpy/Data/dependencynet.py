#!/usr/bin/env python3
from __future__ import annotations
import random
from pprint import pprint
from collections import deque
from . import rocketfuel as rf
dynamic_caching = rf.dynamic_caching
nodes = dict()


class Aionode:
    pass

class Node:
    def __init__(self, **kwargs):
        self.value = None
        self.id = ''
        self.input = []
        self.__dict__.update(kwargs)
        UpdateStream.node_members.append(self)

    def __repr__(self):
        return f"Node({self.id})::value={self.value}::input={self.input}"

class UpdateStream:
    node_members = []
    options = ['a','b','c','d','e','f','g']

    @staticmethod
    def possible_ids():
        def id_generator():
            for ever in range(100):
                yield random.choice(UpdateStream.options)
        id_lottery = next(id_generator())
        return id_lottery

    @staticmethod
    def generate_pair():
        _id = UpdateStream.possible_ids()
        _value = random.randrange(1, 100)
        return (_id,_value)

    @classmethod
    @dynamic_caching
    def retrieve_successors(cls, self_id: str) -> list:
        all_my_successors = []
        for node in cls.node_members:
            if self_id in set(tuple(node.input)):
                all_my_successors.append(node.id)
        if all_my_successors == []:
            return None
        return all_my_successors

    @classmethod
    @dynamic_caching
    def __node__(cls, id: str) -> Node:
        for _node in cls.node_members:
            if id == _node.id: return _node

    @classmethod
    @dynamic_caching
    def effected_nodes(cls, update_pair: tuple) -> deque:
        self_id, value = update_pair
        accounted_for = deque(self_id)
        unvisited = deque()
        screening = deque()
        if cls.retrieve_successors(self_id):
            unvisited.extendleft(cls.retrieve_successors(self_id))

        def gen_stack():
            nonlocal accounted_for
            nonlocal unvisited
            while unvisited:
                try:
                    nextId = unvisited.popleft() 
                    if nextId not in accounted_for:
                        accounted_for.append(nextId)
                    if cls.retrieve_successors(nextId):
                        screening.clear()
                        for potential_cycle in cls.retrieve_successors(nextId):
                            if all([potential_cycle not in unvisited,
                                    potential_cycle not in accounted_for]):
                                screening.append(potential_cycle)
                        unvisited.extendleft(screening)
                except IndexError:
                    break

        gen_stack()
        return accounted_for

    @classmethod
    def update_chain_rxn(cls, self_id: str, value: int) -> None:
        quote = '''
            "The flap of a butterfly's wings in Brazil
            can set off a tornado in Texas." --Edward Lorenz'''
        resolution_sequence = cls.effected_nodes((self_id, value))
        butterfly_node = cls.__node__(resolution_sequence.popleft())
        butterfly_node.value = value
        effected_nodes = deque([cls.__node__(n) for n in resolution_sequence])
        while effected_nodes:
            try:
                node = effected_nodes.popleft()
                for inputNode in node.input:
                    try:
                        node.value += cls.__node__(inputNode).value + value
                    except TypeError:
                        node.value = None
            except IndexError:
                break
