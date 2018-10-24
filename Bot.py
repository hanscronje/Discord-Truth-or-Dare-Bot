# Created by Johannes Cronje 2018, all rights reserved.

# Import needed components
import discord
import time
import os
import math
from random import randint

clientID = '' # ClientID here
botToken  = '' # DiscordBots Token

if not os.path.isdir("servers"):
	os.mkdir("servers")

TRUTHLIST = """When was the last time you cleaned your room?
Is there a mess under your bed?
Is there a mess in your closet?
Have you ever snuck a snack?
Have you ever said you finished your dinner when you really didn’t?
Have you ever cheated on a test?
Have you had your first kiss?
Do you have a crush on anyone?
What would you do with $1,000?
If you could be any celebrity, who would you be and why?
Have you ever faked a sickness to stay home from school?
Have you ever used your lunch money for something other than lunch?
Have you ever watched a movie or TV show that you know you’re not allowed?
What are some ways you cheat on chores?
What is the least favorite gift you’ve ever received?
Are you afraid of the dark?
Do you have any secrets?
Do you keep a diary/journal?
Is there anything that you would change about yourself?
What is your biggest fear?
Have you ever skipped school?
What is your worst habit?
Have you ever lied about your age?
Have you ever lied to me?
Do you bite your nails?
Do you pick your nose?
Have you ever peed in a pool?
What is the grossest thing you've done today?
When was the last time you flossed your teeth?
Which have for dinner, fast-food or Mom's home cooking?
Have you ever cried during a movie? If so, which one?
Do you still enjoy Blues Clues?
What is something you wish you were better at?
Have you ever broken something and blamed someone else?
When was the last time you did something nice for someone else?
What is your favorite meal Mom makes?
Have you ever peeked at Christmas presents early?
Have you ever eaten a bug?
Do you pick scabs?
Have you ever passed gas and blamed someone else?
Who is your favorite Disney Princess and why?
What do you still like that you wish others didn't know about?
If you could make anyone like you, who would it be?
Who would you like to eat with once, the person can be dead or alive?
Tell the group something about yourself they don't already know.
If you could be any animal, which one would it be and why?
If you could decide where to live for a year, where would it be?
What is the favorite vacation you have ever been on?
If you had $1,000 and had to spend it all today, what would you buy?
What is your most embarassing moment?
What do you plan on naming your first child?
Do you talk in your sleep. If so, have others told you what you have said?
What is the funniest thing that has ever happened to you?
Where is the strangest place you have ever broke out laughing?
Do you still sleep with something favorite like a blanket or stuffed animal?
How old were you when you last owned pajama's with feet in them?
What are you most afraid of?
Would you rather be a famous singer or famous actress? Why?
Have you ever played sick and stayed home? Why did you play sick?
Tell something you like most about each person in the room.
What is the most annoying thing about the person to your right and left?
What was the worst lie you ever told? Did you get caught?
Name two people in the group that you could live with for a year. Why?
If you could change places with the opposite gender for a day, would you and why or why not?
Is there one thing you still won't tell your parents you have done?""".splitlines()

