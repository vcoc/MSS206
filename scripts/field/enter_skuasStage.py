# id 867233100 (Abrup Basin : Skuas Forward Defense Line), field 867233100
sm.closeUI(1711)
sm.showFieldEffect("Map/EffectPL.img/MainStream/Skuas/screenEff/base", 0)
sm.showFieldEffect("Map/EffectPL.img/MainStream/Skuas/screenEff/stage/0", 0)
sm.showFieldEffect("Map/EffectPL.img/MainStream/Skuas/screenEff/map/0", 0)
sm.showFieldEffect("Map/EffectPL.img/MainStream/Skuas/screenEff/enemy/4", 0)
sm.showFieldEffect("Map/EffectPL.img/MainStream/Skuas/screenEff/companion/8", 0)
sm.createQuestWithQRValue(64001, "dir1=0;man=720;stage=0;enemy=104253;seq=1;mine=0;Fidx=0;companion=708435216;dir0=0")
sm.playExclSoundWithDownBGM("PL_MONAD.img/effectSound/Skuas_StageStart", 100)
sm.createQuestWithQRValue(64002, "man=128;stage=1;enemy=4;man0=0;man1=0;companion=8")
sm.createQuestWithQRValue(64003, "enemy0=1;enemy1=0;companion0=7;man0=128;companion1=0;man1=35;map0=0")
sm.createQuestWithQRValue(64003, "enemy0=1;enemy1=0;companion0=7;man0=128;companion1=0;man1=35;map0=0;map1=0")
sm.warp(867233150)
