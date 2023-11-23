# Description
Just a trivial sovler for logical formulas containing the operators AND, OR, IMPLIES, EQUIV and NOT, to double check my CS Homework

# How to use
Use the function `logical_satisfiability(formula)`
## Params
### Formula
A `list` that contains the formula in polish notation, where every argument and operator is a string or a boolean.

#### Operators
- $\land$: `"AND"`
- $\lor$: `"OR"`
- $\neg$: `"NOT"`
- $\rightarrow$: `IMPLIES`
- $\leftrightarrow$: `EQUIV`

#### Example
- $a \land b \land c$: `["AND", "a", "b", "c"]`
- $(a \rightarrow b) \lor \neg c$: `["OR", ["IMPLIES", "a", "b"], ["NOT", "c"]]`

*Further Examples in main program...*

## Returns
Nothing. Just prints.

# Runtime
$\mathcal{O}(2^{n}+m)$ where $n$ is the number of different variables and $m$ the number of total variables.
