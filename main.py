import subprocess

# Enviar comandos diretamente ao Waydroid Shell
subprocess.run(["waydroid", "shell", "input tap 500 1000"])
subprocess.run(["waydroid", "shell", "input text 'Teste de automação'"])
subprocess.run(["waydroid", "shell", "input keyevent 66"])
