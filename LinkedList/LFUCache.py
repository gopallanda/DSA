def LFUCache(capacity):
    cache = {}
    freq = {}
    min_freq = 0

    def get(key):
        nonlocal min_freq
        if key not in cache:
            return -1
        value, freq_count = cache[key]
        freq_count += 1
        cache[key] = (value, freq_count)
        if freq_count - 1 in freq:
            freq[freq_count - 1].remove(key)
            if not freq[freq_count - 1]:
                del freq[freq_count - 1]
                if min_freq == freq_count - 1:
                    min_freq += 1
        if freq_count not in freq:
            freq[freq_count] = set()
        freq[freq_count].add(key)
        return value

    def put(key, value):
        nonlocal min_freq
        if capacity <= 0:
            return
        if key in cache:
            cache[key] = (value, cache[key][1])
            get(key)  # Update frequency
            return
        if len(cache) >= capacity:
            evict_key = next(iter(freq[min_freq]))
            freq[min_freq].remove(evict_key)
            if not freq[min_freq]:
                del freq[min_freq]
            del cache[evict_key]
        cache[key] = (value, 1)
        if 1 not in freq:
            freq[1] = set()
        freq[1].add(key)
        min_freq = 1

    return get, put 
if __name__ == "__main__":
    get, put = LFUCache(2)
    
    put(1, 1)
    put(2, 2)
    print(get(1))  # returns 1
    put(3, 3)      # evicts key 2
    print(get(2))  # returns -1 (not found)
    put(4, 4)      # evicts key 3
    print(get(3))  # returns -1 (not found)
    print(get(4))  # returns 4