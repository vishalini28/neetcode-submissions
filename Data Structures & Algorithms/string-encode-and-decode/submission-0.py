class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Format: length + delimiter + string
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        res = []
        i = 0  # Pointer to track our position in the string
        
        while i < len(s):
            # 1. Find the delimiter '#' starting from index i
            j = s.find('#', i)
            
            # 2. Extract the length of the upcoming string
            length = int(s[i:j])
            
            # 3. Extract the string itself using the length
            start_of_str = j + 1
            end_of_str = start_of_str + length
            res.append(s[start_of_str:end_of_str])
            
            # 4. Move pointer to the start of the next encoded block
            i = end_of_str
            
        return res


