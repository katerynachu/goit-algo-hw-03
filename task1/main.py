import sys
from pathlib import Path
import shutil


def handle_file(file_path: Path, destination_path: Path):

    try:
        extension_with_dot = file_path.suffix
        folder_name = extension_with_dot.lstrip(".")

        if not folder_name:
            folder_name = "no_extension"

        target_folder = destination_path / folder_name
        target_folder.mkdir(exist_ok=True)

        target_file = target_folder / file_path.name

        shutil.copyfile(file_path, target_file)
        print(f"    --> Copied to: {target_file}")

    except Exception as e:
        print(f"Error copying file {file_path.name}: {e}")


def read_folder(source_path, destination_path):
    try:
        for element in source_path.iterdir():
            if element.is_dir():
                print(f"Entering directory: {element.name}")
                read_folder(element, destination_path)
            elif element.is_file():
                print(f"Found file: {element.name}")
                handle_file(element, destination_path)

    except Exception as e:
        print(f"Error processing path {source_path}: {e}")


if __name__ == "__main__":
    print("👋 Welcome to the File Sorter Program!")
    print("The program recursively copies and sorts files by extension.")
    print("-" * 30)
    start_command = input("Press Enter or 'S' to START sorting: ").lower()
    if start_command in ["", "s"]:

        source_arg = input(
            "📁 Enter the path to the SOURCE directory (e.g., source_files): "
        )

        if not source_arg:
            print("Operation cancelled: Source directory not provided.")
            sys.exit(1)

        destination_arg = input(
            "📦 Enter the path to the DESTINATION directory (leave blank for 'dist'): "
        )

        if not destination_arg:
            destination_arg = "dist"

        print("-" * 30)
        try:
            source_path = Path(source_arg)
            destination_path = Path(destination_arg)

            if not source_path.is_dir():
                print(f"Error: Source directory '{source_arg}' not found.")
                sys.exit(1)

            destination_path.mkdir(exist_ok=True)
            print(f"Destination directory is ready: {destination_path.resolve()}")

            read_folder(source_path, destination_path)

            print("-" * 30)
            print("Sorting completed successfully!")

        except Exception as e:
            print(f"Critical error during execution: {e}")

    else:
        print("Sorting cancelled.")
