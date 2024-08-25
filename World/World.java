package World;

public class World {
    private Island[][] board;
    private int width;
    private int height;
    private int widthIsland;
    private int heightIsland;

    public World(int width, int height, int widthIsland, int heightIsland, int lengthIsland) {
        if(width > 32) width = 32;
        if(height > 32) height = 32;
        if(widthIsland > 255) widthIsland = 255;
        if(heightIsland > 255) heightIsland = 255;
        if(lengthIsland > 255) lengthIsland = 255;

        board = new Island[height][width];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                board[i][j] = new Island(widthIsland, heightIsland, lengthIsland);
            }
        }
        this.width = width;
        this.height = height;
    }

    public void update() {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {

            }
        }
    }

    public Island[][] getBoard() {
        return board;
    }
    public int getwidth() {
        return width;
    }
    public int getHeight() {
        return height;
    }
}
