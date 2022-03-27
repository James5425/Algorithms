l1 = [9]
l2 = [9]


def Add(l1, l2):
    final = []

    if len(l1) == 1:
        if len(l2) == 1:
            final.append(l1[0] + l2[0])
            return final
        else:
            pass
    else:
        pass

    strings = [str(integer) for integer in l1]
    a_string = "".join(strings)
    an_integer = str(a_string)

    strings1 = [str(integer) for integer in l2]
    a_string1 = "".join(strings1)
    an_integer1 = str(a_string1)

    an_integer = int(an_integer[::-1])
    an_integer1 = int(an_integer1[::-1])

    combine = an_integer + an_integer1
    combine = str(combine)
    combine = (combine[::-1])

    for x in combine:
        final.append(int(x))

    return final


print(Add(l1, l2))

"""

Because LeetCode is fucked and uses ListNode we need to use this code however with a normal array the code above works works.

head = l1
        
        carry, l1.val = divmod(l1.val + l2.val, 10)
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            carry, l1.val = divmod(l1.val + l2.val + carry, 10)
        
        if l2.next:
            l1.next = l2.next
        
        while l1.next:
            l1 = l1.next
            carry, l1.val = divmod(l1.val + carry, 10)
        
        if carry:
            l1.next = ListNode(carry)
        
        return head

"""
