# exospace-game
Open sourcing all the stuff for my Scratch game, Exospace.

## What is this?

This is open-sourcing all assets and everything for my Scratch game, Exospace.

You can find it [here](https://scratch.mit.edu/projects/1019880332/)

To run code found here, use the [Turbowarp editor or desktop editor](https://turbowarp.org/editor), as Scratch runs it way too slow.

## Can I contribute?

Kind of?

You can edit it, but the odds of me merging forks to `main` is low.

This is because Scratch stores everything as one big `.sb3` file, which means that it isn't really Github merge-compatible.

I would recommend using forks to create mods instead.

## Why is this repo a thing?

Recently, I found a bunch of old versions of Exospace, and it made me realize I really need to set up some sort of source control.

Also, it allows me to put out a bunch of creative files that aren't necessarily Scratch-compatible out here.

(For example, `.xcf` files are used by GIMP ([GNU Image Manipulation Program](https://www.gimp.org/)) for the creation of backgrounds,
but Scratch will not allow you to put them in the `.sb3`. However, being able to access this file allows you to access the various layers
of the background.)

Finally, just for the hope that someone will find it and try to mod it.

## Why Scratch?

For the longest time, my only computer was an old busted Chromebook that wouldn't allow any OS other than ChromeOS, and Scratch was the lowest
level online engine that I could find.

## What is going on with your disorganized, nonsensical code?

Great question!

- Part of it is disorganized because Scratch lacks classes, objects, or anything other than strings, booleans, numbers and arrays.

- Part of it is disorganized because Scratch also doesn't allow temporary variables.

- Part of it is disorganized because I would run into limitations mid-development, which would either require a big rewrite (to write clean code), or a quick patch (to make it work). Spoiler, I opted for a quick patch.

## Where do I start?

I suggest reading the documentation, and start simple. Maybe try adding a new type of tile?
