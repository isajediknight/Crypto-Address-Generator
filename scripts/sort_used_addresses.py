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
my_args = parse_args('dict',False,[],['-line-begin','-line-end'],False,[])
if('-line-begin' in list(my_args.keys())):
    line_begin = int(my_args['-line-begin'].value)
    if(line_begin < 0):
        line_begin = 1
if('-line-end' in list(my_args.keys())):
    line_end = int(my_args['-line-end'].value)

#33586206
readfile = open(INPUTS_DIR+'blockchair_bitcoin_addresses_latest.tsv','r')

counter = 0
address_counter = 0
for line in readfile:

    if(counter > line_end):
        break

    if((counter >= line_begin) and (counter < line_end)):
        address = line.strip().split('\t')[0]

        #if((address[0] == '1') or (address[0] == '3')):
        #    path_plus_file = '/media/luke/Data/Crypto/BTC/used_addresses/' + address[0].upper() + '/' + address[1].upper() + '/'+ address[0].upper() + '_used_addresses.txt'
        #else:
        #    path_plus_file = '/media/luke/Data/Crypto/BTC/used_addresses/other/' + address[1].upper() + '/' + address[0].upper() + '_used_addresses.txt'

        path_plus_file = '/media/luke/Data/Crypto/BTC/used_addresses/' + address[0].upper() + address[1].upper() + '_used_addresses.txt'

        #print(">"+path_plus_file+"<")

        if(not (os.path.isfile(path_plus_file))):
            os.system("touch " + path_plus_file)
            #print("touch " + path_plus_file)
            #create_file = open('/media/luke/Data/Crypto/BTC/used_addresses/' + address[0] + '/' + address[0] + '_used_addresses.txt','w')
            #create_file.write('')
            #create_file.close()
            #cre
        one_address = open(path_plus_file,'a')
        #print('/media/luke/Data/Crypto/BTC/used_addresses/' + address[0] + '/' + address[0] + '_used_addresses.txt')
        one_address.write(address + '\n')
        one_address.close()
        del one_address
        address_counter += 1

    counter += 1

#print(str(counter))
readfile.close()
runtime.stop()
#print("Program Runtime: "+runtime.seconds_to_human_readable(runtime.get_seconds()))
print("Generated " + str(address_counter) + " Addresses in " + runtime.human_readable_string())