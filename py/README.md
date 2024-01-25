# algorithm
algorithm
change

mit

git commit -m "find_list_cross_2" --date="Mar 31 23:59:59 2023 +0900"


git commit --allow-empty -m "yesterday" --date="Sep 13 10:59:59 2023 +0900"

## binary search
1. **Procedure:**
   - Start with the entire sorted array.
   - Compare the target value to the middle element of the array.
   - If the target is equal to the middle element, the search is successful.
   - If the target is less than the middle element, continue the search in the lower half of the array.
   - If the target is greater than the middle element, continue the search in the upper half of the array.
   - Repeat the process until the target is found or the search range becomes empty.

2. **Key Characteristics:**
   - The array must be sorted for binary search to be effective.
   - It is a divide-and-conquer algorithm that reduces the search space by half at each step.
   - The time complexity of binary search is O(log n), making it more efficient than linear search for large datasets.
