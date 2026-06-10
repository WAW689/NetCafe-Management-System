from login import login

from member import member_menu
from topup import topup_member
from internet import internet_menu
from computer import computer_menu
from report import report_menu
from product import product_menu
from sales import sales_menu


def main():

    if not login():

        print("登录失败，系统退出")
        return

    while True:

        print("""
=================================
        网吧管理系统
=================================

1. 会员管理

2. 会员充值

3. 上网管理

4. 电脑管理

5. 统计报表

6. 商品管理

7. 商品销售

0. 退出系统

=================================
""")

        choice = input("请选择功能：")

        if choice == "1":

            member_menu()

        elif choice == "2":

            topup_member()

        elif choice == "3":

            internet_menu()

        elif choice == "4":

            computer_menu()

        elif choice == "5":

            report_menu()

        elif choice == "6":

            product_menu()

        elif choice == "7":

            sales_menu()

        elif choice == "0":

            print("感谢使用网吧管理系统！")
            break

        else:

            print("输入错误，请重新选择！")


if __name__ == "__main__":

    main()