# Equation Solver & Simplifier 🧮  

A small GUI application built with **CustomTkinter** and **SymPy** that allows you to **solve equations** and **simplify algebraic expressions** interactively.

The app accepts expressions such as:  

```
x^2 - 4
3x + 2 = 14
sin(x) + cos(x)
```

…and automatically converts them into valid SymPy syntax behind the scenes.

---

## ✨ Features  

### ✔ Real-time Expression Parsing 
Automatically inserts multiplication signs when needed (`3x` → `3*x`)  

### ✔ Equation Solving  
Enter an equation (like `x^2 = 9`) and specify variables, e.g.:
```
x
```
Output shows:
- symbolic solutions  
- numeric (float) solutions  

### ✔ Expression Simplification  
Enter an expression and press **Simplify** — for example:

Input:
```
3x + 2x
```

Output:
```
Simplified Expression: 5x
```

### ✔ GUI-based  
Uses **CustomTkinter** with light/dark mode respect.

---

## 🧑‍💻 Requirements  

| Library | Purpose |
|--------|---------|
| sympy | symbolic math / solving |
| customtkinter | GUI |
| re | parsing helpers |
| Python 3.10+ | recommended |

Install requirements using:

```bash
pip install sympy customtkinter
```

---

## 🖥 How to Use  

1. Run the script  
2. Type an expression or equation into the input field  
3. Optionally enter variable names separated by commas  
4. Click either:
- **Simplify**
- **Solve**

Examples:

| Input | Variables | Action |
|---|---|---|
| `x^2 - 9 = 0` | `x` | Solve |
| `sin(x) + sin(x)` | — | Simplify |

---

## 🔍 Internals (brief explanation)

### Automatic multiplication fixing
`add_mulsign()` detects patterns like:
```
3x → 3*x
2(x+1) → 2*(x+1)
```

### Caret replacement  
Human-friendly `^` becomes Python’s `**`.

### Solving
```
sp.Eq(...) → sp.solve(...)
```

### Simplification
```
sp.simplify(...)
```

---

## 🛠 Error Handling
If the window is closed early or an unexpected error happens inside UI setup, the script safely exits instead of crashing.

---

## .exe file
If you don't have the interpreter installed check the releases for a .exe file that will have this exact code in the file, the original .py code is ~3 KB but the release
is a whopping ~46 MB, this is probably caused by the fact that this .exe file contains the interpreter and also the sympy module, the module that the code uses ot solve
problems, this is a huge file.

---

## 🚀 Future Improvements (ideas)
- multiple equation solving
- step-by-step algebra
- plotting
- downloadable solutions
- fraction / exact / symbolic display toggle

---

## License
MIT — free to use, modify, and redistribute.
