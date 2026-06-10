class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length-1;
        int back = numbers[j];
        int front = numbers[i];
        int[] sol = new int[2];
        
        boolean found = false;
        while (!found) {
            if (back + front > target) {
                j--;
            } else {
                if (back + front < target) {
                i++;
                } else {
                    sol = new int[]{i+1, j+1};
                    found = true;
                }
            }
            back = numbers[j];
            front = numbers[i];
        }
        return sol;
    }
}
