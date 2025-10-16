#!/bin/sh
rm ~/.config/Code/User/settings.json
rm ~/.config/Code/User/keybindings.json

work_dir=$(cd "$(dirname "$0")" && pwd)
ln -s ${work_dir}/settings.json ~/.config/Code/User/settings.json
ln -s ${work_dir}/keybindings.json ~/.config/Code/User/keybindings.json
cat ${work_dir}/extensions.list | xargs -L 1 code --install-extension