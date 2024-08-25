package GUI;

import World.Island;
import Hero.Hero;

import javax.swing.*;

public class GameFrame extends JFrame {

    Render render = new Render();

    public GameFrame(Island island, Hero hero, String pathToTranslate, String pathToTileset)
    {
        updateBoardOnScreen(island, hero);
        updateTileset(pathToTileset);
        updateTranslate(pathToTranslate);

        this.setTitle("RogMine");
        this.add(render);
        this.setSize(500, 500);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null);
    }

    public void updateBoardOnScreen(Island island, Hero hero) {
        render.setBufferedBoard(BufferedBoard.BufferedBoardFromIsland(island, hero.getX(), hero.getY(), hero.getZ()));
    }

    public void updateTranslate(String path) {
        render.setTranslate(path);
    }

    public void updateTileset(String path) {
        render.setTileset(path);
    }


}
