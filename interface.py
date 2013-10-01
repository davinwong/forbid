import sys, time, os, heapq

# command line arguments
history = sys.argv[1]
control_input = sys.argv[2]
control_output = sys.argv[3]
bid_stream_1 = sys.argv[4]

# min heap with negative numbers
# heapq.heapify(history_data)
bid_heap = []
heapq.heapify(bid_heap)

history_file = open(history)

for line in history_file:
    heapq.heappush(bid_heap, -1*int(line.strip()))
history_file.close()


""" taken from stack overflow"""

#Set the filename and open the file
file = open(control_input,'r')

#Find the size of the file and move to the end
st_results = os.stat(control_input)
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
        # print line, # already has newline
        input_command = line.split()
        print input_command
        try:
            # print input_command[0]
            total_bids = int(input_command[1])
            bids_requested = int(input_command[2])
            if input_command[0] == 'top':
                print "len(bid_heap)"
                print len(bid_heap)
                if len(bid_heap) == total_bids:
                    print heapq.nsmallest(bids_requested, bid_heap)
                else:
                    print "old data"
        except:
            pass
        
            # if input_command[0] == 'top':
            #   print bid_heap.size()


# remove from heap, add them back
# print heapq.nsmallest(3, bid_heap)







# while bid_heap:
#     print -1*heapq.heappop(bid_heap)

# print bid_heap