#```python
import subprocess

# Ввод адреса репозитория
repo_url = input("Введите адрес репозитория GitHub: ")

# Клонирование репозитория
result = subprocess.run(["git", "clone", repo_url])
if result.returncode == 0:
    print("Репозиторий успешно склонирован.")
    
    # Получение имени каталога
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    # Запуск команды bandit
    bandit_command = ["bandit", "-r", f"./{repo_name}", "-ll", "-f", "html", "-o", f"report_{repo_name}.html"]
    subprocess.run(bandit_command)
else:
    print("Ошибка при клонировании репозитория.")
#```
