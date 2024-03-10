## Preface

The usage of the library usually follows the following pattern:

1. Create a loop using one of the factory functions (which return a `Loop` instance).
1. Apply one or more modifier methods (in a method chaining style) to customize the looping behaviour.
1. Finally, consume the loop, for example using a `for` statement. 

## Factory Functions

::: loop.loop_over

::: loop.loop_range

## Modifier Methods

::: loop.Loop.map

::: loop.Loop.filter

::: loop.Loop.next_call_with

::: loop.Loop.returning

::: loop.Loop.show_progress

::: loop.Loop.concurrently

## Consumer Methods

::: loop.Loop.__iter__

::: loop.Loop.exhaust

::: loop.Loop.reduce
