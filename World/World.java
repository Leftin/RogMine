package World;

public class World {
    private Island[][] board;
    private int wight;
    private int height;
    private int wightIsland;
    private int heightIsland;

    public World(int wight, int height, int wightIsland, int heightIsland, int lenghtIsland) {
        if(wight > 32) wight = 32;
        if(height > 32) height = 32;
        if(wightIsland > 255) wightIsland = 255;
        if(heightIsland > 255) heightIsland = 255;
        if(lenghtIsland > 255) lenghtIsland = 255;

        board = new Island[height][wight];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < wight; j++) {
                board[i][j] = new Island(wightIsland, heightIsland, lenghtIsland);
            }
        }
        this.wight = wight;
        this.height = height;
    }

    public void update() {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < wight; j++) {

            }
        }
    }

    public Island[][] getBoard() {
        return board;
    }
    public int getWight() {
        return wight;
    }
    public int getHeight() {
        return height;
    }
}
