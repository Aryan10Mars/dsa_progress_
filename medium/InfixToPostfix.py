class Solution:
    def InfixtoPostfix(self, exp):
        precedence = {
            '^' : 3,
            '*' : 2,
            '/' : 2,
            '+' : 1,
            '-' : 1,
            '(' : 0,
            ')' : 0
        }
        ans = ""
        st = []
        
        for i in exp:
            if i.isalpha() or i.isdigit():
                ans = ans + i
                
            elif i is '(':
                st.append('(')
            
            elif i is ')':
                while st[-1] is not '(':
                    ans = ans + st[-1]
                    st.pop()
                st.pop()
                
            else:
                while st and precedence[st[-1]] >= precedence[i]:
                    ans = ans + st[-1]
                    st.pop()
                st.append(i)
            
        while st:
            ans = ans + st[-1]
            st.pop()
        
        return ans