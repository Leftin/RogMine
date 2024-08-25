package World;

import World.Cells.Air;
import World.Cells.Tree;

public class CellFactory {

    public static Cell createCellFromId(int id, int x, int y, int z)
    {
        switch (id)
        {
            case 0:
                return new Air(x, y, z);
            case 1:
                return new Tree(x, y, z);
            default:
                return new Air(x, y, z);
        }
    }

}
