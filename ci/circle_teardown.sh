#!/bin/bash
#
# Usage: circle_teardown.sh

case $CIRCLE_NODE_INDEX in
    1)
        ci/heroku_teardown.sh \
            circle-minicomi-$CIRCLE_BUILD_NUM \
            $HEROKU_AUTH_TOKEN
        ;;
esac
