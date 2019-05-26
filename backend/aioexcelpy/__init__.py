#!/usr/bin/python3
from __future__ import annotations
from .Data import Node, UpdateStream, nodes
from pprint import pprint
import time

async def default_container() -> list:
    pass


def setupStream() -> list:
    global nodes
    stream = []
    for i in range(20):
        stream.append(UpdateStream.generate_pair())
    starting_context = [
        {'id': 'a', 'input': []},
        {'id': 'b', 'input': ['a','e']},
        {'id': 'c', 'input': ['b']},
        {'id': 'd', 'input': ['e']},
        {'id': 'e', 'input': ['a', 'c']},
        {'id': 'f', 'input': ['e','g','d']},
        {'id': 'g', 'input': []},
     ]
    for _dict in starting_context:
        nodes[_dict['id']] = Node(**_dict)
    return stream

def main() -> None:
    start = time.time()
    global nodes
    stream = setupStream()
    pprint(UpdateStream.node_members)
    print('\n')
    for update_pair in stream:
        pprint(f"Update Pair: {update_pair}")
        _id, _value = update_pair
        UpdateStream.update_chain_rxn(_id, _value)
        pprint(UpdateStream.node_members)
        print('\n')

if __name__ == '__main__':
    main()
