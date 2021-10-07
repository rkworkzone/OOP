import multiprocessing
import time

# Sharing data between processes can be done by using Queue, Array, Value. These are multiprocessing module classes
# There are core python Queue and Array modules available.


def cal_squire(numbers, result):
    #print map(lambda x: x *x, numbers)
    for idx , n in enumerate(numbers):
        time.sleep(2)
        print 'squire ' + str(n * n)
        result[idx] = n * n


def cal_cube(numbers, result):
    for idx, n in enumerate(numbers):
        time.sleep(2)
        print 'cube '+ str(n * n * n)
        result.append(n * n * n)


if __name__ == "__main__":
    start =  time.time()
    arr=[2,4,5,6,3]
    result = multiprocessing.Array('i',5)
    t1 = multiprocessing.Process(target=cal_squire, args=(arr, result))
    t2 = multiprocessing.Process(target=cal_cube, args=(arr, result))
    #cal_squire(arr)
    #cal_cube(arr)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end  = time.time()

    print result[:]
    print  end - start

