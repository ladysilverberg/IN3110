#!/bin/bash

path=""

if [ $# -eq 0 ]; then
    path="../"
else
    for i in $(seq "$1")
    do
        path="${path}../"
    done
fi

cd ${path}
