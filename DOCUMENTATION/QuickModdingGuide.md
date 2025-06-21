# Quick Modding Start Guide
Okay, so if you want to know HOW this whole show works, this guide is not for you.

However, if you're just here to mod it and get out, this guide should do the trick.

## Adding a new tile

Okay, so to add a new tile you want to go to the `DefineTiles` function under the `Tiles/Items` sprite.

Add a new `AddTileType` block at the ***end*** of the big stack o' blocks.

Here's what each parameter does.

- `type`: The costume that this tile uses.
- `canCol`: Whether or not this tile is solid.
- `specialType`: Whether this is a 'special' tile. Each number represents a different behaviour.
    1. Fluid (flows)
    2. Seed (grows)
- `breakTime`: The time, in seconds, that this tile takes to break with no item.
- `breakToolTag`: The tool tag that this tile is 'vulnerable' to. For example, stone's `breakToolTag` is `pickaxe`.
- `breakToolTier`: The minimum tool tier required for this tile to drop its loot when broken.
- `lootTable`: The loot table that is dropped when this block is broken.
> NOTE: `lootTable` on seed-like tiles (tiles with `specialType` set to 2) instead dictates which types of tiles this can grow into.
- `airBehaviour`: Special behaviours related to this tile being suspended in mid-air. Each number represents a different behaviour.
    1. If there is no solid block under this one, destroy it and drop loot.
    2. If there is no solid block under this one, make it affected by gravity.
    3. If the tile above this one is nonsolid and is not the same type as this tile, then drop this tile as if it were broken.
    4. If the tile below this one is nonsolid and is not the same type as this tile, then drop this tile as if it were broken.
- `transparency`: Is technically the opposite of transparency (opacity). This number is how much the light level is reduced by when the light travels over this block. (max light level is 10, min is 0)
- `lightEmissionLevel`: How much light this tile emits. Leave this space blank if it eemits no light.
- `allowLazyRendering?`: Whether or not to draw walls behind this block. Set this to true for completely solid blocks (no transparent pixels).
- `fertility`: If not blank, allows seeds to grow on this block. It's also a multiplier for how fast the seeds grow - moss has a fertility of 1, rich soil has a fertility of 1.75.