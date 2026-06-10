from db import get_connection

def topup_member():

    member_id = input("会员ID：")
    amount = float(input("充值金额："))

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # 更新余额
        cursor.execute(
            """
            UPDATE member
            SET balance = balance + %s
            WHERE member_id = %s
            """,
            (amount, member_id)
        )

        # 写充值记录
        cursor.execute(
            """
            INSERT INTO topup_record
            (
                member_id,
                admin_id,
                amount,
                bonus,
                topup_time
            )
            VALUES
            (
                %s,
                1,
                %s,
                0,
                NOW()
            )
            """,
            (
                member_id,
                amount
            )
        )

        conn.commit()

        print("充值成功")

    except Exception as e:

        conn.rollback()

        print("错误：", e)

    finally:

        cursor.close()
        conn.close()