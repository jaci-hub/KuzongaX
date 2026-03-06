from gymnasium.envs.registration import register

register(
    id="KuzongaX-v0",
    entry_point="kuzongax.envs.kuzongax:KuzongaX",
)