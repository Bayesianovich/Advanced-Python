# from multiprocessing import Pool

# def square(x):
#     return x * x

# if __name__ == "__main__":
#     with Pool(4) as p:
#         result = p.apply(square, (7,))  # 同步调用
#         print(result)




from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as p:
        result = p.apply_async(square, (7,))  # 异步调用
        print(result.get())  # 使用get方法获取结果