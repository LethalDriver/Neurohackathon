import brainaccess_board as bb

db, status = bb.db_connect()
if status:
    data = db.get_mne()
    print(f"Dictionary of connected devices:\n {data}")
    print(f"MNE structure: {data[next(iter(data))]}")

