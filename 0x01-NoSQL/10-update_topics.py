#!/usr/bin/python3
"""
10-update_topics.py
"""


def update_topics(mongo_collection, name, topics):
    """
     Python function that changes all topics of a school document
     based on the name

    Args:
        mongo_collection (_type_): Mongo collection object
        name (_string): name of a school
        topics (_list): list of topics approached in the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
