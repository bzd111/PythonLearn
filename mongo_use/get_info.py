# -*- coding: utf-8 -*-
import psutil
from models import DiskModle
from models import MemModle
from utils import bytes2human


def df():
    '''disk'''

    name_list = ['disk_name', 'total_space',
                 'used_space', 'free_space', 'perent']
    df = []
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        percent = str(int(usage.percent)) + '%'
        disk = [part.device, bytes2human(usage.total),
                bytes2human(usage.used), bytes2human(usage.free),
                percent]
        df.append(dict(zip(name_list, disk)))
    return df


def mem():
    '''memory'''
    phymem = psutil.virtual_memory()
    total = phymem.total
    # phymem.free + buffers + cached
    free = phymem.available
    used = total - free
    mem_dict = locals()
    del mem_dict['phymem']
    return dict(zip(mem_dict, map(bytes2human, mem_dict.values())))


def store_data():
    disk_dict = df()
    mem_dict = mem()

    # MemModle.drop_collection()
    # DiskModle.drop_collection()
    print(mem_dict)
    MemModle.from_dict(mem_dict).save()

    for disk_info in disk_dict:
        DiskModle(**disk_info).save()


def get_data():
    a = MemModle.objects.all()
    for i in a:
        print(i.total, i.create_at)
    b = DiskModle.objects.all()
    for i in b:
        print(i.perent, i.create_at)


if __name__ == "__main__":
    store_data()
    get_data()
