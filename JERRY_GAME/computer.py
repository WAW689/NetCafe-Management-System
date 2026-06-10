from db import get_connection


def add_computer():

    area = input("区域：")
    seat_no = input("座位号：")
    hourly_rate = float(input("每小时费用："))
    spec = input("电脑配置：")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO computer
        (
            area,
            seat_no,
            status,
            hourly_rate,
            spec
        )
        VALUES
        (
            %s,
            %s,
            '空闲',
            %s,
            %s
        )
        """,
        (
            area,
            seat_no,
            hourly_rate,
            spec
        )
    )

    conn.commit()

    print("电脑添加成功")

    cursor.close()
    conn.close()


def show_computers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM computer
        """
    )

    data = cursor.fetchall()

    print("\n======电脑列表======")

    for row in data:
        print(row)

    cursor.close()
    conn.close()


def delete_computer():

    comp_id = input("电脑ID：")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM computer
        WHERE comp_id=%s
        """,
        (comp_id,)
    )

    conn.commit()

    print("删除成功")

    cursor.close()
    conn.close()
def update_computer():

    comp_id = input("电脑ID：")
    hourly_rate = float(input("新的收费标准："))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE computer
        SET hourly_rate=%s
        WHERE comp_id=%s
        """,
        (
            hourly_rate,
            comp_id
        )
    )

    conn.commit()

    print("修改成功")

    cursor.close()
    conn.close()


def computer_menu():

    while True:

        print("""
=========================
      电脑管理
=========================

1. 新增电脑

2. 查看电脑

3. 删除电脑
              
4. 修改电脑

0. 返回

=========================
""")

        choice = input("请选择：")

        if choice == "1":

            add_computer()

        elif choice == "2":

            show_computers()

        elif choice == "3":

            delete_computer()
        elif choice == "4":

            update_computer()

        elif choice == "0":

            break

        else:

            print("输入错误")