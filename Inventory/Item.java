package Inventory;

import World.Cell;
import World.Island;
import Hero.Hero;

public class Item {
    protected float strenght;
    protected int damageBy;
    protected int id;
    protected String translatePath;

    public float getStrenght() { return strenght; }
    public int getDamageBy() { return damageBy; }
    public int getId() { return id; }
    public String getTranslatePath() { return translatePath; }

    public void use(Hero hero) {

    }

    public void use(Cell useForCell, Island island) {
        
    }
}
