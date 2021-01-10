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

# To Debug: parse_args('dict',True)
my_args = parse_args('dict',False,[],['-filename','-addresses-to-generate','-write-interval','-benchmark-interval'],False,[])
if('-filename' in list(my_args.keys())):
    output_filename = my_args['-filename'].value
if('-addresses-to-generate' in list(my_args.keys())):
    try:
        addresses_to_generate = int(my_args['-addresses-to-generate'].value)
    except:
        print(my_args['-addresses-to-generate'].value + " is not an integer.  Please rerun program.")
        addresses_to_generate = 0
if('-write-interval' in list(my_args.keys())):
    try:
        write_interval = int(my_args['-write-interval'].value)
    except:
        write_interval = 200
        print(my_args['-write-interval'].value + " is not an integer for -write-interval.  Defaulted to: " + str(write_interval))
if('-benchmark-interval' in list(my_args.keys())):
    try:
        benchmark_interval = int(my_args['-benchmark-interval'].value)
    except:
        benchmark_interval = 100000
        print(my_args['-benchmark-interval'].value + " is not an integer for -benchmark-interval.  Defaulted to: " + str(benchmark_interval))

if(os.path.isfile(OUTPUTS_DIR + output_filename)):
    pass
else:
    outfile = open(OUTPUTS_DIR + output_filename, 'w')
    outfile.write('Private_Key,Public_Address_1,Public_Address_3\n')
    outfile.close()
    del outfile

outfile = open(OUTPUTS_DIR + output_filename ,'a')
counter = 0
details = ''
while(counter < addresses_to_generate):
    wallet = Wallet()
    private_key, public_address_1, public_address_3 = wallet._get_the_three()
    details += private_key + ',' + public_address_1 + ',' + public_address_3 + '\n'
    if(counter % write_interval == 0):
        outfile.write(details)
        details = ''
    if((counter != 0) and (counter % benchmark_interval == 0)):
        print("Generated " + str(counter) + " Addresses.  Time Check: " + runtime.current_benchmark_without_stopping())

    counter += 1

if(len(details) > 1):
    outfile.write(details)
    details = ''

outfile.close()
#wallet = Wallet('5JqJzbB72aEnXkNvYHZVhxACdy93FWvKduRJfNVcMp9qMw4uBiW')#'L5JwPtRCbu7KwvNm9NuUcyRVGycrcaSrRh1WdDjqBdhSyEKeGsrn')
#wallet = Wallet('5HqrbgkWPqBy6dvCE7FoUiMuiCfFPRdtRsyi6NuCM2np8qBZxq5')
#print(wallet)
#private_key_wif,public_address_1,public_address_3 = wallet._get_the_three()
#print("Private Key WIF: " + str(private_key_wif))
#print("Public Address 1: " + str(public_address_1))
#print("Public Address 3: " + str(public_address_3))
#print(wallet)
#print(wallet.key.__dict__['mainnet'].__dict__)

runtime.stop()
#print("Program Runtime: "+runtime.seconds_to_human_readable(runtime.get_seconds()))
print("Generated " + str(counter) + " Addresses in " + runtime.human_readable_string())

