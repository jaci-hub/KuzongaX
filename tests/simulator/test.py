import random
from kuzongax.simulator.kuzongaenv_simulator import KuzongaEnvSimulator


if __name__ == "__main__":
    # given state
    state = {
        "s": 19,
        "d": 59,
        "a": {0: [0, 1, 2, 3, 4, 5, 6, 7, 8], 1: [2, 3, 4, 6, 7, 8, 9]},
        "p": [{'i': 0, 'c': -13, 'm': 1}],
        "t": 0
    }
    options = {
        'obs': state
    }
    #   set state
    kuzongaenv_simulator = KuzongaEnvSimulator()
    obs, info = kuzongaenv_simulator.reset(options=options)
    
    # create action
    division = bool(random.randint(0, 1))
    action = {
        "v": division,
        "g": int(random.randint(0, 9)) if not division else int(random.randint(2, 9)),
        "r": int(random.randint(0, 1)) if not division else None
    }
    # apply action
    obs, reward, done, trunc, info = kuzongaenv_simulator.step(action)
    obs = kuzongaenv_simulator._decode_state(obs)

    