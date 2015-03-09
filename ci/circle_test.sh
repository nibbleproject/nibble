#!/bin/bash
#
# Usage: circle_test.sh

case $CIRCLE_NODE_INDEX in
    1)
        ci/heroku_test.sh \
            circle-minicomi-$CIRCLE_BUILD_NUM \
            $HEROKU_AUTH_TOKEN
        ;;
    2)
        ci/docker_test.sh $DOCKER_IP
        ;;
    *)
        ci/python_test.sh
        ;;
esac
