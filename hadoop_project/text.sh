#!/bin/bash
echo "displaying content of lao.txt from HDFS..."
hdfs dfs -cat /holbies/input/lao.txt
echo "content displayed."
