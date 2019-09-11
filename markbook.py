"""
Markbook Application
Group members: 
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {}


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    return {}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0