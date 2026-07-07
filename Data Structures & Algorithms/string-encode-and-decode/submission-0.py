class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        parts = []
        for i in range(len(strs)):
            parts.append(str(len(strs[i])))
            parts.append('#')
            parts.append(strs[i])

        encoded_str = "".join(parts)
        
        
        return encoded_str



    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded_list = []
        i = 0
        while i < len(s):
            
            translator = ""
            length = 0
            while s[i] != '#':
                translator += s[i]
                i += 1
            
            length = int(translator)
            translator = ""
            i += 1

            while length:   
                translator += s[i]
                i += 1
                length -= 1

            decoded_list.append(translator)
            
        return decoded_list


        
