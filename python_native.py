from tkinter import *

def calculate_sum():
    character_power = power_entry1.get()
    character_defend = defend_entry1.get()
    character_speed = speed_entry1.get()

    item_powers = [power_entry2.get(), power_entry3.get(), power_entry4.get(), power_entry5.get(), power_entry6.get(), power_entry7.get(), power_entry8.get(), power_entry9.get(), power_entry10.get()]
    item_defends = [defend_entry2.get(), defend_entry3.get(), defend_entry4.get(), defend_entry5.get(), defend_entry6.get(), defend_entry7.get(), defend_entry8.get(), defend_entry9.get(), defend_entry10.get()]
    item_speeds = [speed_entry2.get(), speed_entry3.get(), speed_entry4.get(), speed_entry5.get(), speed_entry6.get(), speed_entry7.get(), speed_entry8.get(), speed_entry9.get(), speed_entry10.get()]

    item_power_valid_values = [value for value in item_powers if value]
    item_defend_valid_values = [value for value in item_defends if value]
    item_speed_valid_values = [value for value in item_speeds if value]

    pet_power_valid_value = power_entry11.get()
    pet_defend_valid_value = defend_entry11.get()
    pet_speed_valid_value = speed_entry11.get()

    character_power_result = (int(character_power) if character_power else 0) * 0.7
    character_defend_result = (int(character_defend) if character_defend else 0) * 0.7
    character_speed_result = (int(character_speed) if character_speed else 0) * 0.7

    item_power_sum_result = sum(int(value) for value in item_power_valid_values)
    item_defend_sum_result = sum(int(value) for value in item_defend_valid_values)
    item_speed_sum_result = sum(int(value) for value in item_speed_valid_values)

    pet_power_result = (int(pet_power_valid_value) if pet_power_valid_value else 0) * 0.3
    pet_defend_result = (int(pet_defend_valid_value) if pet_defend_valid_value else 0) * 0.3
    pet_speed_result = (int(pet_speed_valid_value) if pet_speed_valid_value else 0) * 0.3

    power_result = int(character_power_result + pet_power_result + item_power_sum_result)
    defend_result = int(character_defend_result + pet_defend_result + item_defend_sum_result)
    speed_result = int(character_speed_result + pet_speed_result + item_speed_sum_result)

    power_result_entry.config(state="normal")
    power_result_entry.delete(0, END)
    power_result_entry.insert(0, str(power_result))
    power_result_entry.config(state="readonly")

    defend_result_entry.config(state="normal")
    defend_result_entry.delete(0, END)
    defend_result_entry.insert(0, str(defend_result))
    defend_result_entry.config(state="readonly")

    speed_result_entry.config(state="normal")
    speed_result_entry.delete(0, END)
    speed_result_entry.insert(0, str(speed_result))
    speed_result_entry.config(state="readonly")


def reset_entry():
    entrys = [power_entry1, power_entry2, power_entry3, power_entry4, power_entry5, power_entry6, power_entry7, power_entry8, power_entry9, power_entry10, power_entry11,
              defend_entry1, defend_entry2, defend_entry3, defend_entry4, defend_entry5, defend_entry6, defend_entry7, defend_entry8, defend_entry9, defend_entry10, defend_entry11,
              speed_entry1, speed_entry2, speed_entry3, speed_entry4, speed_entry5, speed_entry6, speed_entry7, speed_entry8, speed_entry9, speed_entry10, speed_entry11]
    for entry in entrys:
        entry.delete(0, END)
    calculate_sum()


root = Tk()
root.title("탑승 능력치 계산기")
root.geometry("280x490")
root.resizable(False, False)

widthVal = 8

header = Label(root, text="========== 캐릭터 정보 ==========", width=30)
header.grid(row=0, column=0, columnspan=4, pady=5)

power1 = Label(root, text="완력")
power1.grid(row=1, column=1, padx=5)

defend1 = Label(root, text="건강")
defend1.grid(row=1, column=2, padx=5)

speed1 = Label(root, text="순발")
speed1.grid(row=1, column=3, padx=5)

speed1 = Label(root, text="상태창 :")
speed1.grid(row=2, column=0, padx=5)

power_entry1 = Entry(root, width=widthVal)
power_entry1.grid(row=2, column=1)

defend_entry1 = Entry(root, width=widthVal)
defend_entry1.grid(row=2, column=2)

speed_entry1 = Entry(root, width=widthVal)
speed_entry1.grid(row=2, column=3)

header = Label(root, text="========== 아이템 정보 ==========", width=30)
header.grid(row=3, column=0, columnspan=4, pady=5)

header = Label(root, text="공", width=widthVal)
header.grid(row=4, column=1)

header = Label(root, text="방", width=widthVal)
header.grid(row=4, column=2)

header = Label(root, text="순", width=widthVal)
header.grid(row=4, column=3)

header = Label(root, text="장신구 1 :")
header.grid(row=5, column=0, padx=5)

power_entry2 = Entry(root, width=widthVal)
power_entry2.grid(row=5, column=1)

defend_entry2 = Entry(root, width=widthVal)
defend_entry2.grid(row=5, column=2)

