import os

# Define the project structure as a dictionary
project_structure = {
    "ProjectName": {
        "docs": {},
        "src": {
            "components": {},
            "assets": {}
        },
        "public": {
            "index.html": None
        },
        "static": {
            "images": {
                "project1": {
                    "nulympia.webp": None
                },
                "project2": {}
            },
            "videos": {
                "project1": {}
            },
            "documents": {
                "project1": {}
            }
        }
    }
}


def create_project_structure(base_path, structure):
    """Recursively creates the project folder structure."""
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create a directory and recursively create its content
            create_project_structure(path, content)
        else:
            # Create a file
            with open(path, 'w') as file:
                pass  # Just create an empty file for now


# Assuming the project should be created in the current directory
base_directory = os.getcwd()  # You can change this to any directory you want the project to be created in
create_project_structure(base_directory, project_structure)

"Project structure created successfully."

