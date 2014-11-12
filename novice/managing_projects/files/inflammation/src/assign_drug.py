import os 
import sys

def assign_drug(filepath):
    '''Assigns a drug to a filename '''
    filename = os.path.basename(filepath)
    number = filename[13:-4]
    # the above line is error-prone: say someone misspells inflammation so it
    # has less that 13 characters...
    # A more robust funtion uses the Python's split() function for strings:
    #
    # filename_without_ext = filename.split('.')[0]
    # number = filename_without_ext.split('_')[1]
    result = ''
    if (int(number) % 2) == 1:
        result = 'tylenol'
    else:
        result = 'placebo'
    return result


filename = sys.argv[1] 
print assign_drug(filename)
    
assert assign_drug("inflammation_1.dat") == "tylenol" 
assert assign_drug("inflammation_4.dat") == "placebo" 
assert assign_drug("inflammation_3.dat") == "tylenol"
# test for numbers starting with zeroes
assert assign_drug("inflammation_04.dat") == "placebo" 
# test for full paths
assert assign_drug("/somewhere/in/your/disk/inflammation_03.dat") == "tylenol"
