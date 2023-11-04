# Format-Preserving Encryption

Given a set of integers $S = \{0, \ldots, n-1\}$ for $n \in \mathbb{N}$, we seek a bijective function $\delta: S \to S$ that induces some random permutation of $S$. $\delta$ must be easy to compute without having to permute and store the whole set, and the permutation must appear random.

The aim of this repository is to try out different methods that implement such a $\delta$.

The problem is very similar to format-preserving encryption, but the latter also requires strong cryptographic properties, which we don't.

An ideal solution would have the following properties:

* $\delta$ is efficient to compute.
* The sequence $\delta(0), \delta(1), \ldots, \delta(n-1)$ looks random in that $\delta$ is hard to deduce.
* No big dependencies on other libraries.

An experiment yields the following mean computation times per call for each algorithm. 10.000 calls were made for $N = 1.000.000$.

| Algorithm         | Configuration | Time [ms] |
|-------------------|---------------|----------:|
| FF3               | -             |     < 0,1 |
| Shifting Numbers  | -             |     22,21 |
| Thorp Shuffle     | 5.000 rounds  |      1,04 |
| $\mathbb{Z}$ Ring | $p=1.000.003$ |     < 0,1 |


## FF3

This uses the FF3 format-preserving encryption algorithm.

Properties:

* Fast to compute.
* Result is very secure.
* Dependency on crypto libraries.


## Shifting Numbers

The basic idea of this algorithm is that $S$ is permuted by applying several rounds of shifting operations. In each round $r = 2, \ldots, \lfloor n/2 \rfloor$, we consider all numbers at indices $i$ where $i+1$ is a multiples of $r$ (for example, in round $3$, we consider numbers at indices $2, 5, \ldots$) and perform a cyclic shift: the number at index $i$ ends up at index $i + r$, with the number at the highest index circling back to index $r-1$.

To compute $\delta(i)$, we don't actually perform all the shifting on the potentially large sequence of numbers. Instead, we only trace what will happen to $i$ throughout the rounds and return the index it finally ends up in.

Properties:

* As $n$ increases, the number of rounds increases linearly. The whole thing is comparatively slow.
* The permutation does look rather random.


## Thorp Shuffle

The Thorp Shuffle understands $S$ as a deck of an even number of cards and applies several rounds of shuffling. Each round divides the deck into a left and a right half. It produces a new full deck by adding the bottommost cards of each half to the new deck, either from the left or from the right deck first. This decision is informed by a source of randomness, which in this implementation is a key (a sequence of bits) to keep things deterministic.

Properties:

* Comparatively slow.
* The apparent randomness of the induced permutation is highly dependend on the number of rounds.


## $\mathbb{Z}$ Ring

We consider $S = \{0, \ldots, p-1$ with $p \geq n\}$ prime. $S$ is the multiplicative group module $p$. $\phi(i) = (a \cdot i + b) \mod p$, $0 < a,b < p$, is a bijection on $S$ **(WHY???)**.

In general, $n$ won't be prime, so $p > n$. This implies that for certain $i \in S$, $\phi(i) \geq n$ as well. This, however, is no problem. Since $f$ is bijective, we can iterate until we get a result $< n$.

Properties:

* Extremely fast to compute (provided that $p$ is sufficiently close to $n$).
* The apparent randomness of the induced permutation is highly dependend on the choices of $a$ and $b$. In particular, small $a$ won't help. $a$ should probably be $> p/2$.
* Might be easy to reverse-engineer.
