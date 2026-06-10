from db import get_connection
from visual import draw_report


def member_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM member
        """
    )

    total = cursor.fetchone()[0]

    print(f"\n会员总数：{total}")

    cursor.close()
    conn.close()


def computer_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM computer
        """
    )

    total = cursor.fetchone()[0]

    print(f"\n电脑总数：{total}")

    cursor.close()
    conn.close()


def total_income():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT IFNULL(
            SUM(amount_paid),
            0
        )
        FROM internet_record
        """
    )

    income = cursor.fetchone()[0]

    print(f"\n总营业额：{income} 元")

    cursor.close()
    conn.close()


def show_records():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM internet_record
        """
    )

    data = cursor.fetchall()

    print("\n======营业记录======")

    for row in data:

        print(row)

    cursor.close()
    conn.close()


def product_income():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT IFNULL(
            SUM(total_amount),
            0
        )
        FROM sales_order
        """
    )

    income = cursor.fetchone()[0]

    print(f"\n商品销售收入：{income} 元")

    cursor.close()
    conn.close()


def report_menu():

    while True:

        print("""
=========================
        统计报表
=========================

1.会员总数

2.电脑总数

3.营业总额

4.上网记录

5.商品销售收入

6.统计图表

0.返回

=========================
""")

        choice = input("请选择：")

        if choice == "1":

            member_count()

        elif choice == "2":

            computer_count()

        elif choice == "3":

            total_income()

        elif choice == "4":

            show_records()

        elif choice == "5":

            product_income()
        elif choice == "6":

            draw_report()

        elif choice == "0":

            break

        else:

            print("输入错误")