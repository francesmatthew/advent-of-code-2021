""""
File: day12.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-12-2021
Description: https://adventofcode.com/2021/day/12
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

END_NAME = "end"
START_NAME = "start"

class Node:
    """
    self.name: name of the node, case sensitive
    self.is_small: boolean if this node has a lowercase name
    self.links: list of nodes this node is linked to 
    """
    def __init__(self, name:str, *args):
        self.name = name
        self.is_small = name.lower() == name
        self.links = list(args)

    def link(self, node):
        # add the given node to the list of linked nodes
        self.links.append(node)

    def __str__(self):
        fstring= f"{self.name} ->"
        for link in self.links:
            fstring = fstring + " " + link.name
        return fstring

class NodeManager:
    def __init__(self, data_in):
        self.nodes = []
        for line in data_in:
            # parse input data
            # each line has the name of two nodes that are linked to each other
            lname, rname = line.split("-")
            lnode = self.get_node(lname)
            rnode = self.get_node(rname)
            lnode.link(rnode)
            rnode.link(lnode)


    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        # if nodes does not exist, create one
        node = Node(name)
        self.nodes.append(node)
        return node

    def __str__(self):
        rstring = ""
        for node in self.nodes:
            rstring = rstring + str(node) + "\n"
        return rstring

    def get_num_paths_to_end(self, node, visited = [], twice_visited = False):
        # base case
        if node.name == END_NAME:
            return 1

        # recursive case
        num_paths_to_end = 0
        if node.is_small:
            visited.append(node.name)
        for link in node.links:
            if link.name not in visited:
                num_paths_to_end += self.get_num_paths_to_end(link, visited[:], twice_visited)
            elif not(twice_visited) and link.name != START_NAME:
                # if another small cave has not been visited twice, visit this small cave twice
                num_paths_to_end += self.get_num_paths_to_end(link, visited[:], twice_visited=True)

        return num_paths_to_end

def p1(node_mgr):
    return node_mgr.get_num_paths_to_end(node_mgr.get_node(START_NAME), twice_visited=True)

def p2(node_mgr):
    return node_mgr.get_num_paths_to_end(node_mgr.get_node(START_NAME), twice_visited=False)

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day12.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data
    node_manager = NodeManager(data_in)

    solution1 = p1(node_manager)
    solution2 = p2(node_manager)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()