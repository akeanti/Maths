import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import sys


class MathSolver:
    def __init__(self):
        self.var = sp.Symbol('x')

    def print_header(self, title):
        print(f"\n{'=' * 50}")
        print(f"{title:^50}")
        print(f"{'=' * 50}")

    def solve_equation(self, equation_str):
        try:
            equation = sp.sympify(equation_str)
            solutions = sp.solve(equation, self.var)
            return solutions
        except Exception as e:
            return str(e)

    def visualize_equation(self, equation_str):
        try:
            equation = sp.sympify(equation_str)
            f_lambdified = sp.lambdify(self.var, equation, "numpy")
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f_lambdified(x_vals)

            plt.figure(figsize=(12, 8))
            plt.plot(x_vals, y_vals, label=f'{equation_str}')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.title(f'Plot of the equation: {equation_str}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"Error in visualization: {e}")

    def additional_tools(self):
        self.print_header("Advanced Math Tools")
        print("1. Calculate Derivative")
        print("2. Calculate Integral")
        print("3. Simplify Expression")
        print("4. Solve Differential Equation")
        print("5. Find Limit")
        print("6. Matrix Operations")
        print("7. Eigenvalues and Eigenvectors")
        print("8. Exit to Main Menu")
        choice = input("Select an option (1-8): ")

        if choice == '1':
            expr = input("Enter the expression for derivative: ")
            self.calculate_derivative(expr)
        elif choice == '2':
            expr = input("Enter the expression for integral: ")
            self.calculate_integral(expr)
        elif choice == '3':
            expr = input("Enter the expression to simplify: ")
            self.simplify_expression(expr)
        elif choice == '4':
            eq_str = input("Enter the differential equation (e.g., y'' - y = 0): ")
            self.solve_differential_equation(eq_str)
        elif choice == '5':
            expr = input("Enter the expression to find the limit (e.g., limit(x**2, x, oo)): ")
            self.find_limit(expr)
        elif choice == '6':
            self.matrix_operations()
        elif choice == '7':
            self.eigenvalues_eigenvectors()
        elif choice == '8':
            return
        else:
            print("Invalid choice. Returning to main menu.")

    def calculate_derivative(self, expr):
        try:
            expression = sp.sympify(expr)
            derivative = sp.diff(expression, self.var)
            print(f"Derivative: {derivative}")
        except Exception as e:
            print(f"Error calculating derivative: {e}")

    def calculate_integral(self, expr):
        try:
            expression = sp.sympify(expr)
            integral = sp.integrate(expression, self.var)
            print(f"Integral: {integral}")
        except Exception as e:
            print(f"Error calculating integral: {e}")

    def simplify_expression(self, expr):
        try:
            expression = sp.sympify(expr)
            simplified = sp.simplify(expression)
            print(f"Simplified expression: {simplified}")
        except Exception as e:
            print(f"Error simplifying expression: {e}")

    def solve_differential_equation(self, eq_str):
        try:
            # Define y and its derivatives
            y = sp.Function('y')(self.var)
            eq = sp.sympify(eq_str.replace("y'", "y.diff(x)").replace("y''", "y.diff(x, x)"))

            # Solve the differential equation
            solution = sp.dsolve(eq, y)
            print(f"Solution to the differential equation: {solution}")
        except Exception as e:
            print(f"Error solving differential equation: {e}")

    def find_limit(self, expr):
        try:
            limit_expr = sp.sympify(expr)
            limit_value = sp.limit(limit_expr, self.var, sp.oo)
            print(f"Limit: {limit_value}")
        except Exception as e:
            print(f"Error finding limit: {e}")

    def matrix_operations(self):
        try:
            print("Matrix Operations:")
            matrix_input = input("Enter a matrix (e.g., [[1,2],[3,4]]): ")
            matrix = sp.Matrix(sp.sympify(matrix_input))
            print(f"Matrix:\n{matrix}")
            print(f"Transpose:\n{matrix.T}")
            print(f"Determinant: {matrix.det()}")
            print(f"Inverse:\n{matrix.inv()}")
        except Exception as e:
            print(f"Error in matrix operations: {e}")

    def eigenvalues_eigenvectors(self):
        try:
            print("Eigenvalues and Eigenvectors:")
            matrix_input = input("Enter a matrix (e.g., [[1,2],[3,4]]): ")
            matrix = sp.Matrix(sp.sympify(matrix_input))
            eigenvalues = matrix.eigenvals()
            eigenvectors = matrix.eigenvects()
            print(f"Eigenvalues: {eigenvalues}")
            print(f"Eigenvectors: {eigenvectors}")
        except Exception as e:
            print(f"Error in eigenvalues and eigenvectors: {e}")


def main():
    solver = MathSolver()

    while True:
        solver.print_header("Advanced Math Solver")
        print("1. Solve Equation")
        print("2. Visualize Equation")
        print("3. Tools Menu")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            equation_str = input("Enter a mathematical equation: ")
            solutions = solver.solve_equation(equation_str)
            print(f"Solutions: {solutions}")
        elif choice == '2':
            equation_str = input("Enter a mathematical equation: ")
            solver.visualize_equation(equation_str)
        elif choice == '3':
            solver.additional_tools()
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
