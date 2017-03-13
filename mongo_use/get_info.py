from datetime import datetime

import psutil

from mongoengine import NotUniqueError
from utils import bytes2human,to_meg
from models import MemModle,DiskModle

def df():
    '''disk_usage'''
    name_list = ['disk_name','total_space','used_space','free_space','perent']
    df = []
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        percent = str(int(usage.percent)) + '%'
        disk = [part.device, bytes2human(usage.total),
                bytes2human(usage.used), bytes2human(usage.free),
                percent]
        df.append(dict(zip(name_list,disk)))
    return df

def mem():
    phymem = psutil.virtual_memory()
    total = phymem.total
    #phymem.free + buffers + cached
    free = phymem.available
    used = total - free
    # print(del locals()['phymem'])
    mem_dict = locals()
    del mem_dict['phymem']
    return dict(zip(mem_dict,map(bytes2human,mem_dict.values())))

def store_data():
    disk_dict = df()
    # for singal_disk in disk_dict:
    #     print(singal_disk)
    #     try:
    #         DiskModle.from_list(singal_disk).save()
    #     except NotUniqueError:
    #         pass
    mem_dict = mem()
    print(mem_dict)
    MemModle.drop_collection()
    DiskModle.drop_collection()


    # MemModle(**mem_dict).save()

    MemModle.from_dict(mem_dict).save()
    for disk_info in disk_dict:
        DiskModle(**disk_info).save()

    # total_mem,used_mem,free_men = mem_list
    # mem_data = MemModle(total_mem,used_mem,free_men)
    # mem_data.save()


def get_data():
    a = MemModle.objects.all()
    for i in a:
        print(i.total,i.create_at)
    b = DiskModle.objects.all()
    for i in b:
        print(i.perent,i.create_at)

if __name__ =="__main__":
    store_data()
    get_data()
    # print(mem())
    # print(df())