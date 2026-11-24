from random import random
import numpy as np
import math


BASIC_DNA_MUTATION_TABLE = {
    'A': [0.1, 0.3, 0.3, 0.3],
    'C': [0.3, 0.1, 0.3, 0.3],
    'G': [0.3, 0.3, 0.1, 0.3],
    'T': [0.3, 0.3, 0.3, 0.1],
}


def ep_pcr(wt, num, rate, mutation_table=BASIC_DNA_MUTATION_TABLE):
    """
    Simulate error-prone PCR to generate DNA mutants.

    Args:
        wt (str): Wild-type DNA sequence.
        num (int): Number of mutants to generate.
        rate (float): Mutation rate per base.
        mutation_table (dict): Mutation probability table for each base.

    Yields:
        str: Mutant DNA sequence.
    """
    for _ in range(num):
        mutant = list(wt)
        for i in range(len(mutant)):
            if random() < rate:
                p = mutation_table[mutant[i]]
                mutant[i] = np.random.choice(['A', 'C', 'G', 'T'], p=p)
        yield ''.join(mutant)


def generate_barcodes(length, num):
    """
    Generate random DNA barcodes of specified length and number.

    Args:
        length (int): Length of each barcode.
        num (int): Number of barcodes to generate.
    
    Returns:
        Generator[str, None, None]: A generator yielding barcode strings.
    """
    print(f"Generating {num} barcodes of length {length}. Collision probability: {collision_prob_exact(num, length)}")
    for _ in range(num):
        barcode = ''.join(np.random.choice(['A', 'C', 'G', 'T'], size=length))
        yield barcode


def collision_prob_exact(n: int, k: int, alphabet: int = 4) -> float:
    r"""
        Birthday problem:
        Accurate formulation:
        $$P(N, K) = 1 - \prod_{i=0}^{N-1} \left(1 - \frac{i}{4^K}\right) = 1 - \frac{(4^K)!}{(4^K - N)! \cdot (4^K)^N}$$
        
        Approximation for very small P:
        $$P(N, K) \approx \frac{N(N-1)}{2 \cdot 4^K}$$
    """
    if n <= 1:
        return 0.0
    d = alphabet ** k
    if n > d:
        return 1.0
    log_no_collision = sum(math.log1p(-i / d) for i in range(n))
    return -math.expm1(log_no_collision)
