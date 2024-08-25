package GUI;

import Inventory.ItemFactory;
import Translate.Translate;
import World.Cell;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

public class Render extends JPanel {

    private Translate translate = new Translate();
    private Tileset tileset = new Tileset();
    private BufferedBoard bufferedBoard;

    private int cursorX=-1;
    private int cursorY=-1;

    Render() {
        this.setBackground(new Color(66, 103, 34));
        this.setFocusable(true);
        this.addMouseMotionListener(new MyMouseMotionAdapter());
    }

    public void setBufferedBoard(BufferedBoard bufferedBoard) {
        this.bufferedBoard = bufferedBoard;
    }

    public void setTileset(String path) {
        tileset.loadTileSet(path);
    }

    public void setTranslate(String path) {
        translate.loadTranslate(path);
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        paintBoard(g);
        paintLeftPanel(g);
    }

    protected void paintBoard(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        int boardHeight = bufferedBoard.getBoardOnPlayerY().length;
        int boardwidth = bufferedBoard.getBoardOnPlayerY()[0].length;
        if(boardHeight > ((int) this.getSize().height/tileset.getHeightOfSprite()+1)) boardHeight = (int) this.getSize().height/tileset.getHeightOfSprite()+1;
        if(boardwidth > ((int) this.getSize().width/tileset.getHeightOfSprite()+1)) boardwidth = (int) this.getSize().width/tileset.getwidthOfSprite()+1;

        for (int i = 0; i < boardHeight; i++) {
            for (int j = 0; j < boardwidth; j++) {
                g2.drawImage(tileset.getSprite(bufferedBoard.getTexturesUnderPlayer()[i][j]), null, 120+j*tileset.getwidthOfSprite(), i*tileset.getHeightOfSprite());
                g2.drawImage(tileset.getSprite(bufferedBoard.getBoardOnPlayerY()[i][j].getSpriteName()), null, 120+j*tileset.getwidthOfSprite(), i*tileset.getHeightOfSprite());
            }
        }
        g2.drawImage(tileset.getSprite("hero"), null, 120+bufferedBoard.getX()*tileset.getwidthOfSprite(), bufferedBoard.getZ()*tileset.getHeightOfSprite());

    }

    protected void paintLeftPanel(Graphics g) {
        g.setColor(new Color(35, 35, 35));
        g.fillRect(0, 0, 120, this.getHeight());
        if(cursorX == -1) return;
        g.setColor(Color.WHITE);
        Cell currentCell = bufferedBoard.getBoardOnPlayerY()[cursorY][cursorX];
        int x = 10;
        int y = 15;
        y = paintString(g, translate.getTranslate(currentCell.getTranslateName() + ".name"), 10, y, 15);
        y += 20;
        y = paintString(g, translate.getTranslate(currentCell.getTranslateName() + ".description"), 10, y, 15);
        y += 30;
        y = paintString(g, translate.getTranslate("about.hitbox") + (currentCell.getHitbox() ? translate.getTranslate("true") : translate.getTranslate("false")), x, y, 15);
        y += 15;
        y = paintString(g, translate.getTranslate("about.health") + currentCell.getHealth(), x, y, 15);
        y += 15;
        y = paintString(g, translate.getTranslate("about.conductivity") + currentCell.getConductivity(), x, y, 15);
        y += 15;
        y = paintString(g, translate.getTranslate("about.drop"), x, y, 15);

        for(int id : currentCell.getDrop()) {
            paintString(g, translate.getTranslate(ItemFactory.createItemFromId(id).getTranslatePath() + ".name"), x, y, 10);
            y += 12;
        }
        y+=15;
        y = paintString(g, translate.getTranslate("about.breakDamageBy"), x, y, 15);
        for(int material : currentCell.getBreakDamageBy())
        {
            paintString(g, translate.getTranslate("material." + material), x, y, 10);
            y += 12;
        }
        y+=15;
        if((cursorX == bufferedBoard.getX()) && (cursorY == bufferedBoard.getZ())) y = paintString(g, translate.getTranslate("about.you"), x, y, 10);
    }

    private static int paintString(Graphics g, String string, int x, int y, int indent) {
        int deep=0;
        for(String s : string.split("\n")) {
            g.drawString(s, x, y+deep);
            y+=indent;
        }
        return y+deep;
    }

    class MyMouseMotionAdapter extends MouseMotionAdapter {
        @Override
        public void mouseMoved(MouseEvent e) {
            super.mouseMoved(e);
            if(e.getX() < 120) {
                cursorX=-1;
                cursorY=-1;
            } else {
                cursorX = (int) (e.getX()-120) / tileset.getHeightOfSprite();
                cursorY = (int) e.getY() / tileset.getwidthOfSprite();
            }
            repaint();
        }
    }
}
