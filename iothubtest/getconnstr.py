file1 = open('connection-strings', 'r');
for line in file1.readlines():
    if 'HostName' in line:
        for item in line.split(';'):
            if item.startswith('DeviceId'):
                print item[9:]
            if item.startswith('SharedAccessKey'):
                print item[17:]