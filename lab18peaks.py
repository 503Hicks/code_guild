import string


# Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#TO FIND PEAKS
def get_peaks():
    peaks = []
    index_list = list(range(len(data)))

    for i in index_list:
        if (i-1) in index_list and (i+1) in index_list:
            if data[i] >= data[i-1] and data[i] >= data[i+1]:
                peaks.append(i)
    print(peaks)

#TO FIND VALLEYS
def get_valleys():
    valleys = []
    index_list = list(range(len(data)))

    for i in index_list:
        if (i-1) in index_list and (i+1) in index_list:
            if data[i] <= data[i-1] and data[i] <= data[i+1]:
                valleys.append(i)
    print(valleys)



            
get_peaks()
get_valleys()

