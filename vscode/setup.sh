#! /usr/bin/bash

SCRIPT_DIR=$(dirname "$0")

rm ~/.config/Code/User/settings.json
rm ~/.config/Code/User/keybindings.json

ln -s $SCRIPT_DIR/settings.json ~/.config/Code/User/settings.json
ln -s $SCRIPT_DIR/keybindings.json ~/.config/Code/User/keybindings.json
cat $SCRIPT_DIR/extensions.list | xargs -L 1 code --install-extension

wget https://download.jetbrains.com/fonts/JetBrainsMono-2.304.zip -O $SCRIPT_DIR/JetBrainsMono.zip
unzip -d $SCRIPT_DIR/JetBrainsMono $SCRIPT_DIR/JetBrainsMono.zip
mkdir -p ~/.local/share/fonts/
mv $SCRIPT_DIR/JetBrainsMono/fonts/ttf/*.ttf ~/.local/share/fonts/
rm -r $SCRIPT_DIR/JetBrainsMono