DARELIST =  """Dance in the middle of the circle to a random song 
Call one of your siblings and tell them one thing you admire about them
Text three friends you know and tell them "I am AWESOME"
Sit on a balloon until it pops
Stack up canned goods from the pantry until you can't reach the top
Bark like a dog after everything you say for the next 10 minutes
Wrap your knees together with plastic food wrap until the end of the game
Chug a root beer without stopping
Put as many jumbo marshmallows in your mouth as will fit
Talk with a foreign accent until the end of the game
Do your best impression of the person you have a crush on
If anyone says UM, to pretend to sneeze... for the rest of the game
Sing Mary Had a Little Lamb while doing a ballet dance
Pretend a stuffed animal is the boy you like, tell him how you feel
Empty your purse or backack in the circle and tell why you carry each item
Let the group wrap you in toilet paper
Sing your favorite song to the group
Stand with your nose in the corner for one minute
Someone puts 3 food items in a blender and you have to drink some
Check for toe jam between everyone's toes
Wear your clothes backward for the rest of the evening
Hold an ice cube in your hands until it melts
Crack an egg over your head.
Attempt to do 10 pushups.
Eat a plate of (dinner, dessert, whatever) with no hands.
Crabwalk across the room.
Army crawl across the room.
Stand on your hands.
Fetch (item of choice in another room) with a blindfold on.
Eat a spoonful of sugar.
Eat a spoonful of hot sauce.
Eat a hot pepper.
Do your best Buzz Lightyear impression.
Do your best Mickey Mouse impression.
Do your best lion roar.
Do your best Batman impression.
Do your best Disney princess impression.
Attempt a cartwheel.
Make up a poem aloud.
Dump a cup of ice water over your head.
Prank call Grandma.
Attempt to slip on a banana peel (or pretend to).
Make a really silly face and take a selfie.
Draw a picture of (you pick) while blindfolded.
Take off your socks with a pair of tongs.
Run around the outside of the house three times.
Act like a cat.
Act like a monkey.
Chug a cup of (milk, water, juice, etc.).
Touch your nose with your tongue.
Juggle eggs (outside.)
Stick a spoon on your nose and keep it there as long a possible.
Sing the ABCs backward.
Spin in circles for 10 seconds.
Text someone using only your nose.
Pop a balloon without using your hands or your teeth.
Suck an ice cube until melted without chewing (or a couple of ice cubes at the same time if they are small).
Hold an ice cube in your hand until it melts.
Go outside and yell “Happy New Year!
Eat a clove or a spoonful of minced garlic.
Sniff the pepper shaker..
Do your makeup in 10 seconds (eye shadow, blush, and lipstick).
Sniff (choice person)’s shoe.
Do the chicken dance.
Do the macarena silently until it is your turn again.
Go ask the neighbor for a cup of sugar.
Wear your shoes on your hands for the next 5 minutes.
Spin 10 times and try to do hopscotch.
Spin 10 times and try to skip rope.
Do the disco.
Stuff as many marshmallows (or grapes, donut holes, etc.) into your mouth as you can!
Use the driveway as a catwalk for five minutes, while giving the model wave to any passing cars or people.
Wear underwear on your head for the rest of the game.
Draw a mustache on yourself without a mirror.
Switch clothes with someone.
Try to dress the family pet.
Stack five cookies on your forehead. (Oreos work great!)
Do the Hokey Pokey without singing it.
Go outside and yell “I pick my nose!” to the first person you see.
Finish every sentence with the words “while I dance” or “with a cherry on top.” (Or whatever silly thing you can think of!)
Belt out a song of choice.
Let someone tickle you for 30 seconds.
Let someone fix your hair the way they want and leave it that way.
Have a full conversation with a broom.
Sing what you have to say instead of talking.
Try to catch three pieces of small food tossed by someone in your mouth (popcorn, grapes, etc.).
Use a hairbrush as a microphone.
Talk in the third person.
Talk in a high-pitched voice.
Be a commentator for the remainder of the game.
Pretend to be T-Rex.
Talk and act like a robot.
Jump into the pool or submerge yourself in the bathtub fully clothed.
Keep your finger on the tip of your nose as if it’s stuck there.
Stop blinking for 30 seconds.
Talk without moving your lips.
Skip everywhere you go instead of walking or running.
Start every sentence with “what is…”.
Jump while holding a cup full of water above your head without spilling it.
Remove one sock and shoe so that one foot is bare for the rest of the game.
Take a bite of a sandwich made by everyone that contains whatever they desire, and try to guess each ingredient on the sandwich.
Bob for an apple. (Large mixing bowl full of water works well!)
Snort excessively when laughing.
Pretend to have chicken pox by sticking round labels all over yourself.
Talk and act like a cowboy or cowgirl.
Get wrapped from head to toe in toilet paper.
Make a face mask out of sliced cheese.
Walk backwards wherever you go.
Put all clothes on inside out.
Put all clothes on backwards.
Take your age, reverse the numbers, and act that age. (If player is only a single digit, just add a 0 to their age. Example: player is 8, so they must act 80.)
Smell everyone’s breath and guess what they ate last.
Talk with your tongue sticking out.
Talk while holding your tongue with your index finger and thumb.
Put your leg behind your head.
Draw a stickman on paper by holding the writing utensil in your mouth.
Go outside and howl at the moon. (If it’s dark outside).
Do jumping jacks until your next turn.
Do the cha cha until your next turn.
Tie your shoes together and try not to forget!
Hug your mailbox (or a tree or lawn ornament) for 20 seconds.
Take a wet willy.
Eat a huge spoonful of peanut butter and sing the ABCs.
Play fetch like a dog, running on all fours and using only your mouth to fetch.
Take a bite out of a stick of butter.
Put ice cubes down your shirt, with shirt tucked in.
Act like a chicken.""".splitlines()

