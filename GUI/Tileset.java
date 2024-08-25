package GUI;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.*;
import java.util.HashMap;

public class Tileset {
    private File tilesetImage;
    private HashMap<String, String> tilesetsValues = new HashMap<String, String>();
    private HashMap<String, BufferedImage> cache = new HashMap<String, BufferedImage>();

    public void loadTileSet(String path) {
        try {
            tilesetImage = new File(path, "tileset.png");
            BufferedReader reader = new BufferedReader(new FileReader(path + "/settings.txt"));
            String line = reader.readLine();
            do {
                // skip commentary and empty lines
                if((line.toCharArray().length == 0) || (line.toCharArray()[0] == '/')) {
                    line = reader.readLine();
                    continue;
                }
                // load settings and name of sprites
                tilesetsValues.put(line.split("=")[0], line.split("=")[1]);
                line = reader.readLine();
            } while (line != null);

        } catch (IOException e) {
            throw new RuntimeException("File \"settings.txt\"does not exist");
        }
    }

    public BufferedImage getSprite(String nameOfSprite)
    {
        // If exist in cache take in cache
        if(cache.containsKey(nameOfSprite)) return cache.get(nameOfSprite);

        String nameOfSpriteOriginally = nameOfSprite;

        // width and height dont be a sprite, this is settings
        if((nameOfSprite.equals("width")) || (nameOfSprite.equals("height")))
            throw new RuntimeException("Incorrect sprite name");

        // If dont have sprite go to parent and again
        while(!tilesetsValues.containsKey(nameOfSprite))
        {
            String[] namesTreeNameSprite = nameOfSprite.split("\\.");
            if(namesTreeNameSprite.length-1 == 0) throw new RuntimeException("Incorrect sprite name");
            nameOfSprite = "";
            // concatenate string without last string
            for (int i = 0; i < namesTreeNameSprite.length-1; i++) {
                nameOfSprite = nameOfSprite + (i==0 ? "" : ".") + namesTreeNameSprite[i];
            }
        }

        int x = Integer.valueOf(tilesetsValues.get(nameOfSprite).split(",")[0]);
        int y = Integer.valueOf(tilesetsValues.get(nameOfSprite).split(",")[1]);
        int width = Integer.valueOf(tilesetsValues.get("width"));
        int height = Integer.valueOf(tilesetsValues.get("height"));

        // Crop image and add to cache
        try {
            BufferedImage sprite = ImageIO.read(tilesetImage).getSubimage(x*width, y*height, width, height);
            cache.put(nameOfSpriteOriginally, sprite);
            System.out.println("New position in cache: " + nameOfSpriteOriginally);
            return sprite;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public int getwidthOfSprite() { return Integer.valueOf(tilesetsValues.get("width")); }
    public int getHeightOfSprite() { return Integer.valueOf(tilesetsValues.get("height")); }

}
