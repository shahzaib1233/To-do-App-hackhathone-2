"""
Console Todo App - Validators

This module contains validation functions for the todo application.
"""
import re
from typing import Optional


def validate_title_required(title: str) -> str:
    """
    Validate that a title is provided and meets length requirements.

    Args:
        title (str): Title to validate

    Returns:
        str: The validated and trimmed title

    Raises:
        ValueError: If title is empty, exceeds 200 characters, or contains only whitespace
    """
    if not title:
        raise ValueError("Title cannot be empty.")

    trimmed_title = title.strip()
    if not trimmed_title:
        raise ValueError("Title cannot be empty.")

    if len(trimmed_title) > 200:
        raise ValueError(f"Title exceeds maximum length of 200 characters. Current length: {len(trimmed_title)}")

    return trimmed_title


def validate_title_optional(title: Optional[str]) -> Optional[str]:
    """
    Validate an optional title if provided.

    Args:
        title (Optional[str]): Title to validate (or None)

    Returns:
        Optional[str]: The validated and trimmed title, or None if input was None

    Raises:
        ValueError: If title is provided but fails validation
    """
    if title is None:
        return None

    return validate_title_required(title)


def validate_description(description: Optional[str]) -> Optional[str]:
    """
    Validate an optional description if provided.

    Args:
        description (Optional[str]): Description to validate (or None)

    Returns:
        Optional[str]: The validated and trimmed description, or None if input was None

    Raises:
        ValueError: If description exceeds 1000 characters
    """
    if description is None:
        return None

    if len(description) > 1000:
        raise ValueError(f"Description exceeds maximum length of 1000 characters. Current length: {len(description)}")

    return description


def validate_positive_int(raw: str) -> int:
    """
    Validate that a string can be parsed as a positive integer.

    Args:
        raw (str): String to validate and convert

    Returns:
        int: The parsed positive integer

    Raises:
        ValueError: If string cannot be parsed as integer or is not positive
    """
    try:
        value = int(raw)
        if value <= 0:
            raise ValueError(f"Invalid task ID. Please enter a positive number. Got: {value}")
        return value
    except ValueError as e:
        # If it's already a ValueError (like from the positive check), re-raise it
        if "positive number" in str(e):
            raise e
        # Otherwise, it's a parsing error
        raise ValueError(f"Invalid task ID. Please enter a valid number. Got: '{raw}'")