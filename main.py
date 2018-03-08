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

	global BucksenseToken, BucksenseData, BucksenseFilterData, connection

	"""
	Space for description
	"""
	def __init__( self ):
		BucksenseToken	= self.getToken().json()['data'][0]['token'] 
		if BucksenseToken.status_code == 200:
			BucksenseData	= self.getData()
			if BucksenseData.status_code == 200:
				BucksenseFilterData = self.filterData()
				self.connection_constructor()
				self.insertData()
				
			

	"""
	Space for description
	"""
	def getToken( self ):
		return requests.get('https://api.bucksense.com/3.0/login/?username=diana.sanchez@naranya.net&password=c1fe1c273a48fe65aabf39541bd3b584')

	"""
	Space for description
	"""
	def getData( self ):
		return requests.get('https://api.bucksense.com/3.0/report/thirdpart/?token='+token+'&type=1&method=getdata&dimensions=exchange_name,campaign_name,offer_name%20offer_name&metrics=wins,clicks_global,cpm&start_date=2018-02-19T00:00:00.000&end_date=2018-02-23T23:59:59.000&timezone=America/New_York&groupby=P1W')

	"""
	Space for description
	"""
	def filterData( self ):
		BucksenseData

	"""
	Space for description
	"""
	def insertData( self, message, table ):
		message = self.escape_message(message)
		placeholders = ', '.join(['%s'] * len(message))
		columns = ', '.join(message.keys())
		try:
			connection.ping()
			with connection.cursor() as cursor:
				sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
				cursor.execute(sql, message.values())
			connection.commit()
			
		except pymysql.DatabaseError as e:
		    print('Got error {!r}, errno is {}'.format(e, e.args[0]))
		    print "--------------------------"
			print "Error insert ", e, message
			print "--------------------------"
			return False
		
		return True		

	def connection_constructor( self ):
		# Connect to the database
		host='192.168.99.101'
		port=6004
		user='naranya'
		password='50m3p455'
		db='db_test'
		charset='utf8mb4'
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

	def escape_message( self, message ):
		esc_message = {}
		for msg in message:
			if isinstance(message[msg], six.string_types):
				esc_message[msg] = message[msg].replace('^', '')	
			else:
				esc_message[msg] = message[msg]
		return esc_message

c = Main()







