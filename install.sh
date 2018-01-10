#!/usr/bin/env bash

VERCHECK=`python3 -c "import sys; print(int(sys.hexversion >= 0x030600F0))"`

if [ !${VERCHECK} ]
then
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
fi
