<<<<<<< HEAD
#!/bin/sh
rm ~/.config/Code/User/settings.json
rm ~/.config/Code/User/keybindings.json

work_dir=$(cd "$(dirname "$0")" && pwd)
ln -s ${work_dir}/settings.json ~/.config/Code/User/settings.json
ln -s ${work_dir}/keybindings.json ~/.config/Code/User/keybindings.json
cat ${work_dir}/extensions.list | xargs -L 1 code --install-extension
=======
#! /usr/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

rm ~/.config/Code/User/settings.json
rm ~/.config/Code/User/keybindings.json

ln -sfn $SCRIPT_DIR/settings.json ~/.config/Code/User/settings.json
ln -sfn $SCRIPT_DIR/keybindings.json ~/.config/Code/User/keybindings.json
cat $SCRIPT_DIR/extensions.list | xargs -L 1 code --install-extension

wget https://download.jetbrains.com/fonts/JetBrainsMono-2.304.zip -O $SCRIPT_DIR/JetBrainsMono.zip
unzip -d $SCRIPT_DIR/JetBrainsMono $SCRIPT_DIR/JetBrainsMono.zip
mkdir -p ~/.local/share/fonts/
mv $SCRIPT_DIR/JetBrainsMono/fonts/ttf/*.ttf ~/.local/share/fonts/
rm -r $SCRIPT_DIR/JetBrainsMono
>>>>>>> 27cf1984dae6b57af8d35ff9c543d63f26a9ac9a
