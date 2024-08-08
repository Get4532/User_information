import psycopg2

def add_user_data_db(data):

    try:
        conn = psycopg2.connect(database="postgres", user = "postgres", password = "pgadmin", host = "localhost", port = "5432")  #class

# conn.close()  #method
    
        cursor = conn.cursor()
        # conn.cursor() #method
        insert_query = '''
        INSERT INTO information (first_name,last_name,mobile_no,address,email) VALUES(%s, %s, %s, %s, %s)
        '''
        data_to_insert = (data['firstName'],data['lastName'],data['mobileno'],data['address'],data['email'])
        
        cursor.execute(insert_query, data_to_insert)
        conn.commit() #method
    except (Exception, psycopg2.DatabaseError) as e:
            print(f"Error while inserting data to database: {e}")

    finally:
        if conn:
            conn.close()