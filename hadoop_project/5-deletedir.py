#!/usr/bin/python3
"""importing"""
from snakebite.client import Client

def deletedir(l):
    """deleting directory"""
    # initializing the Snakebite client
    client = Client('localhost', 9000)

    # iterating over the list of dirs
    for directory in l:
        for result in client.delete([directory], recurse=True):
            print({'path': result['path'], 'result': result['result']})

# main
if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    deletedir(l)
