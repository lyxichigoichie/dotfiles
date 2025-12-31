#! /usr/bin/python3
from pathlib import Path
import subprocess

SCRIPT_DIR = str(Path(__file__).parent.absolute())
BIN_DIR = str(Path(__file__).parent.parent.joinpath("bin").absolute())

# subprocess.run(["wget", "https://github.com/hacdias/webdav/releases/download/v5.10.2/linux-amd64-webdav.tar.gz"])
subprocess.run(["mkdir", "-p", f"{SCRIPT_DIR}/webdav"])
subprocess.run(["tar", "-xzf", f"{SCRIPT_DIR}/linux-amd64-webdav.tar.gz", "-C", f"{SCRIPT_DIR}/webdav"])
subprocess.run(["mv", f"{SCRIPT_DIR}/webdav/webdav", f"{BIN_DIR}"])
subprocess.run(["rm", "-rf", f"{SCRIPT_DIR}/webdav"])

service = f'''[Unit]
Description=Webdav Server Service
# 这一点很关键：确保网络连接建立后再启动，否则frp会报错连接失败
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
# 为了安全，不要用 root 运行，除非你需要绑定 1024 以下的端口
User=liyx
Group=liyx

# 关键设置：启动失败后自动重启，适合网络波动的情况
Restart=on-failure
RestartSec=5s

# 这里的路径必须是绝对路径！
ExecStart={BIN_DIR}/webdav -c {SCRIPT_DIR}/config.yaml  >> {SCRIPT_DIR}/log.txt

# 如果你的 frpc 依赖工作目录（例如读取同级目录下的其他文件），可以加上这一行
WorkingDirectory={SCRIPT_DIR}

# 这里的设置可以禁止 frp 修改系统文件，增加安全性（可选）
ProtectSystem=full

[Install]
WantedBy=multi-user.target
'''

f = open(f"{SCRIPT_DIR}/webdav.service", "w")
f.write(service)
f.close()

subprocess.run(["ln", "-sfn", f"{SCRIPT_DIR}/webdav.service", f"{Path.home()}/.config/systemd/user/webdav.service"])
subprocess.run(["systemctl", "--user", "daemon-reload"])
subprocess.run(["systemctl", "--user", "start", "webdav"])
subprocess.run(["systemctl", "--user", "enable", "webdav"])
subprocess.run(["systemctl", "--user", "status", "webdav"])