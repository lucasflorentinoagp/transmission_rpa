import subprocess

# Iniciar o Waydroid caso não esteja rodando
subprocess.run(["sudo", "systemctl", "start", "waydroid-container"])

# Ativar o ADB no Waydroid
subprocess.run(["sudo", "waydroid", "shell", "setprop", "service.adb.enabled", "1"])
subprocess.run(["adb", "connect", "localhost:5555"])

# Executar comandos dentro do shell do Waydroid
cmd = "input tap 500 1000"  # Simular um toque na tela (posição X=500, Y=1000)
subprocess.run(["adb", "shell", cmd])

cmd = "input text 'Olá, mundo!'"  # Digitar um texto no chat
subprocess.run(["adb", "shell", cmd])

cmd = "input keyevent 66"  # Pressionar Enter
subprocess.run(["adb", "shell", cmd])
