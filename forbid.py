import sys
from interface import Interface
from bid_market import BidMarket


def main():
    DATA_FILES_FOLDER_PATH = 'data_files/'

    # command line arguments
    history = DATA_FILES_FOLDER_PATH + sys.argv[1]
    control_input = DATA_FILES_FOLDER_PATH + sys.argv[2]
    control_output = DATA_FILES_FOLDER_PATH + sys.argv[3]
    bid_stream_1 = DATA_FILES_FOLDER_PATH + sys.argv[4]

    bid_market = BidMarket()
    bid_market.import_history(history)

    interface = Interface(
        bid_market,
        control_input,
        control_output,
        bid_stream_1)

    interface.open_control_input()

if __name__ == "__main__":
    main()