HYELIST =   """picked my nose and ate it.
ate food that had fallen on the floor.
eaten brussels sprouts.
eaten a raw egg.
used someone else's toothbrush.
had to kiss my brother or sister.
smelled someone else's BO.
picked a scab and ate it.
stuck my hand in ketchup.
used the bathroom and not washed my hands.
thrown up on someone.
wet the bed at someone else's house.
eaten food from the trash can.
walked in on someone in the bathroom.
licked someone's food.
dropped my phone in the toilet.
double dipped.
put something other than my finger in my nose.
eaten something that was expired.
eaten a bug.
played in the mud.
farted in the car.
found week old food in my room.
had a cockroach on me.
spit in someone's drink.
touched a worm.
eaten a bug intentionally.
been gratified by the amount of ear wax I got out of my ear.
pooped my pants.
let a dog lick my face.
eaten something off the ground and realized it wasn't food.
eaten a spoonful of a condiment.
found someone else's hair in my food and continued eating.
written and mailed Santa a letter.
played video games for more than 4 hours in a day.
tried to convince a sibling that something I did was actually something they did.
stuck my finger in a birthday cake.
had an imaginary friend.
stayed awake all night after watching something scary.
had an argument with myself... and lost.
thought of escape plans from an alien, ninja or zombie invasion.
eaten cold pizza.
sang along with Blue’s Clues.
watched a Star Wars marathon.
eaten a large pizza by myself.
jumped into a trash can or dumpster.
eaten a whole box of Little Debbie snack cakes by myself.
eaten the insides of oreos and put them back in the container.
tried to strategically time farts with loud noises.
tried cutting my own hair.
eaten raw cookie dough.
experimented with ants and magnifying glasses.
wanted to be an astronaut.
had sushi.
made silly faces at myself in a mirror.
pretended to have my own cooking show.
rocked out to disco.
eaten so much candy I was sick to my stomach.
drank more than 2 cans of soda in a day.
accidentally put clothes on backwards and not noticed.
accidentally worn shoes on the wrong feet without noticing.
had the wind blow me down.
made up a fake language with my friends.
played a prank on adults.
made a prank phone call.
spun around so much that I threw up.
sneaked desert before dinner.
lied about doing my chores.
put stuff under my bed or in my closet and pretended I cleaned my room.
fed the dog under the table.
drank milk from the jug.
tried on my parents' shoes.
been embarrassed by my parents.
fought with my brother or sister.
played a prank on my brother or sister while they were sleeping.
watched something on TV that I knew I wasn't allowed to.
hid something under my mattress.
didn't like something my mom cooked.
paid my brother or sister to do my chores for me.
stayed up all night.
snuck out of the house.
gotten my brother or sister in trouble.
taken money out of Mom's purse.
asked Dad something after Mom already said "no."
found Christmas presents before Christmas.
eavesdropped on my parents arguments.
gone to bed without brushing my teeth.
been the only one in the family not to catch a cold.
been to a website I knew I shouldn't.
gotten something I didn't want for Christmas, but pretended to be happy.
broken my parents' rules intentionally to see what happens.
sat at the table by myself after dinner because I wouldn't eat my vegetables.
tried to trick the Tooth Fairy.
had to use Dad's hankerchief.
made my brother or sister think they were adopted.
drew a mustache on my brother or sister while they slept.
slept in til after noon during summer break.
tried on Mom's jewelry.
locked myself out of the house on accident.
ordered something on Amazon using Mom and Dad's card.
eaten old candy I've found in mom's purse.
been sent to the principle's office.
gotten straight A's.
copied from someone else's paper.
used the excuse, "My dog ate my homework."
believed cooties existed.
fallen asleep in class.
written my parent's signature on something.
been on a field trip.
chewed on my pencil.
gotten an F.
written a note to someone I liked.
played tetherball.
cheated during hide-and-seek.
tried to change a grade on a report card.
gotten into a fight at school.
lied to a teacher.
cheated on a test.
gone to the clinic.
fallen off playground equipment.
skipped class.
written a book report without reading the book.
thrown something out of the schoolbus window.
fallen asleep on the schoolbus.
missed the schoolbus.
added a teacher as a friend on social media.
texted a teacher.
had a class pet.
done 'show and tell.'
swapped lunches with someone else.
been part of a school musical.
played on a sports team at school.
danced at a school dance.
been a teacher's pet.""".splitlines()

