import streamlit as st
from sympy import symbols, diff, integrate, sympify

# Define the variable
x = symbols('x')

# Function to differentiate
def differentiate_function(f, variable):
    steps = []
    derivative = diff(f, variable)
    steps.append(f"Step 1: Differentiate {f} to get {derivative}")
    return derivative, steps

# Function to integrate (indefinite)
def integrate_function(f, variable):
    steps = []
    integral = integrate(f, variable)
    steps.append(f"Step 1: Integrate {f} to get {integral} + C")
    return integral, steps

# Function to integrate (definite)
def integrate_definite(f, variable, lower_limit, upper_limit):
    steps = []
    indefinite_integral = integrate(f, variable)
    definite_integral = indefinite_integral.subs(variable, upper_limit) - indefinite_integral.subs(variable, lower_limit)
    steps.append(f"Step 1: Integrate {f} to get {indefinite_integral} + C")
    steps.append(f"Step 2: Evaluate from {lower_limit} to {upper_limit} to get {definite_integral}")
    return definite_integral, steps

# Function to display results
def display_results(expr, operation, lower_limit=None, upper_limit=None):
    try:
        # Parse the expression
        function = sympify(expr)

        if operation == "Differentiate":
            derivative, steps = differentiate_function(function, x)
            st.write("### Step-by-Step Derivation")
            for step in steps:
                st.write(step)
            st.write("**Whoopee! Your final derivative is:**", derivative)

        elif operation == "Indefinite Integral":
            integral, steps = integrate_function(function, x)
            st.write("### Step-by-Step Derivation")
            for step in steps:
                st.write(step)
            st.write("**Whoopee! Your final indefinite integral is:**", integral)

        elif operation == "Definite Integral":
            definite_integral, steps = integrate_definite(function, x, lower_limit, upper_limit)
            st.write("### Step-by-Step Derivation")
            for step in steps:
                st.write(step)
            st.write("**Whoopee! Your final definite integral from {} to {} is:**".format(lower_limit, upper_limit), definite_integral)

    except Exception as e:
        st.write("Error:", e)

# Streamlit interface
st.set_page_config(page_title="Differential and Integral Calculator", layout="wide")
st.title("🧮 Differential and Integral Calculator")
st.markdown("""
    Welcome to the **Differential and Integral Calculator**! 
    Here you can compute derivatives and integrals of any valid mathematical function.
    
    ### Features:
    - **Differentiate** a function with respect to \( x \)
    - Compute the **Indefinite Integral**
    - Compute the **Definite Integral** with specified limits
""")

# Dropdown for operation selection
operation = st.selectbox("Choose an operation:", ["Differentiate", "Indefinite Integral", "Definite Integral"])
expr = st.text_input("Enter a function (in terms of x):", "x**2 * sin(x)")

# Show inputs for definite integral
if operation == "Definite Integral":
    lower_limit = st.number_input("Lower limit:", value=0)
    upper_limit = st.number_input("Upper limit:", value=1)
else:
    lower_limit = upper_limit = None

if st.button("Calculate"):
    if expr.strip() == "":
        st.warning("Please enter a valid mathematical expression!")
    else:
        display_results(expr, operation, lower_limit, upper_limit)

# Add footer
st.markdown("""
---
Made with ❤️ using Streamlit. 
""")
