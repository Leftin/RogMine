package GUI;

import World.Cell;
import World.Island;

public class BufferedBoard {
    private Cell[][] boardOnPlayerY;
    private String[][] texturesUnderPlayer;
    private int x;
    private int z;

    BufferedBoard(Cell[][] boardOnPlayerY, String[][] texturesUnderPlayer, int x, int z) {
        this.boardOnPlayerY = boardOnPlayerY;
        this.texturesUnderPlayer = texturesUnderPlayer;
        this.x = x;
        this.z = z;
    }

    public static BufferedBoard BufferedBoardFromIsland(Island island, int x, int y, int z) {
        String[][] texturesUnderPlayer = new String[island.getlength()][island.getwidth()];
        if(island.getHeight() == y) texturesUnderPlayer = new String[][]{};
        else {
            for (int i = 0; i < island.getlength(); i++) {
                for (int j = 0; j < island.getwidth(); j++) {
                    texturesUnderPlayer[i][j] = island.getBoard()[y + 1][i][j].getSpriteName() + ".above";
                }
            }
        }
        return new BufferedBoard(island.getBoard()[y], texturesUnderPlayer, x, z);
    }

    public Cell[][] getBoardOnPlayerY() { return boardOnPlayerY; }
    public String[][] getTexturesUnderPlayer() { return texturesUnderPlayer; }
    public int getX() { return x; }
    public int getZ() { return z; }

}
