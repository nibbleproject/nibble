#!/bin/bash
#
# Usage: circle_test.sh

case $CIRCLE_NODE_INDEX in
    0)
        ci/heroku_test.sh \
            circle-minicomi-$CIRCLE_BUILD_NUM \
            $HEROKU_AUTH_TOKEN
        ;;
    1)
        ci/docker_test.sh $DOCKER_IP
        ;;
    2)
        ci/python_test.sh
        ;;
esac
