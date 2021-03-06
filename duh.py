from random import choice, sample
import re

numbers = [
    ['(house) of fun', 'baby (bun)', 'flying (nun)', 'infant (son)', 'burning (sun)', '(rabbit run)'],
    ['(house) of fun', 'baby (bun)', 'flying (nun)', 'infant (son)', 'burning (sun)', '(rabbit run)'],
    ['drop of (dew)', '(scooby doo)', 'big (to-do)', 'tall (bamboo)', 'blue (canoe)'],
    ['giant (tree)', 'bumble (bee)', 'wheel of (brie)', 'sounding (sea)', 'new (TV)', 'apple (tree)'],
    ['old barn (door)', 'big boat (oar)', 'wild (boar)', 'apple (core)', 'mushroom (spore)', 'red barn (door)'],
    ['big bee (hive)', '(sour cream and chive)', 'old bee (hive)'],
    ['pile of (sticks)', 'ton of (bricks)', 'muffin (mix)', 'candle (wicks)', 'stack of (sticks)'],
    ['(rose) of heaven', '(bread) with leaven', '(epitaph) of Stevin'],
    ['heavy (weight)', '(twist) of fate', 'wooden (crate)', 'iron (grate)', 'tall green (gate)'],
    ['twisty (vine)', 'bottle of (wine)', '(friend) of mine', 'crooked (line)', 'Norway (pine)', 'cucumber (vine)']
    ]

arbitrary = [
    ['Eggs go crack.', 'Ducks go quack.'],
    ['Kitty cats mew.', 'Skunks go spew.', 'Owls go whoo.', 'Lilies gather dew.'],
    ['Swallows swoop.', 'Barn owls whoop.', 'Planes do loops.'],
    ['Dogs go woof.', 'Babies eat poofs.', 'Horses take hoof.'],
    ['Bunnies jump.', 'Politicians stump.', 'Camels hump.'],
    ['Rain goes drip.', 'Scissors snip.', 'Terriers yip.'],
    ['Fat cats snore.', 'Apples have cores.', 'Weevils bore.', 'Mouse explores.', 'Old dog snores.'],
    ['Doorknobs twist.', 'Mills have grist.'],
    ['Birdies perch.', 'Spotlights search.', 'Priests have church.'],
    ['Bees go buzz.', 'Peaches have fuzz.'],
    ['Hummingbirds hum.', 'Hands have thumbs.', 'Pirates drink rum.', 'Bees hum.', 'Crickets strum.'],
    ['Birdies tweet.', 'Babies have feet.', 'Cats eat meat.', 'Hungry things eat.', 'Millers grind wheat.'],
    ['Puppies sigh.', 'Birdies fly.'],
    ['Kitty cats purr.', 'Gears go whirr.', 'Dogs have fur.', 'Kitten stirs.', 'Gray cat purrs.'],
    ['Raccoons chirp.', 'Babies burp.'],
    ['Long grass bends.', 'Spider mends.'],
    ['Wind sighs.', 'Whippoorwill cries.', 'Cats close their eyes.'],
    ['Blossoms close.', 'Ducklings doze.'],
    ['Fireflies blink.', 'First stars wink.', 'Philosophers think.'],
    ['Cattails swish.', 'Herons fish.']
    ]

actions = 'leap jump race romp roam scoot amble splash lope'.split()
num_words = 'Zero One Two Three Four Five Six Seven Eight Nine Ten'.split()
samp_act = sample(actions, 9)
samp_arb = sample(arbitrary, 9)
recap = []

print("""A randomly generated parody of "Ten Sleepy Sheep" by Phyllis Root

"Time to sleep,"
call the mama sheep
in the grass knee-deep.
But ten little sheep
don't want to sleep.
""")

for i in range(10,1,-1):
    rhymes_next = choice(numbers[i-1])
    recap.append(rhymes_next)
    rhymes_next = rhymes_next.replace('(','').replace(')','')
    print(i)
    print(num_words[i], 'sheep', samp_act[i-2])
    print(choice(['past', 'by']), 'the', rhymes_next + '.')
    print('\n'.join(sample(samp_arb[i-2], 2)))
    if i != 2:
        print('Sleep, sheep.\nNow there are...')
    else:
        print('Sleep, sheep.\nNow there is...')
    print()

print("""1
One sheep bleats,
"Mama, I can't sleep."
"Hush," says her mama.
"Have you tried counting sheep?" """)

for s1 in recap:
     s2 = re.sub('.*\(', '', s1)
     noun = re.sub('\).*', '', s2)
     print("One by the " + noun + ',')

print("""
and one sheep in
the grass knee-deep,
nestled by her mama,
fast asleep.""")
