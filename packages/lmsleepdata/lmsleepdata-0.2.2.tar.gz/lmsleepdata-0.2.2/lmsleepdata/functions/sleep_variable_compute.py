from lm_datahandler.postprocess.label_smooth import pp_label_smooth
import numpy as np

"""
Compute sleep variables for human sleep staging result
Common input:
    Hypno: Sleep staging result
    class_count: 
        The class count in the hypno, also meaning the type for sleep staging.
        4: vague staging, {0: "N3(Deep Sleep)", 1: "N1/N2(Light Sleep)", 2: "REM", 3: "Wake"}
        5: specific staging,  {0: "N3", 1: "N1", 2: "N2", 3: "REM", 4: "Wake"}
    epoch_length: seconds for single sleep staging epoch, usually 30s or 15s
"""
def tst_compute(hypno, class_count, epoch_length):
    """
    compute total sleep time from hypno
    :param hypno: sleep stage
    :param epoch_length: seconds per epoch
    :return: tst: total sleep time
    """
    copy = hypno.copy()
    is_sleep = np.zeros(copy.shape)
    if class_count == 5:
        is_sleep[copy < 4] = 1
    elif class_count == 4:
        is_sleep[copy < 3] = 1
    sleep_epoch_count = np.sum(is_sleep)

    return sleep_epoch_count * epoch_length


def sl_compute(hypno, class_count, epoch_length):
    """
    从记录开始，到第一次进入长时间睡眠(30分钟以上，且中间清醒时间少于3分钟)开始的时间
    前期若存在短时睡眠则忽略
    :param class_count: class count is 5 means N1 is specified
    :param hypno: sleep stage
    :param epoch_length: seconds per epoch
    :return sl: sleep latency
    """
    index = -1
    hypno = pp_label_smooth(hypno, window=5)
    copy = hypno.copy()

    if class_count == 5:
        copy[hypno >= 4] = 1
        copy[hypno < 4] = 0
    elif class_count == 4:
        copy[hypno >= 3] = 1
        copy[hypno < 3] = 0
    for i in range(hypno.shape[0] - 30 * 4):
        score = np.sum(copy[i:i + 30 * 4])
        if score < 3 * 4:
            index = i
            break

    while index < hypno.shape[0] - 5 * 4 and np.sum(copy[index:index + 5 * 4]) > 0:
        index += 1

    return -1 if index < 0 else index * epoch_length


def get_up_time_compute(hypno, class_count, epoch_length):
    copy = hypno.copy()
    copy = np.asarray(copy).tolist()
    copy.reverse()

    index = sl_compute(np.asarray(copy), class_count, epoch_length)


    return -1 if index < 0 else index


def waso_compute(hypno, class_count, epoch_length, sleep_range=None):
    """
    :param hypno: sleep stage
    :param class_count: 分类数，4 or 5
    :param epoch_length: seconds per epoch
    :param sleep_range: 睡眠持续范围，从第一个睡眠epoch到最后一个睡眠epoch
    :return: waso: awake time during sleep
    """

    if sleep_range is None:
        first_sleep_time = sl_compute(hypno, class_count, epoch_length)
        if first_sleep_time == -1:
            return -1
        last_sleep_time = get_up_time_compute(hypno, class_count, epoch_length)
    else:
        first_sleep_time = sleep_range[0]
        first_sleep_time = int(first_sleep_time / epoch_length)
        last_sleep_time = sleep_range[1]
        last_sleep_time = int(last_sleep_time / epoch_length)

    sleep_hypno = hypno[first_sleep_time:last_sleep_time]
    sleep_hypno = sleep_hypno.copy()
    sleep_hypno = pp_label_smooth(sleep_hypno, window=5)
    if class_count == 5:
        sleep_hypno[sleep_hypno < 4] = 0
        sleep_hypno[sleep_hypno == 4] = 1
    elif class_count == 4:
        sleep_hypno[sleep_hypno < 3] = 0
        sleep_hypno[sleep_hypno == 3] = 1
    arousal_time = np.sum(sleep_hypno)

    return arousal_time * epoch_length


def se_compute(hypno, class_count):
    """
    :param hypno: sleep stage
    :param class_count: 分类数，4 or 5
    :return: se: sleep efficiency
    """
    copy = hypno.copy()
    is_sleep = np.zeros(hypno.shape)
    if class_count == 5:
        is_sleep[copy < 4] = 1
    elif class_count == 4:
        is_sleep[copy < 3] = 1
    sleep_epoch_count = np.sum(is_sleep)

    return sleep_epoch_count / hypno.shape[0]


def arousal_time_compute(hypno, class_count, epoch_length, sleep_range=None):
    """
    :param hypno: sleep stage
    :param class_count: 分类数， 4 or 5
    :param epoch_length: 单个epoch时长，单位秒
    :return: sleep_range: 睡眠持续范围，从第一个睡眠epoch到最后一个睡眠epoch
    """
    copy = np.copy(hypno)
    hypno_smooth = pp_label_smooth(copy, window=5)


    if sleep_range is None:
        first_sleep_time = sl_compute(hypno, class_count, epoch_length)
        if first_sleep_time == -1:
            return -1
        last_sleep_time = get_up_time_compute(hypno, class_count, epoch_length)
    else:
        first_sleep_time = sleep_range[0]
        last_sleep_time = sleep_range[1]
    first_sleep_time = int(first_sleep_time / epoch_length)

    last_sleep_time = len(hypno) - int(last_sleep_time / epoch_length)

    sleep_hypno = hypno_smooth[first_sleep_time:last_sleep_time]
    sleep_hypno = sleep_hypno.copy()
    if class_count == 5:
        sleep_hypno[sleep_hypno < 4] = 0
        sleep_hypno[sleep_hypno == 4] = 1
    elif class_count == 4:
        sleep_hypno[sleep_hypno < 3] = 0
        sleep_hypno[sleep_hypno == 3] = 1
    arousal_count = sleep_hypno[1:] - sleep_hypno[0:-1]
    arousal_count = np.where(arousal_count == 1)[0]
    arousal_time = np.where(sleep_hypno == 1)[0]
    return arousal_count.shape[0], first_sleep_time + arousal_time
