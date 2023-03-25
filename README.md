# Cache-using-Python

## **The cache memory operates in the following manner:**

When a page from memory is requested, the cache memory is searched for that page

- if the page is found in the cache memory, then this is called a "hit"
- if the page is not found in the cache memory, then this is called a "miss". When the miss happens, the page must be retrieved for the main memoory. If the cache memory is not full, then the page is simply added. If it's full, one of the pages in the cache memory is replaced.

There are multiple ways in which we can choose which page to replace from the cache. Two of these methods are ["First in First Out (FIFO)"](#first-in-first-out-fifo) algorithm and ["Least Frequently Used (LFU)"](#least-frequently-used-lfu) algorithm.

## First in First Out (FIFO)

In First in First Out (FIFO) cache memory, the new page is replaced with the one that has the longest time since it was added.

## Least Frequently Used (LFU)

In Least Frequently Used (LFU) cache memory, the new page is replaced with the one that had the fewest requests so far. In case of two pages having the same amount of requests, the lowest numbered page should be replaced. The number of requests that a page has had is maintained throughout the parsing of the whole set of requests, and it is not "forgotten" once a page has been removed from the cache memory.

## Specifics:

In this exercise, we will assume that:

- every page is represented by a positive integer.
- the capacity of the cache memory is 8 pages.

In particular, a request for a page will be indicated by a number, e.g., the number 3 means that we request page 3. If the requested page is in the cache memory, then this will be a hit. If the requested page is not in the cache memory, then this will be a miss. In this latter case, the page has to be retrieved from the main memory and placed into the cache memory. If the cache memory is not full (i.e., it has fewer than 8 pages already in it), then we can simply add the requested page to the cache memory. If the cache memory is full (meaning that it has exactly 8 pages in in), then we have to replace one page already in the cache memory, in order to bring the newly requested page in. Which page to replace is decided based on one of the two algorithms above, FIFO or LFU
