"""Portfolio example adapted from the project's paper-structure validation logic."""

VALID_DIFFICULTIES = {"Easy", "Medium", "Hard", "Mixed"}

def validate_structure(structure):
    """Return an error message if the paper structure is invalid; otherwise None."""
    if not isinstance(structure, list) or not structure:
        return "Add at least one section to the paper."

    for index, section in enumerate(structure, start=1):
        title = str(section.get("title", "")).strip()
        if not title or not title.replace(" ", "").isalpha():
            return f"Section {index} title must contain letters and spaces."

        try:
            count = int(section.get("count", 0))
            marks = int(section.get("marks", 0))
            attempt = int(section.get("attempt", 0))
        except (TypeError, ValueError):
            return f"Section {index}: count, marks and attempt must be numbers."

        if count <= 0 or marks <= 0 or attempt <= 0:
            return f"Section {index}: count, marks and attempt must be greater than 0."
        if marks > 100:
            return f"Section {index}: marks cannot be greater than 100."
        if attempt > count:
            return f"Section {index}: attempt cannot exceed the question count."

        difficulty = str(section.get("difficulty", "Medium")).title()
        if difficulty not in VALID_DIFFICULTIES:
            return f"Section {index}: invalid difficulty."

    return None


if __name__ == "__main__":
    example = [
        {"title": "Short Answers", "count": 6, "marks": 2,
         "attempt": 5, "difficulty": "Medium"}
    ]
    print(validate_structure(example) or "Paper structure is valid.")
