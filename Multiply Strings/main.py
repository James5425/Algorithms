num1 = "2"
num2 = "3"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(f"{num1} * {num2}"))

print(Solution().multiply(num1, num2))

