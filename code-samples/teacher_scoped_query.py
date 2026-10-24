"""Portfolio example adapted from the project's teacher-specific paper lookup.

The application obtains teacher_id from the authenticated session.
This example shows the SQL pattern; it is not a complete login system.
"""
import sqlite3


def get_teacher_paper(database_path, paper_id, authenticated_teacher_id):
    """Return a paper only when it belongs to the authenticated teacher."""
    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row
        return connection.execute(
            """
            SELECT id, subject, exam_title, marks, created_at
            FROM papers
            WHERE id = ? AND teacher_id = ?
            """,
            (paper_id, authenticated_teacher_id),
        ).fetchone()


# Parameter placeholders (?) help keep user-supplied values separate from SQL.
# The web application must authenticate the user before calling this function.
