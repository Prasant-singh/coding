# Example: If today is 2025-07-31, time_until_event("2025-08-05") might return "5 days, 0 hours, 0 minutes remaining."

import datetime

today = datetime.datetime.now()
time= datetime.datetime(2025, 8, 5)

time_until_event = time - today
print(time_until_event, "remaining.")