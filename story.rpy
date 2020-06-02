label story:
    stop music fadeout 2.0 
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    "I open my eyes to a new day."
    "I quickly check my phone to see the time."
    mc "Ugh"
    mc "School."
    "I get off my bed, and get dressed."
    "As I start packing my books in my bag, I see through the window the other students in the neighborhood walking to school."
    stop music fadeout 1.0
    "I freeze for a moment."
    mc "Should I?"
    mc "{w=1}.{w=1}.{w=1}.    Eh, why not?"
    "I grab my Nintendo Switch and throw it in My Bag, as I get out of my house."
    scene bg residential_day
    with wipeleft_scene
    play music t2 fadein 1.0
    "I wonder,{w=0.50} where's Sa-{nw}"
    show sayori 4p at t11
    s "DAMN IT"
    "Oh, well there she is,"
    "Good old childhood friend Sayori!"
    s 4a "Oh Hi [player]!"
    mc "Hey Sayori,{w=0.25} why where you screaming back there?"
    s 1m "Oh! {w=0.25}that?"
    show sayori 5a at t11
    s "Well...{w=0.50} You See.."
    s 5b "I may or may not have gotten hit by a Blue Shell like two seconds away from the finish line..."
    "A Blue Shell?{w=0.50} Oh She's talking about Mario Kart!"
    "But since when has Sayori been into Gaming?"
    mc "Hey Sayori, Since When Have You Been Into Gaming?"
    s 1n "G-{w=0.50}Gaming?"
    s 3a "Well,{w=0.25} very recently actually!"
    s 4q "I actually joined a Gaming Club!"
    mc "A-{w=0.50}Gaming Club?!"
    "Sayori Notices I'm Kind Of Interested."
    s 1b "That face!"
    s 3x "Are you interested in joining the Gamer Club?"
    "I can feel my face getting red."
    "Why does Sayori always get me in situations like this?!"
    mc "Well,{w=0.50} Maybe."
    s 4r "Yay!"
    mc "Wait!{w=0.25} I'm not sure yet,{w=0.50} I'll think about it."
    s 4q "Okay!"
    scene bg class_day
    with wipeleft_scene
    "The School Bell Rings and Class Is Over."
    "I Can See Sayori Running Through The Classroom Towards Me."
    "What Do I Do?!"
    show sayori 1a at l11
    s "Hey [player], Decided yet?"
    mc "Uhhh,{w=0.50} Yes But No."
    mc "I Think I'll Go For Today and See How It Goes.."
    s 4r "Good Enough For Me!"
    "Sayori Grabs My Hand and Drags Me Out of the Classroom."
    stop music fadeout 2.0
    scene bg corridor 
    with wipeleft_scene
    "I Can Feel My Heart Pounding Super Fast."
    show sayori 1a at t11
    s "Stay Here Until I Call You, Okay?"
    mc "Alright."
    hide sayori with moveoutleft 
    "Sayori Goes Into The Clubroom."
    "I Slide Next To It To Hear Inside."
    $ n_name = "Girl 1"
    $ y_name = "Girl 2"
    $ m_name = "Girl 3"
    s "Guess What I Just Did Today?"
    n "What Did You Do This Time?"
    s "Well,{w=0.25} I Got Someone To Join The Club!"
    "Huh? I Never Agreed Joining smh"
    y "Then,{w=0.25} Who is It?"
    m "Yeah!{w=0.25} Who Is It Sayori?"
    "I See Sayori Waving at Me Through the Door's Window To Come Inside."
    "This Is It."
    scene black with wipeleft
    "I Gently Open The Door..."
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    $ renpy.call_screen("dialog", "lol jk", ok_action=Return())
    stop music fadeout 1.0
    scene bg club_day with wipeleft
    play music t3
    show sayori 4 at l41
    s "So,{w=0.25} Here He Is!"
    show sayori at lhide
    hide sayori
    "Huh,{w=0.25} I glance around the room."
    "I can see multiple bottles of Mountain Dew and Doritos on the Floor."
    show yuri 1a at t11
    y "Welcome To The Gamer Club,{w=0.50} N00b."
    show yuri at t22
    show natsuki 4b at t21
    n "Seriously? You Brought a Boy?"
    n "Way to kill-{nw}"
    n 5g "Actually, Nevermind."
    show yuri at t31
    show natsuki at t32
    show monika 1k at t33
    m "Oh Hey [player]! I,{w=0.25} Actually kind of expected you eventually lol."
    m "Welcome to the Club!"
    show monika 1a
    mc "Oh, Hi Monika? "
    "I, am incredibly confused."
    "I'm Seeing a pair of Laptops, one with some Horror Game and One With, Mi-{w=0.50} MINECRAFT?!"
    "I DECLARE MARRYING WHOEVER OWNS THAT LAPTOP"
    n 5b "Ok, Are we done now? I was making some Cupcakes and wanna finish them."
    y 1h "Natsuki! Don't say that in front of our New Member, [player] was it?"
    mc "Yeah.."
    $ n_name = "Natsuki"
    $ m_name = "Monika"
    "So the pink haired one is named Natsuki.."
    n 5v "Yuri!"
    "Yuri, Huh?"
    $ y_name = "Yuri"
    show monika 1k at t44
    show natsuki 5v at t43
    show yuri 1h at t42
    show sayori 1o at t41
    s "Guys! Stop Fighting!"
    "Weed"