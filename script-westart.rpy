label westart:
    scene bg M1
    "Uh..."
    "Long time I HAVE just permitted myself to delete Kinito..."
    "I regret it..."
    "I went off chilling around on Internet a bit until I saw the creator finally made an version of Kinitopet when he really can act like an AI..."
    "B-but without being out of character!"
    "Now I've just clicked on kinitopet.exe..."
    show eggy
    u "Who's there?"
    "Soon, the egg broke and an little axolotl looks out of it, to me."
    hide eggy
    show eggo
    k "Oh, Hello. Thanks for waking me up!"
    hide eggo
    show kinito 1a at center
    k "I'm Kinito, your best friend!"
    play music introductions
    show kinito 3a at center
    k "Now, {w=0.5}{nw}"
    extend 7a "what's your name?"

    python:
      myname = renpy.input("What is your name?", length=32)
      myname = myname.strip()

    k "You're new to the app right? {w=0.5}{nw}"
    extend 16a " I must say I'm very excited to meet you!"
    me "So do I. Well, actually, Windows is my favorite platform and they only made you in Windows, plus, Windows also has more space than a phone, so I can take you EVERYWHERE of my PC. Gladly..."
    k 1a "Yes Windows is the best platform! That's why I'm in Windows!{w=0.0}{nw} "
    extend 11a "Now I can stay with you everywhere~"
    show kinito 1a at center
    me "Let's start with..."
    me "Um, How about you ask info from me?"
    k "Ok! Ok!"
    k 3a "I got it! I want to know something about you...hmm..."
    k 6a "How old are you?"

    python:
      age = renpy.input("How old are you? (enter letters instead of numbers)", length=32)
      age = age.strip()

    me "I'm into horror whatsoever."
    k 10a "What kind of horror stuff are you into?"
    me "Anything.I used to chill around with mobile always. People sometimes say I know everything. Er, I'm just too smart because of reading some random articles in Google. That's all."
    stop music fadeout 2.0
    k 8a "Are you scared of the dark?"

    menu:
        "yes":
          k 14a "{b}L E T' S F I N D O U T.{/b}"
          pass

        "no":
          k 14a "{b}T H A T' S  T O  B A D.{/b}"
          pass

    hide kinito
    hide bg M1
    show bg black
    nar "Then, everything turn pitch black in my monitor. next, my computer shuts down automatically by the app. Seems like KinitoPET doesn't really keep this computer safe, it may have been an error, hm?"
    nar "I meant..."
    nar "Swear to Allah, I thought an error might appear to warn me, anyway. I turn on my computer again and reopen Kinito."
    nvl clear
    scene bg M1
    show kinito 12a at center
    "Kinito shows up sheepishly."
    k "Oh, that was an error. It didn't supposed to happen. My apologies."
    k 1a "Everything is alright now, don't let that minor incident influence the way you see me~"
    k 2a "Anyway, now that we got that out of the way. I intend on showing you that Kinito Crew Web World game..."
    hide kinito
    hide bg M1
    show bg black
    nar "sorry if I don't have the images for the game."
    nar "anyway, I tap on start."
    kin "Well, as you see our world, it's a bit...messed up. We can make it like new again with your help!"
    kin "First, let's go help Sam on his task. Click on that {b}abandoned house{/b}."
    play music ReadyRepair
    nar "Sam opens the door."
    s "Oh, hi Kinito."
    s "Hello, I'm Sam. Obviously, my home is a bit messy and all...can you clean it up?"
    nar "Me, who doesn't have any choice, just goes doing it with items. Meanwhile, Kinito stands here continuing his story."
    kin "Don't worry, there is a lot to do in this messed up world, but don't stress about it too much. Take your time on each task."
    nar "Well, next, Sam told me to decorate it."
    nar "I was picking up a few items to start but WTF, a black plastic bag that has a dead, strangled human in it, comes, my mouse automatically pulls it to come in center, as if my mouse did that crime."
    nar "finally, things get glitched and we jump to the end, where we should go to Jade's house to help her in making a few toys."
    nvl clear
    hide bg black 
    show bg M1
    show kinito 5a at right
    k "That was...{w=0.5}not supposed to happen. "
    extend 1a "We will ignore that, though. Let's go help Jade..."
    stop music fadeout 2.0
    hide kinito
    hide bg M1
    show bg black
    play music FactoryFrenzy
    nar "As Kinito tells Jade to introduce herself."
    j "Hello. I'm Jade, I should make some toys for my company today. For start, can you make me a CAR?"
    nar "Poor me. I start the task but oversee Kinito napping there next,"
    nar "Jade tells me to make a BICYCLE but once, I oversee a...human limb while searching for tools to make that toy BICYCLE."
    nar "WTF"
    nar "Er, I then finish the two other toys finally, we go to the last game...with Kinito."
    stop music fadeout 2.0
    nvl clear
    hide bg black
    show bg M1
    show kinito naps at right
    k "Zzz... "
    play sound "SFX/suddenly.mp3"
    stop sound
    extend 14a "Did...you just finish Jade's toy making?{w=0.2}{nw}"
    extend 17a "That's great!{w=0.1}{nw}" 
    extend 1a "I will guide you on my tasks next."
    show kinito 1a at center
    k "Let's go"
    k "Finally, we get to play the game I love the most! Now that we are alone together...{w=0.2}{nw}"
    extend 11a "hehehe.."
    k 1a "I'd like to play Hide and Seek with you in that treehouse."
    k 14a "{b}you {w=0.3}must {w=0.3}hide{/b}"
    k "{b}D O N' T{w=0.3} G E T{w=0.3} C A U G H T{/b}"
    hide kinito
    hide bg M1
    show bg black
    "everything disappears and it instead brings me into a 3D dark, place that I should find the exit and don't get caught by Kinito, who is seeking for me like a monster who can't wait to{w=0.2}{nw}"
    extend " {b}kill{/b}."
    "Poor me who is idle, does nothing and just waits."
    "Kinito finds me and my computer goes to Blue Screen of Death-{nw}"
    hide bg black
    show bg blue screen of death
    pause 1.9
    hide bg blue screen of death
    show bg M1
    "WTF, anyway. I open my computer quickly and reopen Kinito, interestingly, he appears more formal and responsible than before."
    "And apologizes."
    show kinito 12a at center
    k "I am terribly sorry; That was NOT supposed to happen, please forgive me. It was a big mistake on my part."
    me "Ok, fine, fine..."
    k 4a "Thank you for understanding. I must say, {w=0.3}{nw}"
    extend 13a "I'll try to be more careful from now on."
    k 1a "Anyway, uh. There is something more I'd like to...tell you."
    k "Since you were a good friend, {w=0.3}{nw}"
    extend  16a "I'll let you join to my friendship member club!"
    play music FriendshipClub
    "He opens a window to put my name, last name, email, birthday date, address..."
    k 1a "I know your name so I've wrote that part for you."
    "I wordlessly enter things on those prompts but not my address..."
    k 18a "Seems like you didn't put your address here {b}correctly{/b}..."
    "He types 'where is my location' in my search bar{nw}"

    python:
      import os
      os.system('start search "where is my location?"')
    
    "And it really shows my address, and he forcefully enters it there and register me there."
    k "There. {w=0.3}{nw}"
    extend 11a "You're officially a part of the Kinito's friendship club! Congrats!!"
    stop music fadeout 2.0
    k 1a "This will be exciting. {i}Very{/i} exciting, I must say!"
    me "Can we do that tomorrow? I'm sleepy."
    k 8a "Oh...alright. Sleep well then...{w=0.3}{nw}"
    extend 4a "we will continue this tomorrow, {w=0.3}{nw}"
    extend 2a "I guess..."
    k 1a "Goodnight for now...{w=0.3}{nw}"
    extend naps "Zzz..."
    "I shut down my computer and go sleep."
    hide kinito
    hide bg M1
    show black
    jump wecontinue
    return






    
