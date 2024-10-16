import streamlit as st
import math

# Set the page configuration
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# Initialize session state for the calculator expression
if 'expression' not in st.session_state:
    st.session_state.expression = ''

# Function to handle button clicks
def add_to_expression(value):
    st.session_state.expression += value

def clear_expression():
    st.session_state.expression = ''

def calculate():
    try:
        # Define allowed names
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['abs'] = abs
        allowed_names['round'] = round

        # Evaluate the expression
        result = eval(st.session_state.expression, {"__builtins__": None}, allowed_names)
        st.session_state.expression = str(result)
    except Exception as e:
        st.session_state.expression = "Error"

# Display the calculator title
st.title("🧮 Scientific Calculator")

# Display the current expression
st.text_input("Expression", st.session_state.expression, key="input", disabled=True, 
              placeholder="Enter your expression")

# Define the calculator buttons
buttons = [
    ['7', '8', '9', '/', 'Clear'],
    ['4', '5', '6', '*', '('],
    ['1', '2', '3', '-', ')'],
    ['0', '.', '^', '+', 'C'],
    ['sin', 'cos', 'tan', 'log', 'ln'],
    ['√', 'π', 'e', '=', 'Del']
]

# Create buttons in a grid layout
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        if cols[i].button(button):
            if button == 'Clear' or button == 'C':
                clear_expression()
            elif button == '=':
                calculate()
            elif button == 'Del':
                st.session_state.expression = st.session_state.expression[:-1]
            elif button in ['sin', 'cos', 'tan', 'log', 'ln', '√', '^', 'π', 'e']:
                if button == '√':
                    add_to_expression('math.sqrt(')
                elif button == 'pi' or button == 'π':
                    add_to_expression('math.pi')
                elif button == 'e':
                    add_to_expression('math.e')
                elif button == 'ln':
                    add_to_expression('math.log(')
                elif button == '^':
                    add_to_expression('**')
                else:
                    add_to_expression(f'math.{button}(')
            else:
                add_to_expression(button)

# Instructions
st.markdown("""
---
**Instructions:**
- Click the buttons to build your expression.
- Use `Clear` or `C` to reset the expression.
- Click `=` to evaluate the expression.
- Use `Del` to delete the last character.
- Functions like `sin`, `cos`, `tan`, `log`, `ln`, and `√` can be used by clicking their respective buttons.
""")
