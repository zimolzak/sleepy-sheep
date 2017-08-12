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
    ['Eggs go crack.', 'ducks go quack'],
    ['Kitty cats mew.', 'Skunks go spew.', 'Owls go whoo.'],
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
    ['Puppies sigh.', 'Cats close their eyes.', 'Birdies fly.'],
    ['Kitty cats purr.', 'Gears go whirr.', 'Dogs have fur.', 'Kitten stirs.', 'Gray cat purrs.'],
    ['Raccoons chirp.', 'Babies burp.'],
    ['Long grass bends.', 'Spider mends.'],
    ['Wind sighs.', 'Whippoorwill cries.'],
    ['Blossoms close.', 'Ducklings doze.'],
    ['Fireflies blink.', 'First stars wink.'],
    ['Cattails swish.', 'Herons fish.']
    ]

samp_arb = sample(arbitrary, 11)
recap = []
for i in range(10,1,-1):
    rhymes_next = choice(numbers[i-1])
    recap.append(rhymes_next)
    rhymes_next = rhymes_next.replace('(','').replace(')','')
    print(i)
    print(i, 'sheep jump\nby the', rhymes_next + '.')
    print('\n'.join(sample(samp_arb[i], 2)))
    print('Sleep, sheep.\nNow there are...')
    print()

print("""1
One sheep bleats,
"Mama, I can't sleep."
"Hush," says her mama.
"Have you tried counting sheep?" """)

for s1 in recap:
     s2 = re.sub('.*\(', '', s1)
     noun = re.sub('\).*', '', s2)
     print("One by the " + noun)

print("""
and one sheep in
the grass knee-deep,
nestled by her mama,
fast asleep.""")
