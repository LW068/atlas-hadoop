#!/usr/bin/python3
"""importing"""
from snakebite.client import Client

def createdir(l):
    """creating idrectory"""
    # initializing the Snakebite client
    client = Client('localhost', 9000)

    # iterating over the list of dirs
    for directory in l:
        for result in client.mkdir([directory], create_parent=True):
            print({'path': directory, 'result': 'result' in result})

# main
if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)
