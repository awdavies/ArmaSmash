#!/bin/bash
TEST=

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



while getopts "t:h:r" OPTION
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

# TODO: Check python version.
python2 ArmaSmash.py
