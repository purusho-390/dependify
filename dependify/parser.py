import ast
import os

def parse_imports(file_path):
    """
    Parse a Python file to find all imported modules.
    """
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())
    return {
        node.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    }

def find_all_imports(directory):
    """
    Recursively parse all Python files in the given directory.
    """
    imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                imports.update(parse_imports(file_path))
    return imports
