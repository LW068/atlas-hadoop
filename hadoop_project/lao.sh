#!/bin/bash
echo "uplooding lao.txt to /holbies/input on HDFS..."
hdfs dfs -put lao.txt /holbies/input/lao.txt
echo "upload complete."
