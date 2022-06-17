"""file contains Hashmap ADT"""


class ChainingHashTableItem:
    """initialized (key, value) pairs"""

    def __init__(self, item_key, item_value):
        self.key = item_key
        self.value = item_value
        self.next = None

    def __str__(self):
        """prints the (key, value) pairs"""
        return str(self.key) + " " + str(self.value)


class HashMap:
    """Hashmap ADT being test"""

    def hash_key(self, key):
        """Return the value for key if key is in the dictionary.
        If key is not in the dictionary, raise a KeyError."""
        r_val = 2
        sum_of_parts = key[0] + key[1]
        squared_key = sum_of_parts * sum_of_parts

        low_bits_to_remove = (32 - r_val) // 2
        extracted_bits = squared_key >> low_bits_to_remove
        extracted_bits = extracted_bits & (0xFFFFFFFF >> (32 - r_val))
        return extracted_bits % len(self.table)

    def __init__(self, initial_capacity=7):
        """initialized capacity"""
        self.table = [None] * initial_capacity

    def __str__(self):
        for item in self.table:
            if item is not None:
                while item is not None:
                    print(item)
                    item = item.next
            else:
                print("(empty")
        return " "

    def set(self, key, value):
        """inserts a (key,value) pair to the Hashmap"""
        initial_capacity = self.capacity()
        initial_size = self.size()
        load_factor = initial_size / initial_capacity

        while load_factor >= .8:
            print(f"load factor {load_factor}")
            self.resize_hash()
            initial_capacity = self.capacity()
            initial_size = self.size()
            load_factor = initial_size / initial_capacity

        bucket_index = self.hash_key(key) % len(self.table)

        item = self.table[bucket_index]
        previous = None
        while item is not None:
            if key == item.key:
                item.value = value
                return True

            previous = item
            item = item.next

        if self.table[bucket_index] is None:
            self.table[bucket_index] = ChainingHashTableItem(key, value)
        else:
            previous.next = ChainingHashTableItem(key, value)
        return True

    def remove(self, key):
        """removes key from the Hashtable"""
        bucket_index = self.hash_key(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        if item is None:
            raise KeyError("KeyError exception thrown")
        else:
            previous = None
            while item is not None:
                if key == item.key:
                    if previous is None:
                        self.table[bucket_index] = item.next
                    else:
                        previous.next = item.next
                    return True
                previous = item
                item = item.next
            return False

    def search(self, key):
        """Return the value for key if key is in the dictionary."""

        bucket_index = self.hash_key(key) % len(self.table)
        item = self.table[bucket_index]
        while item is not None:
            if key == item.key:
                return item.value
            item = item.next
        return None

    def get(self, key):
        """Return the value for key if key is in the dictionary."""
        a_value = self.search(key)
        if a_value is None:
            raise KeyError("KeyError exception thrown")

        return a_value

    def clear(self):
        """Empties all contents of Hashmap"""
        self.__init__()

    def capacity(self):
        """Returns the current number of buckets"""
        capacity = len(self.table)
        return capacity

    def size(self):
        """Returns the number of (key, value) pairs"""
        size = len(self.keys())
        return size

    def keys(self):
        """Returns the list of keys"""
        keys_list = []
        for item in self.table:
            if item is not None:
                while item is not None:
                    keys_list.append(item.key)
                    item = item.next
        return keys_list

    def values(self):
        """Returns a list of values"""
        value_list = []
        for item in self.table:
            if item is not None:
                while item is not None:
                    value_list.append(item.value)
                    item = item.next
        return value_list

    def resize_hash(self):
        """routine called by set if hashtable needs to be larger. (2k-1)"""
        resized_capacity = 2 * self.capacity() - 1
        list_of_keys = self.keys()
        list_of_values = self.values()

        self.__init__(resized_capacity)
        for i in range(len(list_of_keys)):
            self.set(list_of_keys[i], list_of_values[i])
        return self
