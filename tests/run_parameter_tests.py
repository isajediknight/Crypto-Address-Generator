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

# Parse the Arguments
from command_line_arguments import *

# Benchmark all the things
from benchmark import *

# Used to measuring our testing results
from testing_results import *
# < ---  End  Custom Classes Import --- >



set_verbosity = 0
show_results_for = 'both'
pass_fail_message = 'number'

## Set verbosity of the Unit Test Class
#try:
#    if('-set-verbosity' in list(my_args.keys())):
#        set_verbosity = int(my_args['-set-verbosity'].value)
#    else:
#        set_verbosity = 2
#        parameter_messages += " -set-verbosity was not passed in\n"
#except:
#    set_verbosity = 2
#finally:
#    if(set_verbosity not in [0,2]):
#        parameter_messages += "\n -set-verbosity = " + str(set_verbosity) + " which is not valid\n"
#        parameter_messages += " You may pass in -set-verbosity with a value of 0 or 2\n"
#        parameter_messages += " 0 will display custom Pass/Fail test results\n"
#        parameter_messages += " 2 will display normal results\n"



# Create an instance of Benchmark Class
runtime = Benchmark()

# Variable for accessing all tests
all_tests_list = []

class TestAPIClass(unittest.TestCase):

    def test_parameters(self):
        """
        Benchmark Class Variables Initialized to Zero
        """

        # Instance of Colored Text for displaying custom colors in print statements
        text = ColoredText(['datatype'],['38;5;30m'])

        # Initialization
        try:
            actual_comparison = False
            check = 'test = Parse()'
            test = Parse()
            actual_comparison = test.get_class_validation()
        except:
            actual_comparison = False

        description = "Initialized " + text.cc('Parse','orange')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if(set_verbosity != 0):
            assert(actual_comparison)

        # Initialized with string
        try:
            actual_comparison = False
            check = "test = Parse('-')"
            test = Parse('-')
            actual_comparison = test.get_class_validation()
        except:
            actual_comparison = False

        description = "Initialized " + text.cc('Parse', 'orange') + " with " + text.cc('String','datatype')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if (set_verbosity != 0):
            assert (actual_comparison)

        # Initialized with list
        try:
            actual_comparison = False
            check = "test = Parse(['-','--'])"
            test = Parse(['--'])
            actual_comparison = test.get_class_validation()
        except:
            actual_comparison = False

        description = "Initialized " + text.cc('Parse', 'orange') + " with " + text.cc('List', 'datatype')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if (set_verbosity != 0):
            assert (actual_comparison)

        # Initialized with dictionary
        try:
            actual_comparison = False
            check = "test = Parse({'-':'--'})"
            test = Parse({'-':'abc123'})
            actual_comparison = not test.get_class_validation()
        except:
            actual_comparison = False

        # Message when wrong datastype is sent in
        if actual_comparison:
            description = 'Not '
        else:
            description = ''
        description += "Initialized " + text.cc('Parse', 'orange') + " with " + text.cc('Dictionary', 'datatype')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if (set_verbosity != 0):
            assert (actual_comparison)

        # Initialized with float
        try:
            actual_comparison = False
            check = "test = Parse(1.776)"
            test = Parse(1.776)
            actual_comparison = not test.get_class_validation()
        except:
            actual_comparison = False

        # Message when wrong datastype is sent in
        if actual_comparison:
            description = 'Not '
        else:
            description = ''
        description += "Initialized " + text.cc('Parse', 'orange') + " with " + text.cc('Float', 'datatype')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if (set_verbosity != 0):
            assert (actual_comparison)

        # Initialized with Integer
        try:
            actual_comparison = False
            check = "test = Parse(1776)"
            test = Parse(1776)
            actual_comparison = not test.get_class_validation()
        except:
            actual_comparison = False

        # Message when wrong datastype is sent in
        if actual_comparison:
            description = 'Not '
        else:
            description = ''
        description += "Initialized " + text.cc('Parse', 'orange') + " with " + text.cc('Integer', 'datatype')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if (set_verbosity != 0):
            assert (actual_comparison)

        print(sys.argv)

        # test parsing parameters
        #try:
        actual_comparison = False
        check = "test = Parse('-')"
        test = Parse('-')
        test.add_expectation('-filename','string')
        test.add_expectation('-user', 'string', True, False)
        test.add_expectation('-password', 'string', True, True)
        test.add_expectation('-token', 'integer', False, False)
        test.parse_commandline()
        test.validate_requirements()
        actual_comparison = test.get_class_validation()
        #except:
        #    actual_comparison = False

        description = "Initialized " + text.cc('Parse', 'orange') + " with " + text.cc('String', 'datatype')
        unit_sub_test = TestResults(description, actual_comparison, check)
        all_tests_list.append(unit_sub_test)
        if (set_verbosity != 0):
            assert (actual_comparison)

    def test_print_all_test_results(self):
        """
        Used to Print Testing Results to the screen on verbosity = 0
        This should always be the last unit test
        """

        # Variable for printing colored text
        color_test = ColoredText()

        if(set_verbosity == 0):
            for each_test in all_tests_list:
                # Print both passed and failed
                if(show_results_for == 'both'):

                    if(all_tests_list[0] == each_test):
                        print("")

                    if(pass_fail_message == 'number'):
                        print(each_test.return_pass_or_fail_test_number_string(), end="")
                    elif(pass_fail_message == 'string'):
                        print(each_test.return_pass_or_fail_string(), end="")
                    else:
                        print(each_test.return_pass_or_fail_string(), end="")
                    print(each_test.description)
                    if(not each_test.result):
                        print(color_test.cc("            " + each_test.check,'grey'))
                # Print only failed
                elif(show_results_for == 'failed'):

                    if(all_tests_list[0] == each_test and len(each_test.fail_counter) > 0):
                        print("")

                    if(not each_test.result):
                        if(pass_fail_message == 'number'):
                            print(each_test.return_pass_or_fail_test_number_string(), end="")
                        elif(pass_fail_message == 'string'):
                            print(each_test.return_pass_or_fail_string(), end="")
                        else:
                            print(each_test.return_pass_or_fail_string(), end="")
                        print(each_test.description)
                        if(not each_test.result):
                            print(color_test.cc("            " + each_test.check,'grey'))
                # Print only passed
                elif(show_results_for == 'passed'):

                    if(all_tests_list[0] == each_test):
                        print("")

                    if (each_test.result):
                        if (pass_fail_message == 'number'):
                            print(each_test.return_pass_or_fail_test_number_string(), end="")
                        elif (pass_fail_message == 'string'):
                            print(each_test.return_pass_or_fail_string(), end="")
                        else:
                            print(each_test.return_pass_or_fail_string(), end="")
                        print(each_test.description)
                        if (not each_test.result):
                            print(color_test.cc("            " + each_test.check, 'grey'))

            fail = TestResults('Count Tests Run',True,'')

            print("")
            print(" Total Tests Run: " + str(len(fail.total_counter) - 1))
            print("")
            if(len(fail.fail_counter) == 0):
                display = color_test.cc('Passed', 'green')
                print(" [ " + display + " ] All "+str(len(fail.pass_counter) - 1)+" Tests!")
            else:
                display = color_test.cc('Passed', 'green')
                print(" [ " + display + " ] " + str(len(fail.pass_counter) - 1))
            display = color_test.cc('Failed', 'red')
            print(" [ " + display + " ] " + str(len(fail.fail_counter)))

            print("")

            # Only print the Legend if we got failures
            if(len(fail.fail_counter) > 0 or show_results_for == 'both' or show_results_for == 'passed'):
                print(" Color Legend:\n")
                color_test = ColoredText(['datatype'], ['38;5;30m'])
                display = color_test.cc(' Test Succeeded', 'green')
                print(display)
                display = color_test.cc(' Test Failed', 'red')
                print(display)
                display = color_test.cc(' Method', 'blue')
                print(display)
                display = color_test.cc(' Variable', 'purple')
                print(display)
                display = color_test.cc(' Datatype', 'datatype')
                print(display)
                display = color_test.cc(' Class', 'orange')
                print(display)
                print("")

                runtime.stop()
                print(" Test Runtime: " + runtime.human_readable_string() + "\n")

    #def test_print_for_james(self):
    #    print("\nThe world is going to die in 5 minutes")

# Run all the Unit Tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestAPIClass)
unittest.TextTestRunner(verbosity=set_verbosity).run(suite)
