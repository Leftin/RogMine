package World;

import java.util.Random;

public class Island {
    private Random random = new Random();
    private Cell[][][] board;
    private int wight;
    private int height;
    private int lenght;

    Island(int wight, int height, int lenght) {
        this.wight = wight;
        this.height = height;
        this.lenght = lenght;
        board = new Cell[height][lenght][wight];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < lenght; j++) {
                for (int k = 0; k < wight; k++) {
                    board[i][j][k] = CellFactory.createCellFromId(random.nextInt(2), k, i, j);
                }
            }
        }
    }

    private void generate() {

    }

    public int getLenght() { return lenght; }
    public int getWight() { return wight; }
    public int getHeight() { return height; }
    public Cell[][][] getBoard() { return board; }

    public void update() {

        }
}
