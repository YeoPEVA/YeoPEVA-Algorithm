menu_list = [int(input()) for _ in range(5)]

set_menu = min(menu_list[0], menu_list[1], menu_list[2])  # 햄버거 중 가장 싼 것
set_menu += min(menu_list[3], menu_list[4])               # 음료 중 가장 싼 것

print(set_menu-50)
