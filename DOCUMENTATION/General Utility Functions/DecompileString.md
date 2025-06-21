# Decompile String
Seperates a string into an array, with each element being seperated by a specified character.

## Notable Limitations
- Intensive and inefficient.
- Can accidentally add more elements if seperation character is present in text.

## Notable Usages
As a way to store an array, either for passing into a function or for storing in an array.

## Example
```
// Pseudocode

DecompileString("Hello;33|World.329|320;50", ";")
print(decompiledString) // ["Hello", "33|World.329|320", "50"]

DecompileString("Hello;33|World.329|320;50", "|")
print(decompiledString) // ["Hello;33", "World.329", "320;50"]

DecompileString("Hello;33|World.329|320;50", ".")
print(decompiledString) // ["Hello;33|World", "329|320;50"]

// The point of this is to show how one string can have multiple outputs depending on the seperation character used.
```