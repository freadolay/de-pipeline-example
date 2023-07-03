from datetime import datetime

today_str = datetime.now().strftime('%A, %B ')
print(f"Date and time at DAG run was: {today_str}")