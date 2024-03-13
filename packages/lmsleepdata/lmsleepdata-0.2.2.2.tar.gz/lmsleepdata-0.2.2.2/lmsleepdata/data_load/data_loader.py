import numpy as np
from .loaders import EEGLoader, ACCLoader, BLELoader, STILoader, BaseLoader_X8


def load_data(eeg_path, acc_path, sti_path, ble_path, data_type, logger, do_padding=False):
    """
    根据设备型号，进行不同的数据处理加载
    X7：旧版数据格式；断连数据单独存到ble.ble文件中；刺激数据单独存到sti.sti文件（二进制文件）
    X8：新版数据格式；断连数据从eeg.eeg和acc.acc的包头数据中计算；刺激文件单独存到sti.log文件（文本文件）
    :param eeg_path: eeg.eeg路径
    :param acc_path: acc.acc路径
    :param sti_path: sti.sti路径
    :param ble_path: ble.ble路径
    :param data_type: 记录数据的设备型号
    :param logger: 日志器
    :param do_padding: 是否进行丢包补充以及断连补充
    :return:
    """
    if eeg_path is None:
        logger.error("The EEG file not exist, please check.")
        return
    if data_type == 'X7':
        return load_data_x7(eeg_path, acc_path, sti_path, ble_path, logger, do_padding)
    if data_type == 'X8':
        return load_data_x8(eeg_path, acc_path, sti_path, logger, do_padding)
    return

