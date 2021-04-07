'''
====================================================
How to change current working directory in python?
====================================================
'''
'''
# Possible error while changing directory
NotADirectoryError: [Error 20] Not a directory: '/tmp/hi.txt'
FileNotFoundError: [Error 2] No such file or directory: '/tmp/hello.txt'
PermissionError: [Error 13] Permission denied: '/etc/httpd/conf'
'''
import os
def main():
    req_path=input("Enter path to change working dir: ")
    print("The current working dir is: ",os.getcwd())
    try:
        os.chdir(req_path)
        print("Now your new working dir is: ",os.getcwd())
    except FileNotFoundError:
        print("Given path is not a valid path. So can't change working directory")
    except NotADirectoryError:
        print("Given path is a file path. So can't change working directory")
    except PermissionError:
        print("Sorry you don't have access for the given path. So can't change the working directory")
    except Exception as e:
        print(e)
    return None

if __name__ == "__main__":
    main()
