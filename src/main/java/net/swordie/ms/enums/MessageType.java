package net.swordie.ms.enums;

import net.swordie.ms.util.Util;

/**
 * Created on 1/25/2018.
 */
public enum MessageType {
    DROP_PICKUP_MESSAGE(0),
    QUEST_RECORD_MESSAGE(1),
    QUEST_RECORD_MESSAGE_ADD_VALID_CHECK(2),
    CASH_ITEM_EXPIRE_MESSAGE(3),
    INC_EXP_MESSAGE(4),
    INC_SP_MESSAGE(5),
    INC_POP_MESSAGE(6),
    INC_MONEY_MESSAGE(7),
    INC_GP_MESSAGE(8),
    INC_COMMITMENT_MESSAGE(9),
    GIVE_BUFF_MESSAGE(10),
    GENERAL_ITEM_EXPIRE_MESSAGE(11),
    SYSTEM_MESSAGE(12),
    UNK_MESSAGE(13),
    QUEST_RECORD_EX_MESSAGE(14),
    WORLD_SHARE_RECORD_MESSAGE(15),
    ITEM_PROTECT_EXPIRE_MESSAGE(16),
    ITEM_EXPIRE_REPLACE_MESSAGE(17),
    ITEM_ABILITY_TIME_LIMITED_EXPIRE_MESSAGE(18),
    SKILL_EXPIRE_MESSAGE(19),
    INC_NON_COMBAT_STAT_EXP_MESSAGE(20),
    LIMIT_NON_COMBAT_STAT_EXP_MESSAGE(21),
    ANDROID_MACHINE_HEART_ALSET_MESSAGE(23),
    INC_FATIGUE_BY_REST_MESSAGE(24),
    INC_PVP_POINT_MESSAGE(25),
    PVP_ITEM_USE_MESSAGE(26),
    WEDDING_PORTAL_ERROR(27),
    INC_HARDCORE_EXP_MESSAGE(28),
    NOTICE_AUTO_LINE_CHANGED(29),
    ENTRY_RECORD_MESSAGE(30),
    EVOLVING_SYSTEM_MESSAGE(31),
    EVOLVING_SYSTEM_MESSAGE_WITH_NAME(32),
    CORE_INVEN_OPERATION_MESSAGE(33),
    NX_RECORD_MESSAGE(34),
    BLOCKED_BEHAVIOR_MESSAGE(35),
    INC_WP_MESSAGE(37),
    MAX_WP_MESSAGE(38),
    STYLISH_KILL_MESSAGE(39),
    BARRIER_EFFECT_IGNORE_MESSAGE(40),
    EXPIRED_CASH_ITEM_RESULT_MESSAGE(41),
    COLLECTION_RECORD_MESSAGE(42),
    RANDOM_CHANCE_MESSAGE(43),
    UNK(44),

    ACHIEVEMENT_INIT(47),
    ACHIEVEMENT_MESSAGE(48), // v200.1 updated

    ;

    private byte val;

    MessageType(int val) {
        this.val = (byte) val;
    }

    public static MessageType getByVal(byte type) {
        return Util.findWithPred(values(), v -> v.getVal() == type);
    }

    public byte getVal() {
        return val;
    }
}
