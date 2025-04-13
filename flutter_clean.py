import os
import subprocess
from typing import List, Tuple

def run_flutter_clean(directory: str) -> bool:
    """
    Run flutter clean in the specified directory
    Returns True if successful, False if there was an error
    """
    try:
        # Change to the directory
        os.chdir(directory)
        
        # Run flutter clean and capture output
        process = subprocess.run(['flutter', 'clean'], 
                               capture_output=True, 
                               text=True, 
                               check=True)
        
        # Change back to parent directory
        os.chdir('..')
        return True
        
    except subprocess.CalledProcessError:
        # If flutter clean fails, change back to parent directory and return False
        os.chdir('..')
        return False
    except Exception:
        # For any other error, try to change back to parent directory and return False
        try:
            os.chdir('..')
        except:
            pass
        return False

def clean_flutter_projects() -> Tuple[List[str], List[str]]:
    """
    Clean all Flutter projects in the current directory
    Returns tuple of (successful_cleanups, failed_cleanups)
    """
    # Get the current working directory
    base_dir = os.getcwd()
    
    # Lists to track results
    successful_cleanups = []
    failed_cleanups = []
    
    # Get all directories in the current folder
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    
    print(f"Found {len(directories)} directories")
    
    # Process each directory
    for directory in directories:
        print(f"\nProcessing {directory}...")
        
        # Check if it's a Flutter project (look for pubspec.yaml)
        if os.path.exists(os.path.join(directory, 'pubspec.yaml')):
            print(f"Flutter project found in {directory}")
            
            # Run flutter clean
            if run_flutter_clean(directory):
                successful_cleanups.append(directory)
                print(f"✅ Successfully cleaned {directory}")
            else:
                failed_cleanups.append(directory)
                print(f"❌ Failed to clean {directory}")
        else:
            print(f"Skipping {directory} - Not a Flutter project")
    
    return successful_cleanups, failed_cleanups

def main():
    print("Starting Flutter projects cleanup...\n")
    
    successful, failed = clean_flutter_projects()
    
    print("\n=== CLEANUP SUMMARY ===")
    
    print("\n✅ Successfully cleaned projects:")
    if successful:
        for project in successful:
            print(f"  - {project}")
    else:
        print("  None")
    
    print("\n❌ Failed to clean projects:")
    if failed:
        for project in failed:
            print(f"  - {project}")
    else:
        print("  None")
    
    print(f"\nTotal: {len(successful)} succeeded, {len(failed)} failed")

if __name__ == "__main__":
    main()
