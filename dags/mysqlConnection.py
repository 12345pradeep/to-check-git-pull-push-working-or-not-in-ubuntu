from ast import operator
from datetime import datetime, timedelta
from multiprocessing.dummy import Array
from sre_constants import ANY
from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.transfers.mysql_to_s3 import MySQLToS3Operator
import pandas as pd
import pyarrow
from io import StringIO
with DAG(
    'MySQLTOS3',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['sksingh@calance.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='connection python mysql',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022,8,2),
    # schedule_interval='0 0 * * *',
    catchup=False,
    tags=['example'],
) as dag:

    # def load_data():
    #     conn = MySqlHook(mysql_conn_id='atcost_stage_db').get_conn()
    #     cursor = conn.cursor()
    #     cursor.execute("select * from atcost_stage.oc_order limit 10")
    #     data = cursor.fetchall()
    #     print(data)
        # print(data)
        
        # outFileName="atcost.txt"
        # outFile=open(outFileName, "w")
        # outFile.write(df)
        # outFile.close() 
        # return df
    # def hdfsConn():
    #     hconn = HDFSHook(hdfs_conn_id='hdfs_local_conn',proxy_user=None, autoconfig=False).get_conn()
    #     path=hconn.ls("/")
    


    # task_hdfs_conn = PythonOperator(
    #     task_id='hdfs_conn',
    #     python_callable=hdfsConn,
    #     dag=dag
    # )
    


    # Sqooopimport = SqoopOperator(
    #     conn_id='atcost_stage_db',
    #     table='oc_order',
    #     cmd_type="import",
    #     target_dir="/sumit",
    #     num_mappers=3,
    #     task_id='sqoop_import',
    #     dag=dag
    # )





    # task_get_data = PythonOperator(
    #     task_id='load_data',
    #     python_callable=load_data,
    #     dag=dag
    # )

    tbls=(
"a_temp",
"customer_extra_refund",
"delivery_slots",
"oc_active_packers",
"oc_active_queue",
"oc_address",
"oc_affiliate",
"oc_affiliate_activity",
"oc_affiliate_login",
"oc_affiliate_transaction",
"oc_api",
"oc_api_insert",
"oc_api_ip",
"oc_api_session",
"oc_area",
"oc_attribute",
"oc_attribute_description",
"oc_attribute_group",
"oc_attribute_group_description",
"oc_auditdata",
"oc_auditdata_Dec2020",
"oc_banner",
"oc_banner_image",
"oc_banner_image_description",
"oc_blog",
"oc_blog_category",
"oc_blog_category_description",
"oc_blog_category_to_layout",
"oc_blog_category_to_store",
"oc_blog_comment",
"oc_blog_description",
"oc_blog_related",
"oc_blog_to_category",
"oc_blog_to_layout",
"oc_blog_to_store",
"oc_cart",
"oc_category",
"oc_category_description",
"oc_category_filter",
"oc_category_path",
"oc_category_to_layout",
"oc_category_to_store",
"oc_catwarehouse",
"oc_city",
"oc_country",
"oc_coupon",
"oc_coupon_cashback_return",
"oc_coupon_category",
"oc_coupon_delivery_slots",
"oc_coupon_history",
"oc_coupon_product",
"oc_coupon_query_list",
"oc_coupon_track",
"oc_criteria",
"oc_currency",
"oc_custom_field",
"oc_custom_field_customer_group",
"oc_custom_field_description",
"oc_custom_field_value",
"oc_custom_field_value_description",
"oc_customer",
"oc_customer_activity",
"oc_customer_activity_Dec2020",
"oc_customer_activity_old_25112019",
"oc_customer_group",
"oc_customer_group_description",
"oc_customer_history",
"oc_customer_ip",
"oc_customer_ip_Dec2020",
"oc_customer_login",
"oc_customer_membership",
"oc_customer_notification_list",
"oc_customer_notification_list_Dec2020",
"oc_customer_old_25112019",
"oc_customer_online",
"oc_customer_promo_migrate",
"oc_customer_query",
"oc_customer_rating",
"oc_customer_referral_reward",
"oc_customer_request",
"oc_customer_reward",
"oc_customer_transaction",
"oc_customer_transaction_old_25112019",
"oc_customer_transaction_positive",
"oc_customer_wishlist",
"oc_delivery_slot",
"oc_delivery_slots_by_warehouse",
"oc_download",
"oc_download_description",
"oc_event",
"oc_extension",
"oc_facebook_events",
"oc_facebook_product",
"oc_fcm_channels",
"oc_fcm_customer",
"oc_filter",
"oc_filter_description",
"oc_filter_group",
"oc_filter_group_description",
"oc_fraud_ip",
"oc_fraudlabspro",
"oc_free_promo",
"oc_future_upload_sheet",
"oc_geo_zone",
"oc_information",
"oc_information_description",
"oc_information_to_layout",
"oc_information_to_store",
"oc_invoice_register",
"oc_language",
"oc_latest_sale_prediction",
"oc_layout",
"oc_layout_module",
"oc_layout_route",
"oc_length_class",
"oc_length_class_description",
"oc_location",
"oc_locationwise_delivery_slots",
"oc_long_running_query",
"oc_manufacturer",
"oc_manufacturer_to_store",
"oc_marketing",
"oc_marketing_multiplier",
"oc_mega_menu",
"oc_mega_menu_modules",
"oc_menu_permission_to_user",
"oc_menu_setting",
"oc_modification",
"oc_module",
"oc_newsletter",
"oc_option",
"oc_option_description",
"oc_option_value",
"oc_option_value_description",
"oc_order",
"oc_order_Dec2020",
"oc_order_custom_field",
"oc_order_data",
"oc_order_delivery",
"oc_order_delivery_status",
"oc_order_history",
"oc_order_history_Dec2020",
"oc_order_option",
"oc_order_packed_products",
"oc_order_packed_products_Mar2021",
"oc_order_packed_products_all",
"oc_order_packer_mapping",
"oc_order_payment",
"oc_order_payment_details",
"oc_order_product",
"oc_order_product_Dec2020",
"oc_order_product_delivery",
"oc_order_product_history",
"oc_order_product_history_Dec2020",
"oc_order_product_transition",
"oc_order_product_transition_Dec2020",
"oc_order_recurring",
"oc_order_recurring_transaction",
"oc_order_status",
"oc_order_total",
"oc_order_total_Dec2020",
"oc_order_total_history",
"oc_order_total_history_Dec2020",
"oc_order_track",
"oc_order_track_Dec2020",
"oc_order_voucher",
"oc_ospos_location_to_warehouse",
"oc_ospos_sales_purchase",
"oc_ospos_sales_purchase_data",
"oc_paytm_order_data",
"oc_product",
"oc_product_attribute",
"oc_product_description",
"oc_product_discount",
"oc_product_enabledisabe_history",
"oc_product_filter",
"oc_product_image",
"oc_product_option",
"oc_product_option_value",
"oc_product_quantity_type",
"oc_product_recurring",
"oc_product_related",
"oc_product_reward",
"oc_product_setting",
"oc_product_special",
"oc_product_stock",
"oc_product_tab",
"oc_product_to_category",
"oc_product_to_download",
"oc_product_to_layout",
"oc_product_to_store",
"oc_product_weight_base",
"oc_productwarehouse",
"oc_promo_cash_master",
"oc_promo_product_mapping",
"oc_promotions",
"oc_purchase_invoice",
"oc_quantity_type",
"oc_question",
"oc_queue_category_mapping",
"oc_receiving_location",
"oc_recurring",
"oc_recurring_description",
"oc_refund",
"oc_refund_status",
"oc_reports",
"oc_return",
"oc_return_action",
"oc_return_history",
"oc_return_reason",
"oc_return_status",
"oc_review",
"oc_revslider_attachment_images",
"oc_revslider_css",
"oc_revslider_layer_animations",
"oc_revslider_settings",
"oc_revslider_sliders",
"oc_revslider_slides",
"oc_revslider_static_slides",
"oc_sale_prediction_history",
"oc_sale_to_stock_till_order1",
"oc_sendmail",
"oc_setting",
"oc_soft_product",
"oc_stock_event",
"oc_stock_status",
"oc_stock_user",
"oc_store",
"oc_tab",
"oc_tab_description",
"oc_table_optimize_record",
"oc_tag_cloud",
"oc_tax_class",
"oc_tax_rate",
"oc_tax_rate_to_customer_group",
"oc_tax_rule",
"oc_temp_customer_address",
"oc_temp_merged_telephone",
"oc_temp_telephone",
"oc_temporary_cart",
"oc_testimonial",
"oc_testimonial_description",
"oc_upload",
"oc_upload_sheet",
"oc_url_alias",
"oc_user",
"oc_user_group",
"oc_user_location",
"oc_user_reports_access",
"oc_user_to_warehouse",
"oc_vendor_details",
"oc_voucher",
"oc_voucher_history",
"oc_voucher_theme",
"oc_voucher_theme_description",
"oc_warehouse",
"oc_warehouse_active",
"oc_warehouse_cron_log",
"oc_warehouse_mapping",
"oc_warehouse_queue_mapping",
"oc_warehouse_user_mapping",
"oc_weight_class",
"oc_weight_class_description",
"oc_zone",
"oc_zone_to_geo_zone",
"ospos_atcost_api",
"toupdatedata",
"toupdatedelete",
"trans_last_id",
"update_cashback",
)
    mysql_to_s3 = [MySQLToS3Operator(
    task_id=tbl,
    query="select * from atcost_stage."+tbl+ " union all select * from atcost_myrwashop_stage."+tbl+"",
    s3_bucket='atcostdb',           
    s3_key=tbl+".parquet",
    mysql_conn_id='test_schema',
    aws_conn_id='atcost_s3_conn',
    index=False,
    header=True,
    dag=dag
    ) for tbl in tbls]

mysql_to_s3
