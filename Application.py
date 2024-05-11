import subprocess
from Database import first_run

def run_streamlit_app(app_file):
  command = ["streamlit", "run", app_file]  # Build the command list
  subprocess.run(command)  # Execute the command


first_run()
app_to_run = "UI.py"  
run_streamlit_app(app_to_run)

