import pandas as pd
import re
from datetime import datetime

df = pd.read_csv("orders.csv")
df_ab = pd.read_csv('abandoned.csv')

username = input("Mysql db username: ")
password = input("Mysql db password: ")
ip_address = input("Mysql db IP address: ")
port = input("Mysql db port number: ")
db_name = input("Mysql db Name: ")

# make order table

def Make_Order_Table(df):
    order = df[
        [    'Name','Created at','Financial Status',
            'Paid at', 'Fulfillment Status', 
             'Fulfilled at','Accepts Marketing', 'Currency', 'Subtotal', 'Shipping',
             'Taxes','Total', 'Discount Code', 'Discount Amount', 'Shipping Method',
             'Billing Name', 'Billing Address1', 'Billing Address2', 
             'Billing City', 'Billing Zip', 'Billing Province', 'Billing Country',
             'Billing Phone', 'Shipping Name', 'Shipping Address1', 
             'Shipping Address2', 'Shipping City', 'Shipping Zip',
             'Shipping Province', 'Shipping Country', 'Shipping Phone',
             'Notes','Payment Method', 'Email'
    ]
    ].copy()


    #Map Proper names
    order.rename(columns =
                    {
                        'Name':'order_id',
                        'Created at':'created_at',
                        'Financial Status':'financial_status',
                        'Paid at':'paid_at',
                        'Fulfillment Status':'fulfillment_status', 
                        'Fulfilled at':'fulfilled_at',
                        'Accepts Marketing':'accepts_marketing',
                        'Currency':'currency',
                        'Subtotal':'subtotal',
                        'Shipping':'shipping',
                        'Taxes':'taxes',
                        'Total':'total',
                        'Discount Code':'discount_code',
                        'Discount Amount':'discount_amount',
                        'Shipping Method':'shipping_method',
                        'Billing Name': 'billing_name',
                        'Billing Address1':'billing_address1',
                        'Billing Address2':'billing_address2',
                        'Billing City':'billing_city',
                        'Billing Zip':'billing_zip',
                        'Billing Province':'billing_province',
                        'Billing Country': 'billing_country',
                        'Billing Phone':'billing_phone',
                        'Shipping Name':'shipping_name',
                        'Shipping Address1' : 'shipping_address1',
                        'Shipping Address2' : 'shipping_address2',
                        'Shipping City':'shipping_city',
                        'Shipping Zip':'shipping_zip',
                        'Shipping Province':'shipping_province',
                        'Shipping Country':'shipping_country',
                        'Shipping Phone':'shipping_phone', 
                        'Notes':'notes',
                        'Payment Method':'payment_method',    
                        'Email':'email'
                    }, 
                    
                    inplace = True
                   )
    order.reset_index(drop = True, inplace = True)

    #Remove duplicate values
    order['order_id'] = order['order_id'].str.replace("#", "")
    order['order_id'] = order["order_id"].drop_duplicates()
    order = order[order["order_id"].notna()]
    
    
    # Convert to datetime object and remove timezone info
    order['created_at'] = pd.to_datetime(order['created_at']).dt.tz_localize(None)
    order['paid_at'] = pd.to_datetime(order['paid_at']).dt.tz_localize(None)
    order['fulfilled_at'] = pd.to_datetime(order['paid_at']).dt.tz_localize(None)
    
    # Format as string in desired format
    order['created_at'] = order['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    order['paid_at'] = order['paid_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    order['fulfilled_at'] = order['fulfilled_at'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Fill NaN values
    order['created_at'] = order['created_at'].fillna('2020-01-01 00:00:00')
    order['paid_at'] = order['paid_at'].fillna('2020-01-01 00:00:00')
    order['fulfilled_at'] = order['fulfilled_at'].fillna('2020-01-01 00:00:00')
    order.fillna('null', inplace = True)
    
    #drop null
    order = order[order["email"] != 'null']
    
    return order

# Customer Table

def Make_Customer_Table(df, df_ab):
    customer = pd.concat([df[['Email', 'Billing Name', 'Billing Province']], 
                          df_ab[['Email', 'Billing Name', 'Billing Province']]],
                         axis = 0)

    customer.reset_index(drop = True, inplace = True)   
   
    
    customer.rename(columns = {
                            'Email':'email',
                            'Billing Name':'full_name',
                            'Billing Province':'location'
                    },                    
                    inplace=True
                   )
    
    customer['email'] = customer["email"].drop_duplicates()
    customer = customer[customer["email"].notna()]
    
    customer.fillna('null', inplace = True)
    customer.reset_index(drop=True, inplace=True)   
    return customer

# Product Table

def Make_Product_Table(df, df_ab):
#     product = df[
#         ['Lineitem sku', 'Lineitem name', 'Lineitem price',
#          'Lineitem compare at price','Lineitem requires shipping',
#          'Lineitem taxable']
#     ].copy()

    product = pd.concat([df[['Lineitem sku', 'Lineitem name', 'Lineitem price',
                            'Lineitem compare at price','Lineitem requires shipping','Lineitem taxable']],
                        df_ab[['Lineitem sku', 'Lineitem name', 'Lineitem price',
                            'Lineitem compare at price','Lineitem requires shipping','Lineitem taxable']]],
                        axis = 0)

    #Map Proper names
    product.rename(columns =
                    {
                        'Lineitem sku':'product_sku',
                        'Lineitem name':'product_name',
                        'Lineitem price':'product_price',
                        'Lineitem compare at price':'product_compare_at_price',
                        'Lineitem requires shipping':'product_requires_shipping', 
                        'Lineitem taxable':'product_taxable',                      
                    },
                   
                   inplace = True
                  )  
    
    product.reset_index(drop = True, inplace = True)  
 
    #drop null

    product['product_sku'] = product["product_sku"].drop_duplicates()
    product = product[product["product_sku"].notna()]

    product = product[product["product_sku"] != 'null']
    
    product.fillna('null', inplace = True)
    
    
    product.reset_index(drop = True, inplace = True)
    
    return product


# Order Item

def Make_Order_Item_Table(df):
    order_item = df[
        ['Name', 'Lineitem sku', 'Lineitem quantity', 'Lineitem fulfillment status']
    ].copy()
    
    order_item['Name'] = order_item['Name'].str.replace("#", "")
    
    order_item.fillna('null', inplace = True)
    
    order_item.rename(columns =
                    {
                      'Name':'order_id',
                      'Lineitem sku':'product_sku',
                      'Lineitem quantity':'quantity',
                      'Lineitem fulfillment status':'product_fulfillment'                
                    },
    
                   inplace = True
                  )  
    
    #drop duplicate items in one order
    order_item.drop_duplicates(subset=['order_id', 'product_sku'], inplace=True)
    
    order_item = order_item[order_item["product_sku"] != 'null']
    
    order_item.reset_index(drop = True, inplace = True)
    
    return order_item


# Abandoned_order

abandoned_order = Make_Order_Table(df_ab)
abandoned_order.rename(columns = {'order_id':'abandoned_order_id'}, inplace = True)
abandoned_order.drop(['financial_status', 'paid_at',
                      'fulfillment_status', 'fulfilled_at', 
                      'payment_method'],
                     axis = 1,
                     inplace = True 
                    )

# Abandoned_order_item

abandoned_order_item = Make_Order_Item_Table(df_ab)
abandoned_order_item.rename(columns = {'order_id':'abandoned_order_id'}, inplace = True)

# Other_tables

order_item = Make_Order_Item_Table(df)
product = Make_Product_Table(df, df_ab)
customer = Make_Customer_Table(df, df_ab)
order = Make_Order_Table(df)

# Transfer to DB

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(user = username, password = password,
                        host = ip_address, port = port, database = db_name,
                        auth_plugin='mysql_native_password')    
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
        # Insert into customer
        
        n = 1
        
        for i,row in customer.iterrows():
            sql = ("INSERT INTO coolina.customer "
                   "(email, full_name, location) "
                   "VALUES (%s, %s, %s)"
                  )
            cursor.execute(sql, tuple(row))
            print(f"{n} Record inserted Customer")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            n += 1
            
        
        # Insert into orders
        
        n = 1
        
        for i,row in order.iterrows():
            sql = ("INSERT INTO coolina.orders "
                   "(order_id, created_at, financial_status, paid_at,"
               "fulfillment_status, fulfilled_at, accepts_marketing, currency,"
               "subtotal, shipping, taxes, total, discount_code,"
               "discount_amount, shipping_method, billing_name,"
               "billing_address1, billing_address2, billing_city, billing_zip,"
               "billing_province, billing_country, billing_phone, shipping_name,"
               "shipping_address1, shipping_address2, shipping_city,"
               "shipping_zip, shipping_province, shipping_country,"
               "shipping_phone, notes, payment_method, email)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
                   " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                   )
            cursor.execute(sql, tuple(row))
            print(f"{n} Record inserted to ORDERS")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            n += 1            
                    
        # Insert into Abandoned orders
        
        n = 1
        
        for i,row in abandoned_order.iterrows():
            sql = ("INSERT INTO coolina.abandoned_order "
                   "(abandoned_order_id, created_at, accepts_marketing, currency,"
               "subtotal, shipping, taxes, total, discount_code,"
               "discount_amount, shipping_method, billing_name,"
               "billing_address1, billing_address2, billing_city, billing_zip,"
               "billing_province, billing_country, billing_phone, shipping_name,"
               "shipping_address1, shipping_address2, shipping_city,"
               "shipping_zip, shipping_province, shipping_country,"
               "shipping_phone, notes, email)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
                   " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                   )
            cursor.execute(sql, tuple(row))
            print(f"{n} Record inserted to ABANDONED ORDERS")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            n += 1    
            
         
        # Insert into product
        n = 1
        
        for i,row in product.iterrows():
            sql = ("INSERT INTO coolina.product "
            "(product_sku, product_name, product_price, product_compare_at_price, product_requires_shipping, product_taxable) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
             )
            cursor.execute(sql, tuple(row))
            print(f"{n} Record inserted Product")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            n += 1
         
        # Insert into order_item
        n = 1
        
        for i,row in order_item.iterrows():
            sql = ("INSERT INTO coolina.order_item "
            "(order_id, product_sku, quantity, product_fulfillment)"                
            "VALUES (%s, %s, %s, %s)"
             )
            cursor.execute(sql, tuple(row))
            print(f"{n} Record inserted Order Item")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            n += 1
                   
       # Insert into abandoned_order
        n = 1
        
        for i,row in abandoned_order_item.iterrows():
            sql = ("INSERT INTO coolina.abandoned_order_item "
            "(abandoned_order_id, product_sku, quantity, product_fulfillment)"                
            "VALUES (%s, %s, %s, %s)"
             )
            cursor.execute(sql, tuple(row))
            print(f"{n} Record inserted Abandoned Order Item")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            n += 1
            
            
except Error as e:
    print("Error while connecting to MySQL", e)

conn.close()