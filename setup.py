import os


dirs = [
    "src","components","pipeline","exception","log","utils"
]

init = "__init__.py"
curr = os.getcwd()
for i in dirs:
    path = os.path.join(curr,i)
    os.makedirs(path,exist_ok=True)
    with open(os.path.join(path,init),"w+") as initial:
        pass