speed_entry2 = Entry(root, width=widthVal)
speed_entry2.grid(row=5, column=3)

header = Label(root, text="장신구 2 :")
header.grid(row=6, column=0, padx=5)

power_entry3 = Entry(root, width=widthVal)
power_entry3.grid(row=6, column=1)

defend_entry3 = Entry(root, width=widthVal)
defend_entry3.grid(row=6, column=2)

speed_entry3 = Entry(root, width=widthVal)
speed_entry3.grid(row=6, column=3)

header = Label(root, text="투구 :")
header.grid(row=7, column=0, padx=5)

power_entry4 = Entry(root, width=widthVal)
power_entry4.grid(row=7, column=1)

defend_entry4 = Entry(root, width=widthVal)
defend_entry4.grid(row=7, column=2)

speed_entry4 = Entry(root, width=widthVal)
speed_entry4.grid(row=7, column=3)

header = Label(root, text="갑옷 :")
header.grid(row=8, column=0, padx=5)

power_entry5 = Entry(root, width=widthVal)
power_entry5.grid(row=8, column=1)

defend_entry5 = Entry(root, width=widthVal)
defend_entry5.grid(row=8, column=2)

speed_entry5 = Entry(root, width=widthVal)
speed_entry5.grid(row=8, column=3)

header = Label(root, text="무기 :")
header.grid(row=9, column=0, padx=5)

power_entry6 = Entry(root, width=widthVal)
power_entry6.grid(row=9, column=1)

defend_entry6 = Entry(root, width=widthVal)
defend_entry6.grid(row=9, column=2)

speed_entry6 = Entry(root, width=widthVal)
speed_entry6.grid(row=9, column=3)

header = Label(root, text="토템 :")
header.grid(row=10, column=0, padx=5)

power_entry7 = Entry(root, width=widthVal)
power_entry7.grid(row=10, column=1)

defend_entry7 = Entry(root, width=widthVal)
defend_entry7.grid(row=10, column=2)

speed_entry7 = Entry(root, width=widthVal)
speed_entry7.grid(row=10, column=3)

header = Label(root, text="보조 1 :")
header.grid(row=11, column=0, padx=5)

power_entry8 = Entry(root, width=widthVal)
power_entry8.grid(row=11, column=1)

defend_entry8 = Entry(root, width=widthVal)
defend_entry8.grid(row=11, column=2)

speed_entry8 = Entry(root, width=widthVal)
speed_entry8.grid(row=11, column=3)

header = Label(root, text="보조 2 :")
header.grid(row=12, column=0, padx=5)

power_entry9 = Entry(root, width=widthVal)
power_entry9.grid(row=12, column=1)

defend_entry9 = Entry(root, width=widthVal)
defend_entry9.grid(row=12, column=2)

speed_entry9 = Entry(root, width=widthVal)
speed_entry9.grid(row=12, column=3)

header = Label(root, text="보조 3 :")
header.grid(row=13, column=0, padx=5)

power_entry10 = Entry(root, width=widthVal)
power_entry10.grid(row=13, column=1)

defend_entry10 = Entry(root, width=widthVal)
defend_entry10.grid(row=13, column=2)

speed_entry10 = Entry(root, width=widthVal)
speed_entry10.grid(row=13, column=3)

header = Label(root, text="========== 페트 정보 ==========", width=30)
header.grid(row=14, column=0, columnspan=4, pady=5)

header = Label(root, text="공", width=widthVal)
header.grid(row=15, column=1)

header = Label(root, text="방", width=widthVal)
header.grid(row=15, column=2)

header = Label(root, text="순", width=widthVal)
header.grid(row=15, column=3)

header = Label(root, text="페트창 :", width=widthVal)
header.grid(row=16, column=0, padx=5)

power_entry11 = Entry(root, width=widthVal)
power_entry11.grid(row=16, column=1)

defend_entry11 = Entry(root, width=widthVal)
defend_entry11.grid(row=16, column=2)

speed_entry11 = Entry(root, width=widthVal)
speed_entry11.grid(row=16, column=3)

reset_button = Button(root, text="초기화", command=reset_entry, width=5)
reset_button.grid(row=17, column=0, pady=10, padx=5)

calculate_button = Button(root, text="계산", command=calculate_sum, width=20)
calculate_button.grid(row=17, column=1, columnspan=3, pady=10)

header = Label(root, text="공", width=widthVal)
header.grid(row=18, column=1)

header = Label(root, text="방", width=widthVal)
header.grid(row=18, column=2)

header = Label(root, text="순", width=widthVal)
header.grid(row=18, column=3)

header = Label(root, text="결과 :", width=widthVal)
header.grid(row=19, column=0, padx=5)

power_result_entry = Entry(root, state="readonly", width=widthVal)
power_result_entry.grid(row=19, column=1)

defend_result_entry = Entry(root, state="readonly", width=widthVal)
defend_result_entry.grid(row=19, column=2)

speed_result_entry = Entry(root, state="readonly", width=widthVal)
speed_result_entry.grid(row=19, column=3)

root.mainloop()