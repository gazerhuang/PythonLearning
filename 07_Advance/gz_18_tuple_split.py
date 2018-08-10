def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "Ming","Age": 18}
demo(*gl_nums, **gl_dict)
