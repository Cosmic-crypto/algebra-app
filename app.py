import sympy as sp
import customtkinter as ctk
from re import sub
from sys import exit

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

APP = ctk.CTk()
APP.geometry("500x500")
APP.title("Equation Solver & Simplifier")

OUTPUT_FRAME = ctk.CTkFrame(APP)
OUTPUT_FRAME.pack(pady=10, fill="both", expand=True)

# auto insert * – example: 3x => 3*x
def add_mulsign(expression: str) -> str:
    return sub(r"(\d)([a-zA-Z(])", r"\1*\2", expression)


# solve x=…
def solve_equation(equation: str, *variables: str) -> str:
    equation = add_mulsign(equation)
    equation = equation.replace("^", "**")
    
    if "=" in equation:
        equation = equation.replace("=", ",")

    symbols = sp.symbols(variables)

    left = sp.sympify(equation.split(',')[0])
    right = sp.sympify(equation.split(',')[1])

    eq = sp.Eq(left, right)
    solutions = sp.solve(eq, symbols)

    return (
        f"Solutions for {', '.join(variables)}:\n"
        f"{', '.join(str(sol) for sol in solutions)}\n"
        f"As float:\n{', '.join(str(float(sol)) for sol in solutions)}"
    )


# simplify expression
def simplify(expression: str) -> str:
    expression = add_mulsign(expression)
    expression = expression.replace("^", "**")

    simplified = sp.simplify(sp.sympify(expression))
    return f"Simplified expression:\n{str(simplified).replace('**', '^').replace('*', '')}"


# substitute values
def sub_solve(expr: str, subs_dict):
    expr = sp.sympify(add_mulsign(expr))
    expr = expr.subs({sp.Symbol(k): sp.sympify(v) for k, v in subs_dict.items()})
    return f"After substitution:\n{expr}"


def clear_all():
    for widget in OUTPUT_FRAME.winfo_children():
        widget.destroy()

    expr_entry.delete(0, 'end')
    vars_entry.delete(0, 'end')
    subs_entry.delete(0, 'end')


# ------------------------------------------------------------
# GUI
# ------------------------------------------------------------
expr_entry = ctk.CTkEntry(APP, width=300, placeholder_text="Enter equation (example: x^2 = 4)")
expr_entry.pack(pady=10)

vars_entry = ctk.CTkEntry(APP, width=300, placeholder_text="Variables (example: x)")
vars_entry.pack(pady=10)

subs_entry = ctk.CTkEntry(APP, width=300, placeholder_text="Replacements (example: 5)")
subs_entry.pack(pady=10)


def print_output(text):
    ctk.CTkLabel(OUTPUT_FRAME, text=text).pack(pady=5)


# simplify button
ctk.CTkButton(
    APP,
    text="Simplify",
    command=lambda: print_output(simplify(expr_entry.get()))
).pack(pady=5)


# solve button
ctk.CTkButton(
    APP,
    text="Solve equation",
    command=lambda: print_output(solve_equation(
        expr_entry.get(),
        *vars_entry.get().replace(" ", "").split(',')
    ))
).pack(pady=5)


# substitute + show expression
ctk.CTkButton(
    APP,
    text="Substitute and show",
    command=lambda: print_output(
        sub_solve(
            expr_entry.get(),
            dict(zip(
                vars_entry.get().replace(" ", "").split(','),
                subs_entry.get().replace(" ", "").split(',')
            ))
        )
    )
).pack(pady=5)


# clear button
ctk.CTkButton(
    APP,
    text="Clear",
    command=clear_all
).pack(pady=5)


APP.mainloop()
