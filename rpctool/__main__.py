#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
Tools for Retail-Product-Checkout-Dataset(RPC)
'''

import boxx
from .rpc_config import config
from .__init__ import get_skudf
from .__init__ import evaluate

import argparse
parser = argparse.ArgumentParser(description="Evaluate resFile with annFile and return markdown")
if config.debug:
    parser.add_argument(
        "--resFile",
        default="/home/dl/junk/output/mix_11/inference/coco_format_val/bbox.json",
        metavar="FILE",
        help="path to result json(support bbox and check out list)",
    )
    parser.add_argument(
        "--annFile",
        default="/home/dl/dataset/retail_product_checkout/rpc.tiny/instances_test2017.json",
        metavar="FILE",
        help="path to ground truth json(support bbox and chech out list)",
    )
    
else:
    parser.add_argument(
        "resFile",
        metavar="FILE",
        help="path to result json(support bbox and check out list)",
    )
    parser.add_argument(
        "annFile",
        metavar="FILE",
        help="path to ground truth json(support bbox and chech out list)",
    )
parser.add_argument(
    "--mmap",
    action='store_true',
    help="Evaluate mAP50 and mmAP",
)
parser.add_argument(
    "--vis",
    action='store_true',
    help="visualization after evaluate",
)
parser.add_argument(
    "--cn",
    action='store_true',
    help="Use raw Chinese class name, to instead of English name",
)

if __name__ == '__main__':
    args = parser.parse_args()
    
    resJs = boxx.loadjson(args.resFile)
    annJs = boxx.loadjson(args.annFile)
    skudf = get_skudf(annJs)
    md = evaluate(resJs, annJs, mmap=args.mmap)
    print("## result on RPC-Dataset")
    print(md)
    print('''\nYou could submit this markdown resoult to RPC-Leaderboard by new a issue here: 
        https://github.com/RPC-Dataset/RPC-Leaderboard/issues''')