from collections import Counter
class Encoding:
    def __init__(self,message):
        self.message = message
        self.encoded = self.Huffman(message)
    def Huffman(self,message):
        self.count = Counter(message)
        def code():
            

if __name__ == "__main__":
    Encoder = Encoding("ACBD")
    
