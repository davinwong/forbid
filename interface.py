import sys, time, os, heapq, threading, Queue

class Interface:
    def __init__(self, bid_market, control_input, control_output, bid_stream_1):
        self.bid_market = bid_market
        self.control_input = control_input
        self.control_output = control_output
        self.bid_stream_1 = bid_stream_1

    def open_control_input(self):
        """ some stack overflow code"""

        #Set the filename and open the file
        file = open(self.control_input,'r')

        #Find the size of the file and move to the end
        st_results = os.stat(self.control_input)
        st_size = st_results[6]
        file.seek(st_size)

        while 1:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                line.strip()
                input_command = line.split()

                try:
                    total_bids = int(input_command[1])
                    requested_bids = int(input_command[2])
                    if input_command[0] == 'top':
                        print self.bid_market.top_bids(total_bids, requested_bids)
                except:
                    pass