def load_data_x7(eeg_path, acc_path, sti_path, ble_path, logger, do_padding):
    """
    X7数据加载：丢包补充在eeg加载和acc加载内部，断连补充在外部（当前函数中）
    :param eeg_path: eeg路径
    :param acc_path: acc路径
    :param sti_path: sti路径
    :param ble_path: ble路径
    :param logger:
    :param do_padding: 是否进行丢包补充以及断连补充
    :return:
    """
    raw_acc = raw_eeg = acc = eeg = raw_sti = acc_loss_rate = eeg_loss_rate = package_loss_rate = total_time = start_time = end_time = disconnections = disconnect_rate = None
    if acc_path is not None:
        logger.info("ACC loading start...")
        acc_loader = ACCLoader()
        raw_acc, acc, acc_loss_rate, total_time, start_time, end_time = acc_loader.load_data(acc_path, do_padding)
        logger.info("ACC loading finished.")
    if eeg_path is not None:
        logger.info("EEG loading start...")
        eeg_loader = EEGLoader()
        raw_eeg, eeg, eeg_loss_rate, total_time, start_time, end_time = eeg_loader.load_data(eeg_path, do_padding)
        logger.info("EEG loading finished.")
    if sti_path is not None:
        sti_loader = STILoader()
        raw_sti = sti_loader.load_data(sti_path)

    if raw_acc is not None and raw_eeg is not None:
        # assert eeg.shape[1]//10 == acc.shape[1], "eeg and acc epoch length is not equal."
        # assert eeg_loss_rate == acc_loss_rate, "eeg and acc package loss rate is not equal."
        epoch = min(eeg.shape[1]//7500, acc.shape[1]//750)
        eeg = eeg[:, 0:epoch*7500]
        acc = acc[:, 0:epoch*750]
        raw_eeg = raw_eeg[:, 0:epoch*7500]
        raw_acc = raw_acc[:, 0:epoch*750]
        package_loss_rate = eeg_loss_rate

    if ble_path is not None:
        ble_loader = BLELoader()
        disconnections = ble_loader.load_data(ble_path)

        if disconnections is not None and disconnections.shape[0] != 0:
            disconnections = disconnections / 1000.0 / 1000.0
            time_gap = (disconnections[:, 1] - disconnections[:, 0])

            # 断连填充，做成可配置，不做断连补充的数据可以用于数据标记
            if do_padding:
                start_timestamp = start_time.timestamp()
                eeg1 = eeg[0, :]
                eeg2 = eeg[1, :]
                acc1 = acc[0, :]
                acc2 = acc[1, :]
                acc3 = acc[2, :]
                for i in range(disconnections.shape[0]):
                    # 创建一个2x100的ndarray
                    eeg_zeros = np.zeros(round(time_gap[i]*500)).astype(np.int32)
                    acc_zeros = np.zeros(round(time_gap[i] * 50)).astype(np.int32)
                    eeg_index = np.int32(np.around((disconnections[i, 0]-start_timestamp)*500))
                    acc_index = np.int32(np.around((disconnections[i, 0]-start_timestamp)*50))
                    # 在索引为50的位置插入10个0
                    if eeg_index < eeg.shape[1] and acc_index < acc.shape[1]:
                        eeg1 = np.insert(eeg1, eeg_index, eeg_zeros)
                        eeg2 = np.insert(eeg2, eeg_index, eeg_zeros)
                        acc1 = np.insert(acc1, acc_index, acc_zeros)
                        acc2 = np.insert(acc2, acc_index, acc_zeros)
                        acc3 = np.insert(acc3, acc_index, acc_zeros)
                eeg = np.vstack([eeg1, eeg2])
                acc = np.vstack([acc1, acc2, acc3])
                total_time = total_time + np.sum(time_gap)
                disconnect_rate = np.sum(time_gap) / total_time * 100
            else:
                disconnect_rate = np.sum(time_gap) / total_time * 100
        else:
            disconnect_rate = 0


    return raw_eeg, eeg, raw_acc, acc, raw_sti, disconnections, total_time, start_time, end_time, package_loss_rate, disconnect_rate


def load_data_x8(eeg_path, acc_path, sti_path, logger, do_padding):
    """
    X8数据加载：丢包补充和断连补充都在eeg加载和acc加载内部
    :param eeg_path: eeg路径
    :param acc_path: acc路径
    :param sti_path: sti路径
    :param logger:
    :param do_padding: 是否进行丢包补充以及断连补充
    :return:
    """
    raw_acc = raw_eeg = acc = eeg = raw_sti = acc_loss_rate = eeg_loss_rate = package_loss_rate = total_time = start_time = end_time = disconnections = disconnect_rate = None
    if acc_path is not None:
        logger.info("ACC loading start...")
        acc_loader = BaseLoader_X8()
        acc_loader.load_data(acc_path, do_padding)
        raw_acc, acc, acc_loss_rate, total_time, start_time, end_time = acc_loader.raw_data, acc_loader.data_total, acc_loader.package_loss, acc_loader.time_length, acc_loader.start_time, acc_loader.end_time
        disconnect_rate = acc_loader.disconnection_rate
        logger.info("ACC loading finished.")
    if eeg_path is not None:
        logger.info("EEG loading start...")
        eeg_loader = BaseLoader_X8()
        eeg_loader.load_data(eeg_path, do_padding)
        raw_eeg, eeg, eeg_loss_rate, total_time, start_time, end_time = eeg_loader.raw_data, eeg_loader.data_total, eeg_loader.package_loss, eeg_loader.time_length, eeg_loader.start_time, eeg_loader.end_time
        disconnect_rate = eeg_loader.disconnection_rate
        logger.info("EEG loading finished.")
    if sti_path is not None:
        sti_loader = STILoader()
        raw_sti = sti_loader.load_sti_log(sti_path)

    if raw_acc is not None and raw_eeg is not None:
        # assert eeg.shape[1]//10 == acc.shape[1], "eeg and acc epoch length is not equal."
        # assert eeg_loss_rate == acc_loss_rate, "eeg and acc package loss rate is not equal."
        epoch = min(eeg.shape[1] // 7500, acc.shape[1] // 750)
        eeg = eeg[:, 0:epoch * 7500]
        acc = acc[:, 0:epoch * 750]
        raw_eeg = raw_eeg[:, 0:epoch * 7500]
        raw_acc = raw_acc[:, 0:epoch * 750]
        package_loss_rate = eeg_loss_rate



    return raw_eeg, eeg, raw_acc, acc, raw_sti, disconnections, total_time, start_time, end_time, package_loss_rate, disconnect_rate