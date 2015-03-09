#!/bin/bash
#
# Usage: circle_setup.sh

case $CIRCLE_NODE_INDEX in
    1)
        ci/heroku_setup.sh \
            $CIRCLE_SHA1 \
            circle-minicomi-$CIRCLE_BUILD_NUM \
            $HEROKU_AUTH_TOKEN
        ;;
    2)
        ci/docker_setup.sh
        ;;
    *)
        ci/python_setup.sh
        ;;
esac
