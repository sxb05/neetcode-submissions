class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            # Find the '#'
            j = i

            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move past '#'
            i = j + 1

            # Extract the string
            result.append(s[i:i + length])

            # Move to next encoded string
            i = i + length

        return result
