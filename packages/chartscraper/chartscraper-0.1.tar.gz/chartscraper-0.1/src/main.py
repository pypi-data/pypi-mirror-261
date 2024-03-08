from src.logic import get_chart
import click

@click.command()
@click.option(
    "--ticker",
    help="This is the name of stock as listend on googlefinance",
)
@click.option(
    "--time_interval",
    help="Duartion of each candlestick",
)
@click.option(
    "--time_period",
    help="This is the time period for which charts will get downloaded.",
)
@click.option(
    "--store_location",
    help="Folder location where the charts will get stored.",
)
def main(ticker,
        time_interval,
        time_period,
        store_location):
    get_chart(ticker,time_interval,time_period, store_location)

if __name__ == "__main__":
    main()