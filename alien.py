print(r'''
**************************************************************
                      A L | E N S  .---._
                                  /==----\_
                 |\              |8=---()-\|   |\
         /|      ::\             |8=-/|\(_)&gt;_   \\
         |:\     `::\_            \=/:\= (_)\|   |\
         `::|     |::::.            \;:\=\(_)&gt;_  |\\
          |b\\_,_ \`::::\             \:\=\( \/  \_(
          `\88b`\|/|'`:::\   .-----   :8:\=|`=&gt;_  [d[
           \;\88b.\=|///::`-/::;;;;:\ |8;|=\( )/   [8[
      __    ||/`888b.\_\/\:/:;/'/-\::\/( \|=(=)&gt;_  [d|
     //):.. `::|/|\"96.\|//;/|'| /-\::+\|-\=(. )/  [8[
    |(/88e::.. `'.|| "min;/\\/8|\.-|::|8|||=|`='_  `[d|
     `-|8888ee::,,,`\/88utes8P//8|-|::|8||\=|( )/   ]8[
      |:`"|####b:::/8pq8e/::'`;q8|/::dP'|\|=|`='_   [d|
 .=-. \::..`""##Gst:q| e|:/..\:|8|.:/|'/\/|/|(_)/   ]8[
/(,:;:, \::::.\#/88q;`;'\||.:/-//.;/&lt;8\\\^\||./&gt;    `]d[
`8888b::,,_ ::/88q;.`;|d8/`-.]/|./  |8|\|:|;/.d|     [8|
  `"88###n::-/d8P.\e/-|d/ _//;;|/   |8(|::(/).8/     ]d[
    `"###o2:1dP;`q./=/d/_//|8888\   ;8|^\/`-'8/      [8\
       `"v7|9q8e;./=/d//=/\|eeeb|  /dP= =&lt;ee8/       ]d-
          \|9; qe/-d/ .|/=/888|:\ `--=- =88p'        [8[
          (d5b;,/ d/.|/=-\Oo88|:/                   ,8_\
         _|\q88| d/ /'=q8|888/:/                    ]d|
        _\\\/q8/|8\_""/////eb|/_                    [8_\
        \|\\&lt;==_(;d888b,.////////--._               ]8|
       _/\\\/888p |=""";;;;`eee.////.;-._          ,8p\
      /,\\\/88p\ /==/8/.'88`""""88888eeee`.        ]8|
    .d||8,\/p   /-dp_d8|:8:.d\=\    `""""|=\\     .[8_\
    |8||8||8.-/'d88/8p/|:8:|8b\=\        /|\\|    ]8p|
    |8||8||8b''d.='8p//|:8:'`88b`\       |||||)   [8'\
    `8b:qb.\888:e8P/'/P'8:|:8:`888|      |'\||'  /8p|
     q8q\\qe---_P;'.'P|:8:|:8:|`q/\\     '_///  /8p_\
     _|88b-:==:-d6/P' |8::'|8:| ,|\||    '-=' .d8p/
    |__8Pdb-q888P-'  .:8:| |8:| |/\||\     .-e8p/\|
     .-\888b.__      |:8/' |8:| \ _|;|,-eee8\8\|
     \.-\'88/88/e.e.e|8/|\_--.-.-e8|8|88\8p\|
       .'`-;88]88|8|/':|:\ `q|8|8|8'-\| \|
        `' || || |_/(/|;\)`-\\`--,\|
              `' /v"""' `""""""vVV\
**************************************************************
''')
print("Welcome to back to LV-426.")
print("Your mission is to find Newt\nand make it off the planet alive.")
play = input('Would you like to play?\n     Type "Y" for yes or "N" for no: ')

if play == "Y" or play == "y":
    print("Let's begin!")
    cross_road = input('You enter the terrafroming compound, which way do you go?\n     '
                       'type "Left" or "Right"\n').lower()
    if cross_road == "left":
        print("Good choice. the lifeform signal is getting stronger")
        swim = input('You\'ve come to a room full of alien eggs. '
                     'the signal is coming from the other side.\n     '
                     'Type "Walk" to walk through the room quietly. Or type "Wait" to ride the lift across.\n').lower()
        if swim == "wait":
            print("Good idea, the eggs stir, but nothing emerges as you ride the lift.")
            door = input('You\'ve reached the other side safely and come to 3 colored doors.\n'
                         'Newt must be behind one of these doors. Which once will you choose?\n     '
                         'Type "Red" "Yellow" or "Blue"\n').lower()
            if door == "red":
                print("Sorry, you've been attacked by a massive Xenomorph!\nGame Over Man, GAME OVER!")
            elif door == "yellow":
                print("You\'ve found newt!!! Congratulations!!!\n"
                      "You both ecape aboard the Marine Dropship and fly safely back to Earth...\n"
                      "or do you.")
            elif door == "blue":
                print("Sorry, you've been attacked by a facehugger and die as an Alien Queen is born\nGame Over Man, GAME OVER!")
            else:
                print("Sorry, you\ve run out of time and the colony self destructs\nGame Over Man, GAME OVER!")
        else:
            print("Ouch!! you've been attacked by a facehugger!!!.\n     "
                  "Game Over Man, GAME OVER!")
    else:
        print("Oh No!! You walked right into a group of hungry Xenomorphs!!!\n     "
              "Game Over Man, GAME OVER!")
else:
    print("Well that's great, that's just great, man. Now what are we supposed to do?.")
