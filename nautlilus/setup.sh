#!/bin/bash

if [ -f /etc/os-release ]; then
    . /etc/os-release
else
    echo "错误: 无法找到 /etc/os-release 文件，无法识别发行版。"
    exit 1
fi

case "$ID" in
    (ubuntu|debian)
        sudo apt install python3-nautilus
        ;;
    (arch)
        sudo pacman -S nautilus-python
        ;;
esac

mkdir -p ~/.local/share/nautilus-python/extensions
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
cp $SCRIPT_DIR/nautilus-wezterm.py ~/.local/share/nautilus-python/extensions
cp $SCRIPT_DIR/nautilus-vscode.py ~/.local/share/nautilus-python/extensions