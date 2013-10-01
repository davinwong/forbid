import sys
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

    interface = Interface(
        bid_market,
        control_input,
        control_output,
        bid_stream_1)

    interface.open_control_input()

if __name__ == "__main__":
    main()
