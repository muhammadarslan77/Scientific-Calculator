import streamlit as st
import math

# Set the page configuration
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# Predefine allowed names for safe evaluation
ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
ALLOWED_NAMES.update({
    'abs': abs,
    'round': round
})

# Initialize session state for the calculator expression
if 'expression' not in st.session_state:
    st.session_state.expression = ''

# Function to handle button clicks
def add_to_expression(value):
    st.session_state.expression += value

def clear_expression():
    st.session_state.expression = ''

def delete_last():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate():
    try:
        # Evaluate the expression safely
        result = eval(st.session_state.expression, {"__builtins__": None}, ALLOWED_NAMES)
        st.session_state.expression = str(result)
    except Exception:
        st.session_state.expression = "Error"

# Display the calculator title
st.title("🧮 Scientific Calculator")

# Display the current expression
st.text_input("Expression", st.session_state.expression, key="input", disabled=True, 
              placeholder="Enter your expression")

# Define the calculator buttons in a list of lists
buttons = [
    ['7', '8', '9', '/', 'Clear'],
    ['4', '5', '6', '*', '('],
    ['1', '2', '3', '-', ')'],
    ['0', '.', '^', '+', 'Del'],
    ['sin', 'cos', 'tan', 'log', 'ln'],
    ['√', 'π', 'e', '=', '']
]

# Create buttons in a grid layout
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        if button:  # Skip empty strings for alignment
            if cols[i].button(button):
                if button in ['Clear']:
                    clear_expression()
                elif button in ['Del']:
                    delete_last()
                elif button == '=':
                    calculate()
                elif button in ['sin', 'cos', 'tan', 'log', 'ln']:
                    add_to_expression(f'math.{button}(')
                elif button == '√':
                    add_to_expression('math.sqrt(')
                elif button == 'π':
                    add_to_expression(str(math.pi))
                elif button == 'e':
                    add_to_expression(str(math.e))
                elif button == '^':
                    add_to_expression('**')
                else:
                    add_to_expression(button)

# Instructions
st.markdown("""
---
**Developed By:** Muhammad Arslan 
""")

