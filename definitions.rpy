


define audio.introductions = "musics/introductions.mp3"
define audio.FactoryFrenzy = "musics/Factory Frenzy.mp3"
define audio.ReadyRepair = "musics/Ready Repair.mp3"
define audio.FriendshipClub = "musics/Friendship Club.mp3"
define audio.aworldIbuiltforyou = "musics/a world I built for you.mid"
define audio.iseek = "musics/I Seek.mp3"
define audio.rest = "musics/Get some rest!.mp3"
define audio.suddenly = "sounds/suddenly.mp3"

image bg M1 = "images/desktop/M1.png"
image bg black = "images/desktop/M2.png"
image bg blue screen of death = "images/desktop/M3.png"
image bg bedroomnight = "images/bg/bedroomnight.png"
image bg bedroomday = "images/bg/bedroomday.png"
image bg goodtime = "images/bg/goody.png"

image kinito 1a:
    "images/kinito/1.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 2a:
    "images/kinito/2.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 3a:
    "images/kinito/3.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 4a:
    "images/kinito/4.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 5a:
    "images/kinito/5.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 6a:
    "images/kinito/6.png"

    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 7a:
    "images/kinito/7.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 8a:
    "images/kinito/8.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 9a:
    "images/kinito/9.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 10a:
    "images/kinito/10.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 11a:
    "images/kinito/11.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 12a:
    "images/kinito/12.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 13a:
    "images/kinito/13.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 14a:
    "images/kinito/14.png"
    pause 3
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito 15a = im.Composite((960, 960), (0, 0), "images/kinito/15.png")
image kinito 16a = im.Composite((960, 960), (0, 0), "images/kinito/16.png")
image kinito 17a = im.Composite((960, 960), (0, 0), "images/kinito/17.png")
image non = im.Composite((960, 960), (0, 0), "images/kinito/non.png")

image kinito 18a:
    "images/kinito/18.png"
    pause 5
    "images/kinito/blink.png"
    pause 0.1
    repeat

image kinito naps = im.Composite((960, 960), (0, 0), "images/kinito/sleep.png")
image kinito innight = im.Composite((960, 960), (0, 0), "images/kinito/innight.png")
image point = im.Composite((960, 960), (0, 0), "images/kinito/pointing.png")

image eggy:
    "images/kinito/egg.png"
    pause 4
    "images/kinito/egg1.png"

image eggo:
    "images/kinito/egg1.png"
    pause 0.1
    "images/kinito/egg2.png"



define narrator = Character(position="fixed")
define me = Character("[myname]", what_prefix='"', what_suffix='"', position="fixed")
define k = DynamicCharacter("k_name", image='kinito', what_prefix='"', what_suffix='"', position="fixed")
default k_name = "Kinito"