# 📊 Exporting Pandas DataFrames to LaTeX with Style

This project demonstrates how to export `pandas.DataFrame` objects to LaTeX format with styling, captions, labels, and formatting. It's perfect for generating publication-quality tables for scientific papers, reports, or documentation.

---

## 🛠️ Requirements

```bash
pip install pandas
```

> A LaTeX distribution (like TeX Live or MikTeX) is required to compile `.tex` files into PDFs.

---

## 📁 Loading the Data

Make sure your CSV files are available in your working directory:

```python
import pandas as pd

df_employee_data = pd.read_csv('employee_data.csv')
df_experiment_data = pd.read_csv('experiment_data.csv')
df_large_table_1 = pd.read_csv('large_table_1.csv')
df_large_table_2 = pd.read_csv('large_table_2.csv')
```

---

## 📄 Exporting a Basic LaTeX Table

```python
from your_module import save_latex_table

save_latex_table(
    df_employee_data,
    filename="table.tex",
    float_format="%.2f",
    caption="Employee Data",
    label="tab:employee_data",
    center=True
)
```

---

## 🎨 Highlighting Specific Values in LaTeX

Apply custom formatting:

```python
def highlight_high_values(val):
    return "\\textbf{" + str(val) + "}" if val > 90 else str(val)

df_styled = df_experiment_data.style.format({
    "Temperature (°C)": highlight_high_values,
    "Success Rate ($\\%$)": highlight_high_values
})
```

Save styled table:

```python
from your_module import save_latex_table_styled

save_latex_table_styled(
    df_styled,
    filename="styled_table.tex",
    caption="Styled table with bolded values",
    label="tab:styled"
)
```

---

## 📑 Creating Multi-Column Tables

```python
df_employee = pd.DataFrame({
    "ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"],
    "Joining Date": ["2020-01-10", "2019-07-23", "2021-06-15"]
})

df_employee.columns = pd.MultiIndex.from_tuples([
    ("Employee Info", "ID"),
    ("Employee Info", "Name"),
    ("Work Details", "Department"),
    ("Work Details", "Joining Date"),
])

save_latex_table(
    df_employee,
    filename="employee_table.tex",
    caption="Employee Details",
    label="tab:employee"
)
```

---

## 🔬 Controlling Float Precision

```python
print(df_experiment_data.to_latex(float_format="%.1f"))

save_latex_table(
    df_experiment_data,
    filename="precision_table1.tex",
    float_format="%.4f",
    caption="Scientific Notation Example",
    label="tab:precision_table1"
)

save_latex_table(
    df_large_table_1,
    filename="precision_table2.tex",
    float_format="%.3f",
    caption="Presentation of employee data.",
    label="tab:data_emp"
)
```

---

## 🚀 Command Line Interface (CLI)

You can also export tables using the command line!

### ▶️ Usage

```bash
python export_table_cli.py \
  --input employee_data.csv \
  --output employee_table.tex \
  --caption "Employee Overview" \
  --label tab:employee \
  --float_format "%.2f" \
  --center \
  --position h!
```

### 🔧 CLI Options

| Option           | Description                                      | Required | Default         |
|------------------|--------------------------------------------------|----------|-----------------|
| `--input`        | Path to the input CSV file                       | ✅        | —               |
| `--output`       | Output `.tex` filename                           | ❌        | `table.tex`     |
| `--caption`      | Table caption                                    | ❌        | `"Table Caption"` |
| `--label`        | LaTeX reference label                            | ❌        | `tab:label`     |
| `--float_format` | Format for float numbers                         | ❌        | `"%.2f"`        |
| `--center`       | Add `\\centering` for table alignment            | ❌        | False           |
| `--position`     | Float position (e.g., `h!`, `t`, `b`, etc.)      | ❌        | `"h!"`          |

---

## 📂 File Output

All exports will generate:
- A standalone `.tex` file (compilable with LaTeX)
- Includes required packages (`booktabs`, `longtable`, `graphicx`, `adjustbox`)
- Centered tables with optional float formatting

To compile:

```bash
pdflatex table.tex
```

---

## ✨ Advanced Ideas to Extend

- Add support for longtables
- Wrap wide tables using `adjustbox`
- Auto-compile to PDF or image format
- Combine multiple tables into one report
- Highlight using `Styler.applymap()` or `highlight_max()`
- Create a Python package (`pip install latex-table-exporter`)

---

## 📚 License

MIT License — Free to use, modify, and distribute.

---

Let me know if you'd like the CLI script bundled in a module with installable CLI support via `setup.py` or `pyproject.toml`.
