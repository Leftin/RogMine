package World;

import java.util.Random;

public class Island {
    private Random random = new Random();
    private Cell[][][] board;
    private int width;
    private int height;
    private int length;

    Island(int width, int height, int length) {
        this.width = width;
        this.height = height;
        this.length = length;
        board = new Cell[height][length][width];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < length; j++) {
                for (int k = 0; k < width; k++) {
                    board[i][j][k] = CellFactory.createCellFromId(i==1 ? 1 : 0, k, i, j);
                }
            }
        }
    }

    private void generate() {

    }

    public int getlength() { return length; }
    public int getwidth() { return width; }
    public int getHeight() { return height; }
    public Cell[][][] getBoard() { return board; }

    public void update() {

        }
}
