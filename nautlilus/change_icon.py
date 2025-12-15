from pathlib import Path
import subprocess

dir = Path(__file__).parent
source = open('/usr/share/applications/org.gnome.Nautilus.desktop', 'r', encoding='utf-8')
target = open(dir.joinpath('org.gnome.Nautilus.desktop'), 'w', encoding='utf-8')
for line in source:
    current_line = line.rstrip('\n')
    if current_line == 'Icon=org.gnome.Nautilus':
        target.write('Icon=' + dir.joinpath('folder2.png').absolute().__str__() + '\n')
    else:
        target.write(line)

subprocess.run([
                "ln", "-sfn", 
                dir.joinpath('org.gnome.Nautilus.desktop').__str__(),
                Path('~/.local/share/applications/org.gnome.Nautilus.desktop').expanduser().__str__()
                ])
subprocess.run([
                "update-desktop-database",
                Path('~/.local/share/applications/').expanduser().__str__()
                ])