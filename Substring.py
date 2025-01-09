class KMP:
    def __init__(self,text,pattern):
        self.kmp(pattern,text)
    def kmp(self,pattern,text):
        j = 0
        i = 1
        temp_array=[0]*len(pattern)
        while j < i and i < len(pattern):
            if pattern[i] != pattern[j] and j > 0:
                j = temp_array[j-1]
                continue
            if pattern[i] == pattern[j]:
                temp_array[i] = j+1
                i += 1
                j += 1
                continue
            i += 1
    
        i = 0
        j = 0
        ans = -1
        while i < len(text) and j < len(pattern):
            if text[i] == pattern[j]:
                ans = i-j
                i += 1
                j += 1
            if text[i] != pattern[j]:
                if j > 0:
                    j = temp_array[j-1]
                else:
                    i += 1
        return ans

if __name__ == "__main__":
    text = "abdeabcf"
    pattern = "abcasd"
    print(KMP(pattern,text))
    
