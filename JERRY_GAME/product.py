from db import get_connection


def add_product():

    name = input("商品名称：")
    price = float(input("价格："))
    stock = int(input("库存："))
    unit = input("单位：")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO product
        (
            product_name,
            price,
            stock,
            unit
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
            name,
            price,
            stock,
            unit
        )
    )

    conn.commit()

    print("商品添加成功")

    cursor.close()
    conn.close()


def show_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM product
        """
    )

    data = cursor.fetchall()

    print("\n======商品列表======")

    for row in data:

        print(row)

    cursor.close()
    conn.close()
def update_product():

    product_id = input("商品ID：")
    stock = int(input("新的库存："))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE product
        SET stock=%s
        WHERE product_id=%s
        """,
        (
            stock,
            product_id
        )
    )

    conn.commit()

    print("修改成功")

    cursor.close()
    conn.close()


def product_menu():

    while True:

        print("""
=========================
       商品管理
=========================

1.新增商品

2.查看商品
              
3.修改商品

0.返回

=========================
""")

        choice = input("请选择：")

        if choice == "1":

            add_product()

        elif choice == "2":

            show_products()
        elif choice == "3":

            update_product()

        elif choice == "0":

            break