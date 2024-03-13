#!/bin/bash
JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home}" HADOOP_LOG_DIR="/opt/homebrew/var/hadoop" exec "/opt/homebrew/Cellar/hadoop/3.3.6/libexec/sbin/hadoop-daemon.sh"  "$@"
