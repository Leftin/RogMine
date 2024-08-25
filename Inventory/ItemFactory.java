package Inventory;

import Inventory.items.Tree;

public class ItemFactory {

    public static Item createItemFromId(int id)
    {
        switch (id) {
            case 0:
                return new Tree();
            default:
                return new Tree();
        }
    }

}
