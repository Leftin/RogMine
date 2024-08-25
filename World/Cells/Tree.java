package World.Cells;

import World.Cell;

public class Tree extends Cell {

    {
        hitbox = true;
        breakDamageBy = new int[]{0, 1};
        drop = new int[]{1, 1, 1};
        health = 3;
        conductivity = 0;
        spriteName = "cell.tree";
        translateName = "cell.tree";
    }

    public Tree(int x, int y, int z)
    {
        super.start(x, y, z);
    }

}
