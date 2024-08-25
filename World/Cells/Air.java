package World.Cells;

import World.Cell;

public class Air extends Cell {

    {
        hitbox = false;
        breakDamageBy = new int[]{};
        drop = new int[]{};
        health = 0;
        conductivity = 0;
        spriteName = "cell.air";
        translateName = "cell.air";
    }

    public Air(int x, int y, int z)
    {
        super.start(x, y, z);
    }

}
