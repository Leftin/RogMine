package Translate;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class Translate {
    private HashMap<String, String> translate = new HashMap<String, String>();

    public void loadTranslate(String path) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();
            do {
                // skip commentary and empty lines
                if((line.toCharArray().length == 0) || (line.toCharArray()[0] == '/')) {
                    line = reader.readLine();
                    continue;
                }
                // load translate
                translate.put(line.split("=")[0], line.split("=")[1].replace("\\n", "\n"));
                line = reader.readLine();
            } while (line != null);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public String getTranslate(String keyOfTranlate) {
        if(translate.containsKey(keyOfTranlate)) return translate.get(keyOfTranlate);
        return keyOfTranlate;
    }

}
