#!/usr/bin/env python3
"""
8-all.py
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The PyMongo collection object.

    Returns:
        A list of documents in the collection.
        Returns an empty list if there are no documents.
    """
    return list(mongo_collection.find())
