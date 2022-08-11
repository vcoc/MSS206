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

    // Message
    public static String SLIDE_MSG = "Welcome to MapleStory!!"; // Message that is shown at the top of in-game screen.
    public static String[] CS_SLIDE_MSG = {"Welcome to MapleStory!!", "Happy Mapling!!"}; // Message that is shown inside cash shop.
    public static String EVENT_MSG = String.format("Buffed Channels: %d-%d\r\nOnline Players: ",
            GameConstants.BUFFED_CH_ST, GameConstants.BUFFED_CH_END); // Message that is shown on channel selection.
    public static String RECOMMEND_MSG = "A Recommended Message."; // Message that is shown when viewing recommended.
    public static String BUFFED_CH_MSG = "Beware! You entered a buffed channel."; // Message that is shown when you enter a buffed channel.

    // Other
    public static final String HEAP_DUMP_DIR = "../heapdumps";
}