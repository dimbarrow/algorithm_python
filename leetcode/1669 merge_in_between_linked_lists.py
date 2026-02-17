class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        current = list1

        for i in range (a - 1):
            current = current.next
        current2 = current.next

        for i in range (b - a + 1):
            current2 = current2.next
        current.next = list2

        while current.next:
            current = current.next
        current.next = current2

        return list1