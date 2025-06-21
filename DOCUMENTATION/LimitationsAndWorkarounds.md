# New to Scratch? Start Here!
> NOTE: There is not a great way to represent Scratch code, so I will be using pseudocode.

Okay, so this guide assumes that you've written in some other language like Javascript, Typescript, Python, Lua, C#, etc.
So, what's the deal with Scratch? What makes it so annoying?
For starters...

**DATA STRUCTURES.**

Unlike actual languages, Scratch is meant as an introduction.

For whatever reason, this means that...
1. Temporary variables do not exist.
2. Functions cannot return values.
3. Only strings, booleans, and numbers can be represented by the orange variable blocks.
4. Only arrays can be represented by the scarlet variable blocks.
5. You cannot pass arrays in as parameters to functions (or anything, really), basically meaning that you can't reference an array outside of getting, setting, replacing and inserting items.
6. Arrays cannot contain arrays, only numbers, strings, and booleans
7. Variable 'types' are just non-arrays (numbers, strings, and booleans) and arrays. No further differentiation.
8. Arrays are one-indexed

> QUICK NOTE: Limit #2 can easily be bypassed by creating a variable dedicated to being the return value for that function, and then setting that variable in the function.
> An example would be
> ```
> // Psuedocode
> var helloReturn
>
> define hello(num1, num2):
>   helloReturn = num1+num2
>
> hello(5, 5)
> print(helloReturn)
> ```
> This will cause problems later, but we'll cross that bridge when we come to it.
> (see "General Utility Functions/Get \[list\] data" for more information.)

**NOTE: Throughout this piece, I will be referencing these rules by number.**

## Why this Matters

This may not seem horrible at first, but here's an example of why it's such a pain.

Let's say we want to create an item with 3 properties, one of which is an object in of itself.


Instead of:

```
// JS
let item = {
    name: "Iron Pickaxe",
    toolTag: "pickaxe",
    properties: {
        maxDurability: 100,
        durability: 75
    }
}
```

...which is simple, elegant, and readable, you have to do a really, *really* hacky workaround.

So basically, there are multiple problems.
For one, if we were to represent it in an array, we run into multiple problems.

```
[
    "Iron Pickaxe",
    "pickaxe",
    [
        100,
        75
    ]
]
```

The problems here are that:
- You cannot pass this in anywhere. If you have a `PickupItem()` function, you wouldn't be able to pass this in as a parameter. (see rule #5)
- There's a nested array present (the properties array), which doesn't work. (see rule #6)
- You could not create an array at runtime (see rule #1)

## Workaround

So, there's a problem. We want an object with properties, but Scratch can't store objects.
We want nested arrays, but Scratch doesn't support that either.
Finally, we want to be able to pass this 'object' in to functions.

One problem at a time.

## Objects with Properties

There are two workarounds that I frequently use in tandem.

### Storing Arrays as Strings

I've seen this occasionally used in *actual* data storage, though it's not usually considered best practice.
You can store an array as a string by formatting it like...

```
// Pseudocode
array = ["HelloWorld", 123, false]
string = "HelloWorld|123|false"
```

...and then use the character `|` to seperate it back into an array.

> NOTE:
> Scratch doesn't care about typing, so this means that "123" can act as the number 123 or the string "123" depending on which function it's passed in to.
> This also means that we don't have to worry about typing of things in the decompiled string.

> **IMPLEMENTATION:**
> Most Scratch sprites in Exospace use this through two functions.
>
> `DecompileString(str, char)` seperates `str` into array `decompiled string` based off of `char`.
>
> `RecompileString(char)` compiles `decompiled string` into `recompiled string` based off of `char`.
>
>> NOTE: This is one workaround to passing in arrays for parameters: you can just pass in a string.
> 
> ```
> // Pseudocode
>
> DecompileString("HelloWorld|123|false", "|")
>
> print(decompiledString[1]) // HelloWorld
> print(decompiledString[2]) // 123
> print(decompiledString[3]) // false
> ```
>> NOTE: Scratch is 1-indexed
>
> ```
> // Pseudocode
> decompiledString = ["HelloWorld", 123, false]
>
> RecompileString(";")
> 
> print(recompiledString) // "HelloWorld;123;false"
> ```

This seems to work fine in any instance, so why do I use the other method?
It all comes down to performance.

**`DecompileString()` loops through every character of the entire string**

So, if I were to use this in place of arrays EVERY TIME, Exospace would run at 1 fps.
Most of the time, just defining a global array works (like for tiles).

## Storing Objects as Arrays

Exospace uses a lot of 'objects', so the previous approach would absolutely TANK performance.
So, with credit to [@Griffpatch on Scratch](https://scratch.mit.edu/users/Griffpatch), I present the system for storing objects in arrays.

Say that you want 100 different TileType objects, each with 4 properties.
The previous approach would be to store each TileType in an array, like so.

```
// Pseudocode

var TileTypes = [
    "property1;property2;property3;property4",
    "property1;property2;property3;property4",
    "property1;property2;property3;property4",
    "property1;property2;property3;property4",
    // ...repeat for 96 more lines...
]

var propertyReturn

// Note that you can pass a tile type in, because it
// is a string.
define getPropertyOfTileType(propertyIndex, tileType):
    DecompileString(tileType, ";")
    propertyReturn = decompiledString[propertyIndex]
```

However, if you need to call `getPropertyOfTileType(propertyIndex, tileType)` *30 times a frame*, then you can expect performance to tank or crash.

So, here's the strategy.
Store multiple objects in one array.

So long as you know how many properties are in each item, you can do something like...

```
// Pseudocode

var dataPerTile = 4

var TileData = [
    "property1OfTile1",
    "property2OfTile1",
    "property3OfTile1",
    "property4OfTile1",
    "property1OfTile2",
    // ...repeat 395 times...
]

var propertyReturn

define getPropertyOfTileType(tileTypeIndex, dataIndex):
    propertyReturn = TileData[(tileTypeIndex - 1) * dataPerTile + dataIndex]

define addTileType(property1, property2, property3, property4):
    add (property1) to [TileData v]
    add (property2) to [TileData v]
    add (property3) to [TileData v]
    add (property4) to [TileData v]
```

This has the bonus of *NOT* crashing your computer, because it doesn't need a loop. Unfortunately, this means that each object has to have a fixed amount of properties.
It can also be applied to item data, UI data, object data, and enemy template data.

> NOTE: You've probably noticed that a lot of this is numbers-based (more specifically, a lot of indicies). Get used to this.
> (If you haven't noticed: the properties don't have names, they have indexes; the tile types are represented with indexes; etc.)

## Problem Solved!

So, using the Iron Pickaxe example,

```
// JS
let item = {
    name: "Iron Pickaxe",
    toolTag: "pickaxe",
    properties: {
        maxDurability: 100,
        durability: 75
    }
}
```

...you could represent this in Scratch as...

```
// Pseudocode
var dataPerItem = 3

ItemData = [
    "Iron Pickaxe",
    "pickaxe",
    "maxDurability;100;durability;75"
]
```

### CONGRATULATIONS!
If you're still with me, congrats. You've realized how bad of an idea modding is. If you still want to give it a shot, there's further documentation for a reason.