#!/usr/bin/env python3
"""
101-students.py
"""


def top_students(mongo_collection):
    """
    Python function that returns all students sorted by average score:

    Args:
        mongo_collection (_type_): _description_
    """
    for score in  mongo_collection.find( {}, {"topics.score": True, "_id": False} ):
        for value in score.values():
            mongo_collection.update_one({}, {'$set': {"averageScore": {'$avg': value}}})
    return mongo_collection.find({}).sort({"averageScore": 1})
