import os
import sys
import shutil
from generate_pages_recursive import generate_pages_recursive

def copy_directory(source_dir, dest_dir):
    """
    Recursively copy all files from source_dir to dest_dir.
    Delete the contents of dest_dir first if it exists.
    """
    # Delete destination directory if it exists
    if os.path.exists(dest_dir):
        print(f"Deleting directory: {dest_dir}")
        shutil.rmtree(dest_dir)
    
    # Create destination directory
    print(f"Creating directory: {dest_dir}")
    os.makedirs(dest_dir)
    
    # Copy all files and subdirectories
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_item):
            print(f"Copying file: {source_item} -> {dest_item}")
            shutil.copy(source_item, dest_item)
        else:
            # Recursively copy subdirectories
            copy_directory(source_item, dest_item)

def main():
    # Get base path from command line argument, default to "/static_site_generator/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/static_site_generator/"
    
    # Step 1: Delete public directory if it exists
    public_dir = "public"
    if os.path.exists(public_dir):
        print(f"Deleting directory: {public_dir}")
        shutil.rmtree(public_dir)
    
    # Step 2: Copy static files to public directory
    print("Copying static files...")
    copy_directory("static", "public")
    
    # Step 3: Generate all pages recursively with configurable base path
    print(f"Generating pages with base path: {basepath}")
    generate_pages_recursive("content", "template.html", "public", basepath)
    
    print("Site generation complete!")

if __name__ == "__main__":
    main()