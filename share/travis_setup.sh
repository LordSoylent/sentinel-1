#!/bin/bash
set -evx

mkdir ~/.suncoincore

# safety check
if [ ! -f ~/.suncoincore/.suncoin.conf ]; then
  cp share/suncoin.conf.example ~/.suncoincore/suncoin.conf
fi
