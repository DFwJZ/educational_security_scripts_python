#!/bin/bash

# Set the output log file
LOG_FILE="/Users/jasonzhang/Documents/Job_Application/interview_coding/verily_second_round/disk_usage.log"

# Get the current disk usage
DISK_USAGE=$(df -h / | grep -E '^/dev' | awk '{print $5}')

# Log the current date and disk usage
echo "$(date +"%Y-%m-%d %H:%M:%S") - Disk usage: ${DISK_USAGE}" >> "${LOG_FILE}"