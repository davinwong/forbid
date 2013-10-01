import sys

# command line arguments
history = sys.argv[1]
control_input = sys.argv[2]
control_output = sys.argv[3]
bid_stream_1 = sys.argv[4]

# print history
# print control_input
# print control_output
# print bid_stream_1

history_file = open(history)
history_data = history_file.readlines()
print history_data