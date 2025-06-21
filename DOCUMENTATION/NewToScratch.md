# New to Scratch? Start Here! [CHAPTER 0]
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
- You cannot pass this in anywhere. If you have a PickupItem() function, you wouldn't be able to pass this in as a parameter. (see rule #5)
- There's a nested array present (the properties array), which doesn't work. Remember, you would need to do 'add (properties) to \[item v\]', but properties is an array, and thus could not be passed in. (see rule #5)
- You could not create an array at runtime (see rule #1)

## Workaround

So, there's a problem. We want an object with properties, but Scratch can't store objects.
We want nested arrays, but Scratch doesn't support that either.
Finally, we want to be able to pass this 'object' in to functions.

One problem at a time.

## Objects with Properties

There are two workarounds that I frequently use in tandem.

### Storing Arrays as Strings

I've seen this occasionally used in data storage.