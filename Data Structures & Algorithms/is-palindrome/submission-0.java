class Solution {
    public boolean isPalindrome(String s) {
        String alnumstr = s.replaceAll("[^a-zA-Z0-9]", "");
        alnumstr = alnumstr.toLowerCase();
        for(int i = 0; i < alnumstr.length() / 2; i++) {
            char front = alnumstr.charAt(i);
            char back = alnumstr.charAt(alnumstr.length() - i - 1);
            if(front != back) {
                return false;
            }
        }
        return true;
    }
}
