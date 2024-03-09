import numpy as np
from typing import Tuple

from .utils import temperature_schedule, sample_temperature, f


def sample_temperature_range(Q: np.ndarray):
    """Sample the temperature range for the annealing process.
    Pretty much exactly from https://github.com/jtiosue/qubovert/blob/master/qubovert/sim/_anneal_temperature_range.py

    Args:
        Q (np.ndarray): The QUBO matrix.

    Returns:
        Tuple[float, float]: The start and end time as a tuple.
    """
    start_flip_prob = 0.5
    end_flip_prob = 0.01

    factor = 2.0
    min_del_energy = factor * np.min(np.abs(Q)[np.nonzero(Q)])
    Q_full = Q.T + Q
    np.fill_diagonal(Q_full, np.diagonal(Q))
    max_del_energy = factor * np.max(np.sum(np.abs(Q_full), axis=0))

    t0 = -max_del_energy / np.log(start_flip_prob)
    t_end = -min_del_energy / np.log(end_flip_prob)
    return t0, t_end


def simulated_annealing(
    Q: np.ndarray, num_t_values: int, seed: int | None = None
) -> Tuple[np.ndarray, float]:
    """Simulated annealing with a computational complexity of O(n * t),
    where t is the number of timesteps.
    This is achieved by computing only the updated values which are at most
    n per update step.

    Args:
        Q (np.ndarray): The QUBO matrix.
        num_t_values (int): Number of update steps.

    Returns:
        Tuple[np.ndarray, float]: The best solutions and its energy.
    """
    rng = np.random.Generator(np.random.PCG64(seed=seed))

    # Create helper matrix
    n = Q.shape[0]
    Q_outer = Q + Q.T
    np.fill_diagonal(Q_outer, 0)

    # Random initial
    x = rng.integers(0, high=2, size=(n,))
    f_x = f(x, Q)

    t0, t_end = sample_temperature_range(Q)  # Sample randomly
    # t0, t_end, _ = sample_temperature(Q)  # Sample randomly

    # Create the inverted temperature values
    ts = temperature_schedule(
        t0=t0, t_end=t_end, num_t_values=num_t_values, generate_inverse=False
    )

    for t in ts:
        # Random flip in x
        idx = np.random.randint(n)
        idx = rng.integers(0, high=n)

        # Compute the difference between the flip and the previous energy
        sign = -(2 * x[idx] - 1)
        f_difference = sign * (np.dot(x, Q_outer[idx]) + Q[idx, idx])
        f_y = f_x + f_difference

        # Accept the new one if better (t is inverted beforehand)
        if f_y <= f_x or (np.exp(-(f_y - f_x) * t) > rng.uniform(0, 1)):
            x[idx] = 1 - x[idx]
            f_x = f_y

    return x, f_x


def simulated_annealing_slow(
    Q: np.ndarray, num_t_values: int, seed: int | None = None
) -> Tuple[np.ndarray, float]:
    """Classical simulated annealing with a computational complexity of O(n^2 * t),
    where t is the number of timesteps.
    This is achieved by computing only the updated values which are at most
    n per update step.

    Args:
        Q (np.ndarray): The QUBO matrix.
        num_t_values (int): Number of update steps.

    Returns:
        Tuple[np.ndarray, float]: The best solutions and its energy.
    """
    rng = np.random.Generator(np.random.PCG64(seed=seed))
    n = Q.shape[0]

    t0, t_end, _ = sample_temperature(Q)  # Sample randomly

    # Create the inverted temperature values
    ts = temperature_schedule(
        t0=t0, t_end=t_end, num_t_values=num_t_values, generate_inverse=False
    )

    # Random initial x
    x = rng.integers(0, high=2, size=(n,))
    f_x = f(x, Q)

    for t in ts:
        # Random flip in x
        idx = np.random.randint(n)
        x[idx] = 1 - x[idx]

        # Compute differences
        f_y = f(x, Q)

        # Accept the new one if better
        if f_y <= f_x or (np.exp(-(f_y - f_x) * t) > np.random.uniform()):
            f_x = f_y
        else:
            # Otherwise flip back
            x[idx] = 1 - x[idx]

    return x, f_x
