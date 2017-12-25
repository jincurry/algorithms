#! /usr/bin/env python

from collections import deque


# 图的构建
graph = {}
graph["curry"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_seller(name):
    return name == "thom"


def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]

    searched = []

    while search_queue:
        print(search_queue)
        people = search_queue.popleft()
        print("pop the people {}".format(people))
        if not people in searched:
            if is_seller(people):
                print("{} is a mango seller!!!".format(people))
                print(search_queue)
                return True
            else:
                search_queue += graph[people]
                print("after append, search queue is {}".format(search_queue))
                searched.append(people)
    return False

if __name__ == "__main__":
    breadth_first_search("curry")