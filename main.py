import os
import argparse
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

parser = argparse.ArgumentParser()

parser.add_argument("--now",
                    help="run crawlers immediately",
                    action="store_true")
args = parser.parse_args()

if __name__ == "__main__":

    process = CrawlerProcess(get_project_settings())
    process.crawl('brinvesting')

    if args.now:
        process.start()

    else:

        scheduler = AsyncIOScheduler()
        schedule_exp = os.getenv('CRAWL_SCHEDULE', '0 21,03,12 * * *')
        scheduler.add_job(process.start, CronTrigger.from_crontab(schedule_exp, timezone='America/Sao_Paulo'))

        scheduler.start()

        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass
