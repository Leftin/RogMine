package World;

public class Cell {
    protected int x;
    protected int y;
    protected int z;
    protected boolean hitbox;
    protected int[] breakDamageBy;
    protected int[] drop;
    protected float health;
    protected float conductivity;
    protected String spriteName;
    protected String translateName;

    public void update() {
        System.out.print("Hello, World!");
    }

    protected void start(int x, int y, int z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public int getX() { return x; }
    public int getY() { return y; }
    public boolean getHitbox() { return hitbox; }
    public int[] getBreakDamageBy() { return breakDamageBy; }
    public int[] getDrop() { return drop; }
    public float getHealth() { return health; }
    public String getSpriteName() { return spriteName; }
    public String getTranslateName() { return translateName; }
    public float getConductivity() { return conductivity; }
}