WYRLIST =   """be the author of a popular book or a musician in a band who released a popular album?
be a detective or a pilot?
live in a house shaped like a circle or a house shaped like a triangle?
live in a place with a lot of trees or live in a place near the ocean?
do school work as a group or by yourself?
have your room redecorated however you want or ten toys of your choice (can be any price)?
have a magic carpet that flies or a see-through submarine?
be able to do flips and backflips or break dance?
everything in your house be one color or every single wall and door be a different color?
visit the international space station for a week or stay in an underwater hotel for a week?
see a firework display or a circus performance?
go skiing or go to a water park?
fly a kite or swing on a swing?
only be able to walk on all fours or only be able to walk sideways like a crab?
start a colony on another planet or be the leader of a small country on Earth?
be a wizard or a superhero?
be able to see things that are very far away, like binoculars or be able to see things very close up, like a microscope?
be an incredibly fast swimmer or an incredibly fast runner?
own an old-timey pirate ship and crew or a private jet with a pilot and infinite fuel?
be able to create a new holiday or create a new sport?
play hide and seek or dodgeball?
be able to jump as far as a kangaroo or hold your breath as long as a whale?
be incredibly funny or incredibly smart?
dance or sing?
it be warm and raining or cold and snowing today?
be able to type/text very fast or be able to read really quickly?
randomly turn into a frog for a day once a month or randomly turn into a bird for a day once every week?
have the chance to design a new toy or create a new TV show?
be really good at math or really good at sports?
become five years older or two years younger?
have a full suit of armor or a horse?
be a master at drawing or be an amazing singer?
have ninja-like skills or have amazing coding skills in any language?
be able to control fire or water?
have a new silly hat appear in your closet every morning or a new pair of shoes appear in your closet once a week?
be able to remember everything you’ve ever seen or heard or be able to perfectly imitate any voice you heard?
drink every meal as a smoothie or never be able to eat food that has been cooked?
meet your favorite celebrity or be on a TV show?
sail a boat or ride in a hang glider?
brush your teeth with soap or drink sour milk?
be a famous inventor or a famous writer?
be a master at origami or a master of sleight of hand magic?
have a tail that can’t grab things or wings that can’t fly?
have a special room you could fill with as many bubbles as you want, anytime you want or have a slide that goes from your roof to the ground?
dance in front of 1000 people or sing in front of 1000 people?
ride a very big horse or a very small pony?
be able to shrink down to the size of an ant any time you wanted to or be able to grow to the size of a two-story building anytime you wanted to?
be able to move silently or have an incredibly loud and scary voice?
be bulletproof or be able to survive falls from any height?
eat a whole raw onion or a whole lemon?
be incredibly luck with average intelligence or incredibly smart with average luck?
be able to change color to camouflage yourself or grow fifteen feet taller and shrink back down whenever you wanted?
instantly become a grown up or stay the age you are now for another two years?
have a personal life-sized robot or a jetpack?
never have any homework or be paid 10$ per hour for doing your homework?
take a coding class or an art class?
eat a bowl of spaghetti noodles without sauce or a bowl of spaghetti sauce without noodles?
have eyes that change color depending on your mood or hair that changes color depending on the temperature?
eat an apple or an orange?
taste the best pizza that has ever existed once but never again or have the 4th best pizza restaurant in the world within delivery distance?
go snorkeling on a reef or camping by a lake?
have an elephant-sized cat or a cat-sized elephant?
be able to jump into any picture and instantly be in that place and time but able to return or be able to take pictures of the future, just stand in a place think of a time in the future and take a picture?
play outdoors or indoors?
eat broccoli flavored ice cream or meat flavored cookies?
eat one live nonpoisonous spider or have fifty nonpoisonous spiders crawl on you all at once?
live on a sailboat or in a cabin deep in the woods?
have an amazing tree house with slides and three rooms or an amazing entertainment system with a huge TV and every game console?
eat a popsicle or a cupcake?
own a hot air balloon or an airboat?
have a bubble gun that shoots giant 5-foot bubbles or a bathtub-sized pile of Legos?
eat a worm or a grasshopper?
have super strength or super speed?
never eat cheese again or never drink anything sweet again?
have your very own house next to your parent’s house or live with your parents in a house that’s twice the size of the one you live in now?
have a cupcake or a piece of cake?
be able to move wires around with your mind or be able to turn any carpeted floor into a six-foot deep pool of water?
be able to speak any language but not be able to read in any of them or read any language but not be able to speak any of them?
live in a house where all the walls were made of glass or live in an underground house?
stay a kid until you turn 80 or instantly turn 40?
be able to watch any movies you want a week before they are released or always know what will be trendy before it becomes a trend?
be an athlete in the Summer Olympics or the Winter Olympics?
be fluent in 10 languages or be able to code in 10 different programming languages?
drive a police car or an ambulance?
have a piggy bank that doubles any money you put in it or find ten dollars under your pillow every time you wake up?
own a mouse or a rat?
live in a cave or a tree house?
do a book report or a science project for a school assignment?
fly an airplane or drive a fire truck?
be a talented engineer or a talented coder?
spend the whole day in a huge garden or spend the whole day in a large museum?
be able to find anything that was lost or every time you touched someone they would be unable to lie?
be a babysitter or a dog sitter?
ride a bike or ride a kick scooter?
work alone on a school project or work with others on a school project?
open one 5$ present every day or one big present that costs between 100$ to 300$ once a month?
have an unlimited supply of ice cream or a popular ice cream flavor named after you?
live in a place that is always dusty or always humid?
have any book you wanted for free or be able to watch any movie you wanted for free?
be able to play the piano or the guitar?
be able to read lips or know sign language?
eat a hamburger or a hot dog?
ride a roller coaster or see a movie?
be able to change the color of anything with just a thought or know every language that has ever been spoken on Earth?
have super strong arms or super strong legs?
move to a different city or move to a different country?
be wildly popular on the social media platform of your choice or have an extremely popular podcast?
be able to talk to animals and have them understand you, but you can’t understand them, or be able to understand what animals say but they can’t understand you?
eat smores or cupcakes?
ride in a hang glider or ride in a helicopter?
never have to sleep or never have to eat?
be an amazing photographer or an amazing writer?
sneeze uncontrollably for 15 minutes once every day or sneeze once every 3 minutes of the day while you are awake?
be able to remember everything in every book you read or remember every conversation you have?
have 10 mosquito bites or 1 bee sting?
be an actor/actress in a movie or write a movie script that would be made into a movie?
be able to talk to dogs or cats?
have a jetpack or a jet?
ride a roller coaster or go down a giant water slide?
get every Lego set that comes out for free or every new video game system that comes out for free?
go on vacation to a new country every summer vacation or get an extra three weeks of summer break?
eat a turkey sandwich with vanilla ice cream inside or eat vanilla ice cream with bits of turkey inside?
ride a skateboard or a bike?
visit every country in the World or be able to play any musical instrument?
control the outcome of any coin flip or be unbeatable at rock, paper, scissors?
be able to type faster than anyone or speak faster than anyone?
have a private movie theater or your own private arcade?
be a cyborg or a robot?
ride in a hang glider or skydive?
every vegetable you eat taste like candy but still be healthy or all water you drink taste like a different delicious beverage every time you drink it?
be really good at skateboarding or really good at any video game you tried?
lay in a bathtub filled with worms for 5 minutes or lay in a bathtub filled with beetles that don’t bite for 5 minutes?
live next to a theme park or next to a zoo?
have a room with whiteboard walls that you can draw on or a room where the whole ceiling is one big skylight?
have a house with trampoline floors or a house with aquarium floors?
live in a castle or a spaceship traveling far from earth?
play soccer or baseball?
ride a camel or ride a horse?
be amazing at drawing and painting or be able to remember everything you ever read?
have a jetpack or a hoverboard that actually hovers (no wheels)?
have a ten dollar bill or ten dollars in coins?
get up early or stay up late?
be able to eat any spicy food without a problem or never be bitten by another mosquito?
never have to take a bath/shower but still always smell nice or never have to get another shot but still be healthy?
be able to learn everything in a book by putting it under your pillow while you slept or be able to control your dreams every night?
be able to see new colors that no other people could see or be able to hear things that no other humans can hear?
move to a country and city of your choice or stay in your own country but not be able to decide where you moved?
have pancakes every day for breakfast or pizza every day for dinner?
drive a race car or fly a helicopter?
be unable to control how fast you talk or unable to control how loud you talk?
be rich and unknown or be famous and have enough money, but not be rich?
live in a house in the forest where there aren’t many people around or live in a city with lots of people around?
dance or draw?
have a 3d printer or the best phone on the market?
go snow skiing or water skiing?
never be able to eat any type meat again or never be able to eat things with sugar in them?
have no homework or no tests?
be able to control the length of your hair with your mind or be able to control the length of your fingernails with your mind? (Hair and nails grow/shrink about 1 inch in 10 seconds.)
get to name a newly discovered tree or a newly discovered spider?
swim in Jell-O or swim in Nutella?
play on swings or play on a slide?
have the power to shrink things to half their size or the power to enlarge things to twice their size?
live in a base under the ocean or a floating base in the sky?
not need to eat and never be hungry or not need to drink and never be thirsty?
be the fastest kid at your school or the smartest kid at your school?
be a scientist or be the boss of a company?
have a magic freezer that always has all your favorite ice cream flavors or one that has a different ice cream flavor every time you open the door?
have a very powerful telescope or a very powerful microscope?
hang out for an hour with 10 puppies or 10 kittens?
be able to change colors like a chameleon or hold your breath underwater for an hour?
learn to surf or learn to ride a skateboard?
eat your favorite food every day or find 5 dollars under your pillow every morning?
have a pet penguin or a pet Komodo dragon?
be able to eat pancakes as much as you want without it hurting your health or be able to eat as much bacon as you want without it hurting your health?
be able to talk to animals or be able to fly?
own a restaurant or be a chef?
have a pet dinosaur of your choosing or a dragon the size of a dog?
have an amazing tree house or your whole yard be a trampoline?
have a slide that goes from your home’s roof to the ground or be able to change and control what color the lights are in your home?
be a famous musician or a famous business owner?
play in a giant mud puddle or a pool?
have your favorite artist perform a private show just for you or perform on stage next to your favorite artist for thousands of people?
be too hot or too cold?
have 100$ now or 1000$ in a year?
have a real triceratops or a robot triceratops? (Both are the same size.)
have everything you draw become real or become a superhero of your choice?
be given every Lego set that was ever made or get every new Lego set that comes out for free?
go to the beach or go to the zoo?
get a new pair of shoes or a jacket?
read a book or read a magazine?
be the fastest swimmer on earth or the third fastest runner on earth?
drink orange juice or milk?
go camping or stay in a hotel room?
go to the doctor for a shot or the dentist to get a cavity filled?
be able to make plants grow very quickly or be able to make it rain whenever you wanted?
be a falcon or a dolphin?
be able to read minds or see one day into the future?
have fireworks go off every evening for an hour or have Christmas three times a year?
eat a bowl of spaghetti that was just one long noodle or eat ice cream launched from a catapult?
watch a two-hour movie or watch two hours of shows?""".splitlines()


