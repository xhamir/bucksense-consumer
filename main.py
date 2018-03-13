#!/usr/bin/python
# -*- coding: utf-8 -*-

# HTTP FOR HUMANS
import requests

# MYSQL
import pymysql.cursors

# ESCAPE DATA
import pymysql.cursors


class Main:
    """
    Space for description
    """

    


    def __init__(self):
    	global BucksenseToken, BucksenseData, BucksenseFilterData, connection
        response = self.getToken()
        BucksenseToken = response.json()['data'][0]['token']
        if response.status_code == 200:
            BucksenseData = self.getData()
            if BucksenseData.status_code == 200:
            	print 'ALL GO ALRIGHT'
                # BucksenseFilterData = self.filterData()
                # self.connection_constructor()
                # self.insertData()


    def getToken(self):
        return requests.get('https://api.bucksense.com/3.0/login/?username=diana.sanchez@naranya.net&password=c1fe1c273a48fe65aabf39541bd3b584')



    def getData(self):
        return requests.get('https://api.bucksense.com/3.0/report/thirdpart/?token=' + BucksenseToken + '&type=1&method=getdata&dimensions=exchange_name,campaign_name,offer_name%20offer_name&metrics=wins,clicks_global,cpm&start_date=2018-02-19T00:00:00.000&end_date=2018-02-23T23:59:59.000&timezone=America/New_York&groupby=P1W')


    # def filterData(self):
        # BucksenseData
        # DONT KNOW WHAT ?
        #
        # {u'result': {u'message': u'', u'data': [{u'event': {u'cpm': 0.93484600507145, u'wins': 22947, u'clicks_global': 946, u'campaign_id': u'19984', u'company_spent': 21.451911278375, u'exchange_id': u'1', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 21.451911278375, u'exchange_name': u'Mopub'}}, {u'event': {u'cpm': 1.1257665988144, u'wins': 6895, u'clicks_global': 56, u'campaign_id': u'19984', u'company_spent': 7.762160698825, u'exchange_id': u'15', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 7.762160698825, u'exchange_name': u'Avocarrot'}}, {u'event': {u'cpm': 0.84383617602294, u'wins': 2870, u'clicks_global': 61, u'campaign_id': u'19984', u'company_spent': 2.4218098251858, u'exchange_id': u'14', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 2.4218098251858, u'exchange_name': u'PubNative'}}, {u'event': {u'cpm': 0.95376642684757, u'wins': 2753, u'clicks_global': 21, u'campaign_id': u'20139', u'company_spent': 2.6257189731114, u'exchange_id': u'1', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 2.6257189731114, u'exchange_name': u'Mopub'}}, {u'event': {u'cpm': 0.048470233183325, u'wins': 2227, u'clicks_global': 0, u'campaign_id': u'19984', u'company_spent': 0.10794320929926, u'exchange_id': u'17', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 0.10794320929926, u'exchange_name': u'Mgid'}}, {u'event': {u'cpm': 0.62261261478448, u'wins': 1566, u'clicks_global': 5, u'campaign_id': u'20139', u'company_spent': 0.9750113547525, u'exchange_id': u'4', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 0.9750113547525, u'exchange_name': u'Millennial'}}, {u'event': {u'cpm': 0.63785580740324, u'wins': 1542, u'clicks_global': 3, u'campaign_id': u'19984', u'company_spent': 0.98357365501579, u'exchange_id': u'4', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 0.98357365501579, u'exchange_name': u'Millennial'}}, {u'event': {u'cpm': 0.466562625958, u'wins': 539, u'clicks_global': 0, u'campaign_id': u'20139', u'company_spent': 0.25147725539136, u'exchange_id': u'12', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 0.25147725539136, u'exchange_name': u'Opera'}}, {u'event': {u'cpm': 0.66493942457247, u'wins': 214, u'clicks_global': 3, u'campaign_id': u'19984', u'company_spent': 0.14229703685851, u'exchange_id': u'74', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 0.14229703685851, u'exchange_name': u'AXL SSP'}}, {u'event': {u'cpm': 0.46139809359026, u'wins': 94, u'clicks_global': 0, u'campaign_id': u'19984', u'company_spent': 0.043371420797484, u'exchange_id': u'18', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'mx_cyk_juegos', u'spent': 0.043371420797484, u'exchange_name': u'Adsnative'}}, {u'event': {u'cpm': 0.62582800081665, u'wins': 35, u'clicks_global': 0, u'campaign_id': u'20139', u'company_spent': 0.021903980028583, u'exchange_id': u'14', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 0.021903980028583, u'exchange_name': u'PubNative'}}, {u'event': {u'cpm': 0.8098030812107, u'wins': 7, u'clicks_global': 0, u'campaign_id': u'20139', u'company_spent': 0.0056686215684749, u'exchange_id': u'8', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 0.0056686215684749, u'exchange_name': u'Axonix'}}, {u'event': {u'cpm': 0.01680000059423, u'wins': 1, u'clicks_global': 0, u'campaign_id': u'20139', u'company_spent': 1.680000059423e-05, u'exchange_id': u'90', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 1.680000059423e-05, u'exchange_name': u'Appodeal'}}, {u'event': {u'cpm': 0, u'wins': 0, u'clicks_global': 0, u'campaign_id': u'20139', u'company_spent': 0, u'exchange_id': u'5', u'timestamp': u'2018-02-19T00:00:00', u'campaign_name': u'juegos_cykg_banner_bks', u'spent': 0, u'exchange_name': u'Inneractive'}}], u'error': False}}
        #


    def insertData(self, message, table):
        message = self.escape_message(message)
        placeholders = ', '.join(['%s'] * len(message))
        columns = ', '.join(message.keys())
        try:
            connection.ping()
            with connection.cursor() as cursor:
                sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (
                    table, columns, placeholders)
                cursor.execute(sql, message.values())
            connection.commit()

        except pymysql.DatabaseError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            print "--------------------------"
            print "Error insert ", e, message
            print "--------------------------"
            return False

        return True

    def connection_constructor(self):
        # Connect to the database
        host = '192.168.99.101'
        port = 6004
        user = 'naranya'
        password = '50m3p455'
        db = 'db_test'
        charset = 'utf8mb4'
        try:
            connection = pymysql.connect(host=host,
                                         port=port,
                                         user=user,
                                         password=password,
                                         db=db,
                                         charset=charset,
                                         cursorclass=pymysql.cursors.DictCursor)
            # connection = pymysql.connect(host, port, user, password, db, charset,cursorclass=pymysql.cursors.DictCursor)
        except Exception, e:
            print "--------------------------"
            print "Error al conectar a DB", e
            print "--------------------------"

    def escape_message(self, message):
        esc_message = {}
        for msg in message:
            if isinstance(message[msg], six.string_types):
                esc_message[msg] = message[msg].replace('^', '')
            else:
                esc_message[msg] = message[msg]
        return esc_message

c = Main()
