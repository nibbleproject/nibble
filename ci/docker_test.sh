#!/bin/bash
#
# Usage: docker_test.sh [DOCKER_IP]

set -e

DOCKER_IP="$1"

if [ -z "$DOCKER_IP" ]; then
    DOCKER_IP='127.0.0.1'
fi

make smoke REMOTE_URL="http://$DOCKER_IP:5000"
