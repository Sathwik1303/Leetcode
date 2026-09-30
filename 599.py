#MINIMUM INDEX SUM OF TWO LISTS

class Solution(object):
    def findRestaurant(self, list1, list2):
        new=[]
        count=None
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if (count is None) or (count==i+j):
                        count=i+j
                        new.append(list1[i])
                    elif count>i+j:
                        count=i+j
                        new=[list1[i]]
        return new                