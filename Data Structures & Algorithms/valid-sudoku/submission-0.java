

class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < 9; i++ ) {
            char[] row = board[i];
            HashSet<Character> rowSet = new HashSet<>();
            for (int j = 0; j<9; j++) {
                if (row[j] != '.') {
                    if(rowSet.contains(row[j])) {
                        return false;
                    }
                    rowSet.add(row[j]);
                }
            }
        }

        for(int i = 0; i < 9; i++ ) {
            HashSet<Character> colSet = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                char currVal = board[j][i];
                if (currVal != '.') {
                    if (colSet.contains(currVal)) {
                        return false;
                    }
                    colSet.add(currVal);
                }
            }
        }

        HashSet<Character>[] boxes = new HashSet[9];
        for (int i = 0; i < 9; i++) {
            boxes[i] = new HashSet<>();
        }


        for (int i = 0; i <9; i++) {
            for (int j = 0; j <9; j++) {
                char currVal = board[i][j];
                if (currVal != '.') {
                    int boxIndex = (i/3) * 3 + (j/3);
                    if (boxes[boxIndex].contains(currVal)) {
                        return false;
                    }
                    boxes[boxIndex].add(currVal);
                }
                
            }
        }
        return true;
    }
}
