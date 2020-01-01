# imports
import os
import time
from datetime import datetime

# initialize timer variable
start_time = time.time()

# export to log
# exports the terminal's output to a local txt file within the same directory
def export_log(status):
    print('Exporting current status to local log...')
    # open and append to the txt file
    log_file = open("pingertest.txt", "a+")
    # write the imported status (termianl output)
    log_file.write(status)
    # close the open txt file
    log_file.close()

# check network status
# pings a hostname and returns a result
def check_network_status(time_stamp):
    # custom hostname
    hostname = "8.8.8.8"
    # runs a system ping cmd against the hostname
    response = os.system("ping -c 3 {}".format(hostname))

    # if contact is made, set to a positive status output
    if response == 0:
        status = "We can make contact to {} at [{}]\n".format(hostname, time_stamp)
    # else if no packets made contact, set to a negative status output
    else:
        status = "We can NOT make contact to {} at [{}]\n".format(hostname, time_stamp)

    # print status output to terminal
    print(status)
    # save and export the status to a local txt file
    export_log(status)

# main
# start of the script that initializes and formats the timer
def main():
    # get the current date and time
    now = datetime.now()
    # format the datetime to the following string
    current_time = now.strftime("%H:%M:%S - %d/%m/%Y")
    # run a network status check and pass in the current datetime string
    # (this will be used as a time stamp later)
    check_network_status(current_time)
    # timer sleeps for 60 seconds before starting again
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))

# main script loop
# constantly loops the script's main function
while True:
    main()