import subprocess
import os


def kill_port():
    print("\n---KILL HANGING PORT---")
    port=input("Enter  the port number to kill (e.g., 3000 , 8000): ")
    if port.strip().isdigit():
        print(f"Searching and terminating processes on port {port}...")
        os.system(f"kill -9 $(lsof -t -i:{port}) 2>/dev/null || echo 'No active process found on port {port}.'")
    else:
        print("Invalid port number.")

def git_sync():
    print("\n--- QUICK GIT SYNC---")
    commit_msg= input("Enter your commit message: ")
    if commit_msg.strip():
        print("Staging changes...")
        os.system("git add  . ")
        print("Commiting  changes...")
        commit_result = os.system(f'git commit -m "{commit_msg}"')
        if commit_result == 0:
            #check if a remote origin exists
            remote_check = os.popen("git remote").read().strip()
            if not remote_check:
                print("No remote repository found.")
                repo_url:input("Enter your Github repository URL to link : ").strip()
                if repo_url:
                    os.system(f"git remote add origin {repo_url}")
                    os.system("git branch -M main")
                    print("Git sync complete")
                else:
                    print("Nothing new to commit or commit failed.")
            else:
                print("Commit message cannot be blank.")
        

def show_menu():
    print("===LATCH: WORKFLOW STREAMLINER ===")
    print("1, Open Dev Workspace")
    print("2, Scan/Kill hanging ports")
    print("3, Quick Git sync")
    print("4, Exit")

def main():
    while True:
        show_menu()
        choice= input("\nSelect an option (1-4): ")

        if choice=="1":
            print("Workspace is active. You are already in the project directory!")
        elif choice=="2":
          kill_port()
        elif choice=="3":
            git_sync()
        elif choice=="4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main() 