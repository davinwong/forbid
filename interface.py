import sys
import time
import os
import threading
import Queue

# Lock allows 1 thread to access the bid market at a time
# adding/reading bids synchronously prevents interference with each other
LOCK = threading.Lock()


class Interface:
    def __init__(self, bid_market, control_input, control_output):
        self.bid_market = bid_market
        self.control_input = control_input
        self.control_output = control_output
        self.command_queue = Queue.Queue()

    def open_control_input_stream(self):
        """ some stack overflow code"""

        #Set the filename and open the file
        file = open(self.control_input, 'r')

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
                LOCK.acquire()
                line.strip()
                input_command = line.split()

                try:
                    if input_command[0] == 'top':
                        total_bids = int(input_command[1])
                        requested_bids = int(input_command[2])

                        if requested_bids <= total_bids:
                            top_bids = self.bid_market.top_bids(total_bids, requested_bids)

                            # convert numbers to strings, join with space, return positives
                            print " ".join(map(str, map(lambda x: -1*x, top_bids)))
                    if input_command[0] == 'end':
                        sys.exit()
                    LOCK.release()
                except:
                    LOCK.release()


class BidStream(threading.Thread):
    def __init__(self, bid_stream_file, bid_market):
        self.bid_stream_file = bid_stream_file
        self.bid_market = bid_market
        threading.Thread.__init__(self)

    def run(self):
        #Set the filename and open the file
        file = open(self.bid_stream_file, 'r')

        #Find the size of the file and move to the end
        st_results = os.stat(self.bid_stream_file)
        st_size = st_results[6]
        file.seek(st_size)

        while 1:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                LOCK.acquire()
                line.strip()
                input_command = line.split()

                try:
                    bid = int(input_command[0])
                    self.bid_market.insert_bid(bid)
                    LOCK.release()
                except:
                    LOCK.release()
