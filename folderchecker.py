import os
import sys

def format_size(size_bytes):
    # Convert shits into human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def folder_checker(folder_path, show_subfolders=True):
    #Inspect folder contents with total file/folder count and file type breakdown
    try:
        if not os.path.exists(folder_path):
            print(f"\n[!] HOLY FUCK The folder doesn’t exist:\n{folder_path}\n")
            sys.exit(1)

        if not os.path.isdir(folder_path):
            print(f"\n[!] You absolute retard. That’s not even a folder:\n{folder_path}\n")
            sys.exit(1)

        total_files = 0
        total_folders = 0
        total_size = 0
        file_types = {}

        print(f"\n[!] Inspecting folder like a german soldier inspecting trenches: {folder_path}")
        print("-" * 60)

        for root, dirs, files in os.walk(folder_path):
            total_folders += len(dirs)
            total_files += len(files)

            for f in files:
                file_path = os.path.join(root, f)
                try:
                    total_size += os.path.getsize(file_path)
                except (FileNotFoundError, PermissionError):
                    print(f"⚠️ Cannot access shit: {file_path}")
                    continue

                ext = os.path.splitext(f)[1].lower() or "NO EXTENSION"
                file_types[ext] = file_types.get(ext, 0) + 1

            if show_subfolders:
                print(f"\n📁 {root}")
                for f in files:
                    print(f"   ├── {f}")

            if not show_subfolders:
                break

        print(f"\n{'-'*60}")
        print(f"📦 Total Files: {total_files}")
        print(f"📂 Total Folders: {total_folders}")
        print(f"💾 Total Size: {format_size(total_size)}")

        if file_types:
            print("\n📊 File Type Breakdown:")
            for ext, count in sorted(file_types.items(), key=lambda x: x[0]):
                print(f"   {ext}: {count} file(s)")

        print("\n[!] Folder check complete.\n")

    except Exception as e:
        print(f"\n[!] HOLY SHIT, UNEXPECTED ERROR: {e}\n")
        sys.exit(1)

# FUCKING MAIN
folder_path = input("\n[!] Enter folder path to inspect: ").strip()
folder_checker(folder_path)