HELPOPTIONS = [
["help", "Shows this help menu"],
["truth", "Responds with a random truth"],
["dare", "Responds with a random dare"],
["hye", "Responds with a random have you ever"],
["wyr", "Responds with a would you rather"],
["invite", "Displays a link to the tord discord server"],
["vote", "Displays the link to vote for the bot"],
["version", "Responds with the bot's current version"],
["donate", "Shows the bot's donation link"],
["servers", "Displays the total amount of servers I'm in"],
["set-prefix", "Changes the prefix to a custom prefix (Admin Only)", "set-prefix new-prefix-here example: set-prefix ! or set-prefix tord"]
]


# Major - Changes that cause significant change or removes backwards compatibility
# Minor - Changes that aren't as significant and doesn't remove backwards compatibility
# Patch - Bug fix
VERSION = "1.0.12"
PREFIX = "-"

client = discord.Client()

@client.event
async def on_message(message):
	# if you're in a server, fetch server prefix, otherwise use default
	if not message.server == None:
		prefix = getPrefix(message)
	else:
		prefix = PREFIX
	
	# if this bot is the author or if the content of the message doesn't start with the prefix, don't bother processing
	if message.author == client.user or not message.content.lower().startswith(prefix):
		return
	
	# remove the prefix so we have a cleaner string to work with
	cmd = message.content.replace(prefix, "", 1).lower()
	
	# changes prefix if you are in a valid server, also checks if you're the admin of the given server
	if cmd.startswith("set-prefix") and not message.server == None:
		prefix = cmd.replace("set-prefix ", "", 1)
		if isAdmin(message.author, message.server):
			setPrefix(message, prefix)
			await client.send_message(message.channel, "Prefix set to " + prefix)
			
		# changes prefix if you are in a valid server, also checks if you're the admin of the given server
	if cmd.startswith("add-question") and not message.server == None:
		data = cmd.replace("add-question ", "", 1)
		if isAdmin(message.author, message.server):
			data = splitAfterFirst(data, " ")
			addCustomData(message.server, data[0], data[1])
			await client.send_message(message.channel, "Added" + prefix)
	
	# sends a random truth
	if cmd.startswith("truth"):
		await client.send_message(message.channel, getRandom(TRUTHLIST))
	
	# sends a random dare	
	if cmd.startswith("dare"):
		await client.send_message(message.channel, getRandom(DARELIST))
		
	# sends a random have you ever
	if cmd.startswith("hye"):
		await client.send_message(message.channel, getRandom(HYELIST))
		
	# sends a random would you rather
	if cmd.startswith("wyr"):
		await client.send_message(message.channel, getRandom(WYRLIST))
	
	# sends an invite link to bring the bot to your server as well as the support server
	if cmd.startswith("invite"):
		embed=discord.Embed(color=0x4fe8dc)
		embed.add_field(name="Invite me to your server!", value="https://discordapp.com/oauth2/authorize?client_id=450041159255851008&scope=bot&permissions=265216 ", inline=False)
		embed.add_field(name="My Support Discord!", value="https://discord.gg/FBBmjP3", inline=False)
		await client.send_message(message.channel, embed=embed)
		
	# sends an invite link to bring the bot to your server as well as the support server
	if cmd.startswith("vote"):
		embed=discord.Embed(color=0x4fe8dc)
		embed.add_field(name="Vote for the bot here!", value="https://discordbots.org/bot/450041159255851008/vote", inline=False)
		await client.send_message(message.channel, embed=embed)
		
	# lists the total amount of servers this bot is connected to
	if cmd.startswith("servers"):
		await client.send_message(message.channel, "I am in " + f'{len(client.servers)}' + " different servers")
		
	# lists the total amount of servers this bot is connected to
	if cmd.startswith("donate"):
		await client.send_message(message.channel, "Please donate to keep me running: https://www.patreon.com/tordbot")
		
	# generates and displays the help message
	if cmd.startswith("help"):
		embed=discord.Embed(title="Commands:", description="All commands must start start with " + prefix, color=0x4fe8dc)
		embed = populateEmbed(embed, HELPOPTIONS, prefix)
		embed.add_field(name="Join the TORD Discord", value="https://discord.gg/FBBmjP3", inline=False)
		await client.send_message(message.channel, embed=embed)
		
	# spews out the current version of the bot
	if cmd.startswith("version"):
		await client.send_message(message.channel, "I am currently running on version: " + VERSION)
		
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	#await update_stats(client.user.id)
	
