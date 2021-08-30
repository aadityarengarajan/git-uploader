import os
import datetime
import json
import pyperclip

MY_DIRECTORY = os.getcwd()
c = 0
for directory in os.listdir('..'):
    with open(f"../{directory}/project.index.json") as jsonfile:
        project = json.loads(jsonfile.read())
        print(f"[{c}][][][][][][][][][][][][][][][][]\nSTEP 1 : Create Repo for \"{project['name']}\" — \"{project['description']}\" : ")
        if input("Report Yes/Skip (Y/S) : ") in "yY":
            print(f"PART 1 : Enter Project Name (\"{project['name']}\")")
            pyperclip.copy(project['name'])
            input()
            print(f"PART 1 : Enter Project Name (\"{project['description']}\")")
            pyperclip.copy(project['description'])
            input()
            os.chdir(f'../{directory}')
            print("git init")
            if "README.md" not in os.listdir():
                print("README FILE NOT FOUND IN DIRECTORY :\n")
                print("\t".join(os.listdir()))
                if input("INITIATE README FILE? (Y/N): ") in "yY":
                    with open("README.md","w") as readmefile:
                        readmefile.write(f"""
# {project['name']}

{project['description']}

```ORIGINALLY CREATED : {project['created']}```""")
                        if project['completed'] == 'true':
                            readmefile.write("\n\n")
                            readmefile.write(f'`UPLOADED AS AN ARCHIVE TO GITHUB ON {datetime.datetime.now().strftime("%m/%d/%Y — %H:%M:%S")}`')
            print("git add .")
            print('git commit -m "just a commit"')
            print(f'GIT_COMMITTER_DATE="{datetime.datetime.strptime(project["created"],"%d/%m/%Y").strftime("%a %b %Y 20:19:19 BST")}" git commit --amend --no-edit --date "{datetime.datetime.strptime(project["created"],"%d/%m/%Y").strftime("%a %b %Y 20:19:19 BST")}"')
            print("git branch -M main")
            print(f"git remote add origin {input('Paste SSH URL : ')}")
            print("git push -u origin main")
            os.chdir(f"{MY_DIRECTORY}")
        else:
            print("SKIPPED.\n")