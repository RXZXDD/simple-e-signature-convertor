import cv2 as cv
import numpy as np


def digitalize(path, threshold):
    img = cv.imread(path)
    #cv.imshow('windowname1', img)
    #cv.waitKey(0) # time in ms
    #cv.destroyAllWindows()
    
    if img is None:
        print("ERR:read err")
    else:
        for x in range(img.shape[0]):
                for y in range(img.shape[1]):
                    if(x / img.shape[0] > 0.12 and x / img.shape[0] < 0.88) and\
                        (y / img.shape[1] > 0.12 and y / img.shape[1] < 0.88):
                    # turn to white if no a handwriting trace
                        if img.item(x, y, 0) > threshold and img.item(x, y, 1) > threshold and img.item(x, y, 2) > threshold:
                            img.itemset((x, y, 0), 255)
                            img.itemset((x, y, 1), 255)
                            img.itemset((x, y, 2), 255)
                        else:
                                img.itemset((x, y, 0), 0)
                                img.itemset((x, y, 1), 0)
                                img.itemset((x, y, 2), 0)
                    else:
                        img.itemset((x, y, 0), 255)
                        img.itemset((x, y, 1), 255)
                        img.itemset((x, y, 2), 255)
    cv.imwrite('e-signature' + str(threshold) + '.jpg', img)
    print('done')
    cv.imshow('windowname' + str(threshold), img)
    cv.waitKey(0) # time in ms
    cv.destroyAllWindows()

if __name__ == '__main__':
    path, threshold = input().split(' ')
    threshold = eval(threshold)
    if path is '':
        #for threshold in range(threshold, 120, 5):
            digitalize('D:\e-signature-src.jpg', threshold)
    else:
        print(path, threshold)
        digitalize(path, threshold)
