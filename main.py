import argparse
import datetime
import random
import time

from request import save_inclusion_result

# Constants
DDD = 0.001
RHO = 10
EXIT_IDX = 3


def iteration(site, rates, holding_rate):
    rand_num = random.random()
    criterion = 0

    criterion += rates[0]
    if rand_num < criterion / holding_rate:
        site[0] += 1
        return

    criterion += rates[1]
    if rand_num < criterion / holding_rate:
        site[0] -= 1
        return

    criterion += rates[2]
    if rand_num < criterion / holding_rate:
        site[0] -= 1
        site[1] += 1
        return

    criterion += rates[3]
    if rand_num < criterion / holding_rate:
        site[0] += 1
        site[1] -= 1
        return

    criterion += rates[4]
    if rand_num < criterion / holding_rate:
        site[1] -= 1
        site[2] += 1
        return

    criterion += rates[5]
    if rand_num < criterion / holding_rate:
        site[1] += 1
        site[2] -= 1
        return

    criterion += rates[6]
    if rand_num < criterion / holding_rate:
        site[2] -= 1
        site[3] += 1
        return

    site[2] += 1
    site[3] -= 1
    return


# Slow but intuitive method

# UPDATES = [
#     [1, 0, 0, 0],
#     [-1, 0, 0, 0],
#     [-1, 1, 0, 0],
#     [+1, -1, 0, 0],
#     [0, -1, 1, 0],
#     [0, 1, -1, 0],
#     [0, 0, -1, 1],
#     [0, 0, 1, -1],
# ]


# def iteration2(site, rates, holding_rate):
#     rand_num = random.random()
#     criterion = 0

#     for idx, rate in enumerate(rates):
#         criterion += rate
#         if rand_num <= criterion / holding_rate:
#             site[0] += UPDATES[idx][0]
#             site[1] += UPDATES[idx][1]
#             site[2] += UPDATES[idx][2]
#             site[3] += UPDATES[idx][3]
#             break


def calc_rates(site):
    [x, y, z, w] = site

    rates = [
        RHO * (x + DDD),
        x * (RHO + DDD),
        x * (y + DDD),
        y * (x + DDD),
        y * (z + DDD),
        z * (y + DDD),
        z * (w + DDD),
        w * (z + DDD),
    ]

    return rates, sum(rates)


def main(verbose, memo, save):
    if EXIT_IDX not in [1, 2, 3]:
        raise "EXIT_IDX should be one of 1, 2, 3"

    start_time = time.time()
    print(f"Start! time: {datetime.datetime.fromtimestamp(start_time)}")

    site = [0, 0, 0, 0]
    index = 0
    timer = 0

    while site[EXIT_IDX] < 1:
        if verbose and not (index % verbose):
            print(f'[{index}, {"{:.3f}".format(timer)}]: {site}')

        rates, holding_rate = calc_rates(site)
        iteration(site, rates, holding_rate)

        index += 1
        timer += 1 / holding_rate

    end_time = time.time()
    elapsed = end_time - start_time

    print(f'[{index}, {"{:.3f}".format(timer)}]: {site}')
    print(f"[D: {DDD}, RHO: {RHO}, index: {index}, timer: {timer}, site: {site}")
    print(f'elapsed: {"{:.2f}".format(elapsed)} seconds')
    print(f"perf: {round(index / elapsed, 2)} /s")

    if save:
        print("saving results to database...")
        _id = save_inclusion_result(
            site, index, timer, start_time, end_time, DDD, RHO, memo=memo
        )
        print(f"result saved to MongoDB. _id: {_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", type=int, default=None)
    parser.add_argument("--memo", "-m", type=str, default="")
    parser.add_argument("--save", action="store_true", default=False)
    parser.add_argument("--iterate", "-i", type=int, default=None)
    args = vars(parser.parse_args())

    iterate = args.pop("iterate")
    memo = args.pop("memo")

    if iterate is None:
        main(**args, memo=memo)
    else:
        for idx in range(iterate):
            print(f"***** {idx + 1} / {iterate} *****")
            main(**args, memo=f"{idx + 1}/{iterate} - {memo}")
            print("******************************************")
