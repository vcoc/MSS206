package net.swordie.ms;

import net.swordie.ms.constants.GameConstants;
import net.swordie.ms.enums.WorldId;

/**
 * Created on 2/18/2017.
 */
public class ServerConfig {
    // World
    public static final WorldId WORLD_ID = WorldId.Scania;
    public static final String SERVER_NAME = "MapleStory";
    public static String[] WORLD_SELECTION_BACKGROUND = new String[] { // Backgrounds to be displayed at World Selection page.
            "SavageT", "adventurePathfinder", "uFarm"
    };

    // Message
    public static String SLIDE_MSG = "Welcome to MapleStory!!"; // Message that is shown at the top of in-game screen.
    public static String[] CS_SLIDE_MSG = { "Welcome to MapleStory!!", "Happy Mapling!!" }; // List of messages that is shown inside cash shop.
    public static String EVENT_MSG = getEventMsg(); // Message that is shown on channel selection.
    public static String RECOMMEND_MSG = "A Recommended Message."; // Message that is shown when viewing recommended.
    public static String BUFFED_CH_MSG = "Beware! You entered a buffed channel."; // Message that is shown when you enter a buffed channel.

    // Other
    public static final String HEAP_DUMP_DIR = "../heapdumps";

    public static String getEventMsg() {
        if (GameConstants.BUFFED_CH_ST == 0 && GameConstants.BUFFED_CH_END == 0) {
            return String.format("#b%s#k v%s.%s\r\nOnline Players:#b ", ServerConfig.SERVER_NAME, ServerConstants.VERSION,
                    ServerConstants.MINOR_VERSION);
        } else {
            return String.format("Buffed Channels: #b%d-%d#k\r\nOnline Players:#b ",
                    GameConstants.BUFFED_CH_ST, GameConstants.BUFFED_CH_END);
        }
    }
}
