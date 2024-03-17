# 启动 Spring 工程并测量启动耗时工具
import socket
import subprocess
import time

import matplotlib.pyplot as plt


def is_port_open(host, port, timeout=10):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


# command: 需要执行的启动命令
# host: 服务将要监听的主机名或IP地址
# port: 服务将要监听的端口号
# timeout: 在放弃之前，愿意等待服务的最大时间,这里给定 2 分钟，即：120 s
# check_interval: 每次检查端口是否开放之前等待的时间间隔，这里给定为 0.1 s
def measure_startup_time(command, host, port, timeout=120, check_interval=0.1):
    start_time = time.time()
    process = subprocess.Popen(command, shell=True)
    try:
        while time.time() - start_time < timeout:
            if is_port_open(host, port, timeout=check_interval):
                return time.time() - start_time
            time.sleep(check_interval)
    finally:
        process.terminate()
        time.sleep(10)
    return None


startup_command1 = "java -jar bean-async-1.0-SNAPSHOT.jar"
startup_command2 = "java -jar bean-async-2.0-SNAPSHOT.jar"
host = 'localhost'
port = 8888

analyze_startup_times1 = []
analyze_startup_times2 = []
# 测试启动 5 次服务
test_times = 5

for i in range(test_times):
    startup_time = measure_startup_time(startup_command1, host, port)
    if startup_time is not None:
        analyze_startup_times1.append(startup_time)
        print(f"Startup time for attempt {i + 1}: {startup_time:.2f} seconds")
    else:
        print(f"Service did not start within the timeout for attempt {i + 1}")

for i in range(test_times):
    startup_time = measure_startup_time(startup_command2, host, port)
    if startup_time is not None:
        analyze_startup_times2.append(startup_time)
        print(f"Startup time for attempt {i + 1}: {startup_time:.2f} seconds")
    else:
        print(f"Service did not start within the timeout for attempt {i + 1}")

print(analyze_startup_times1)
print(analyze_startup_times2)
# 使用 matplotlib 绘制图表

indexes = range(len(analyze_startup_times1))
plt.figure(figsize=(10, 5))
plt.plot(indexes, analyze_startup_times1, color='red', marker='o', linestyle='-')
plt.plot(indexes, analyze_startup_times2, color='blue', marker='o', linestyle='-')
plt.title('spring project started up cost times plot')
plt.xlabel('index')
plt.ylabel('cost time')
plt.show()
