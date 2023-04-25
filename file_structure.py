 
import os

# Define project folder names
project_folder = "Data Warehousing with Amazon Redshift"
input_folder = "input"
output_folder = "output"
etl_folder = "etl"

# Create project folder if it doesn't exist
if not os.path.exists(project_folder):
    os.mkdir(project_folder)

# Create subfolders for input, output, etl if they don't exist
if not os.path.exists(os.path.join(project_folder, input_folder)):
    os.mkdir(os.path.join(project_folder, input_folder))
if not os.path.exists(os.path.join(project_folder, output_folder)):
    os.mkdir(os.path.join(project_folder, output_folder))
if not os.path.exists(os.path.join(project_folder, etl_folder)):
    os.mkdir(os.path.join(project_folder, etl_folder))

# Create empty files in the input folder
with open(os.path.join(project_folder, input_folder, "data_source_1.csv"), "w") as f:
    pass

with open(os.path.join(project_folder, input_folder, "data_source_2.csv"), "w") as f:
    pass

# Create empty files in the etl folder
with open(os.path.join(project_folder, etl_folder, "extract.py"), "w") as f:
    pass

with open(os.path.join(project_folder, etl_folder, "transform.py"), "w") as f:
    pass

with open(os.path.join(project_folder, etl_folder, "load.py"), "w") as f:
    pass

# Create empty files in the output folder
with open(os.path.join(project_folder, output_folder, "dashboard.py"), "w") as f:
    pass
