from functions import select_function

try:
    select_function()
except KeyboardInterrupt:
    print("Процесс был остоновлен в ручную админом")

