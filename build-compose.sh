#!/bin/bash
SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
cd $SHELL_FOLDER && python3 ./compose-build.py $1
ymlfile=$SHELL_FOLDER/docker-compose.yml
envfile=$SHELL_FOLDER/bee.env
echo "cd $SHELL_FOLDER &&docker-compose -f $ymlfile --env-file $envfile up -d" > $SHELL_FOLDER/startup.sh
# docker compose up -d