# randomly selects an object from the given list
def getRandom(list):
	return list[randint(0, len(list)-1)]
	
# prefix changing
def setPrefix(message, prefix):
	dir = "servers/" + f'{message.server.id}' + "/"
	
	if not os.path.isdir(dir):
		os.mkdir(dir)
	
	file = "servers/" + f'{message.server.id}' + "/prefix.txt"
	
	fp = tryLoadFile(file, 'w+')
	
	if (fp == False):
		return PREFIX
	
	fp.write(prefix.lstrip())
	
	fp.close()
	
	return prefix.lstrip()
	
# loading prefix
def getPrefix(message):
	dir = "servers/" + f'{message.server.id}' + "/"
	
	if not os.path.isdir(dir):
		os.mkdir(dir)
	
	file = dir + "prefix.txt"
	
	fp = tryLoadFile(file, 'r+')
	
	if (fp == False):
		return PREFIX
	
	found = False
	n = 0
	
	prefix = fp.readlines()
	
	if len(prefix) == 0:
		return PREFIX
	
	fp.close()
	
	return prefix[0].lstrip()
	
def getCustomDataCount(server, data):
	dir = "servers/" + f'{server}' + "/"
	
	file = dir + "custom" + data + ".txt"
	
	fp = tryLoadFile(file, 'r+')
	
	if (fp == False):
		return 0
	
	l = len(fp.readlines())
	
	fp.close()
		
	return l
	
