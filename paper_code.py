import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def figure3(path):
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 50,
             }

    car_num = 200
    interation = 12000
    disturb_time = 5000
    p_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    initspeed = 20
    fig = plt.figure(figsize=(60, 80))
    topo_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    for item in range(11):
        ax = fig.add_subplot(4, 3, item + 1, projection='3d')
        p = p_list[item]
        data = pd.read_csv(path, encoding='ISO-8859-1')
        all_id = data['id'].unique()
        mpl.rcParams['legend.fontsize'] = 25
        color_list = ['#1672b2', '#d75013', '#f1ad1f', '#4baeea']
        for i in range(len(all_id) - 1, 0, -1):
            time = np.array(range(int((interation - disturb_time) / 10)))
            aim_data = data[data['id'] == all_id[i]]
            aim_color = color_list[int(aim_data.iloc[-1, -1])]
            speed = np.array(aim_data.iloc[500:, 2])
            id = np.ones(int((interation - disturb_time) / 10)) * i
            ax.plot(id, time, speed, label='parametric curve', color=aim_color)
        ax.legend()
        ax.set_zlim3d(5, initspeed + 5)
        ax.set_xlim3d(0, car_num)
        ax.set_ylim3d(0, int((interation - disturb_time) / 10))
        ax.set_xticks([0, 40, 80, 120, 160, 200])
        ax.set_yticks([0, 100, 200, 300, 400, 500, 600, 700])
        ax.set_zticks([5, 10, 15, 20, 25])
        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.tick_params(direction='in', labelsize=30, pad=10)
        ax.view_init(30, 40)
        ax.grid(True)
        ax.set_ylabel('Time(s)', labelpad=50, fontdict=font1)
        ax.set_xlabel('Vehicle ID', labelpad=50, fontdict=font1)
        ax.set_zlabel('Velocity(m/s)', labelpad=20, rotation=90, fontdict=font1)
        ax.set_title('({}) p={}'.format(topo_list[item], p), y=-0.01, fontdict=font1)
        ax.grid(False)
    plt.tight_layout()
    plt.savefig('./stability_figure{}.png'.format(car_num), format="png", transparent=True)


def figure4(aim_map1, aim_map2):
    nan = np.zeros(1000, 2500)
    result1 = aim_map1.iloc[:1000, :2500]
    result2 = aim_map1.iloc[1:1001, 1:2501]
    result2.index = range(len(result2))
    result1.index = range(len(result1))
    result1.columns = [i for i in range(2500)]
    result2.columns = [i for i in range(2500)]
    result = result1 * result2
    arr_result = np.array(result)
    neg_x, neg_y = np.where(arr_result <= 0)

    result12 = aim_map2.iloc[:1000, :2500]
    result22 = aim_map2.iloc[1:1001, 1:2501]
    result22.index = range(len(result22))
    result12.index = range(len(result12))
    result12.columns = [i for i in range(2500)]
    result22.columns = [i for i in range(2500)]
    result_2 = result12 * result22
    arr_result_2 = np.array(result_2.iloc[::-1])
    neg_x2, neg_y2 = np.where(arr_result_2 <= 0)

    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 25,
             }
    figure, ax = plt.subplots(figsize=(15 * 2, 4.5 * 2))
    negx = [1000 - i for i in neg_x]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.scatter(neg_y, negx, s=0.2, c='dodgerblue', marker='o', label='stable with time delays')
    plt.scatter(neg_y2, neg_x2, s=0.2, c='firebrick', marker='o', label='stable without time delays')
    plt.xlabel('speed(m/s)', fontdict=font1)
    plt.ylabel('CAV MPR', fontdict=font1)

    new_pos_x = list(range(0, 3001, 500))
    new_ticks_x = [0, 5, 10, 15, 20, 25, 30]
    plt.xticks(new_pos_x, new_ticks_x, rotation=0, fontproperties='Times New Roman')
    new_pos_y = list(range(0, 1001, 100))
    new_ticks_y = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    plt.yticks(new_pos_y, new_ticks_y, fontproperties='Times New Roman')
    plt.xlim((0, 3201))
    plt.ylim((0, 1000))
    plt.tick_params(direction='in', labelsize=25)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname("Times New Roman") for label in labels]
    ax1 = plt.gca()
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width, box.height])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=25, markerscale=12)

    plt.tight_layout()
    plt.savefig('neg_contour.png')


def figure5(aim_map1, aim_map3):
    nan = np.zeros(1000, 2500)
    result1 = aim_map1.iloc[:1000, :2500]
    result2 = aim_map1.iloc[1:1001, 1:2501]
    result2.index = range(len(result2))
    result1.index = range(len(result1))
    result1.columns = [i for i in range(2500)]
    result2.columns = [i for i in range(2500)]
    result = result1 * result2
    arr_result = np.array(result)
    neg_x, neg_y = np.where(arr_result <= 0)

    result13 = aim_map3.iloc[:1000, :3200]
    result23 = aim_map3.iloc[1:1001, 1:3201]
    result23.index = range(len(result23))
    result13.index = range(len(result13))
    result13.columns = [i for i in range(3200)]
    result23.columns = [i for i in range(3200)]
    result_3 = result13 * result23
    arr_result_3 = np.array(result_3.iloc[::-1])
    neg_x3, neg_y3 = np.where(arr_result_3 <= 0)
    font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
    figure, ax = plt.subplots(figsize=(15 * 2, 4.5 * 2))

    negx = [1000 - i for i in neg_x]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.scatter(neg_y, negx, s=0.2, c='dodgerblue', marker='o', label='stable with platoon management')
    plt.scatter(neg_y3, neg_x3, s=0.2, c='firebrick', marker='o', label='stable without platoon management')
    plt.xlabel('speed(m/s)', fontdict=font1)
    plt.ylabel('CAV MPR', fontdict=font1)

    new_pos_x = list(range(0, 3001, 500))
    new_ticks_x = [0, 5, 10, 15, 20, 25, 30]
    plt.xticks(new_pos_x, new_ticks_x, rotation=0, fontproperties='Times New Roman')
    new_pos_y = list(range(0, 1001, 100))
    new_ticks_y = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    plt.yticks(new_pos_y, new_ticks_y, fontproperties='Times New Roman')
    plt.xlim((0, 3201))
    plt.ylim((0, 1000))
    plt.tick_params(direction='in', labelsize=25)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname("Times New Roman") for label in labels]
    ax1 = plt.gca()
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width, box.height])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=25, markerscale=12)
    plt.tight_layout()
    plt.savefig('neg_contour2.png')
