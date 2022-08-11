package net.swordie.ms;

import net.swordie.ms.enums.WorldId;

/**
 * Created on 2/18/2017.
 */
public class ServerConfig {
    public static final int USER_LIMIT = 20;
    public static final WorldId WORLD_ID = WorldId.Scania;
    public static final String SERVER_NAME = "MapleStory";
    public static String SLIDE_MSG = "Welcome to MapleStory!!";
    public static String[] CS_SLIDE_MSG = {"Welcome to MapleStory!!", "Happy Mapling!!"};
    public static final String EVENT_MSG = String.format("Buffed Channels 6-10\r\nOnline Players: ");
    public static final String RECOMMEND_MSG = "";
    public static final int MAX_CHARACTERS = 30;
    public static final String HEAP_DUMP_DIR = "../heapdumps";
}