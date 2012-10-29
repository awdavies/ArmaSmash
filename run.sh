#!/bin/bash
TEST=0

# For now, this needs to be changed if the python version
# should be different.
py() {
  python2 $@
}

usage() {
  cat << EOF
  usage: $0 options

  This script runs the main program (for now).  It will also be running
  tests soon enough.

  OPTIONS:
  -t      Run all tests.
  -h      Prints this message.
EOF
}

while getopts "tt:h" OPTION
do
  case $OPTION in
    h)
      usage
      exit
      ;;
    t)
      TEST=1
      ;;
    ?)
      usage
      exit
      ;;
  esac
done

if [[ $TEST != 1 ]]; then
  py arma_smash.py
else
  nosetests-2.7
fi
