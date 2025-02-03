def find_world_readable_files(directory):
    import os, stat
    result = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if os.path.isfile(path) and os.stat(path).st_mode & stat.S_IROTH:
                result.append(path)
    return result

