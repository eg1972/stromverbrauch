#!/bin/bash

PROJECTDIR="/home/eddgest/PycharmProjects/stromverbrauch"
PYLIBSDIR="/home/eddgest/.local/lib/python3.6/site-packages/stromverbrauch"
EXECDIR="${HOME}/.local/bin"

mkdir -p ${PYLIBSDIR}
rm -rf ${PYLIBSDIR}/*

cp ${PROJECTDIR}/stromverbrauch.py ${EXECDIR}/.

touch ${PYLIBSDIR}/__init__.py
cp ${PROJECTDIR}/libs/*.py ${PYLIBSDIR}/.
