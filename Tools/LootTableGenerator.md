# Loot Table Generator
> NOTE: All prompts are case-sensitive.

When first running this script, it will ask if you wish to load a loot table.
If you want to modify an existing one, type `Y`. Otherwise, type `N`.

The way a loot table works is that each 'entry' (aka 'item') has a certain probability of being chosen.
If it is chosen, it rolls a random amount between the specified min/max amounts.

So, to add your item, type `Add Item`. Then, it will prompt you for either the name or sprite of the item. The 'sprite' is the costume name of the item, and the 'name' is the name as appears. For example, Gemfruit could either be represented by "Gemfruit" or `fruit`.

> NOTE: Some costume names don't match with the item names (like Gemfruit being internally known as `fruit`.)

Next, it will prompt you to specify the count of the item.

- `Fixed Count` makes the item drop in a fixed quantity
- `Min Max` selects a random number between a minimum and maximum value.

Finally, it will prompt you to specify how common this is. A value of `1` represents a guaranteed drop (100%), and a value of `0` represents an impossible drop (0%).

It will confirm with you that you wish to add
- Item (confirms using internal item ID)
- Count (structured as `min`..`max`)
- Chance (represented as a percentage)

If something looks wrong, then type `N` and start over. If this looks correct, type `Y`. This will bring you back to the first menu, asking if you would like to add a new item or quit.

If you want to add a new item to the table, type `Add Item` and do it again. If you're happy with your loot table, type `Exit`. This will end in it telling you the final string-array that represents your loot table.