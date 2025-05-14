class Solution(object):
    def addBinary(self, a, b):
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        return ''.join(reversed(result))