class Solution:
    def countAndSay(self, n: int) -> str:
        
        cas = "1"

        for _ in range(n - 1):

            res = ""
            count = 1

            for i in range(1, len(cas)):

                if cas[i] == cas[i - 1]:
                    count += 1

                else:
                    res += str(count) + cas[i - 1]
                    count = 1

            # add last group
            res += str(count) + cas[-1]

            cas = res

        return cas
