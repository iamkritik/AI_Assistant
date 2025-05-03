import random
import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)
def Speak(audio):   
    print("    ")   
    print(f":{audio}")    
    engine.say(audio)
    engine.runAndWait()
    print(" ")
    
def TakeCommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print(":listening.....")
        print("\n") 
        r.pause_threshold = 0.5
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...") 
        query=r.recognize_google(audio,language='en-in')
        
        print(f": Your::{query}\n")
    except:   
        return "none"
    return query.lower() 

story=('''Title:The Boy And The Filberts.   A Boy was given permission to put his hand into a pitcher to get some filberts. But he took such a great fistful that he could not draw his hand out again. There he stood, unwilling to give up a single filbert and yet unable to get them all out at once. Vexed and disappointed he began to cry.

"My boy," said his mother, "be satisfied with half the nuts you have taken and you will easily get your hand out. Then perhaps you may have some more filberts some other time."

Do not attempt too much at once.''',''''Title:The Night Came Slowly. I am losing my interest in human beings; in the significance of their lives and their actions. Some one has said it is better to study one man than ten books. I want neither books nor men; they make me suffer. Can one of them talk to me like the night – the Summer night? Like the stars or the caressing wind?

The night came slowly, softly, as I lay out there under the maple tree. It came creeping, creeping stealthily out of the valley, thinking I did not notice. And the outlines of trees and foliage nearby blended in one black mass and the night came stealing out from them, too, and from the east and west, until the only light was in the sky, filtering through the maple leaves and a star looking down through every cranny.

The night is solemn and it means mystery.

Human shapes flitted by like intangible things. Some stole up like little mice to peep at me. I did not mind. My whole being was abandoned to the soothing and penetrating charm of the night.

The katydids began their slumber song: they are at it yet. How wise they are. They do not chatter like people. They tell me only: “sleep, sleep, sleep.” The wind rippled the maple leaves like little warm love thrills.

Why do fools cumber the Earth! It was a man’s voice that broke the necromancer’s spell. A man came to-day with his “Bible Class.” He is detestable with his red cheeks and bold eyes and coarse manner and speech. What does he know of Christ? Shall I ask a young fool who was born yesterday and will die tomorrow to tell me things of Christ? I would rather ask the stars: they have seen him. '''
,'''Title:One Summer Night. The fact that Henry Armstrong was buried did not seem to him to prove that he was dead: he had always been a hard man to convince. That he really was buried, the testimony of his senses compelled him to admit. His posture -- flat upon his back, with his hands crossed upon his stomach and tied with something that he easily broke without profitably altering the situation -- the strict confinement of his entire person, the black darkness and profound silence, made a body of evidence impossible to controvert and he accepted it without cavil.

But dead -- no; he was only very, very ill. He had, withal, the invalid's apathy and did not greatly concern himself about the uncommon fate that had been allotted to him. No philosopher was he -- just a plain, commonplace person gifted, for the time being, with a pathological indifference: the organ that he feared consequences with was torpid. So, with no particular apprehension for his immediate future, he fell asleep and all was peace with Henry Armstrong.

But something was going on overhead. It was a dark summer night, shot through with infrequent shimmers of lightning silently firing a cloud lying low in the west and portending a storm. These brief, stammering illuminations brought out with ghastly distinctness the monuments and headstones of the cemetery and seemed to set them dancing. It was not a night in which any credible witness was likely to be straying about a cemetery, so the three men who were there, digging into the grave of Henry Armstrong, felt reasonably secure.

Two of them were young students from a medical college a few miles away; the third was a gigantic negro known as Jess. For many years Jess had been employed about the cemetery as a man-of-all-work and it was his favourite pleasantry that he knew 'every soul in the place.' From the nature of what he was now doing it was inferable that the place was not so populous as its register may have shown it to be.

Outside the wall, at the part of the grounds farthest from the public road, were a horse and a light wagon, waiting.

The work of excavation was not difficult: the earth with which the grave had been loosely filled a few hours before offered little resistance and was soon thrown out. Removal of the casket from its box was less easy, but it was taken out, for it was a perquisite of Jess, who carefully unscrewed the cover and laid it aside, exposing the body in black trousers and white shirt. At that instant the air sprang to flame, a cracking shock of thunder shook the stunned world and Henry Armstrong tranquilly sat up. With inarticulate cries the men fled in terror, each in a different direction. For nothing on earth could two of them have been persuaded to return. But Jess was of another breed.

In the grey of the morning the two students, pallid and haggard from anxiety and with the terror of their adventure still beating tumultuously in their blood, met at the medical college.

'You saw it?' cried one.

'God! yes -- what are we to do?'

They went around to the rear of the building, where they saw a horse, attached to a light wagon, hitched to a gatepost near the door of the dissecting-room. Mechanically they entered the room. On a bench in the obscurity sat the negro Jess. He rose, grinning, all eyes and teeth.

'I'm waiting for my pay,' he said.

Stretched naked on a long table lay the body of Henry Armstrong, the head defiled with blood and clay from a blow with a spade.''','''Title:Amy's Question. "Amy!"

Mrs. Grove called from the door that opened towards the garden. But no answer came. The sun had set half an hour before, and his parting rays were faintly tinging with gold and purple, few clouds that lay just alone the edge of the western sky. In the east, the full moon was rising in all her beauty, making pale the stars that were sparking in the firmament.

"Where is Amy?" she asked. "Has any one seen her come in?"

"I saw her go up stairs with her knitting in her hand half an hour ago," said Amy's brother, who was busily at work with his knife on a block of pine wood, trying to make a boat.

Mrs. Grove went to the foot of the stairs, and called again. But there was no reply.

"I wonder where the child can be," she said to herself, a slight feeling of anxiety crossing her mind. So she went up stairs to looks for her. The door of Amy's bedroom was shut, but on pushing it open Mrs. Grove saw her little girl sitting at the open window, so lost in the beauty of the moonlit sky and her own thoughts that she did not hear the noise of her mother's entrance.

"Amy," said Mrs. Grove.

The child started, and then said quickly,--

"O, mother! Come and see! Isn't it lovely?"

"What are you looking at, dear?" asked Mrs. Grove, as she sat down by her side, and drew an arm around her.

"At the moon, and stars, and the lake away off by the hill. See what a great road of light lies across the water! Isn't it beautiful, mother? And it makes me feel so quiet and happy. I wonder why it is?"

"Shall I tell you the reason?"

"O, yes, mother, dear! What is the reason?"

"God made everything that is good and beautiful."

"O, yes, I know that!"

"Good and beautiful for the sake of man; because man is the highest thing of creation and nearest to God. All things below him were created for his good; that is, God made them for him to use in sustaining the life of his body or the life of his soul."

"I don't see what use I can make of the moon and stars," said Amy.

"And yet," answered her mother, "you said only a minute ago that the beauty of this moon-light evening made you feel so quiet and happy."

"O, yes! That is so; and you were going to tell me why it was."

"First," said the mother, "let me, remind you that the moon and stars give us light by night, and that, if you happened to be away at a neighbor's after the sun went down, they would be of great use in showing you the path home-ward."

"I didn't think of that when I spoke of not seeing what use I could make, of the moon and stars," Amy replied.

Her mother went on,--

"God made everything that is good and beautiful for the stake of man, as I have just told you; and each of these good and beautiful things of creation comes to us with a double blessing,--one for our bodies and the other for our souls. The moon and stars not only give light this evening to make dark ways plain, but their calm presence fills our souls with peace. And they do so, because all things of nature being the work of God, have in them a likeness of something in himself not seen by our eyes, but felt in our souls. Do you understand anything of what I mean, Amy?"

"Just a little, only," answered the child. "Do you mean, mother dear, that God is inside of the moon and stars, and everything else that he has made?"

"Not exactly what I mean; but that he has so made them, that each created thin is as a mirror in which our souls may see something of his love and his wisdom reflected. In the water we see an image of his truth, that, if learned, will satisfy our thirsty minds and cleanse us from impurity. In the sun we see an image of his love, that gives light, and warmth, and all beauty and health to our souls."

"And what in the moon?" asked Amy.

"The moon is cold and calm, not warm and brilliant like the sun, which tells us of God's love. Like truths learned, but not made warm and bright by love, it shows us the way in times of darkness. But you are too young to understand much about this. Only keep in your memory that every good and beautiful thing you see, being made by God, reflects something of his nature and quality to your soul and that this is why the lovely, the grand, the beautiful, the pure, and sweet things of nature fill your heart with peace or delight when you gaze at them."

For a little while after this they sat looking out of the window, both feeling very peaceful in the presence of God and his works. Then voice was heard below, and Amy, starting up, exclaimed,"O, there is father!" and taking her mother's hand, went down to meet him.''', ''' Title:. The Open Window. "My aunt will be down presently, Mr. Nuttel," said a very self-possessed young lady of fifteen; "in the meantime you must try and put up with me."

Framton Nuttel endeavored to say the correct something which should duly flatter the niece of the moment without unduly discounting the aunt that was to come. Privately he doubted more than ever whether these formal visits on a succession of total strangers would do much towards helping the nerve cure which he was supposed to be undergoing

"I know how it will be," his sister had said when he was preparing to migrate to this rural retreat; "you will bury yourself down there and not speak to a living soul, and your nerves will be worse than ever from moping. I shall just give you letters of introduction to all the people I know there. Some of them, as far as I can remember, were quite nice."

Framton wondered whether Mrs. Sappleton, the lady to whom he was presenting one of the letters of introduction came into the nice division.

"Do you know many of the people round here?" asked the niece, when she judged that they had had sufficient silent communion.

"Hardly a soul," said Framton. "My sister was staying here, at the rectory, you know, some four years ago, and she gave me letters of introduction to some of the people here."

He made the last statement in a tone of distinct regret.

"Then you know practically nothing about my aunt?" pursued the self-possessed young lady.

"Only her name and address," admitted the caller. He was wondering whether Mrs. Sappleton was in the married or widowed state. An undefinable something about the room seemed to suggest masculine habitation.

"Her great tragedy happened just three years ago," said the child; "that would be since your sister's time."

"Her tragedy?" asked Framton; somehow in this restful country spot tragedies seemed out of place.

"You may wonder why we keep that window wide open on an October afternoon," said the niece, indicating a large French window that opened on to a lawn.

"It is quite warm for the time of the year," said Framton; "but has that window got anything to do with the tragedy?"

"Out through that window, three years ago to a day, her husband and her two young brothers went off for their day's shooting. They never came back. In crossing the moor to their favorite snipe-shooting ground they were all three engulfed in a treacherous piece of bog. It had been that dreadful wet summer, you know, and places that were safe in other years gave way suddenly without warning. Their bodies were never recovered. That was the dreadful part of it." Here the child's voice lost its self-possessed note and became falteringly human. "Poor aunt always thinks that they will come back someday, they and the little brown spaniel that was lost with them, and walk in at that window just as they used to do. That is why the window is kept open every evening till it is quite dusk. Poor dear aunt, she has often told me how they went out, her husband with his white waterproof coat over his arm, and Ronnie, her youngest brother, singing 'Bertie, why do you bound?' as he always did to tease her, because she said it got on her nerves. Do you know, sometimes on still, quiet evenings like this, I almost get a creepy feeling that they will all walk in through that window--"

She broke off with a little shudder. It was a relief to Framton when the aunt bustled into the room with a whirl of apologies for being late in making her appearance.

"I hope Vera has been amusing you?" she said.

"She has been very interesting," said Framton.

"I hope you don't mind the open window," said Mrs. Sappleton briskly; "my husband and brothers will be home directly from shooting, and they always come in this way. They've been out for snipe in the marshes today, so they'll make a fine mess over my poor carpets. So like you menfolk, isn't it?"

She rattled on cheerfully about the shooting and the scarcity of birds, and the prospects for duck in the winter. To Framton it was all purely horrible. He made a desperate but only partially successful effort to turn the talk on to a less ghastly topic, he was conscious that his hostess was giving him only a fragment of her attention, and her eyes were constantly straying past him to the open window and the lawn beyond. It was certainly an unfortunate coincidence that he should have paid his visit on this tragic anniversary.

"The doctors agree in ordering me complete rest, an absence of mental excitement, and avoidance of anything in the nature of violent physical exercise," announced Framton, who labored under the tolerably widespread delusion that total strangers and chance acquaintances are hungry for the least detail of one's ailments and infirmities, their cause and cure. "On the matter of diet they are not so much in agreement," he continued.

"No?" said Mrs. Sappleton, in a voice which only replaced a yawn at the last moment. Then she suddenly brightened into alert attention--but not to what Framton was saying.

"Here they are at last!" she cried. "Just in time for tea, and don't they look as if they were muddy up to the eyes!"

Framton shivered slightly and turned towards the niece with a look intended to convey sympathetic comprehension. The child was staring out through the open window with a dazed horror in her eyes. In a chill shock of nameless fear Framton swung round in his seat and looked in the same direction.

In the deepening twilight three figures were walking across the lawn towards the window, they all carried guns under their arms, and one of them was additionally burdened with a white coat hung over his shoulders. A tired brown spaniel kept close at their heels. Noiselessly they neared the house, and then a hoarse young voice chanted out of the dusk: "I said, Bertie, why do you bound?"

Framton grabbed wildly at his stick and hat; the hall door, the gravel drive, and the front gate were dimly noted stages in his headlong retreat. A cyclist coming along the road had to run into the hedge to avoid imminent collision.

"Here we are, my dear," said the bearer of the white mackintosh, coming in through the window, "fairly muddy, but most of it's dry. Who was that who bolted out as we came up?"

"A most extraordinary man, a Mr. Nuttel," said Mrs. Sappleton; "could only talk about his illnesses, and dashed off without a word of goodby or apology when you arrived. One would think he had seen a ghost."

"I expect it was the spaniel," said the niece calmly; "he told me he had a horror of dogs. He was once hunted into a cemetery somewhere on the banks of the Ganges by a pack of pariah dogs, and had to spend the night in a newly dug grave with the creatures snarling and grinning and foaming just above him. Enough to make anyone lose their nerve."

Romance at short notice was her speciality.''','''Title:The Selfish Giant. Every afternoon, as they were coming from school, the children used to go and play in the Giant's garden.

It was a large lovely garden, with soft green grass. Here and there over the grass stood beautiful flowers like stars, and there were twelve peach-trees that in the spring-time broke out into delicate blossoms of pink and pearl, and in the autumn bore rich fruit. The birds sat on the trees and sang so sweetly that the children used to stop their games in order to listen to them. "How happy we are here!" they cried to each other.

One day the Giant came back. He had been to visit his friend the Cornish ogre, and had stayed with him for seven years. After the seven years were over he had said all that he had to say, for his conversation was limited, and he determined to return to his own castle. When he arrived he saw the children playing in the garden.

"What are you doing here?" he cried in a very gruff voice, and the children ran away.

"My own garden is my own garden," said the Giant; "any one can understand that, and I will allow nobody to play in it but myself." So he built a high wall all round it, and put up a notice-board.

TRESPASSERS
WILL BE
PROSECUTED

He was a very selfish Giant.

The poor children had now nowhere to play. They tried to play on the road, but the road was very dusty and full of hard stones, and they did not like it. They used to wander round the high wall when their lessons were over, and talk about the beautiful garden inside. "How happy we were there," they said to each other.

Then the Spring came, and all over the country there were little blossoms and little birds. Only in the garden of the Selfish Giant it was still winter. The birds did not care to sing in it as there were no children, and the trees forgot to blossom. Once a beautiful flower put its head out from the grass, but when it saw the notice-board it was so sorry for the children that it slipped back into the ground again, and went off to sleep. The only people who were pleased were the Snow and the Frost. "Spring has forgotten this garden," they cried, "so we will live here all the year round." The Snow covered up the grass with her great white cloak, and the Frost painted all the trees silver. Then they invited the North Wind to stay with them, and he came. He was wrapped in furs, and he roared all day about the garden, and blew the chimney-pots down. "This is a delightful spot," he said, "we must ask the Hail on a visit." So the Hail came. Every day for three hours he rattled on the roof of the castle till he broke most of the slates, and then he ran round and round the garden as fast as he could go. He was dressed in grey, and his breath was like ice.

"I cannot understand why the Spring is so late in coming," said the Selfish Giant, as he sat at the window and looked out at his cold white garden; "I hope there will be a change in the weather."

But the Spring never came, nor the Summer. The Autumn gave golden fruit to every garden, but to the Giant's garden she gave none. "He is too selfish," she said. So it was always Winter there, and the North Wind, and the Hail, and the Frost, and the Snow danced about through the trees.

One morning the Giant was lying awake in bed when he heard some lovely music. It sounded so sweet to his ears that he thought it must be the King's musicians passing by. It was really only a little linnet singing outside his window, but it was so long since he had heard a bird sing in his garden that it seemed to him to be the most beautiful music in the world. Then the Hail stopped dancing over his head, and the North Wind ceased roaring, and a delicious perfume came to him through the open casement. "I believe the Spring has come at last," said the Giant; and he jumped out of bed and looked out.

What did he see?

He saw a most wonderful sight. Through a little hole in the wall the children had crept in, and they were sitting in the branches of the trees. In every tree that he could see there was a little child. And the trees were so glad to have the children back again that they had covered themselves with blossoms, and were waving their arms gently above the children's heads. The birds were flying about and twittering with delight, and the flowers were looking up through the green grass and laughing. It was a lovely scene, only in one corner it was still winter. It was the farthest corner of the garden, and in it was standing a little boy. He was so small that he could not reach up to the branches of the tree, and he was wandering all round it, crying bitterly. The poor tree was still quite covered with frost and snow, and the North Wind was blowing and roaring above it. "Climb up! little boy," said the Tree, and it bent its branches down as low as it could; but the boy was too tiny.

And the Giant's heart melted as he looked out. "How selfish I have been!" he said; "now I know why the Spring would not come here. I will put that poor little boy on the top of the tree, and then I will knock down the wall, and my garden shall be the children's playground for ever and ever." He was really very sorry for what he had done.

So he crept downstairs and opened the front door quite softly, and went out into the garden. But when the children saw him they were so frightened that they all ran away, and the garden became winter again. Only the little boy did not run, for his eyes were so full of tears that he did not see the Giant coming. And the Giant stole up behind him and took him gently in his hand, and put him up into the tree. And the tree broke at once into blossom, and the birds came and sang on it, and the little boy stretched out his two arms and flung them round the Giant's neck, and kissed him. And the other children, when they saw that the Giant was not wicked any longer, came running back, and with them came the Spring. "It is your garden now, little children," said the Giant, and he took a great axe and knocked down the wall. And when the people were going to market at twelve o'clock they found the Giant playing with the children in the most beautiful garden they had ever seen.

All day long they played, and in the evening they came to the Giant to bid him good-bye.

"But where is your little companion?" he said: "the boy I put into the tree." The Giant loved him the best because he had kissed him.

"We don't know," answered the children; "he has gone away."

"You must tell him to be sure and come here to-morrow," said the Giant. But the children said that they did not know where he lived, and had never seen him before; and the Giant felt very sad.

Every afternoon, when school was over, the children came and played with the Giant. But the little boy whom the Giant loved was never seen again. The Giant was very kind to all the children, yet he longed for his first little friend, and often spoke of him. "How I would like to see him!" he used to say.

Years went over, and the Giant grew very old and feeble. He could not play about any more, so he sat in a huge armchair, and watched the children at their games, and admired his garden. "I have many beautiful flowers," he said; "but the children are the most beautiful flowers of all."

One winter morning he looked out of his window as he was dressing. He did not hate the Winter now, for he knew that it was merely the Spring asleep, and that the flowers were resting.

Suddenly he rubbed his eyes in wonder, and looked and looked. It certainly was a marvellous sight. In the farthest corner of the garden was a tree quite covered with lovely white blossoms. Its branches were all golden, and silver fruit hung down from them, and underneath it stood the little boy he had loved.

Downstairs ran the Giant in great joy, and out into the garden. He hastened across the grass, and came near to the child. And when he came quite close his face grew red with anger, and he said, "Who hath dared to wound thee?" For on the palms of the child's hands were the prints of two nails, and the prints of two nails were on the little feet.

"Who hath dared to wound thee?" cried the Giant; "tell me, that I may take my big sword and slay him."

"Nay!" answered the child; "but these are the wounds of Love."

"Who art thou?" said the Giant, and a strange awe fell on him, and he knelt before the little child.

And the child smiled on the Giant, and said to him, "You let me play once in your garden, to-day you shall come with me to my garden, which is Paradise."

And when the children ran in that afternoon, they found the Giant lying dead under the tree, all covered with white blossoms.''')

story_telling=random.choice(story)

Speak(story_telling)