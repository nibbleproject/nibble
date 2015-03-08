#!/bin/bash
#
# Usage: circle_setup.sh

case $CIRCLE_NODE_INDEX in
    0)
        ci/heroku_setup.sh \
            $CIRCLE_SHA1 \
            circle-minicomi-$CIRCLE_BUILD_NUM \
            $HEROKU_AUTH_TOKEN
        ;;
    1)
        ci/docker_setup.sh
        ;;
    2)
        ci/python_setup.sh
        ;;
esac
