import unittest

class Test(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 0, 4, 3), 2)
    def test_neg(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 0, 4, 6), None)
        
def search(arr, low, high, key):
    if(low <= high):
        mid = (low + high) / 2
        if(key == arr[mid]):
            print "Value", key, "found at position", mid
            return mid
        elif(key < arr[mid]):
            return search(arr, low, mid - 1, key)
        else:
            return search(arr, mid + 1, high, key)
    print "Value", key, "not found"

arr = []
with open("input.txt", "r") as f:
    for num in f:
        arr.append(int(num))
        
print "Unsorted array: ", arr
arr.sort()
print "Sorted array: ", arr
key = input("Enter key to be searched: ")
search(arr, 0, len(arr) - 1, key)
print "Unit testing: "
unittest.main()