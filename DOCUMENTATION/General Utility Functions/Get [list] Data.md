# Get \[list\] Data
Several forms of this are present as `GetTileData`, `GetItemData`, or `GetBuffData`. Gets a property of a certain tile/item/buff.

Returns data through the `data` variable.

## Notable Limitations
There's only one data return variable, so you can't get multiple data values at once, unless you store the first data in a seperate variable first.

## Notable Usages
Getting data of an 'object'

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

GetBuffData(1,2) // "You're stuck in place!"
print(data)

GetBuffData(2,1) // "Invisible"
print(data)

// This is used pretty much everywhere in Exospace. It's basically the function that allows you to have objects.
```