class MemModle():

    def __init__(self,total,used,free):

        self.total_mem = total
        self.used_mem = used
        self.free_mem = free

    @classmethod
    def from_dict(cls,data_list):
        print("class init data",data_list)
        return cls(**data_list)
mem_dict={'total': '15.9G', 'free': '4.7G', 'used': '11.1G'}
a=MemModle.from_dict(mem_dict)
print(a.free_mem)