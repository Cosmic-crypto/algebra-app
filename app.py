import sympy as sp
import customtkinter as ctk
from re import search, sub
from sys import exit

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

APP = ctk.CTk()
APP.geometry("500x450")
APP.title("Equation Solver & Simplifier")

OUTPUT_FRAME = ctk.CTkFrame(APP)
OUTPUT_FRAME.pack(pady=10, fill="both", expand=True)

def add_mulsign(expression: str) -> str:
    return sub(r"(\d)([a-zA-Z(])", r"\1*\2", expression)

def solve_equation(equation: str, *variables: str) -> str:
    equation = add_mulsign(equation)
    equation = equation.replace("^", "**")
    if "=" in equation:
        equation = equation.replace("=", ",")
    equation = equation.replace(" ", "")
    symbols = sp.symbols(variables)
    eq = sp.sympify(equation.replace("=", ","))

    eq = equation.split(',')[0]
    eq = sp.sympify(eq)

    ans = equation.split(',')[1] if ',' in equation else '0'
    ans = sp.sympify(ans)

    eq = sp.Eq(eq, ans)
    solutions = sp.solve(eq, symbols)
    return f"Solutions for {', '.join(variables)}: {', '.join(str(sol) for sol in solutions)}\n Solution as float: {', '.join(str(float(sol)) for sol in solutions)}"

def simplify(expression: str) -> str:
    expression = add_mulsign(expression)
    expression = expression.replace(" ", "")
    expression = expression.replace("^", "**")
    expr = sp.sympify(expression)
    simplified_expr = sp.simplify(expr)
    return f"Simplified Expression: {str(simplified_expr).replace('**', '^').replace('*', '')}"

def clear_all():
    for widget in OUTPUT_FRAME.winfo_children():
        widget.destroy()

    expr.delete(0, 'end')
    vars_.delete(0, 'end')

try:
    expr = ctk.CTkEntry(APP, width=300, placeholder_text="Enter equation (e.g., x^2 - 4)")
    expr.pack(pady=10)

    vars_ = ctk.CTkEntry(APP, width=300, placeholder_text="Enter variables (e.g., x)")
    vars_.pack(pady=10)

    simplify_button = ctk.CTkButton(APP, text="Simplify", command=lambda: ctk.CTkLabel(OUTPUT_FRAME, text=simplify(expr.get().strip())).pack())
    clear_button = ctk.CTkButton(APP, text="Clear All", command=clear_all)
    clear_button.pack(pady=5)

    while not search(r"=\s*\d", expr.get().strip()) or not vars_.get().strip():
        if expr.get() and not search(r"=\s*", expr.get().strip()):
            simplify_button.pack(pady=10)
            APP.update()
        else:
            simplify_button.pack_forget()
        APP.update()

    solve_button = ctk.CTkButton(APP, text="Solve", command=lambda: ctk.CTkLabel(OUTPUT_FRAME, text=solve_equation(expr.get().strip(), *vars_.get().strip().split(','))).pack())
    solve_button.pack(pady=10)

except Exception:
    exit(1)

APP.mainloop()