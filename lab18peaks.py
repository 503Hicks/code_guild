import string


# Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

for i in range(len(data)):
    if (i-1) in data and (i+1) in data:
        print(i)
    if data[i] <= data[i-1] and data[i] <= data[i+1]:
            data.append(i)
print(data[i])

# for i in range(len(data)):
#         # print(data[i])
#         if data[-i] >= data[i-1] and data[i] <= data[i+1]:
#             print(data[i])

# print(data)





# def peaks():

#     for i in range(len(data)):
#         if data[i] >= data[i-1] and data[i] <= data[i+1]:
#             print(data)

# def valleys():
    
#     for i range(len(data)):
#         if data[i] < data[i] and data[i] 

# def peaks_and_valleys():

