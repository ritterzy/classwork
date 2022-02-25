def  tree (size):
    for i in range(0 ,size):
        if size < 3 or type(size) == str:
            print("Error")
        print( '*' *(i + 1))

tree(6)


# def draw_rectangular(size1,size2):
#     for i in range ( size2):
#         print('*' * size1  )

# draw_rectangular(13 , 5)

# def clear_tex_from_uppercase(text):
#     new_text =''
#     for i in text:
#         if i.isupper():pass
#         else:new_text = new_text + i
#     return new_text


# print(clear_tex_from_uppercase('bvldkfbrlkKBlkjkkj'))


# def show_devisors(num):
#     for i in range (1, num + 1):
#         if num % i ==0:
#             print (i)
        
        
# show_devisors(24)
             









