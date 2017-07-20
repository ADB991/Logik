# Writing a formal logic agent
### WORK IN PROGRESS

Final aim is to write an agent class that is given symbols, axioms and rules (and possibly sugar) and goes and explores the space of theorems.

Started off wanting to write it for propositional logic, but there is a lot to handle, so I moved to Douglas Hofstadter’s [MU system](https://en.wikipedia.org/wiki/MU_puzzle) instead, which is much, much simpler.

For now, I simply an explore() function which explores all theorems breadth-first.

I want something a little more generalisable, so I am writing some classes in a LogicTypes file. For the moment I simply wrote very simple Theorem and Axiom classes.