def addCustomData(server, data, entry):
	dir = "servers/" + f'{server}' + "/"
	
	file = dir + "custom" + data + ".txt"
	
	fp = tryLoadFile(file, 'a')
	
	if (fp == False):
		return False
		
	if (getCustomDataCount(server, data) > 0):
		fp.write("\n")
		
	fp.write(entry)
	
	fp.close()
	
	return True
	
def getCustomData(server, data, id):
	dir = "servers/" + f'{server}' + "/"
	
	file = dir + "custom" + data + ".txt"
	
	fp = tryLoadFile(file, 'r+')
	
	if (fp == False):
		return 0
	
	l = fp.readlines()[id]
	
	fp.close()
		
	return l
	
	
# check if the user is an admin of a specific server
def isAdmin(user, server):
		
	for role in user.roles:
		if role.permissions.administrator and role.server.id == server.id:
			return True
		
	return False
	
def splitAfterFirst(str, char):
	ary = ["", ""]
	switch = False
	for i in range(0, len(str)):
		if str[0] == char[0]:
			switch = True
		elif not switch:
			ary[0] += str[0]
		else:
			ary[1] += str[0]
		str = str[1:]
			
	return ary
	
def populateEmbed(embed, list, prefix):
	z = 1
	for item in list:
		embed.add_field(name=f'{z}' + ". " + prefix + "" + item[0], value=item[1], inline=False)
		z += 1
		
	return embed
	
def tryLoadFile(fname, type, maxAttempts = 5, waitTime =  1):
	if not os.path.exists(fname):
		open(fname, "w+").close()
	attempts = 0
	while attempts < maxAttempts:
		try:
			f = open(fname, type)
			return f
		except IOError:
			attempts += 1
			time.sleep(waitTime)
			
	return False
	
import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
from dbl.http import HTTPClient

async def update_stats(bot_id):

	http = HTTPClient(botToken)
	while True:
		print('attempting to post server count')
		try:
			await http.post_server_count(bot_id, len(client.servers), None, None)
			print('posted server count ({})'.format(len(client.servers)))
			
		except Exception as e:
			print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
		await asyncio.sleep(10)

client.run(clientID)
