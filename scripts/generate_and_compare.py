# Default Modules
import datetime,time,os,sys

from os import listdir
from os.path import isfile, join

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

master_address_benchmark = Benchmark()
master_addresses = []
master_addresses_1 = []
master_addresses_3 = []
master_addresses_other = []
total_address_check_count = 0
readfile = open(INPUTS_DIR + 'blockchair_bitcoin_addresses_latest.tsv','r')
counter = 0

for line in readfile:
    if(counter == 0):
        pass
    else:
        try:
            just_the_address = line.split('\t')[0]
            address_type = just_the_address[0]
            if address_type == '1':
                master_addresses_1.append(just_the_address)
            elif address_type == '3':
                master_addresses_3.append(just_the_address)
            else:
                master_addresses_other.append(just_the_address)
        except:
            print("Failed: " + line)

    counter += 1
readfile.close()
master_address_benchmark.stop()
print(" Read In " + str(counter) + " Master Addresses in " + master_address_benchmark.human_readable_string())

master_set_benchmark = Benchmark()
master_addresses_1_set = set(master_addresses_1)
master_addresses_3_set = set(master_addresses_3)
master_addresses_other_set = set(master_addresses_other)
master_set_benchmark.stop()
print(" Master Addresses converted to sets in: " + master_set_benchmark.human_readable_string())

# Addresses that we have the private keys to
found = []
found_private_key = []

# Generate Addresses and Compare
address_generation_benchmark = Benchmark()
generated_addresses_1 = {}
generated_addresses_3 = {}
generated_addresses_other = {}
for generated_address_counter in range(1,2):
    wallet = Wallet()
    private_key, public_address_1, public_address_3 = wallet._get_the_three()
    generated_addresses_1[public_address_1] = private_key
    generated_addresses_3[public_address_3] = private_key
address_generation_benchmark.stop()
print(" Generated " + str(generated_address_counter) + " Addresses in " + address_generation_benchmark.human_readable_string())

v2_address_1_benchmark = Benchmark()
if(len(list(set(master_addresses_1).intersection(set(generated_addresses_1.keys()))))> 0):
    found.append(list(set(master_addresses_1).intersection(set(generated_addresses_1.keys()))))
    print(str(found[-1]))
    try:
        print(generated_addresses_1[str(found[-1])])
    except:
        print("counldn't print private key")
    outfile = open(OUTPUTS_DIR + 'WINNER_WINNER_CHICKEN_DINNER_ADDRESSES_1.txt', 'a')
    outfile.write(str(found[-1])+','+generated_addresses_1[str(found[-1])])
    outfile.close()
v2_address_1_benchmark.stop()
print(" v2 Address 1 Check : " + v2_address_1_benchmark.human_readable_string())

v2_address_3_benchmark = Benchmark()
if(len(list(set(master_addresses_3).intersection(set(generated_addresses_3.keys()))))> 0):
    found_addresses = list(master_addresses_3_set.intersection(addresses_check_3_set))
    for found_one in found_addresses:
        found.append(found_one)
        # print(str(found[-1]))
        try:
            found_private_key.append(private_key[address_check_3.index(found_one)])
        except:
            print("counldn't print private key for: " + found_one)
    try:
        outfile = open(OUTPUTS_DIR + 'WINNER_WINNER_CHICKEN_DINNER_ADDRESSES_3.txt', 'a')
        outfile.write(str(found[-1]) + ',' + str(found_private_key[-1]))
        outfile.close()
    except:
        print("could not write out our winner!")
        ans = input("PAUSED HIT ENTER TO UNPAUSE")
v2_address_3_benchmark.stop()
print(" v2 Address 3 Check : " + v2_address_3_benchmark.human_readable_string())

print(" Total Addresses Checked: " + str(total_address_check_count))

runtime.stop()
print(" Program Runtime: " + runtime.human_readable_string())


















mypath = '/media/luke/Data/Crypto/BTC/generated_addresses/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for my_file in onlyfiles:
    address_generated_benchmark = Benchmark()
    read_addresses_counter = 0
    addresses_check_1 = []
    addresses_check_3 = []
    private_key = []
    read_generated_addresses = open('/media/luke/Data/Crypto/BTC/generated_addresses/'+my_file,'r')
    for line in read_generated_addresses:
        addresses_check_1.append(line.strip().split(',')[0])
        addresses_check_3.append(line.strip().split(',')[1])
        private_key.append(line.strip().split(',')[2])
        read_addresses_counter += 1
    total_address_check_count += read_addresses_counter
    read_generated_addresses.close()
    address_generated_benchmark.stop()
    print(" " + my_file + " " +str(read_addresses_counter) + " Generated Addresses's Loaded in: " + address_generated_benchmark.human_readable_string())

    v2_address_1_benchmark = Benchmark()
    addresses_check_1_set = set(addresses_check_3)
    if (len(list(master_addresses_1_set.intersection(addresses_check_1_set))) > 0):
        found_addresses = list(master_addresses_1_set.intersection(addresses_check_1_set))
        for found_one in found_addresses:
            found.append(found_one)
            #print(str(found[-1]))
            try:
                found_private_key.append(private_key[address_check_1.index(found_one)])
            except:
                print("counldn't print private key for: " + found_one)
        try:
            outfile = open(OUTPUTS_DIR + 'WINNER_WINNER_CHICKEN_DINNER_ADDRESSES_3.txt', 'a')
            outfile.write(str(found[-1]) + ',' + str(found_private_key[-1]))
            outfile.close()
        except:
            print("could not write out our winner!")
            ans = input("PAUSED HIT ENTER TO UNPAUSE")
    v2_address_1_benchmark.stop()
    print(" " + my_file + " v2 Address 1 Check : " + v2_address_1_benchmark.human_readable_string())

    v2_address_3_benchmark = Benchmark()
    addresses_check_3_set = set(addresses_check_3)
    if (len(list(master_addresses_3_set.intersection(addresses_check_3_set))) > 0):
        found_addresses = list(master_addresses_3_set.intersection(addresses_check_3_set))
        for found_one in found_addresses:
            found.append(found_one)
            # print(str(found[-1]))
            try:
                found_private_key.append(private_key[address_check_3.index(found_one)])
            except:
                print("counldn't print private key for: " + found_one)
        try:
            outfile = open(OUTPUTS_DIR + 'WINNER_WINNER_CHICKEN_DINNER_ADDRESSES_3.txt', 'a')
            outfile.write(str(found[-1]) + ',' + str(found_private_key[-1]))
            outfile.close()
        except:
            print("could not write out our winner!")
            ans = input("PAUSED HIT ENTER TO UNPAUSE")
    v2_address_3_benchmark.stop()
    print(" "+ my_file + " v2 Address 3 Check : " + v2_address_3_benchmark.human_readable_string())