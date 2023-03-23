# SymbolicComputing

## Integer Arithmetic
- Karatsuba's multiplication algorithm
- Extended Euclidean algoritm

## Integer Factorization
- Wheel factorization

## Modular Arithmetic
- Find multiplicative inverse with Extended Euclidean algorithm

## Prime Numbers
- Sieve of Eratosthenes
- Pritchard's Wheel Sieve
- Rabin-Miller Test
- Lucas primality test

## Polynomial Arithmetic
- Kronecker's method to factor a polynomial $a(x) \in \mathbb{Z}[x]$ such that $a(0) \neq 0$
- Lensta-Lenstra-Lov&aacute;sz lattice basis reduction algorithm

Steps:
  - [x] Binary tree data structure for expression tree
    - [x] non-recursive inorder traversal
  - [x] Interpret mathematical expression into postfix expression
  - [x] Generate expression tree from postfix expression
  - [ ] unit testing
    - [ ] infix expression to postix expression
    - [ ] postfix expression to expression tree
    - [ ] expression tree inorder traversal
  - [ ] simplification techniques (https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html)
    - [ ] polynomial expansion
    - [ ] polynomial factorization
    - [ ] collect common powers
    - [ ] rational function cancellation, p/q with no common factors
    - [ ] partial fraction decomposition of rational functions
    - [ ] trigonemetric identities
    - [ ] powers identities
    - [ ] exponential and logarithmic identities
  - [ ] utility functions
    - [ ] is polynomial irreducible?
    - [ ] expression tree evaluation
