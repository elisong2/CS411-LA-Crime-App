"""Defines all the functions related to the database"""
from app import db
import pandas as pd

def fetch_Crime_Status():
    """Reads all tasks listed in the todo table
    Based on your understanding of stock prices and intrinsic values, which of the following statements is true?

	The intrinsic value of a stock is based only on the perceived risk in the company.
	A stock’s intrinsic value is based on the fundamental cash flows and the company’s risk
    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    Event = pd.read_sql_table('Event', conn)
    conn.close()

    return Event

#CRUD and search functions:
def search_Table(search_text, column_name):
    table_name = "Event"
    query = ""
    if column_name == "DR_NO":
        search_text = int(search_text)
        query = "Select * from {} where {} LIKE '{}' limit 15".format(table_name, column_name, search_text)
    elif column_name == "Time_of_Occurrence":
        search_text = int(str(search_text).replace(":",""))
        query = "Select * from {} where {} LIKE '{}' limit 15".format(table_name, column_name, search_text)
    else:
        search_text = str(search_text)
        query = "Select * from {} where {} LIKE '%%{}%%' limit 15".format(table_name, column_name, search_text)

    conn = db.connect()
    print(query)
    query_results = conn.execute(query)
    query_results = [x for x in query_results]
    conn.close()
    final_df = []
    for x in query_results:
        row = (x[0], x[2], x[3], x[4])
        final_df.append(row)
    final_df = pd.DataFrame(final_df, columns =['DR_NO', 'Date_of_Occurrence', 'Time_of_Occurrence', 'Location'])
    return final_df

def insert_Event(elements_list):

    DR_NO = elements_list[0]
    DR_NO = int(DR_NO)

    Date_of_Report = elements_list[1]
    Date_of_Report =   str(Date_of_Report) 
    
    Date_of_Occurrence = elements_list[2]
    Date_of_Occurrence =  str(Date_of_Occurrence)

    Time_of_Occurrence = elements_list[3]
    Time_of_Occurrence = int(str(Time_of_Occurrence).replace(":",""))

    Location = elements_list[4]
    Location =  str(Location) 

    Cross_Street_Location = elements_list[5]
    Cross_Street_Location =  str(Cross_Street_Location) 

    Latitude = elements_list[6]
    Latitude = float(Latitude)

    Longitude = elements_list[7]
    Longitude = float(Longitude)

    crime_code = elements_list[8]
    crime_code = int(crime_code)

    weapon_code = elements_list[9]
    weapon_code = int(weapon_code)

    area = elements_list[10]
    area = int(area)

    premise_code = elements_list[11]
    premise_code = int(premise_code)

    conn = db.connect()
    query = 'Insert Into Event (DR_NO, Date_of_Report, Date_of_Occurrence, Time_of_Occurrence, Location, Cross_Street_Location, Latitude, Longitude, crime_code, weapon_code, area, premise_code) VALUES ("{}", "{}", "{}","{}", "{}", "{}","{}", "{}", "{}","{}", "{}", "{}");'.format(
        DR_NO, Date_of_Report, Date_of_Occurrence, Time_of_Occurrence, Location, Cross_Street_Location, Latitude, Longitude, crime_code, weapon_code, area, premise_code)
    conn.execute(query)
    conn.close()
    

def update_Event(elements_list):
    DR_NO = int(elements_list[0])
    Date_of_Occurrence = "'" + str(elements_list[1]) + "'"
    Date_of_Occurrence = Date_of_Occurrence.replace(" ","")
    Time_of_Occurrence = str(elements_list[2])
    Time_of_Occurrence = int(Time_of_Occurrence.replace(":",""))
    Location = "'" + str(elements_list[3]) +  "'"

    conn = db.connect()
    
    query = 'UPDATE Event SET Date_of_Occurrence = {}, Time_of_Occurrence = {}, Location = {} WHERE DR_NO = {};'.format(Date_of_Occurrence, Time_of_Occurrence, Location, DR_NO)
    
    conn.execute(query)
    
    conn.close()
    
    #return homepage()


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def delete_Event(case_id):
    """ remove entries based on Event ID """
    conn = db.connect()
    query = 'Delete From Event where DR_NO={};'.format(int(case_id))
    conn.execute(query)
    conn.close()

def categorize_ages(): # 
    conn = db.connect()
    Event = pd.read_sql_table('CategorizedAges', conn)
    print("eeeeeee")
    print(Event)
    conn.close()

    return Event

def categorize_weapons(): # 
    conn = db.connect()
    Event = pd.read_sql_table('CategorizedWeapons', conn)
    print("ffffffff")
    print(Event)
    conn.close()

    return Event

def age_breakdown(): # 
    conn = db.connect()
    Event = pd.read_sql_table('User_Inserted', conn)
    conn.close()

    return Event

    
def top_weapons(): # advanced query 1
    conn = db.connect()
    query = "Select count(Weapon_type_code) as count_weapons, Weapon_Type_Code, Weapon_Description from Event e join Weapon w on (e.weapon_code=w.Weapon_Type_Code) Group by Weapon_type_code order by count_weapons desc limit 15"
    query_results = conn.execute(query)
    query_results = [x for x in query_results]
    query_results = query_results[1:]
    query_results = pd.DataFrame(query_results, columns =['Count', 'Weapon', 'Weapon Description'])
    conn.close()
    return query_results

def top_victim_ages(): # advanced query 2
    conn = db.connect()
    query = "Select (count(v.dr_no)/(select count(v1.dr_no) from Victim v1 where v1.Victim_Age > 0)) * 100 as percent, v.Victim_Age from Event e join Victim v on (e.dr_no=v.dr_no) where v.Victim_Age > 0 Group by v.Victim_Age Order by percent desc limit 50"
    #query = "Select (count(v.dr_no)/(select count(v1.dr_no) from Victim v1)) * 100 as percent, v.Victim_Age from Event e join Victim v on (e.dr_no=v.dr_no) Group by v.Victim_Age Order by percent desc limit 15"
    query_results = conn.execute(query)
    query_results = [x for x in query_results]
    query_results = pd.DataFrame(query_results, columns =['Percent', 'Victim Age'])
    conn.close()
    return query_results


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()
