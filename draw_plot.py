from config import Config
import matplotlib.pyplot as plt

def draw_plot(best_chromosome):

    node_x = []
    node_y = []
    best_path_x = []
    best_path_y = []

    plt.figure()
    plt.axis([0.0, 15.0, 0.0, 15.0])

    _draw_obstacles()

    for element in Config.path_points:
        node_x.append(element[0])
        node_y.append(element[1])

    for element in best_chromosome:

        best_path_x.append(Config.path_points[int(element)][0])
        best_path_y.append(Config.path_points[int(element)][1])

    plt.plot(node_x, node_y, "ko")
    plt.plot(best_path_x, best_path_y, "g-")
    plt.draw()
    plt.savefig("./docs/images/best_path.png")
    plt.pause(0.02)


def _draw_obstacles():

    obs_1_x = [2.5, 3.5, 3.5, 2.5, 2.5]
    obs_1_y = [9, 9, 12, 12, 9]
    plt.plot(obs_1_x, obs_1_y, "g")

    obs_2_x = [3, 4, 4, 3, 3]
    obs_2_y = [6.5, 6.5, 4, 4, 6.5]
    plt.plot(obs_2_x, obs_2_y, "g")

    obs_3_x = [7, 9, 9, 7, 7]
    obs_3_y = [12, 12, 13, 13, 12]
    plt.plot(obs_3_x, obs_3_y, "g")

    obs_4_x = [6.5, 8, 8, 6.5, 6.5]
    obs_4_y = [6, 6, 9.5, 9.5, 6]
    plt.plot(obs_4_x, obs_4_y, "g")

    obs_5_x = [5.7, 8.7, 8.7, 5.7, 5.7]
    obs_5_y = [2, 2, 3, 3, 2]
    plt.plot(obs_5_x, obs_5_y, "g")

    obs_6_x = [11, 12, 12, 11, 11]
    obs_6_y = [8.5, 8.5, 12, 12, 8.5]
    plt.plot(obs_6_x, obs_6_y, "g")

    obs_7_x = [10, 11.5, 11.5, 10, 10]
    obs_7_y = [3.5, 3.5, 5.5, 5.5, 3.5]
    plt.plot(obs_7_x, obs_7_y, "g")