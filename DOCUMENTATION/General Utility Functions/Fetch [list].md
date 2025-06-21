# Fetch \[list\]
Essentially just a higher-powered

Returns data through the `fetch` list.

## Notable Limitations
Only one object can be fetched at once, as there is only one `fetch` list.

Also, not every data list has a fetch function, because you rarely need every property of a tile at once.
Mostly just for players and sprites.

## Notable Usages
Getting every property from an object

## Example
```
// Pseudocode

dataPerBuff = 2
BuffData = [
    "Stunned",
    "You're stuck in place!",
    "Invisible",
    "You're see-through!
]

// NOTE: fetch function is not actually present for buffs in-game.
// It is just for demonstration purposes; in-game it's mostly used for
// sprite properties.

FetchBuff(1)
print(fetch) // ["Stunned", "You're stuck in place!"]

FetchBuff(2)
print(fetch) // ["Invisible", "You're see-through!"]

// This is used pretty much everywhere in Exospace. It's basically the function that allows you to have objects.
```