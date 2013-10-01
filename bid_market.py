import heapq

# min heap with negative numbers
# heapq.heapify(history_data)

class BidMarket:
    def __init__(self, history):
        self.history = history
        self.bid_heap = []
        heapq.heapify(self.bid_heap)
        self.import_history()

    def import_history(self):
        history_file = open(self.history)

        for line in history_file:
            heapq.heappush(self.bid_heap, -1*int(line.strip()))
        history_file.close()

    def top_bids(self, total_bids, requested_bids):
        if len(self.bid_heap) == total_bids:
            return heapq.nsmallest(requested_bids, self.bid_heap)
        else:
            print "old data"
            return False

# remove from heap, add them back
# print heapq.nsmallest(3, bid_heap)

# while bid_heap:
#     print -1*heapq.heappop(bid_heap)