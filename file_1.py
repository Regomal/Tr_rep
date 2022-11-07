st1 = "Задавая задание на дом, учителя метят в учеников, а попадают в родителей."
st2 = "Никогда! Никогда не нюхайте как кипит чайник."
st3 = "Математические задачи - это единственное место где кто-то может купить 60 арбузов и никто его не спросит зачем?"
st4 = "Как только собрался взяться за ум, закончился учебный год."
st5 = "Пропала собака, очень умная. Шарик, если ты сейчас это читаешь, позвони домой!"

#1
print('№1')
def first_last(st, *args):
    for e in args:
        if st.find(e) != -1:
            print(f"{e}: {(st.find(e), st.rfind(e))}")
        else:
            print((None, None))

first_last(st1, 'р', 'q', 'о', 'г')


#2
print("№2")
def camel(st):
    st_a = ''
    ch = False
    for i in st:
        if i.isalpha():
            if ch == False:
                st_a += i.upper()
                ch = True
            else:
                st_a += i.lower()
                ch = False
        else:
            st_a += i
    return st_a

