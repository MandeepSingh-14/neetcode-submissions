class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if s[0]==')' or s[0] == ']' or s[0] == '}':
            return False

        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if not st:
                    return False

                if ch == ')' and st[-1] != '(':
                    return False
                if ch == ']' and st[-1] != '[':
                    return False
                if ch == '}' and st[-1] != '{':
                    return False

                st.pop()

        return len(st) == 0