from irl_benchmark.experiment.run import Run
from irl_benchmark.irl.algorithms.mce_irl import MaxCausalEntIRL
from irl_benchmark.irl.algorithms.me_irl import MaxEntIRL
from irl_benchmark.irl.reward.reward_function import FeatureBasedRewardFunction
from irl_benchmark.rl.algorithms import ValueIteration


env_id = 'FrozenLake8x8-v0'

expert_trajs_path = 'data/frozen/expert'

# factory creating new IR-L algorithms:
def irl_alg_factory(env, expert_trajs):
    # factory defining which RL algorithm is used:
    def rl_alg_factory(env):
        return ValueIteration(env, {'gamma': 0.9})
    return MaxCausalEntIRL(env, expert_trajs, rl_alg_factory, {'gamma': 0.9})


metrics = []

run_config = {
    'reward_function': FeatureBasedRewardFunction,
    'no_expert_trajs': 10000,
    'no_irl_iterations': 200,
    'no_rl_episodes_per_irl_iteration': 1000,
    'no_irl_episodes_per_irl_iteration': 5000,
}


run = Run(env_id, expert_trajs_path, irl_alg_factory, metrics,
                 run_config)

run.start()

print('Spacemacs is best.')