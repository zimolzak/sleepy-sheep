from random import choice, sample

numbers = [
    ['house of fun', 'baby bun', 'flying nun', 'infant son', 'burning sun', 'rabbit run'],
    ['house of fun', 'baby bun', 'flying nun', 'infant son', 'burning sun', 'rabbit run'],
    ['drop of dew', 'scooby doo', 'big to-do', 'tall bamboo', 'blue canoe'],
    ['giant tree', 'bumble bee', 'wheel of brie', 'sounding sea', 'new TV', 'apple tree'],
    ['old barn door', 'big boat oar', 'wild boar', 'apple core', 'mushroom spore', 'red barn door'],
    ['big bee hive', 'sour cream and chive', 'old bee hive'],
    ['pile of sticks', 'ton of bricks', 'muffin mix', 'candle wicks', 'stack of sticks'],
    ['rose of heaven', 'bread with leaven', 'epitaph of Stevin'],
    ['heavy weight', 'twist of fate', 'wooden crate', 'iron grate', 'tall green gate'],
    ['twisty vine', 'bottle of wine', 'friend of mine', 'crooked line', 'Norway pine', 'cucumber vine']
    ]

arbitrary = [
    ['eggs go crack', 'ducks go quack'],
    ['kitty cats mew', 'skunks go spew', 'owls go whoo'],
    ['swallows swoop', 'barn owls whoop', 'planes do loops'],
    ['dogs go woof', 'babies eat poofs', 'horses take hoof'],
    ['bunnies jump', 'politicians stump', 'camels hump'],
    ['rain goes drip', 'scissors snip', 'terriers yip'],
    ['fat cats snore', 'apples have cores', 'weevils bore', 'mouse explores', 'old dog snores'],
    ['doorknobs twist', 'mills have grist'],
    ['birdies perch', 'spotlights search', 'priests have church'],
    ['bees go buzz', 'peaches have fuzz'],
    ['hummingbirds hum', 'hands have thumbs', 'pirates drink rum', 'bees hum', 'crickets strum'],
    ['birdies tweet', 'babies have feet', 'cats eat meat', 'hungry things eat', 'millers grind wheat'],
    ['puppies sigh', 'cats close their eyes', 'birdies fly'],
    ['kitty cats purr', 'gears go whirr', 'dogs have fur', 'kitten stirs', 'gray cat purrs'],
    ['raccoons chirp', 'babies burp'],
    ['long grass bends', 'spider mends'],
    ['wind sighs', 'whippoorwill cries'],
    ['blossoms close', 'ducklings doze'],
    ['fireflies blink', 'first stars wink'],
    ['cattails swish', 'herons fish']
    ]

samp_arb = sample(arbitrary, 11)
for i in range(10,0,-1):
    rhymes_next = choice(numbers[i-1])
    print(i)
    print(i, 'sheep jump by the', rhymes_next)
    print('\n'.join(sample(samp_arb[i], 2)))
    print('Sleep, sheep.\nNow there are...')
    print()
print('None!')
