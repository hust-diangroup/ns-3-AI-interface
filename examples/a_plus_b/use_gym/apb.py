import ns3ai_gym_env
import gymnasium as gym

APB_SIZE = 3


class ApbAgent:

    def __init__(self):
        pass

    def get_action(self, obs, reward, done, info):

        a = obs[0]
        b = obs[1]
        act = a + b

        return [act]


if __name__ == '__main__':

    env = gym.make("ns3ai_gym_env/Ns3-v0")
    ob_space = env.observation_space
    ac_space = env.action_space
    print("Observation space: ", ob_space, ob_space.dtype)
    print("Action space: ", ac_space, ac_space.dtype)

    obs, info = env.reset()
    # print("---obs: ", obs)
    reward = 0
    done = False

    agent = ApbAgent()

    while True:

        action = agent.get_action(obs, reward, info, done)
        # print("---action: ", action)

        obs, reward, done, _, info = env.step(action)
        # print("---obs, reward, done, info: ", obs, reward, done, info)

        if done:
            break

    env.close()