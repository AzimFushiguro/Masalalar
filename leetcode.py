#136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
         result ^= num
        return result
#58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       text = s.split()
       t =  text[-1]
       return len(t)
#66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        ls = str(digits[-1])
        digits.pop()
        for lists in ls:
            ints = int(lists)
            digits.append(ints)
        return digits
# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = haystack.find(needle)
        return a

# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lists = []

        for i in nums:
            if target in nums:
                return nums.index(target)
                break
            elif target is not nums:
                lists.append(i)

        else:
            lists.append(target)
            lists.sort()
            return lists.index(target)

# 67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
         return bin(int(a, 2) + int(b, 2))[2:]
# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            candidate = None
            count = 0

            for num in nums:
                if count == 0:
                    candidate = num
                count += (1 if num == candidate else -1)

            return candidate

# 203. Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to simplify the code
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
