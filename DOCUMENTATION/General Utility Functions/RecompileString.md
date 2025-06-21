# Recompile String
Converts the `decompiled string` array back into a single string, `recompiled string`

## Notable Limitations
None

## Notable Usages
- Modifying an element in a string-array.
- A modified version of this is used for instance-specific item properties.

## Example
```
// Pseudocode

DecompileString("30;60;90", ";")
decompiledString[1] = 0
RecompileString(";")

print(recompiledString) // "0;60;90"

// This is helpful in conjunction with DecompiledString to edit string-arrays.
```