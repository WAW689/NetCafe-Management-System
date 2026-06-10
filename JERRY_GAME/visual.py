from db import get_connection
import matplotlib.pyplot as plt


def draw_report():

    conn = get_connection()
    cursor = conn.cursor()

    # 会员数
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM member
        """
    )
    member_count = cursor.fetchone()[0]

    # 电脑数
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM computer
        """
    )
    computer_count = cursor.fetchone()[0]

    # 上网收入
    cursor.execute(
        """
        SELECT IFNULL(
            SUM(amount_paid),
            0
        )
        FROM internet_record
        """
    )
    internet_income = float(cursor.fetchone()[0])

    # 商品收入
    cursor.execute(
        """
        SELECT IFNULL(
            SUM(total_amount),
            0
        )
        FROM sales_order
        """
    )
    product_income = float(cursor.fetchone()[0])

    cursor.close()
    conn.close()

    names = [
        "Member",
        "Computer",
        "Internet",
        "Product"
    ]

    values = [
        member_count,
        computer_count,
        internet_income,
        product_income
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(names, values)

    plt.title("Internet Cafe Statistics")

    plt.ylabel("Value")

    plt.show()