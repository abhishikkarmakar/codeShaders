import streamlit as st

# Define tasks for each mode
modes_tasks = {
    "Flow of Program": ["01-flow-of-program"],
    "First Java": ["02-first-java"],
    "Conditionals and Loops": ["03-conditionals-loops"],
    "Functions": ["04-functions"],
    "Arrays": ["05-arrays"],
    "Searching": ["06-searching"],
    "Sorting": ["07-sorting"],
    "Strings": ["08-strings"],
    "Patterns": ["09-patterns"],
    "Recursion": ["10-recursion"],
    "Bitwise": ["11-bitwise"],
    "Math": ["12-math"],
    "Complexities": ["13-complexities"],
    "Object Oriented Programming": ["14-oop"],
    "Linked List": ["15-linkedlist"],
    "Stacks and Queues": ["16-stack-queue"],
    "Trees": ["17-trees"],
    "Heaps": ["18-heaps"],
}

# Sidebar - Mode selection
selected_mode = st.sidebar.selectbox("Select Mode", list(modes_tasks.keys()))

# Display tasks for selected mode
st.title(selected_mode)
tasks = modes_tasks[selected_mode]

# Checkbox state persistence
state = {}
for task in tasks:
    state[task] = st.sidebar.checkbox(task, key=task, value=state.get(task, False))

# Save checkbox states
if st.button("Save"):
    st.experimental_set_query_params(**state)

# Display tasks based on checkbox state
for task, checked in state.items():
    if checked:
        st.write(task)
