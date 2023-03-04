import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path,"w")
            file.write("Function {} executed on {} on {} \n".format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S") ))
            file.close()
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file("FILE_CREATE", str(os.getcwd() + r"/Section 5/log_create.txt") )
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")


@wrapper_with_log_file("FILE_DELETE", str(os.getcwd() + r"/Section 5/log_delete.txt") )
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
     
    

create_file(str(os.getcwd() + r"\Section 5\test.txt"))
delete_file(str(os.getcwd() + r"\Section 5\test.txt"))
create_file(str(os.getcwd() + r"\Section 5\test.txt"))
delete_file(str(os.getcwd() + r"\Section 5\test.txt"))
