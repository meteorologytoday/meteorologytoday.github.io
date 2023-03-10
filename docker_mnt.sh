#!/bin/bash

set -x
docker.exe run -v "$( wslpath -w $( pwd ) ):/srv/website" -it jekyll/jekyll:3.5 bash
