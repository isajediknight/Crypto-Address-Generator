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
if((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
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

addresses = []
readfile = open(INPUTS_DIR + 'blockchair_bitcoin_addresses_latest.tsv','r')
counter = 0

for line in readfile:
    if(counter == 0):
        pass
    else:
        try:
            addresses.append(line.split('\t')[0])
        except:
            print("Failed: " + line)

    counter += 1
readfile.close()
print("Read In " + str(counter) + " Addresses in " + runtime.current_benchmark_without_stopping())

benchmark_time = Benchmark()
for address_counter in range(1,2000):
    wallet = Wallet()
    private_key, public_address_1, public_address_3 = wallet._get_the_three()
    details = public_address_1 + ',' + public_address_3 + ',' + private_key + '\n'
    address_counter += 1

    #print(addresses[address_counter])
    #print(public_address_1)
    #print(public_address_3)

    if(public_address_1 in addresses):
        print(public_address_1)
        print(details)
        outfile = open(OUTPUTS_DIR+'WINNER_WINNER_CHICKEN_DINNER.txt','w')
        outfile.write(details)
        outfile.close()
        break

    if(public_address_3 in addresses):
        print(public_address_3)
        print(details)
        outfile = open(OUTPUTS_DIR+'WINNER_WINNER_CHICKEN_DINNER.txt','w')
        outfile.write(details)
        outfile.close()
        break

    if ((address_counter != 0) and (address_counter % 1000 == 0)):
        benchmark_time.stop()
        print("Generated " + str(address_counter) + " Addresses.  Time Check: " + benchmark_time.human_readable_string())  # current_benchmark_without_stopping())

        # del benchmark_time
        benchmark_time = Benchmark()

runtime.stop()
print("Checked " + str(address_counter) + " Addresses in " + runtime.human_readable_string())