class Codec:
    """
    Approach 1: Encode by ID
    time: O(n) for encode(), O(1) for decode()
    space: O(n) for encode(), O(1) for decode()
    """
    def __init__(self):
        self.database = {}
        self.url_to_id = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.url_to_id:
            self.id += 1
            self.database[self.id] = longUrl
            self.url_to_id[longUrl] = self.id
        return "http://tinyurl.com/" + str(self.url_to_id[longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        i = shortUrl.rfind('/')
        id = int(shortUrl[i+1:])
        return self.database[id]


class Codec:
    """
    Approach 2: Encode by Hashing
    time: O(n) for encode(), O(1) for decode()
    space: O(n) for encode(), O(1) for decode()
    """
    def __init__(self):
        self.database = {}
        self.url_to_key = {}
        self.K1, self.K2 = 1117, 10 ** 9 + 7
        self.prefix = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        # If the hash exists:
        if longUrl in self.url_to_key:
            return self.prefix + str(self.url_to_key[longUrl])

        # Calculate the hash value:
        key, base = 0, 1
        for c in longUrl:
            key = (key + ord(c) * base) % self.K2
            base = (base * self.K1) % self.K2

        # If hash collision:
        while key in self.database:
            key = (key + 1) % self.K2

        # Update hash tables:
        self.database[key] = longUrl
        self.url_to_key[longUrl] = key
        return self.prefix + str(key)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        i = shortUrl.rfind('/')
        key = int(shortUrl[i+1:])
        return self.database[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
