import sys
from interface import Interface, BidStream
from bid_market import BidMarket

DATA_FILES_FOLDER_PATH = 'data_files/'
NUMBER_BID_STREAMS = 4


def main():
    # command line arguments
    history = DATA_FILES_FOLDER_PATH + sys.argv[1]
    control_input = DATA_FILES_FOLDER_PATH + sys.argv[2]
    control_output = DATA_FILES_FOLDER_PATH + sys.argv[3]
    bid_stream_files = []
    for i in range(0, NUMBER_BID_STREAMS):
        bid_stream_files.append(DATA_FILES_FOLDER_PATH + sys.argv[4+i])

    bid_market = BidMarket()
    bid_market.import_history(history)

    interface = Interface(
        bid_market,
        control_input,
        control_output)

    bid_streams = []
    for i in range(0, NUMBER_BID_STREAMS):
        bid_streams.append(BidStream(bid_stream_files[i], bid_market))

        # make daemons so threads close with program
        bid_streams[i].daemon = True

        bid_streams[i].start()

    interface.open_control_input_stream()

if __name__ == "__main__":
    main()
