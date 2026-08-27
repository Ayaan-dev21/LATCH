import os
import subprocess

def kill_port():
    print("\n---KILL HANGING PORT---")
    port = input("Enter the poert number to kill (e/g 3000, 8000): ").strip()
    if port.isdigit():
        print(f"Searching and terminating processes on port {port}...")
        exit_code = os.system(f"fuser -k {port}/tcp >/dev/null 2>&1")
        if exit_code == 0:
            print(f"Successfully cleared port {port}.")
        else:
            print(f"No active process found on port {port}.")
    else:
        print("Invalid port number.")
def git_sync():
    print("\n--- QUICK GIT SYNC ---")
    commit_msg = input("Enter your commit message: ").strip()
    if not commit_msg:
        print("Error: Commit message cannot be blank.")
        return
    print("Staging changes...")
    if os.system("/usr/bin/git add .") != 0:
        print("Failed to stage changes.")
        return
    print("Committing changes...")
    commit_result = os.system(f'/usr/bin/git commit -m "{commit_msg}"')
    if commit_result !=0:
        print("Nothing new to commit or commit failed.")
        return
    #check if a remote origin exists
    remote_check = os.popen("/usr/bin/git remote").read().strip()

    if not remote_check:
        print("No remote repository found.")
        repo_url= input("Enter your GitHub repository URL to link: ").strip()
        if repo_url:
            os.system(f"git remote add origin {repo_url}")
            os.system("git branch -M main")
            print("Pushing to remote...")
            os.system("/usr/bin/git push -u origin main")
        else:
            print("Skipped remote linking.")
    else:
        print("Pushing to remote origin...")
        push_result = os.system("/usr/bin/git push")
        if push_result == 0:
            print("Git sync complete.")
        else:
            print("Push failed. Check your branch tracking or credentials.")

def show_menu():
    print("\n=== LATCH: WORKFLOW STREAMLINER ===")
    print("1. Open Dev Workspace")
    print("2. Scan/Kill hanging ports")
    print("3. Quick Git sync")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            print("Workspace is active. You are already in the project directory!")
        elif choice == "2":
            kill_port()
        elif choice == "3":
            git_sync()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")\

if __name__ == "__main__":
    main()

                       