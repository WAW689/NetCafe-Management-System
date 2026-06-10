from db import get_connection


def add_member():

    conn = get_connection()
    cursor = conn.cursor()

    name = input("会员姓名：")
    gender = input("性别(M/F)：")
    phone = input("手机号：")

    sql = """
    INSERT INTO member
    (
        name,
        gender,
        phone,
        balance,
        level,
        register_date,
        status
    )
    VALUES
    (
        %s,
        %s,
        %s,
        0,
        '普通会员',
        CURDATE(),
        1
    )
    """

    cursor.execute(sql, (name, gender, phone))

    conn.commit()

    print("会员添加成功")

    cursor.close()
    conn.close()


def show_members():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM member")

    result = cursor.fetchall()

    print("\n======会员列表======")

    for row in result:
        print(row)

    cursor.close()
    conn.close()


def delete_member():

    member_id = input("请输入会员ID：")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM member
    WHERE member_id=%s
    """

    cursor.execute(sql, (member_id,))

    conn.commit()

    print("删除成功")

    cursor.close()
    conn.close()
def update_member():

    member_id = input("会员ID：")
    phone = input("新手机号：")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE member
        SET phone=%s
        WHERE member_id=%s
        """,
        (
            phone,
            member_id
        )
    )

    conn.commit()

    print("修改成功")

    cursor.close()
    conn.close()


def member_menu():

    while True:

        print("""
====================
      会员管理
====================

1. 新增会员
              
2. 查看会员
              
3. 删除会员
              
4. 修改会员
              
0. 返回

====================
""")

        choice = input("请选择：")

        if choice == "1":

            add_member()

        elif choice == "2":

            show_members()

        elif choice == "3":

            delete_member()
        elif choice == "4":

            update_member()

        elif choice == "0":

            break

        else:

            print("输入错误")