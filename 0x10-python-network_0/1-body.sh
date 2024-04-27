#!/bin/bash
# This script takes a URL, sends a GET request to the URL using curl, and displays the body of the response for a 200 status code
curl -s -o /tmp/body.txt -w "%{http_code}" "$1"
status_code=$(cat /tmp/body.txt)
if [[ $status_code -eq 200 ]]; then
    curl -s "$1"
fi
rm -f /tmp/body.txt
