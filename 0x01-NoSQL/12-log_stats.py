#!/usr/bin/env python3
"""
12-log_stats.py
"""


from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
nginx_collection = client.logs.nginx
number_logs = nginx_collection.count_documents({})
num_get = nginx_collection.count_documents({"method": "GET"})
num_post = nginx_collection.count_documents({"method": "POST"})
num_put = nginx_collection.count_documents({"method": "PUT"})
num_patch = nginx_collection.count_documents({"method": "PATCH"})
num_delete = nginx_collection.count_documents({"method": "DELETE"})
num_status_get = nginx_collection.count_documents({"method": "GET",
                                                  "path": "/status"})

print(
    f"{number_logs} logs\nMethods:\n\tmethod GET: {num_get}\
        \n\tmethod POST: {num_post}\n\t\
method PUT: {num_put}\n\t\
method PATCH: {num_patch}\n\t\
method DELETE: {num_delete}\n\
{num_status_get} status check"
)
