#!/usr/bin/env python3
"""
9-insert_school.py
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document in a collection based on kwargs
    Args:
        mongo_collection (_type_): Mongo collection object
    """
    if not kwargs:
        return None
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
