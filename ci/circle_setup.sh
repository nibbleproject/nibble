#!/bin/bash
#
# Usage: circle_setup.sh

# Install geckodriver
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz > geckodriver.tar.gz
tar -zxvf geckodriver.tar.gz
chmod +x geckodriver
export PATH=$PATH:$(pwd)

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
