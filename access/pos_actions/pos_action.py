from data_connection.h1pos import db1
from access.pos_actions.validation import CL_posvalid

import sys


class CL_posaction(object):

    cancel=0
    suspend=1
    retrieve=2
    def init(self):
        self.conn = db1.connect()

    def FN_ItemInquiry(self,gtin):
        if CL_posvalid.FN_GtinValid(self,gtin):
            try:
                self.conn = db1.connect()
                mycursor = self.conn.cursor()
                sql8 = "SELECT * FROM Hyper1_Retail.POS_ITEM Where POS_GTIN=%s"
                print(sql8)
                val8 = (gtin,)
                mycursor.execute(sql8, val8)
                records = mycursor.fetchall()
                print(records)
            except:
                print(sys.exc_info())
        else:
            print("gtin false")

    def  FN_cashDrawer(self):
        print("open")


    def FN_CustomerInquery(self,data):
        try:
            self.conn = db1.connect()
            mycursor = self.conn.cursor()
            sql8 = "SELECT POSC_NAME,POSC_MOBILE,POSC_EMAIL,POSC_STATUS,POSC_POINTS_AFTER FROM Hyper1_Retail.POS_CUSTOMER join POS_CUSTOMER_POINT on POSC_CUST_ID=POSC_CUSTOMER_ID where POSC_CUST_ID=%s"
            val8 = (data,)
            mycursor.execute(sql8, val8)
            records = mycursor.fetchall()
            if len(records)>0:
                print(records)
            else:
                print("not found")
        except:
            print(sys.exc_info())

    def FN_CouponInquery(self,data):
        try:
            self.conn = db1.connect()
            mycursor = self.conn.cursor()
            sql8 = "SELECT COP_ID,COP_DESC,COP_DISCOUNT_VAL,COP_DISCOUNT_PERCENT FROM Hyper1_Retail.COUPON join COUPON_SERIAL on COP_ID=COUPON_ID where COPS_BARCODE=%s"
            val8 = (data,)
            mycursor.execute(sql8,val8)
            records = mycursor.fetchall()
            if len(records)>0:
                print(records)
            else:
                print("not found")
        except:
            print(sys.exc_info())

    def FN_PromInquery(self,data):
        try:
            self.conn = db1.connect()
            mycursor = self.conn.cursor()
            sql8 = "SELECT * FROM Hyper1_Retail.PROMOTION_HEADER as h join PROMOTION_DETAIL as d on h.PROM_ID=d.PROM_ID where POS_GTIN=%s"
            val8 = (data,)
            mycursor.execute(sql8,val8)
            records = mycursor.fetchall()
            if len(records)>0:
                print(records)
            else:
                print("not found")
        except:
            print(sys.exc_info())

    def FN_VoucherInquery(self,data):
        try:
            self.conn = db1.connect()
            mycursor = self.conn.cursor()
            sql8 = "SELECT * FROM Hyper1_Retail.VOUCHER where GV_BARCODE=%s"
            val8 = (data,)
            mycursor.execute(sql8,val8)
            records = mycursor.fetchall()
            if len(records)>0:
                print(records)
            else:
                print("not found")
        except:
            print(sys.exc_info())

    def FN_CancelSuspendOrder(self, Doctype,INVOICE_NO):
        try:
            self.conn = db1.connect()
            mycursor = self.conn.cursor()
            sql8 = "update Hyper1_Retail.INVOICE_HEADER set DOCTYPE_ID=%s where INVOICE_NO = %s"
            val8 = (Doctype,INVOICE_NO)
            mycursor.execute(sql8, val8)
        except:
            print(sys.exc_info())





if __name__ == '__main__':
    test=CL_posaction
    test.FN_ItemInquiry(test,"6223003778163")
    test.FN_CustomerInquery(test,"13")
    test.FN_CouponInquery(test,"HCOP0b1100011110101111100001001011010100111111")
    test.FN_PromInquery(test,"13")
    test.FN_VoucherInquery(test,"HVOU0b100101011000010110101000000001001011001")
    test.FN_CancelSuspendOrder(test,"","")



