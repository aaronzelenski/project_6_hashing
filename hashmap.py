class HashMap:
    def hash_key(self, key):
        return abs(hash(key))
