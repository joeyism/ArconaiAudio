import os
import json
import datetime

datetime_format = "%Y-%m-%d %H:%M:%S"
current_file_path = os.path.dirname(os.path.realpath(__file__))
cache_file_path = os.path.join(current_file_path, ".cache")
data = {}

if os.path.isfile(cache_file_path):
    data = json.load(open(cache_file_path, "r"))

def set_cache_time():
    data["cache_time"] = datetime.datetime.now().strftime(datetime_format)

def save():
    json.dump(data, open(cache_file_path, "w"))

def should_get_data(show_type):
    if not data:
        return True

    if not data.get("cache_time"):
        return True

    if not data.get(show_type):
        return True

    last_cached_datetime = datetime.datetime.strptime(data.get("cache_time"), datetime_format) 
    a_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    return last_cached_datetime < a_month_ago
