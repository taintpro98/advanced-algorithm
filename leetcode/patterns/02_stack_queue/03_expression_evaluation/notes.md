# Expression Evaluation

## What This Subtopic Is About

Expression evaluation uses stacks to parse and compute arithmetic expressions, handle operator precedence, and convert between notations. This pattern is fundamental for implementing calculators, compilers, and interpreters.

## Typical Patterns & Invariants

- **Operator stack**: Track operators with precedence handling
- **Operand stack**: Store numbers for computation
- **Shunting yard algorithm**: Convert infix to postfix notation
- **Precedence rules**: Higher precedence operators evaluated first
- **State machine**: Handle digits, operators, and parentheses systematically

## How to Recognize This Type of Problem

- Calculator implementation problems
- Expression parsing with operators and parentheses
- Evaluating mathematical or logical expressions
- String-to-number conversion with operations
- Problems involving operator precedence

## LeetCode Problems

- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)
- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
- [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
