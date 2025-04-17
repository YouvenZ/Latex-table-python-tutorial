import pandas as pd
import argparse
import re
import os


def save_latex_table(df, filename="table.tex", float_format="%.2f", caption="Table Caption",
                     label="tab:label", center=True, position='h!', column_format=None):
    """
    Save a Pandas DataFrame as a LaTeX table in a full .tex document.
    """
    if column_format is None:
        column_format = "l" + "c" * (len(df.columns) - 1)

    latex_table = df.to_latex(index=False,
                              float_format=float_format,
                              caption=caption,
                              label=label,
                              column_format=column_format,
                              escape=False,
                              position=position)

    if center:
        pattern = r"\\begin\{table\}\[.*?\]"
        replacement = r"\\begin{table}[" + position + r"]\n\\centering"
        latex_table = re.sub(pattern, replacement, latex_table, count=1)

    latex_code = r"""
\documentclass{article}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{graphicx}
\usepackage{adjustbox}
\begin{document}
""" + latex_table + r"""
\end{document}
"""

    with open(filename, "w") as f:
        f.write(latex_code)

    print(f"LaTeX table saved to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Export CSV file to a styled LaTeX table.")
    parser.add_argument('--input', required=True, help='Path to the CSV input file')
    parser.add_argument('--output', default='table.tex', help='Output .tex file path')
    parser.add_argument('--caption', default='Table Caption', help='Caption for the table')
    parser.add_argument('--label', default='tab:label', help='Label for referencing in LaTeX')
    parser.add_argument('--float_format', default='%.2f', help='Float formatting, e.g. %.3f')
    parser.add_argument('--center', action='store_true', help='Add \\centering to center the table')
    parser.add_argument('--position', default='h!', help='Positioning for the LaTeX table [htbp]')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File not found: {args.input}")
        return

    df = pd.read_csv(args.input)
    save_latex_table(df,
                     filename=args.output,
                     float_format=args.float_format,
                     caption=args.caption,
                     label=args.label,
                     center=args.center,
                     position=args.position)


if __name__ == "__main__":
    main()
