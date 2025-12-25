#! /usr/bin/python3
from pathlib import Path
import subprocess

SCRIPT_DIR = str(Path(__file__).parent.absolute())

# subprocess.run(["wget", "https://github.com/fatedier/frp/releases/download/v0.65.0/frp_0.65.0_linux_amd64.tar.gz"])
subprocess.run(["tar", "-xzf", f"{SCRIPT_DIR}/frp_0.65.0_linux_amd64.tar.gz", "-C", f"{SCRIPT_DIR}"])
subprocess.run(["mv", f"{SCRIPT_DIR}/frp_0.65.0_linux_amd64/frpc", f"{SCRIPT_DIR}"])
subprocess.run(["rm", "-rf", f"{SCRIPT_DIR}/frp_0.65.0_linux_amd64"])

service = f'''
[Unit]
Description=Frp Client Service
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
ExecStart={SCRIPT_DIR}/frpc -c {SCRIPT_DIR}/frpc.toml

# 如果你的 frpc 依赖工作目录（例如读取同级目录下的其他文件），可以加上这一行
WorkingDirectory={SCRIPT_DIR}

# 这里的设置可以禁止 frp 修改系统文件，增加安全性（可选）
ProtectSystem=full

[Install]
WantedBy=multi-user.target
'''

f = open(f"{SCRIPT_DIR}/frpc.service", "w")
f.write(service)
f.close()

subprocess.run(["ln", "-sfn", f"{SCRIPT_DIR}/frpc.service", f"{Path.home()}/.config/systemd/user/frpc.service"])
subprocess.run(["systemctl", "--user", "daemon-reload"])
subprocess.run(["systemctl", "--user", "start", "frpc"])
subprocess.run(["systemctl", "--user", "enable", "frpc"])
subprocess.run(["systemctl", "--user", "status", "frpc"])