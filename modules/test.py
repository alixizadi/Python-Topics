import os
import sys

def relative_path():
    print(__file__)
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(project_root)

    mypath = os.path.join(project_root, 'modules')
    print(mypath)
    sys.path.insert(0, mypath)

    import my_calculator
    my_calculator.add(1,2)