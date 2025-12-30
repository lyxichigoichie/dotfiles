#! /usr/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

rm -rf ~/.config/kitty

ln -sfn $SCRIPT_DIR/../kitty ~/.config/kitty