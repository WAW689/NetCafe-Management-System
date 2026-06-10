from db import get_connection
from datetime import datetime


# 开始上机
def start_internet():

    member_id = input("会员ID：")
    comp_id = input("电脑ID：")

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # 检查会员是否存在
        cursor.execute(
            """
            SELECT balance
            FROM member
            WHERE member_id=%s
            """,
            (member_id,)
        )

        member = cursor.fetchone()

        if member is None:
            print("会员不存在")
            return

        # 检查电脑是否存在
        cursor.execute(
            """
            SELECT status
            FROM computer
            WHERE comp_id=%s
            """,
            (comp_id,)
        )

        computer = cursor.fetchone()

        if computer is None:
            print("电脑不存在")
            return

        if computer[0] != "空闲":
            print("该电脑正在使用")
            return

        # 新建上网记录
        cursor.execute(
            """
            INSERT INTO internet_record
            (
                member_id,
                comp_id,
                admin_id,
                start_time,
                status
            )
            VALUES
            (
                %s,
                %s,
                1,
                NOW(),
                '上机中'
            )
            """,
            (member_id, comp_id)
        )

        # 修改电脑状态
        cursor.execute(
            """
            UPDATE computer
            SET status='使用中'
            WHERE comp_id=%s
            """,
            (comp_id,)
        )

        conn.commit()

        print("开始上机成功")

    except Exception as e:

        conn.rollback()
        print("错误：", e)

    finally:

        cursor.close()
        conn.close()


# 结束上机
def end_internet():

    record_id = input("请输入上网记录ID：")

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # 查询上网记录
        cursor.execute(
            """
            SELECT
                member_id,
                comp_id,
                start_time
            FROM internet_record
            WHERE record_id=%s
            AND status='上机中'
            """,
            (record_id,)
        )

        record = cursor.fetchone()

        if record is None:
            print("上网记录不存在")
            return

        member_id = record[0]
        comp_id = record[1]
        start_time = record[2]

        end_time = datetime.now()

        # 计算时长
        hours = (
            end_time - start_time
        ).total_seconds() / 3600

        if hours < 1:
            hours = 1

        # 查询电脑单价
        cursor.execute(
            """
            SELECT hourly_rate
            FROM computer
            WHERE comp_id=%s
            """,
            (comp_id,)
        )

        hourly_rate = float(
            cursor.fetchone()[0]
        )

        fee = round(
            hours * hourly_rate,
            2
        )

        # 查询余额
        cursor.execute(
            """
            SELECT balance
            FROM member
            WHERE member_id=%s
            """,
            (member_id,)
        )

        balance = float(
            cursor.fetchone()[0]
        )

        if balance < fee:

            print(
                f"余额不足，应付{fee}元，当前余额{balance}元"
            )

            return

        # 扣费
        cursor.execute(
            """
            UPDATE member
            SET balance=balance-%s
            WHERE member_id=%s
            """,
            (
                fee,
                member_id
            )
        )

        # 更新上网记录
        cursor.execute(
            """
            UPDATE internet_record
            SET
                end_time=%s,
                amount_due=%s,
                amount_paid=%s,
                status='已完成'
            WHERE record_id=%s
            """,
            (
                end_time,
                fee,
                fee,
                record_id
            )
        )

        # 释放电脑
        cursor.execute(
            """
            UPDATE computer
            SET status='空闲'
            WHERE comp_id=%s
            """,
            (comp_id,)
        )

        conn.commit()

        print("下机成功")
        print("消费金额：", fee)

    except Exception as e:

        conn.rollback()
        print("错误：", e)

    finally:

        cursor.close()
        conn.close()


# 查看上网记录
def show_internet_records():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM internet_record
        """
    )

    data = cursor.fetchall()

    print("\n======上网记录======")

    for row in data:
        print(row)

    cursor.close()
    conn.close()


# 菜单
def internet_menu():

    while True:

        print("""
=========================
       上网管理
=========================

1. 开始上机

2. 结束上机

3. 查看上网记录

0. 返回

=========================
""")

        choice = input("请选择：")

        if choice == "1":

            start_internet()

        elif choice == "2":

            end_internet()

        elif choice == "3":

            show_internet_records()

        elif choice == "0":

            break

        else:

            print("输入错误")