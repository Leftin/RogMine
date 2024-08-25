package Game;

import GUI.GameFrame;
import Hero.Hero;
import Translate.Translate;
import World.World;

public class Game {
    private World world;
    private GameFrame frame;
    private Hero hero;

    public Game() {
        Hero hero = new Hero();
        World world = new World(16, 16, 32, 32, 32);
        GameFrame frame = new GameFrame(world.getBoard()[0][0], hero, "language/ru.txt", "tilesets/default");
    }

}
