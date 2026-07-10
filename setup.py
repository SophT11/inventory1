from pathlib import Path

# Project root
BASE_DIR = Path(__file__).parent

# Folders to create
folders = [
    "app",
    "app/templates",
    "app/static",
    "config",
    "data",
    "logs",
    "tests",
    "scripts",
]

# Files to create
files = {
    "app/__init__.py": "",
    "app/routes.py": "",
    "app/models.py": "",
    "config/__init__.py": "",
    ".env": "",
    ".gitignore": "",
    "README.md": "# Motor Parts Website\n",
}

print("Creating project structure...\n")

# Create folders
for folder in folders:
    path = BASE_DIR / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for filename, content in files.items():
    file_path = BASE_DIR / filename

    if not file_path.exists():
        file_path.write_text(content)
        print(f"Created file: {filename}")
    else:
        print(f"Skipped: {filename} already exists")

print("\nProject setup completed!")
