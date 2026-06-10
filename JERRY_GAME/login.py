from db import get_connection


def login():

    login_name = input("管理员账号：")
    password = input("管理员密码：")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM admin
        WHERE login_name=%s
        AND password=%s
        AND status=1
        """,
        (
            login_name,
            password
        )
    )

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    if admin:

        print("\n登录成功")
        print("欢迎：", admin[3])

        return True

    else:

        print("\n账号或密码错误")

        return False