import os
files_to_process = [
    r"/home/piotr/Documents/VS Program/KursPythonPL/KursPythonPL/Section 3/DataToLAB13.py/sin_square.py",
    r"/home/piotr/Documents/VS Program/KursPythonPL/KursPythonPL/Section 3/DataToLAB13.py/square_root.py"
    ]

for i in files_to_process:
    print(os.path.basename(i))
    source = open(i).read()
    exec(source)

     
files_to_process = [
    r"/home/piotr/Documents/VS Program/KursPythonPL/KursPythonPL/Section 3/DataToLAB13.py/sin_square.py",
    r"/home/piotr/Documents/VS Program/KursPythonPL/KursPythonPL/Section 3/DataToLAB13.py/square_root.py"
    ]
     
for file_path in files_to_process:
     
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)