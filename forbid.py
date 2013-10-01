import sys, time, os
from interface import Interface
from bid_market import BidMarket


def main():
    # command line arguments
    history = sys.argv[1]
    control_input = sys.argv[2]
    control_output = sys.argv[3]
    bid_stream_1 = sys.argv[4]

    bid_market = BidMarket()
    bid_market.import_history(history)

    interface = Interface(bid_market, control_input, control_output, bid_stream_1)
    interface.open_control_input()

    # print 'go'
    # print bid_market.top_bids(5, 3)
    # print 'no'
    # print bid_market.top_bids(4, 3)

    # print bid_market.bid_heap

if __name__ == "__main__":
    main()