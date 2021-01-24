# Default Modules
import os,sys,getpass

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

    def __init__(self,input_parameter=['-','--']):

        # How do we identify the parameters being passed in?
        self.parameter_flags = []

        # For text coloration
        text = ColoredText(['datatype'], ['38;5;30m'])

        # Was the Class Object initialized successfully
        self.validation = False

        if type([]) == type(input_parameter):
            ##DEBUG
            ##print("List " + str(input_parameter))
            for item in input_parameter:
                ##DEBUG
                ##print("Added: " + item)
                self.parameter_flags.append(item)
                self.validation = True
        elif type('') == type(input_parameter):
            ##DEBUG
            ##print("String " + str(input_parameter))
            if len(input_parameter) > 0:
                self.parameter_flags.append(input_parameter)
                ##DEBUG
                ##print("Added: " + input_parameter)
                self.validation = True
        else:
            pass
            #message = " [ In " + text.cc('__init__','blue') + " " + text.cc('paramter_flags','purple') + " was passed " + str(text.cc(str(type(input_parameter)),'datatype'))
            #message += " which is " + text.cc('not supported','red') + " ]"
            #print(message)
            #print("   " + text.cc('Expected: ','grey') + text.cc('String','datatype') + text.cc(' or ','grey') + text.cc('List','datatype'))# + " but got " + text.cc(str(type(paramter_flags)),'datatype'))

        # Dictionary for holding all the Paramters and their Values
        self.parameters = {}

        # Expectations - what we are expecting to be passed in via commandline
        self.expected_parameters = {}

    #def add_paramter_flags(self,paramter_flags='-'):
    #    """
    #    <paramter_flags>
    #    What string should be used to identify a parameter
    #    '-'
    #    """
    #    self.parameter_flags.append(paramter_flags)

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

    def parse_commandline(self):
        """
        Parse the commandline arguments!
        """
        self.script_file = sys.argv[0]

        previous_item = ''
        for item in sys.argv[1:]:
            for parameter_flag in self.parameter_flags:
                if previous_item.find(parameter_flag) == 0:
                    ##DEBUG
                    ##print("Assigning: " + previous_item + " <-- " + item)
                    self.parameters[previous_item] = Parameter(self.get_value_datatype(item),item,False,False)
                    self.parameters[previous_item].show_parameter()
            previous_item = item

        #return self.parameters

    def add_expectation(self,parameter_name = 'unnamed',datatype = 'string', required = False,hidden = False):
        """
        What do we expect will be added as commandline parameters?
        """
        self.expected_parameters[parameter_name] = Parameter(datatype, None, required, hidden)

    def validate_requirements(self):
        """

        """
        for key in list(self.expected_parameters.keys()):
            if key not in list(self.parameters.keys()) and self.expected_parameters[key].get_required():
                print("Missing: " + key)

                if self.expected_parameters[key].get_hidden():
                    value = getpass.getpass(key + ": ")
                else:
                    value = input(key + ": ")

                while(self.expected_parameters[key].get_parameter_type() != self.get_value_datatype(value)):

                    print(str(self.expected_parameters[key].get_parameter_type()) + " - " + self.get_value_datatype(value))

                    if self.expected_parameters[key].get_hidden:
                        value = getpass.getpass(key + ": ")
                    else:
                        value = input(key + ": ")



    def get_value_datatype(self,value):
        """
        Used for identifying the datatype of the value passed in
        """
        try:
            test = int(value)
            return 'integer'
        except:
            pass

        try:
            test = float(value)
            return 'float'
        except:
            pass

        if type(value) == type([]):
            return 'list'
        elif type(value) == type({}):
            return 'dictionary'
        elif type(value) == type(complex(1j)):
            return 'complaex'
        elif type(value) == type(tuple(("apple", "orange"))):
            return 'tuple'
        elif type(value) == type(range(1)):
            return 'range'
        elif type(value) == type(set([1,2,3])):
            return 'set'
        elif type(value) == type(frozenset(("apple", "orange"))):
            return 'frozenset'
        elif type(value) == type(False):
            return 'boolean'
        elif type(value) == type(bytes(5)):
            return 'bytes'
        elif type(value) == bytearray(5):
            return 'bytearray'
        elif type(value) == memoryview(bytes(5)):
            return 'memoryview'
        else:
            return 'string'

    def get_parameter_names(self):
        return list(self.parameters.keys())

    def get_class_validation(self):
        return self.validation

class Parameter:

    def __init__(self, parameter_type = 'string', value = None, required = False, hidden = False):
        self.parameter_type = parameter_type
        self.required = required
        self.hidden = hidden
        self.value = value
        self.directory = None
        self.absolute_path_to_file = None
        self.relative_path_to_file = None

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
    def get_value(self):
        return self.value

    def get_parameter_type(self):
        return self.parameter_type

    def get_hidden(self):
        return self.hidden

    def get_required(self):
        return self.required
    # < ---  End  Getters --- >

    def show_parameter(self):
        """

        """
        # For text coloration
        text = ColoredText(['datatype'], ['38;5;30m'])

        print("")
        #print("Parameter:\t" + )
        print("Datatype:\t" + text.cc(self.parameter_type,'datatype'))
        print("Required:\t" + str(self.required))
        print("Hidden:\t\t" + str(self.hidden))
        print("Value:\t\t" + str(self.value))
        print("")