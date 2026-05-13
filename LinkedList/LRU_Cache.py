def LRUCache(capacity):
    cache = {}
    order = []
    
    def get(key):
        if key in cache:
            order.remove(key)
            order.append(key)
            return cache[key]
        return -1
    
    def put(key, value):
        if key in cache:
            order.remove(key)
        elif len(cache) >= capacity:
            oldest_key = order.pop(0)
            del cache[oldest_key]
        
        cache[key] = value
        order.append(key)
    
    return get, put

if __name__ == "__main__":
    get, put = LRUCache(2)
    
    put(1, 1)
    put(2, 2)
    print(get(1))  # returns 1
    put(3, 3)      # evicts key 2
    print(get(2))  # returns -1 (not found)
    put(4, 4)      # evicts key 3
    print(get(3))  # returns -1 (not found)
    print(get(4))  # returns 4
    