import sys, time, os, heapq, threading, Queue

class Interface:
    def __init__(self, control_input, control_output, bid_stream_1):
        self.control_input = control_input
        self.control_output = control_output
        self.bid_stream_1 = bid_stream_1

    # def open_control_input():
    #     """ some stack overflow code"""

    #     #Set the filename and open the file
    #     file = open(control_input,'r')

    #     #Find the size of the file and move to the end
    #     st_results = os.stat(control_input)
    #     st_size = st_results[6]
    #     file.seek(st_size)

    #     while 1:
    #         where = file.tell()
    #         line = file.readline()
    #         if not line:
    #             time.sleep(1)
    #             file.seek(where)
    #         else:
    #             line.strip()
    #             # print line, # already has newline
    #             input_command = line.split()
    #             print input_command
    #             try:
    #                 # print input_command[0]
    #                 total_bids = int(input_command[1])
    #                 requested_bids = int(input_command[2])
    #                 if input_command[0] == 'top':
    #                     if len(bid_heap) == total_bids:
    #                         print heapq.nsmallest(requested_bids, bid_heap)
    #                     else:
    #                         print "old data"
    #             except:
    #                 pass