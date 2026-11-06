from pathlib import Path

root = Path(__file__).parent
search_folder = root / "examples"

if not search_folder.is_dir():
    print(f"Folder does not exist: {search_folder}")
else:
    python_files = sorted(
        path for path in search_folder.rglob("*.py")
        if path.is_file()
    )

    if not python_files:
        print("No Python files found.")
    else:
        for path in python_files:
            print(path.relative_to(search_folder))
