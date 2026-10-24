"""Portfolio example adapted from the project's Statistics chart helper.

Install dependency: python -m pip install matplotlib
Run: python chart_generation.py
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def create_bar_chart(labels, values, output_path, title="Statistics Graph"):
    """Create a bar chart from labels and numeric values."""
    if not labels or not values or len(labels) != len(values):
        raise ValueError("Labels and values must be non-empty and have equal lengths.")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig, axis = plt.subplots(figsize=(7.4, 4.6), dpi=160)
    try:
        axis.bar(labels, values)
        axis.set_title(title)
        axis.set_xlabel("Category")
        axis.set_ylabel("Value")
        axis.grid(True, axis="y", alpha=0.25)
        fig.tight_layout()
        fig.savefig(output, bbox_inches="tight")
    finally:
        plt.close(fig)

    return output


if __name__ == "__main__":
    path = create_bar_chart(
        ["A", "B", "C", "D"],
        [12, 19, 8, 15],
        "example_output/bar_chart.png",
        "Example Statistics Data",
    )
    print(f"Chart saved to: {path}")
