forbid
======

forbid uses synchronized multithreading (lock) to collect data from four bid streams, then completes requests to display the top bids. 

`python forbid.py history.txt input.txt output.txt bid1.txt bid2.txt bid3.txt bid4.txt`

View top bids: Add a new line containing `top 5 4` (top 4 bids of 5 total) to input.txt and save.

Add bid: Add a new line containing a number to bid1.txt and save.

Code challenge: http://codercharts.com/puzzle/high-speed-trading

Collaborate: @sumanyu

## maxheap
### time complexity
- access top m bids O(logn) for reasonable m
- add bid O(logn)

The most common operations in this problem are adding new data and retrieving the top bids. The largest numbers are accessed frequently. Maxheap is efficient because it can retrieve the top bids in O(logn) time, and add in O(logn).

Retrieving top bids from a sorted array would be O(1), but keeping a sorted array could be more expensive because adding a new value requires finding the correct position for it, looping through the array in O(n). 

Using a hash table would add in O(1), but would require looping through the entire set to find the top bids, O(n).

### space complexity
- O(n), all data stored in memory

## done
- read history
- heap
- find top bids
- take input command
- receive bid numbers, add to heap
- thread multiple input files
- ~synchronization

## todo
- send to output control
- if not enough data, wait then send

## assumptions
- finish receiving history before dealing with commands