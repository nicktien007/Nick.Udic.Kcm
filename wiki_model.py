class Content:
    def __init__(self, key1, key2):
        # self.key = key
        # self.key1 = self.key[0, self.key.find("/")]
        self.key1 = key1
        self.key2 = key2
        self.count = 1
    def __repr__(self):
        return "【"+self.key1+"】" +"【"+ self.key2 +"】"+ ",S=" + str(self.count)

