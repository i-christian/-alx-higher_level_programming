#!/usr/bin/env bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Send a request to the URL and get the size of the response
response=$(curl -sI $1)
size=$(echo "$response" | awk '/Content-Length/ {print $2}')

# Check if the size of the response is empty
if [ -z "$size" ]; then
    echo "The size of the response could not be determined"
    exit 1
fi

# Display the size of the response in bytes
echo "The size of the response is ${size} bytes"
