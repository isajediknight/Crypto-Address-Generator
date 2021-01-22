# Default Modules
import os,sys

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

# Get our current directory
OUTPUT_FILE_DIRECTORY = os.getcwd()

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

# Create variables for all the paths
if((OS_TYPE == 'windows')):
    # Clear Screen Windows
    os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    MODULES_GITHUB_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\github\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    MODULES_GITHUB_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/github/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    sys.path.insert(0,'../classes/')
    sys.path.insert(0,MODULES_DIR)
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')
    sys.path.insert(0,MODULES_DIR)

# < --- Begin Custom Classes Import --- >
# Custom Colors for printing to the screen
from custom_colors import *
# < ---  End  Custom Classes Import --- >

class Parse:

    def __init__(self,paramter_flags=['-','--']):

        # How do we identify the parameters being passed in?
        self.parameter_flags = []

        # For text coloration
        text = ColoredText(['datatype'], ['38;5;30m'])

        if type([]) == type(paramter_flags):
            for item in paramter_flags:
                self.parameter_flags.append(item)
        elif type('') == type(paramter_flags):
            self.parameter_flags.append(paramter_flags)
        else:
            print(" [ "+text.cc('paramter_flags','purple') + " Datatype " + str(text.cc(str(type(paramter_flags)),'datatype')) + " is " + text.cc('not supported','red') + " ]")
            print("   Expected: " + text.cc('String','datatype') + " or " + text.cc('List','datatype'))# + " but got " + text.cc(str(type(paramter_flags)),'datatype'))

        # Dictionary for holding all the Paramters and their Values
        self.parameters = {}

    def add_paramter_flags(self,paramter_flags='-'):
        """
        <paramter_flags>
        What string should be used to identify a parameter
        '-'
        """


    def add_parameter(self,parameter_name,parameter_type,required,hidden):
        """
        <parameter_name>
        Name of the Parameter
        -filename hello.txt

        <parameter_type>
        Type of the Parameter - one of the following:
        string, int, float, list, array, set

        <required>
        Is the Parameter required?
        Boolean

        <hidden>
        If the Parameter is not passed in when it is prompted should the text be hidden?
        Boolean
        """
        self.parameters[parameter_name] = Parameter(parameter_type,required,hidden)

    def set_value(self,parameter_name,value):
        """
        Attempts to set the Value of a Parameter to the Parameter
        """
        if parameter_name in get_parameter_names:
            self.parameters[parameter_name] = self.parameters[parameter_name].set_value(value)
            return True
        else:
            print(" Paramter Name: " + parameter_name + " is not a Parameter")
            return False

    def get_parameter_names(self):
        return list(self.parameters.keys())

class Parameter:

    def __init__(self, parameter_type = 'string', required = False, hidden = False):
        self.parameter_type = parameter_type
        self.required = required
        self.hidden = hidden
        self.value = None

    # < --- Begin Setters --- >
    def set_value(self,value):
        self.value = value

    def set_parameter_type(self,parameter_type):
        self.parameter_type = parameter_type

    def set_hidden(self,hidden):
        self.hidden = hidden

    def set_required(self,required):
        self.required = required
    # < ---  End  Setters --- >

    # < --- Begin Getters --- >
    def get_value(self,value):
        return self.value

    def get_parameter_type(self,parameter_type):
        return self.parameter_type

    def get_hidden(self,hidden):
        return self.hidden

    def get_required(self,required):
        return self.required
    # < ---  End  Getters --- >