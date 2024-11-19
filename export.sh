#!/usr/bin/env bash

./build.sh

docker save cwlabcourse | gzip -c > cwlabcourse.tar.gz