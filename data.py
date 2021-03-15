"""Routines associated with the application data.
"""
import json
import os
courses = []


def load_data():
    """Load the data from the json file.
    """
    script_dir = os.path.dirname(__file__)
    rel_path = 'json\course.json'
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as json_file:
        courses = json.load(json_file)
        return sorted(courses, key=lambda x: x["id"])
