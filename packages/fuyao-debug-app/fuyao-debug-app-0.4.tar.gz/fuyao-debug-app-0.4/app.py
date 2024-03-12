import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
# 1. 检查所有的node的log，是否有exception，分析exception
def check_log_exception(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


@cli.command()
# 2. 检查所有worker是否完成初始化
def check_workers_initiation():
    pass


@cli.command()
# 3. 检查是否有worker process 退出
def check_workers_exit():
    pass


@cli.command()
# 4. 自动收集所有rank的stack
def collect_ranks_stack():
    pass


@cli.command()
# 5. 自动收集火焰图
def collect_flame_graph():
    pass


@cli.command()
# 6. 自动检查设备是否出现异常；分析是否存在硬件告警及报错（syslog）
def check_device():
    pass


if __name__ == '__main__':
    cli()
