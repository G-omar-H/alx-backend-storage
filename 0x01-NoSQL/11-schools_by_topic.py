#!usr/bin/env python3
"""
11-schools_by_topic.py
"""


def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of school having a
    specific topic

    Args:
        mongo_collection (_type_): _description_
        topic (_type_): _description_
    """
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))
