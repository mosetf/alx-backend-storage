#!/usr/bin/env python3
""" returns all the students sorted by average score """
import pymongo


def top_students(mongo_collection):
    """ returns all the students sorted by average score """
    if not mongo_collection:
        return []
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])