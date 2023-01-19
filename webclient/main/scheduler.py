import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from .modules.GetFearAndGreedIndex import FearAndGreedIndex

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution

from datetime import timedelta, datetime
import pymysql
import configparser as parser


def getFearGreadIndex():
    conn = None
    fgi = None

    try:
        fgi = FearAndGreedIndex()
        response = fgi.get_data()
        fgi.parse_data(response)
    except Exception as e:
        now = str(datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))
        f = open(f"Test1_{now}.txt", 'w', encoding="UTF-8")
        f.write(f"111{e}\n")

    try:
        properties = parser.ConfigParser()
        path = os.path.dirname(os.path.abspath(__file__))
        configPath = os.path.join(path, "config.ini")

        properties.read(configPath)
        host = properties['DB_INFO']['host']
        pwd = properties['DB_INFO']['pwd']
        user = properties['DB_INFO']['user']
        database = properties['DB_INFO']['database']

        conn = pymysql.connect(
                    host=host, user=user, password=pwd, db=database, charset='utf8')
    except Exception as e:
        now = str(datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))
        f = open(f"Test1_{now}.txt", 'w', encoding="UTF-8")
        f.write(f"222{e}\n")


    try:        
        with conn.cursor() as curs:
            sql = """
                    CREATE TABLE IF NOT EXISTS fear_and_greed_index_usa (
                        date DATE,
                        now_value BIGINT(20),
                        week_ago_value BIGINT(20),
                        month_ago_value BIGINT(20),
                        year_ago_value BIGINT(20),
                        PRIMARY KEY (date)
                    )
                    """
            curs.execute(sql)
        conn.commit()

        with conn.cursor() as curs:
            sql = f"REPLACE INTO fear_and_greed_index_usa VALUES ('{fgi.date}', '{fgi.now_value}', '{fgi.one_week_ago_value}', '{fgi.one_month_ago_value}','{fgi.one_year_ago_value}')"
            curs.execute(sql)
        conn.commit()
    except Exception as e:
        now = str(datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))
        f = open(f"Test1_{now}.txt", 'w', encoding="UTF-8")
        f.write(f"333{e}\n")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getFearGreadIndex, 'interval', hours=4, name='getFearGreadIndex', jobstore='default')
    scheduler.start()