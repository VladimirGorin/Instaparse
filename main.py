from functions import select_function
from utils.analytics_functions.get_analytics import get_analytics

try:
    select_function()
except KeyboardInterrupt:
    print("Процесс был остоновлен в ручную админом")