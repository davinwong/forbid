import sys
from interface import Interface, BidStream
from bid_market import BidMarket

DATA_FILES_FOLDER_PATH = 'data_files/'

def main():

    # command line arguments
    history = DATA_FILES_FOLDER_PATH + sys.argv[1]
    control_input = DATA_FILES_FOLDER_PATH + sys.argv[2]
    control_output = DATA_FILES_FOLDER_PATH + sys.argv[3]
    bid_stream_file_1 = DATA_FILES_FOLDER_PATH + sys.argv[4]
    
    print bid_stream_file_1

    bid_market = BidMarket()
    bid_market.import_history(history)

    interface = Interface(
        bid_market,
        control_input,
        control_output,
        bid_stream_file_1)

    bid_stream_1 = BidStream(bid_stream_file_1, bid_market)
    # bid_stream_2 = BidStream(bid_stream_file_2, bid_market)
    # bid_stream_3 = BidStream(bid_stream_file_3, bid_market)
    # bid_stream_4 = BidStream(bid_stream_file_4, bid_market)
    
    bid_stream_1.start()
    # bid_stream_2.start()
    # bid_stream_3.start()
    # bid_stream_4.start()

    interface.control_input_stream()

if __name__ == "__main__":
    main()
