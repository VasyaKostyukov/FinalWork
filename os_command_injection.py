import subprocess

input_domain = input("Введите домен: ")

result = subprocess.check_output(
	f"nslookup {input_domain}", shell=True, encoding="UTF-8"
)

print(result)