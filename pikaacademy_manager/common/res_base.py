# -*- coding: utf-8 -*-
import datetime
import json
import decimal


class BaseResponse:
  __abstract__ = True

  pass


def parse(obj):
  res = None
  if obj:
    res = obj._asdict()
    for attr in obj._fields:
      if isinstance(res[attr], (datetime.date, datetime.datetime)):
        res[attr] = res[attr].timestamp()
      elif isinstance(res[attr], (decimal.Decimal)):
        res[attr] = float(res[attr])
      elif attr == 'chats':
        res[attr] = json.loads(res[attr]) if res.get(attr) else []
  return res


def paginate_result(res):
  return {"list": [parse(i) for i in res.items], "total": res.total}


def result_all(res):
  return [parse(i) for i in res]
