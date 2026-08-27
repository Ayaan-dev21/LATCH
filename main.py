import os
import sys

def kill_port():
    print("\n--- KILL HANGING PORT ---")
    port_input = input("Enter the port number to kill (e.g., 3000, 8000): ").strip()
    if port_input.isdigit():
        port = int(port_input)
        print(f"Scanning port {port}...")
        os.system(f"fuser -k {port}/tcp >/dev/null 2>&1")
        print(f"Port {port} check completed.")
    else:
        print("Invalid port number.")
def workspace_status():
    print("\n---WORKSPACE STATUS ---")
    os.system("/usr/bin/git status -s")
    branch = os.popen("/usr/bin/git branch --show-current").read().strip()
    print(f"Active Branch: {branch if branch else 'None'}")

def git_sync():
    print("\n--- QUICK GIT SYNC ---")
    commit_msg = input("Enter commit message: ").strip()

    if not commit_msg:
        print("Error: Commit message cannot be blank.")
        return
    print("Staging changes...")
    if os.system("/usr/bin/git add .") !=0:
        print("Failed to stage changes.")
        return
    print("Committing changes...")
    if os.system(f'/usr/bin/git commit -m "{commit_msg}"') !=0:
        print("Nothing new to commit or commit failed.")
        return
    remote_check = os.popen("/usr/bin/git remote").read().strip()

    if not remote_check:
        repo_url = input("Enter GitHub repository URL: ").strip()
        if repo_url:
            os.system(f"/usr/bin/git remote add origin {repo_url}")
            os.system("/usr/bin/git branch -M main")
            os.system("/usr/bin/git push -u origin main")
        else:
            print("Skipped remote linking.")
    else:
        print("Pushing to remote origin...")
        if os.system("/usr/bin/git push") == 0:
            print("Git sync complete.")
        else:
            print("Push failed.")

def check_dependencies():
    print("/n---DEPENDENCY MANAGER---")
    if os.path.exists("requirements.txt"):
        print("Found requirements.txt. Checking package status...")
        os.system("/usr/bin/pip list")
        choice = input("Do you want to install/upgrade requirements? (y/n): ").strip().lower()
        if choice == 'y':
            print("Installing dependencies...")
            os.system("/usr/bin/pip install -r requirements.txt")
        else:
            print("Skipped installation.")
    else:
        print("No requirements.txt found in this directory.")
        create = input("Do you want to generate a blank requirements.txt? (y/n): ").strip().lower()
        if create == 'y':
            with open("requirements.txt", "w") as f:
                f.write("# Add your project dependencies here\n")
            print("Created requirements.txt successfully.")
                    
                      
def show_menu():
    print("\n===========================================")
    print("       LATCH: WORKFLOW STEAMLINER          ")
    print("\n=========================================\n")
    print(" [1] Open Dev Workspace")
    print(" [2] Scan and Kill Hanging port")
    print(" [3] Check Workspace Status")
    print(" [4] Quick Git Sync Pipeline")
    print(" [5] Manage Dependencies")
    print(" [6] Exit")
    print("\n===========================================")

def main():
    while True:
        show_menu()
        choice = input ("\nSelect an option (1-6): ").strip()

        if choice == "1":
            if os.path.exists(".git"):
                print("Workspace is active. You are inside a valid project repository.")
            else:
                print("Warning: No active workspace found. You are not in a project root directory.")
        elif choice == "2":
            kill_port()
        elif choice == "3":
            workspace_status()
        elif choice == "4":
            git_sync()
        elif choice == "5":
            check_dependencies()
        elif choice == "6":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


     


        