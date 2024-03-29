import logging
import time
from django_rq import job

from apps.balances.models import Balance
from apps.reports.models import Report

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    # filename="event_log/make_report.log",
    # filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)


@job
def create_reports(clear):
    if clear:
        Report.objects.all().delete()

    while True:
        reports = Report.objects.all().exists()
        counter = 0
        error_counter = 0

        if reports:
            balances = Balance.objects.all()

            for balance in balances:
                last_report = Report.objects.filter(balance=balance).order_by("created_at").last()
                if balance.total() != last_report.total:
                    last_updated_date = last_report.created_at
                    transactions_after = balance.transactions.filter(created_at__gt=last_updated_date)
                    if not transactions_after:
                        logger.warning(
                            f"""
        Balance ID={balance.id}: 
        The total amount from the current balance and the total amount from the report don't match.
        The total amount from the current balance= {balance.total()}
        The total amount from report= {last_report.total}
        The difference is {balance.total() - last_report.total}.""")
                        error_counter += 1
                        continue

                    total_after = sum(t.amount for t in transactions_after)
                    total_before = last_report.total

                    total_1 = total_after + total_before
                    total_2 = balance.total()

                    difference = total_1 - total_2
                    if difference:
                        logger.warning(
                            f"""
        Balance ID={balance.id}
        Difference is {difference} for '{balance}'.""")
                        error_counter += 1
                    else:
                        Report.objects.create(
                            balance=balance,
                            total=total_2
                        )
                        counter += 1
        else:
            balances = Balance.objects.all()

            for balance in balances:
                total_2 = balance.total()
                Report.objects.create(
                    balance=balance,
                    total=total_2
                )
                counter += 1
        if counter == 1:
            logger.info("All balances have been checked. 1 report has been created.")

        elif counter > 1:
            logger.info(f"All balances have been checked. {counter} reports have been created.")
        else:
            if error_counter > 1:
                logger.warning(f"There are some errors ({error_counter}).")
            else:
                logger.info(msg="All balances have been checked.")

        # Delay
        time.sleep(30)
