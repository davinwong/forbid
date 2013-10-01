import sys, heapq

# command line arguments
history = sys.argv[1]
control_input = sys.argv[2]
control_output = sys.argv[3]
bid_stream_1 = sys.argv[4]

# print history
# print control_input
# print control_output
# print bid_stream_1

# min heap with negative numbers
bid_heap = []
heapq.heapify(bid_heap)

history_file = open(history)

for line in history_file:
    heapq.heappush(bid_heap, -1*int(line.strip()))
history_file.close()


# heapq.heapify(history_data)


while bid_heap:
    print heapq.heappop(-1*bid_heap)

print bid_heap