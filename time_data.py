import time

seconds = time.time()
local_time = time.localtime(seconds)
mdy = (local_time.tm_mon, local_time.tm_mday, local_time.tm_year)