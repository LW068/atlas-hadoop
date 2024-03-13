#!/usr/bin/python2.7
from snakebite.client import Client
import os

def download(l):
    # initializng the Snakebite client
    client = Client('localhost', 9000)

    # iterating over the list of files to download each one
    for hdfs_path in l:
        local_path = "/tmp" + hdfs_path[hdfs_path.rfind("/"):]
        try:
            for result in client.copyToLocal([hdfs_path], local_path):
                print({
                    'path': local_path,
                    'result': result.get('result', False),
                    'error': result.get('error', ''),
                    'source_path': hdfs_path
                })
        except Exception as e:
            print({
                'path': local_path,
                'result': False,
                'error': str(e),
                'source_path': hdfs_path
            })

# main
if __name__ == "__main__":
    l = ["/holbies/input/lao.txt"]
    download(l)
