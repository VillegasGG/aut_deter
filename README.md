# Deterministic finite automaton 🔍

## Description
Implementation of a **deterministic automaton**.
The automaton moves between states according to the labels defined in the transitions.
Its objective is to evaluate whether the string is accepted or not.

## Algorithm
The algorithm goes through the input string character by character, and goes through the respective labels of the graph.
The automaton starts in an initial state and, upon finishing reading the string, verifies whether an acceptance state has been reached.

## Example

### Input
String to evaluate: 0 1 1 0 1 1

### Automaton Image
![Automaton Diagram](example.png)

### Output
**Accepted string**

Explanation: Since the initial state is q1, the string reaches the accepting state q3.

