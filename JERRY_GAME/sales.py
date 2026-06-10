from db import get_connection


def create_order():

    member_id = input("会员ID：")
    product_id = input("商品ID：")
    quantity = int(input("购买数量："))

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # 商品信息
        cursor.execute(
            """
            SELECT price,stock
            FROM product
            WHERE product_id=%s
            """,
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:

            print("商品不存在")
            return

        price = float(product[0])
        stock = int(product[1])

        if stock < quantity:

            print("库存不足")
            return

        total = price * quantity

        # 创建订单
        cursor.execute(
            """
            INSERT INTO sales_order
            (
                member_id,
                admin_id,
                sale_time,
                total_amount,
                pay_method
            )
            VALUES
            (
                %s,
                1,
                NOW(),
                %s,
                '现金'
            )
            """,
            (
                member_id,
                total
            )
        )

        order_id = cursor.lastrowid

        # 创建订单明细
        cursor.execute(
            """
            INSERT INTO order_detail
            (
                order_id,
                product_id,
                quantity,
                subtotal
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                order_id,
                product_id,
                quantity,
                total
            )
        )

        # 扣库存
        cursor.execute(
            """
            UPDATE product
            SET stock=stock-%s
            WHERE product_id=%s
            """,
            (
                quantity,
                product_id
            )
        )

        conn.commit()

        print("订单创建成功")

    except Exception as e:

        conn.rollback()

        print("错误：", e)

    finally:

        cursor.close()
        conn.close()


def show_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM sales_order
        """
    )

    data = cursor.fetchall()

    print("\n======订单列表======")

    for row in data:

        print(row)

    cursor.close()
    conn.close()


def sales_menu():

    while True:

        print("""
=========================
       商品销售
=========================

1.创建订单

2.查看订单

0.返回

=========================
""")

        choice = input("请选择：")

        if choice == "1":

            create_order()

        elif choice == "2":

            show_orders()

        elif choice == "0":

            break