 
import os

PROJECT_NAME = "real_time_data_analysis_with_streamlit_and_kafka"

# Define the file structure
file_structure = {
    "data": {
        "streaming_data": {},
        "batch_data": {}
    },
    "output": {},
    "source": {}
}

# Create the directories and empty files
for directory, subdirectories in file_structure.items():
    os.makedirs(os.path.join(PROJECT_NAME, directory), exist_ok=True)
    for subdirectory, files in subdirectories.items():
        os.makedirs(os.path.join(PROJECT_NAME, directory, subdirectory), exist_ok=True)
        for file in files:
            open(os.path.join(PROJECT_NAME, directory, subdirectory, file), 'w').close()
            
print(f"Created file structure and empty files for {PROJECT_NAME}.")
