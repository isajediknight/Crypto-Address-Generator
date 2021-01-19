# HOW TO RUN
# python3 bulk_address_creation.py -filename test_output.csv -addresses-to-generate 500 -write-interval 100 -benchmark-interval 600
# python3 bulk_address_creation.py -filename 2021_01_09_Thread_01.csv -addresses-to-generate 4000000 -write-interval 200 -benchmark-interval 100000
# python3 bulk_address_creation.py -filename 2021_01_09_Thread_02.csv -addresses-to-generate 4000000 -write-interval 200 -benchmark-interval 100000
# python3 bulk_address_creation.py -filename 2021_01_09_Thread_03.csv -addresses-to-generate 1000000 -write-interval 200 -benchmark-interval 100000
# python3 bulk_address_creation.py -filename 2021_01_09_Thread_04.csv -addresses-to-generate 4000000 -write-interval 200 -benchmark-interval 100000
# python3 bulk_address_creation.py -filename 2021_01_10_Thread_03.csv -addresses-to-generate 6500000 -write-interval 200 -benchmark-interval 100000

# Default Modules
import datetime,time,os,sys

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
if((OS_TYPE == 'linux')):
    sys.path.insert(0,'../classes/')
    sys.path.insert(0,MODULES_DIR)
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')
    sys.path.insert(0,MODULES_DIR)

# < --- Begin Custom Classes Import --- >
# Custom Colors for printing to the screen
from custom_colors import *

# Allows Parameters to be read by Python more easily
from reuseable_methods import parse_args

from benchmark import *
# < ---  End  Custom Classes Import --- >

# < --- Begin pypi.org Module Import -- >
from bitcoinaddress_mainnet import Wallet
#from bitcoinaddress import Wallet

# < ---  End  pypi.org Module Import -- >

runtime = Benchmark()
benchmark_time = Benchmark()

# To Debug: parse_args('dict',True)
my_args = parse_args('dict',False,[],['-addresses-to-generate','-benchmark-interval'],False,[])
if('-addresses-to-generate' in list(my_args.keys())):
    try:
        addresses_to_generate = int(my_args['-addresses-to-generate'].value)
    except:
        print(my_args['-addresses-to-generate'].value + " is not an integer.  Please rerun program.")
        addresses_to_generate = 0
if('-benchmark-interval' in list(my_args.keys())):
    try:
        benchmark_interval = int(my_args['-benchmark-interval'].value)
    except:
        print(my_args['-benchmark-interval'].value + " is not an integer.  Please rerun program.")
        benchmark_interval = 100000

counter = 0

while(counter < addresses_to_generate):

    wallet = Wallet()
    private_key, public_address_1, public_address_3 = wallet._get_the_three()
    details = public_address_1 + ',' + public_address_3 + ',' + private_key + '\n'

    #if((details.lower().find('trump') > 0) or (details.lower().find('biden') > 0) or (details.lower().find('harris') > 0) or (details.lower().find('america') > 0)):
    #    print("Political: " + details)

    #if ((details.lower().find('blacklivesmater') > 0) or (details.lower().find('systematicracism') > 0)):
    #    print("Liberal: " + details)

    #if ((details.lower().find('facebook') > 0) or (details.lower().find('google') > 0) or (
    #        details.lower().find('twitter') > 0) or (details.lower().find('microsoft') > 0)):
    #    print("Corporate: " + details)

    path_plus_file = '/media/luke/Data/Crypto/BTC/generated_addresses/' + public_address_1[0:2].upper() + '_' + public_address_3[0:2].upper() + '_generated_addresses.txt'

    if(not (os.path.isfile(path_plus_file))):
        os.system("touch " + path_plus_file)

    try:
        one_address = open(path_plus_file, 'a')
        one_address.write(details)
        one_address.close()
        del one_address
    except:
        try:
            one_address.close()
        except:
            pass
        one_address = open(path_plus_file, 'a')
        one_address.write(details)
        one_address.close()
        del one_address

    counter += 1
    if((counter != 0) and (counter % benchmark_interval == 0)):
        benchmark_time.stop()
        print("Generated " + str(counter) + " Addresses.  Time Check: " + benchmark_time.human_readable_string())#current_benchmark_without_stopping())

        #del benchmark_time
        benchmark_time = Benchmark()

runtime.stop()
print("Generated " + str(counter) + " Addresses in " + runtime.human_readable_string())

