#!/bin/bash
docker run -d -v "$PWD/testing:/home/jovyan/testing" --name micro phaustin/micro:dec11 tail -F nothere
#docker run --rm -it -v "$PWD/testing:/home/jovyan/testing" phaustin/micro:dec11 ls -al /home/jovyan/testing
