import brainaccess_board as bb


def get_and_label_data(db):
    channels = [
        "time",
        "F3",
        "F4",
        "C3",
        "C4",
        "P3",
        "P4",
        "O1",
        "O2",
        "Accel_x",
        "Accel_y",
        "Accel_z",
        "Sample",
        "Streaming",
        "Battery",
    ]
    data = db.get_mne()
    devices = list(data.keys())
    device = devices[0]
    data = data[device].get_data()
    samples_labeled = {
        channel_name: samples for samples, channel_name in zip(data, channels)
    }
    return samples_labeled


db, status = bb.db_connect()
if status:
    print(get_and_label_data(db))
