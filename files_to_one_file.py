import os
import fnmatch

# Open the output file in write mode
with open('results.py', 'w') as res:
    for path, dirs, files in os.walk('.'):
        for each_file in fnmatch.filter(files, '*.py'):
            fullname = os.path.abspath(os.path.join(path, each_file))
            res.write('#' + fullname + '\n')
            
            # Open the input file in read mode using a context manager
            with open(fullname, 'r') as file_in_path:
                for line in file_in_path:
                    if line.strip():
                        res.write(line)
