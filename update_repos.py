import os
import subprocess


PROJECTS_DIR = "/root/Workspace/projects"

def update_repositories():
    updated_repositories = []

    if not os.path.exists(PROJECTS_DIR):
        print(f"Diretório {PROJECTS_DIR} não encontrado.")
        return

    def traverse_directories(root_dir):
        for root, dirs, files in os.walk(root_dir):
            if ".git" in dirs:
                repo_dir = os.path.join(root, ".git")
                print(f"Repositório encontrado em: {root}")
                try:
                    current_branch = subprocess.check_output(
                        ["git", "-C", root, "rev-parse", "--abbrev-ref", "HEAD"],
                        text=True
                    ).strip()

                    if current_branch != "master":
                        print(f"Alterando para a branch master no repositório {root}")
                        subprocess.run(["git", "-C", root, "checkout", "master"], check=True)

                    subprocess.run(["git", "-C", root, "pull"], check=True)
                    
                    updated_repositories.append(root)

                except subprocess.CalledProcessError as e:
                    print(f"Erro ao atualizar o repositório {root}: {e}")
                dirs[:] = []
    
    traverse_directories(PROJECTS_DIR)

    if updated_repositories:
        print("\nRepositórios atualizados:")
        for repo in updated_repositories:
            print(f"- {repo}")
    else:
        print("\nNenhum repositório foi atualizado.")

if __name__ == "__main__":
    update_repositories()