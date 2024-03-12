from multiprocessing import Process, Queue
from init import DelayLine, Task
import matplotlib.pyplot as plt
import numpy as np
import init
import time_util_wj

offset = 0
length = 70
iteration = 2

time_n, freq_n = int(length / init.interval), 8192
t_seq, f_seq = np.arange(time_n) * init.interval, np.arange(freq_n) / init.interval / freq_n
t_data, f_data = None, None


def scan_exec(q: Queue, n: int):
    """ Scan Exec """
    delay = DelayLine()
    task = Task('Dev3')

    init.offset = offset
    init.length = length

    init.delay_init(delay)

    init.task_init(task)

    delay.start()

    for i in range(n):
        del task.buffer
        task.start()
        delay.run()
        for ii in range(delay.iteration):
            task.read(int(delay.length / delay.interval), 10)
        q.put(np.mean(task.buffer, axis=0))
        task.stop()

    task.close()
    time_util_wj.sleep(2)
    delay.close()



def data_plot(n: int):
    """ Data Plot """
    plt.clf()
    plt.suptitle("[Current: %d | Value %.2f Vpp]" % (n + 1, max(t_data) - min(t_data)))

    plt.subplot(121)
    plt.plot(t_seq, t_data)
    plt.title('T-Domain')
    plt.xlabel('Time (ps)')
    plt.ylabel('Voltage (V)')

    plt.subplot(122)
    plt.plot(f_seq, np.log10(abs(f_data)) * 20)
    plt.title('F-Domain')
    plt.xlabel('Frequency (THz)')
    plt.ylabel('Magnitude (dB)')
    plt.xlim(0, 10)

    plt.tight_layout()
    plt.pause(.1)


if __name__ == '__main__':

    queue = Queue()
    proc = Process(target=scan_exec, args=(queue, iteration))
    proc.start()

    plt.figure(figsize=(12, 6))
    plt.ion()

    for i in range(iteration):
        t_data = queue.get(timeout=10)
        t_data = np.array(t_data)
        f_data = np.fft.fft(t_data[:len(t_seq)], freq_n)
        data_plot(i)

    plt.ioff()
    plt.show()
