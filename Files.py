# with open("test.txt", 'r') as rf:
#     with open("test_copy.txt", 'w') as wf:
#         for line in rf:
#             wf.write(line)

import chunk


with open("panorama.jpeg", 'rb') as rf:
    with open("panorama_copy.jpeg", 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
    # f.write('Test')
    # f.seek(0)
    # f.write("R")
    # for line in f:
    #     print(line, end='')
    # size_to_read = 10

    # f_contents = f.read(size_to_read)
    # print(f_contents, end="")

    # f.seek(0)

    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end="*")
    #     f_contents = f.read(size_to_read)
      
# f_contents = f.readline()
# # print(f_contents)


# print(f.name)
# f = open("test.txt", 'r')
# f.close()